"""Shorts SIN VOZ (canal Fútbol Sin Relato): texto que se teclea, efectos de sonido y música de fondo.

Uso: python3 pipeline/sinvoz.py futbol/NNN-slug          → build/ + entrega/NNN.mp4 + entrega/SUBIR.md
     python3 pipeline/sinvoz.py futbol/NNN-slug --frames → solo una hoja de fotogramas (build/hoja.png) para revisar

guion.py del Short:
  CARDS = [dict(text="Texto con *palabras en amarillo* y ^en rojo^.", hero=dict(type=..., ...), crowd=False, cut=False, d=None), ...]
  META  = dict(code="001", title=..., description=..., tags=[...], sources=[...])
  MUSIC = 0            (índice de la pista de futbol/music/*.mp3)

Tipos de hero (parte de arriba): score, counter (style="tag" = etiqueta de precio), quiz, place, redcard, big, items, player,
badges, clock, tactic, stamp, final.  Cada tarjeta dura lo que tarda en teclearse + lectura (o lo que pida su animación).
Zona segura de Shorts: nada importante abajo del todo ni en la franja derecha de los botones.
"""
import glob, math, os, re, subprocess, sys, json, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from concurrent.futures import ProcessPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
ANTON = os.path.join(FONTS, "Anton.ttf")
BLACK = os.path.join(FONTS, "InterDisplay-Black.otf")
SEMI = os.path.join(FONTS, "InterDisplay-SemiBold.otf")
W, H, FPS, SR = 1080, 1920, 30, 48000
GREEN_D, GREEN_L = (13, 52, 33), (17, 63, 40)
YEL, RED, WHITE, INK, OK = (255, 209, 102), (230, 57, 70), (245, 245, 240), (10, 14, 20), (46, 204, 113)
CHANNEL = "FÚTBOL SIN RELATO"
TYPE_CPS = 30.0          # caracteres por segundo del tecleo
T0 = 0.25                # empieza a teclear
HERO_Y, HERO_H = 300, 640
TEXT_Y, TEXT_CX, TEXT_W = 975, W // 2 - 40, 800   # texto algo a la izquierda: a la derecha van los botones de YouTube

_fc = {}
def font(p, s):
    if (p, s) not in _fc: _fc[(p, s)] = ImageFont.truetype(p, int(s))
    return _fc[(p, s)]

def eo(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def back(x):  # entrada con rebote
    x = max(0.0, min(1.0, x)); c = 1.9; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2

def fmt(v, pre="", suf=""):
    return pre + f"{int(round(v)):,}".replace(",", ".") + suf

def fit(path, size, txt, maxw):
    s = size
    while s > 20 and font(path, s).getlength(txt) > maxw: s -= 4
    return font(path, s)

# ---------------------------------------------------------------- texto tecleado
def parse(text):
    """'a *b c*. ^d^' -> [palabras]; cada palabra es una lista de trozos (texto, estilo None | 'y' | 'r').
    La puntuación pegada a una marca ('*perdió*.') se une a esa palabra sin espacio."""
    out, prev_space = [], True
    for seg in re.split(r"(\*[^*]+\*|\^[^^]+\^)", text):
        if not seg: continue
        st = "y" if seg.startswith("*") else "r" if seg.startswith("^") else None
        if st: seg = seg[1:-1]
        glue = out and not prev_space and not seg[0].isspace()
        for i, w in enumerate(seg.split()):
            if i == 0 and glue: out[-1].append((w, st))
            else: out.append([(w, st)])
        prev_space = seg[-1].isspace()
    return out

def wtext(w): return "".join(c for c, _ in w)

def layout(text, f=None):
    f = f or font(BLACK, 64)
    words = parse(text); lines, cur = [], []
    for w in words:
        trial = " ".join(wtext(x) for x in cur + [w])
        if cur and f.getlength(trial) > TEXT_W: lines.append(cur); cur = [w]
        else: cur.append(w)
    if cur: lines.append(cur)
    return lines, f

def nchars(text):
    return len(" ".join(wtext(w) for w in parse(text)))

def hl_times(text, cps=TYPE_CPS):
    """Segundo (desde el inicio de la tarjeta) en que se termina de teclear cada palabra resaltada."""
    pos, out = 0, []
    for w in parse(text):
        for c, st in w:
            pos += len(c)
            if st: out.append(T0 + pos / cps)
        pos += 1
    return out

def draw_text(im, text, t, cps=TYPE_CPS):
    lines, f = layout(text)
    n = int(max(0, t - T0) * cps); done = n >= nchars(text)
    if n == 0: return
    d = ImageDraw.Draw(im); lh = 98; y = TEXT_Y; used = 0; cur_xy = None
    shake = 0
    for ht in hl_times(text, cps):
        if 0 <= t - ht < 0.12: shake = 5
    for ln in lines:
        full = " ".join(wtext(w) for w in ln)
        if used >= n and used > 0: break
        lw = f.getlength(full); x0 = TEXT_CX - lw / 2
        d.rounded_rectangle([x0 - 22, y - 10, x0 + lw + 22, y + lh - 14], 10, fill=INK)
        x = x0 + (shake if (y // lh) % 2 else -shake)
        for w in ln:
            if used >= n: break
            for c, st in w:
                if used >= n: break
                k = min(len(c), n - used); part = c[:k]
                col = YEL if st == "y" else RED if st == "r" else WHITE
                d.text((x, y), part, font=f, fill=col); x += f.getlength(part); used += k
            if used < n: x += f.getlength(" "); used += 1
            cur_xy = (x, y)
        y += lh
    if cur_xy and (not done or int(t * 2.2) % 2 == 0):
        d.rectangle([cur_xy[0] + 6, cur_xy[1] + 8, cur_xy[0] + 18, cur_xy[1] + 72], fill=YEL)

# ---------------------------------------------------------------- fondo y marcador
_bg = {}
def pitch_layers():
    if "s" in _bg: return _bg["s"], _bg["l"], _bg["v"]
    st = Image.new("RGB", (W, H + 320), GREEN_D); d = ImageDraw.Draw(st)
    for i in range(0, H + 320, 160):
        if (i // 160) % 2: d.rectangle([0, i, W, i + 159], fill=GREEN_L)
    ln = Image.new("RGBA", (W, H), (0, 0, 0, 0)); o = ImageDraw.Draw(ln); c = (255, 255, 255, 46)
    o.rectangle([50, 290, W - 50, H - 90], outline=c, width=5)
    o.line([50, H // 2 + 60, W - 50, H // 2 + 60], fill=c, width=5)
    o.ellipse([W // 2 - 170, H // 2 + 60 - 170, W // 2 + 170, H // 2 + 60 + 170], outline=c, width=5)
    o.rectangle([W // 2 - 270, H - 90 - 300, W // 2 + 270, H - 90], outline=c, width=5)
    o.rectangle([W // 2 - 120, H - 90 - 110, W // 2 + 120, H - 90], outline=c, width=5)
    for (x, y) in [(230, 740), (850, 880), (270, 1520), (800, 1380), (520, 1180)]:
        q = (255, 255, 255, 52); o.line([x - 20, y - 20, x + 20, y + 20], fill=q, width=6); o.line([x - 20, y + 20, x + 20, y - 20], fill=q, width=6)
    v = Image.new("L", (W, H), 0); ImageDraw.Draw(v).ellipse([-320, -160, W + 320, H + 160], fill=255)
    v = v.filter(ImageFilter.GaussianBlur(170))
    _bg.update(s=st, l=ln, v=v)
    return st, ln, v

def background(tg):
    st, ln, v = pitch_layers()
    off = int(tg * 14) % 320
    im = st.crop((0, off, W, off + H)).convert("RGBA")
    im.alpha_composite(ln)
    im = Image.composite(im, Image.new("RGBA", (W, H), (0, 0, 0, 255)), v)
    return im

def topbar(im, tg, total):
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([60, 150, W - 60, 262], 22, fill=INK)
    d.text((104, 206), CHANNEL, font=font(BLACK, 38), fill=WHITE, anchor="lm")
    m = min(90, int(90 * tg / max(total, 0.1)))
    d.rounded_rectangle([W - 250, 166, W - 78, 246], 14, fill=YEL)
    d.text((W - 164, 207), f"{m}'", font=font(ANTON, 58), fill=INK, anchor="mm")
    d.rectangle([60, 272, W - 60, 282], fill=(32, 40, 50))
    d.rectangle([60, 272, 60 + int((W - 120) * min(1, tg / total)), 282], fill=YEL)

# ---------------------------------------------------------------- heroes (capa RGBA de W x HERO_H)
def layer():
    L = Image.new("RGBA", (W, HERO_H), (0, 0, 0, 0)); return L, ImageDraw.Draw(L)

def pill(d, cx, cy, txt, f, bg=INK, fg=WHITE, pad=26):
    w = f.getlength(txt); d.rounded_rectangle([cx - w / 2 - pad, cy - f.size * 0.75, cx + w / 2 + pad, cy + f.size * 0.75], int(f.size * 0.5), fill=bg)
    d.text((cx, cy), txt, font=f, fill=fg, anchor="mm")

def score_vals(v, t):
    a, b = v.get("frm", (v["a"], v["b"]))
    if v.get("roll"):
        k = eo((t - 0.15) / v["roll"]); a = a + (v["a"] - a) * k; b = b + (v["b"] - b) * k
    elif "steps" not in v:
        a, b = v["a"], v["b"]
    last = None
    for (ts, aa, bb) in v.get("steps", []):
        if t >= ts: a, b, last = aa, bb, ts
    return int(round(a)), int(round(b)), last

def h_score(v, t, D):
    L, d = layer(); a, b, last = score_vals(v, t)
    pop = 1 + 0.25 * (1 - eo((t - last) / 0.3)) if last is not None and t - last < 0.3 else 1
    for cx, val, team in [(W * 0.27, a, v.get("ta", "")), (W * 0.73, b, v.get("tb", ""))]:
        if team: pill(d, cx, 120, team, fit(BLACK, 40, team, 430))
        f = font(ANTON, int(250 * pop))
        d.text((cx, 380), str(val), font=f, fill=WHITE, anchor="mm", stroke_width=10, stroke_fill=(0, 0, 0))
    d.text((W / 2, 380), "–", font=font(ANTON, 200), fill=YEL, anchor="mm", stroke_width=8, stroke_fill=(0, 0, 0))
    return L

def h_counter(v, t, D):
    L, d = layer(); st = v.get("st", 0.2); dur = v.get("dur", 1.4)
    val = v.get("frm", 0) + (v["to"] - v.get("frm", 0)) * eo((t - st) / dur)
    s = fmt(val, v.get("pre", ""), v.get("suf", ""))
    if v.get("style") == "tag":
        tag = Image.new("RGBA", (820, 360), (0, 0, 0, 0)); g = ImageDraw.Draw(tag)
        g.polygon([(110, 0), (820, 0), (820, 360), (110, 360), (0, 180)], fill=WHITE)
        g.ellipse([60, 155, 100, 195], fill=(13, 52, 33))
        g.text((470, 150), s, font=fit(ANTON, 200, s, 640), fill=INK, anchor="mm")
        g.text((470, 300), v.get("label", ""), font=fit(BLACK, 40, v.get("label", ""), 620), fill=RED, anchor="mm")
        tag = tag.rotate(6 * math.sin(t * 2.2) - 4, expand=True, resample=Image.BICUBIC)
        d.line([(W / 2 - 330, 40), (W / 2 - 300, 300)], fill=WHITE, width=4)
        L.alpha_composite(tag, (int(W / 2 - tag.width / 2), int(330 - tag.height / 2)))
    else:
        col = {"red": RED, "white": WHITE}.get(v.get("col"), YEL)
        d.text((W / 2, 300), s, font=fit(ANTON, 300, s, 940), fill=col, anchor="mm", stroke_width=10, stroke_fill=(0, 0, 0))
        if v.get("label"): pill(d, W / 2, 520, v["label"], fit(BLACK, 48, v["label"], 860))
    return L

def quiz_cstart(card):
    if card.get("_dur"): return T0 + card["_dur"] + 0.2      # con relato: la cuenta atrás empieza cuando termina la voz
    return T0 + nchars(card["text"]) / TYPE_CPS + 0.3

def h_quiz(v, t, D, card):
    L, d = layer(); rv = v.get("reveal")
    if rv is None:
        cs = quiz_cstart(card); left = 3 - int(max(0, t - cs))
        if t >= cs:
            num = str(max(left, 0)) if left > 0 else "?"
            k = (t - cs) % 1.0; r = 78 * (1 + 0.18 * (1 - eo(k / 0.25)))
            d.ellipse([W / 2 - r, 70 - r, W / 2 + r, 70 + r], fill=RED if left <= 1 else YEL)
            d.text((W / 2, 72), num, font=font(ANTON, 100), fill=INK, anchor="mm")
            d.arc([W / 2 - 92, 70 - 92, W / 2 + 92, 70 + 92], -90, -90 + 360 * (1 - k), fill=WHITE, width=8)
    for i, o in enumerate(v["opts"]):
        y = 220 + i * 140; app = eo((t - 0.1 - i * 0.12) / 0.3)
        x0 = 120 - (1 - app) * 600; x1 = 920 - (1 - app) * 600
        good = rv is not None and i == rv; dim = rv is not None and i != rv
        bg = OK if good else (40, 46, 56) if dim else INK
        d.rounded_rectangle([x0, y - 55, x1, y + 55], 20, fill=bg)
        d.ellipse([x0 + 18, y - 40, x0 + 98, y + 40], fill=WHITE if not dim else (90, 96, 106))
        d.text((x0 + 58, y + 2), "ABC"[i], font=font(ANTON, 54), fill=INK, anchor="mm")
        d.text((x0 + 130, y), o, font=font(BLACK, 54), fill=(150, 156, 166) if dim else WHITE, anchor="lm")
    return L

def pin(d, cx, cy, s=1.0):
    r = 70 * s
    d.polygon([(cx - r * 0.86, cy - r * 0.5), (cx + r * 0.86, cy - r * 0.5), (cx, cy + r * 1.6)], fill=RED)
    d.ellipse([cx - r, cy - r * 1.5, cx + r, cy + r * 0.5], fill=RED)
    d.ellipse([cx - r * 0.4, cy - r * 0.9, cx + r * 0.4, cy - r * 0.1], fill=WHITE)

def h_place(v, t, D):
    L, d = layer(); k = back((t - 0.05) / 0.45)
    pin(d, W / 2, 40 + 140 * k, 1.0)
    a = eo((t - 0.35) / 0.3)
    if a > 0:
        f = fit(ANTON, 150, v["name"], 940)
        d.text((W / 2, 380 + (1 - a) * 40), v["name"], font=f, fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=(0, 0, 0))
        if v.get("sub"): pill(d, W / 2, 520, v["sub"], fit(BLACK, 46, v["sub"], 860), bg=YEL, fg=INK)
    return L

def h_redcard(v, t, D):
    L, d = layer(); k = back((t - 0.05) / 0.5)
    card = Image.new("RGBA", (280, 390), RED + (255,)); ImageDraw.Draw(card).rectangle([0, 0, 279, 389], outline=(160, 25, 35), width=6)
    card = card.rotate(-35 + 27 * k, expand=True, resample=Image.BICUBIC)
    L.alpha_composite(card, (int(W / 2 - card.width / 2), int(-300 + 300 * k)))
    if v.get("text") and t > 0.45:
        d.text((W / 2, 545), v["text"], font=fit(ANTON, 130, v["text"], 900), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=(0, 0, 0))
    return L

def h_big(v, t, D):
    L, d = layer(); k = back((t - 0.05) / 0.35); col = RED if v.get("col") == "red" else YEL
    lines = v["text"].split("\n"); n = len(lines)
    for i, ln in enumerate(lines):
        f = fit(ANTON, int(230 * max(k, 0.01)), ln, 940)
        d.text((W / 2, 330 + (i - (n - 1) / 2) * 230), ln, font=f, fill=col, anchor="mm", stroke_width=10, stroke_fill=(0, 0, 0))
    return L

def shirt(d, cx, cy, s, col=WHITE, num=None):
    p = [(-0.5, -0.62), (-0.18, -0.72), (0, -0.62), (0.18, -0.72), (0.5, -0.62), (0.82, -0.25), (0.6, -0.05), (0.42, -0.2),
         (0.42, 0.75), (-0.42, 0.75), (-0.42, -0.2), (-0.6, -0.05), (-0.82, -0.25)]
    d.polygon([(cx + x * s, cy + y * s) for x, y in p], fill=col, outline=INK)
    d.line([(cx - 0.18 * s, cy - 0.72 * s), (cx, cy - 0.55 * s), (cx + 0.18 * s, cy - 0.72 * s)], fill=YEL, width=max(3, int(s * 0.05)))
    if num is not None: d.text((cx, cy + 0.08 * s), str(num), font=font(ANTON, int(s * 0.62)), fill=INK, anchor="mm")

def h_items(v, t, D):
    L, d = layer()
    for i, it in enumerate(v["items"]):
        a = eo((t - 0.3 - i * 0.55) / 0.25)
        if a <= 0: continue
        y = 150 + i * 190 - (1 - a) * 60
        shirt(d, 190, y, 120, col=WHITE if i % 2 == 0 else YEL)
        f = font(BLACK, 60); rows = []
        for w_ in it.split():
            if rows and f.getlength(rows[-1] + " " + w_) <= 640: rows[-1] += " " + w_
            else: rows.append(w_)
        for r_, row in enumerate(rows):
            d.text((290, y + (r_ - (len(rows) - 1) / 2) * 70), row, font=f, fill=WHITE, anchor="lm", stroke_width=4, stroke_fill=(0, 0, 0))
    return L

def h_player(v, t, D):
    L, d = layer(); k = back((t - 0.05) / 0.45)
    shirt(d, W / 2, 245, 300 * max(k, 0.05), col=WHITE, num=v.get("num"))
    if t > 0.3:
        d.text((W / 2, 495), v["name"], font=fit(ANTON, 110, v["name"], 940), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=(0, 0, 0))
        if v.get("sub"): pill(d, W / 2, 600, v["sub"], fit(BLACK, 40, v["sub"], 880), bg=YEL, fg=INK)
    return L

def h_badges(v, t, D):
    L, d = layer(); n = len(v["items"])
    for i, it in enumerate(v["items"]):
        k = back((t - 0.25 - i * 0.6) / 0.35)
        if k <= 0.01: continue
        cx = W / 2 + (i - (n - 1) / 2) * 420; cy = 300; r = 180 * k
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=INK, outline=YEL, width=max(2, int(12 * k)))
        top, _, bot = it.partition("\n")
        d.text((cx, cy - 55 * k), top, font=font(BLACK, max(8, int(44 * k))), fill=YEL, anchor="mm")
        d.text((cx, cy + 35 * k), bot, font=font(ANTON, max(8, int(120 * k))), fill=WHITE, anchor="mm")
    return L

def h_clock(v, t, D):
    L, d = layer(); mm, ss = [int(x) for x in v["to"].split(":")]; tot = mm * 60 + ss
    cur = int(tot * eo((t - 0.2) / v.get("dur", 1.1)))
    d.rounded_rectangle([W / 2 - 360, 150, W / 2 + 360, 470], 36, fill=INK, outline=(60, 66, 76), width=6)
    d.text((W / 2, 312), f"{cur // 60:02d}:{cur % 60:02d}", font=font(ANTON, 250), fill=YEL if cur < tot else RED, anchor="mm")
    if v.get("label"): pill(d, W / 2, 560, v["label"], fit(BLACK, 44, v["label"], 860))
    return L

def tactic_segs(v):
    return v["path"]  # [[x0,y0,x1,y1,"pase"|"tiro"], ...] en coordenadas de 0..1 del campo

def h_tactic(v, t, D):
    L, d = layer(); x0, y0, x1, y1 = 120, 40, 960, 620; fw, fh = x1 - x0, y1 - y0
    d.rectangle([x0, y0, x1, y1], fill=(0, 0, 0, 90), outline=WHITE, width=5)
    d.rectangle([x0 + fw * 0.3, y0, x1 - fw * 0.3, y0 + fh * 0.18], outline=WHITE, width=4)
    d.rectangle([x0 + fw * 0.42, y0 - 18, x1 - fw * 0.42, y0], fill=WHITE)
    d.line([x0, y1 - 4, x1, y1 - 4], fill=WHITE, width=4)
    d.arc([x0 + fw / 2 - 110, y1 - 110, x0 + fw / 2 + 110, y1 + 110], 180, 360, fill=WHITE, width=4)
    P = lambda px, py: (x0 + px * fw, y0 + py * fh)
    for (px, py, mark) in v.get("players", []):
        cx, cy = P(px, py)
        if mark == "x": d.line([cx - 22, cy - 22, cx + 22, cy + 22], fill=RED, width=9); d.line([cx - 22, cy + 22, cx + 22, cy - 22], fill=RED, width=9)
        else: d.ellipse([cx - 24, cy - 24, cx + 24, cy + 24], outline=YEL, width=9)
    segs = tactic_segs(v); step = v.get("step", 0.7); ball = None
    for i, (ax, ay, bx, by, kind) in enumerate(segs):
        k = eo((t - 0.3 - i * step) / (step * 0.8))
        if k <= 0: continue
        A, B = P(ax, ay), P(bx, by); E = (A[0] + (B[0] - A[0]) * k, A[1] + (B[1] - A[1]) * k)
        col = YEL if kind == "tiro" else WHITE
        n = int(math.hypot(E[0] - A[0], E[1] - A[1]) // 28)
        for j in range(n + 1):
            if j % 2 == 0:
                p0 = (A[0] + (B[0] - A[0]) * k * j / max(n + 1, 1), A[1] + (B[1] - A[1]) * k * j / max(n + 1, 1))
                p1 = (A[0] + (B[0] - A[0]) * k * (j + 1) / max(n + 1, 1), A[1] + (B[1] - A[1]) * k * (j + 1) / max(n + 1, 1))
                d.line([p0, p1], fill=col, width=8 if kind == "tiro" else 6)
        if k >= 1:
            ang = math.atan2(B[1] - A[1], B[0] - A[0])
            d.polygon([B, (B[0] - 34 * math.cos(ang - 0.45), B[1] - 34 * math.sin(ang - 0.45)), (B[0] - 34 * math.cos(ang + 0.45), B[1] - 34 * math.sin(ang + 0.45))], fill=col)
        ball = E
    if ball: d.ellipse([ball[0] - 16, ball[1] - 16, ball[0] + 16, ball[1] + 16], fill=WHITE, outline=INK, width=3)
    return L

def h_stamp(v, t, D):
    L, d = layer(); k = eo((t - 0.05) / 0.25); s = 1.7 - 0.7 * k; col = RED if v.get("col") == "red" else YEL
    txt = v["text"]; f = fit(ANTON, 150, txt, 820)
    tw = f.getlength(txt); st = Image.new("RGBA", (int(tw + 120), int(f.size * 1.5)), (0, 0, 0, 0)); g = ImageDraw.Draw(st)
    g.rectangle([6, 6, st.width - 6, st.height - 6], outline=col + (255,), width=14)
    g.text((st.width / 2, st.height / 2 + 4), txt, font=f, fill=col, anchor="mm")
    st = st.resize((max(1, int(st.width * s)), max(1, int(st.height * s))), Image.BICUBIC).rotate(-8, expand=True, resample=Image.BICUBIC)
    if k < 1: st.putalpha(st.getchannel("A").point(lambda a: int(a * k)))
    L.alpha_composite(st, (int(W / 2 - st.width / 2), int(330 - st.height / 2)))
    return L

def h_final(v, t, D):
    L, d = layer(); b = abs(math.sin(t * 5)) * 30
    d.text((W / 2 - 40, 150), v.get("text", "COMENTA"), font=font(ANTON, 160), fill=WHITE, anchor="mm", stroke_width=8, stroke_fill=(0, 0, 0))
    cx, cy = W / 2 - 40, 380 + b
    d.polygon([(cx - 60, cy - 110), (cx + 60, cy - 110), (cx + 60, cy), (cx + 130, cy), (cx, cy + 140), (cx - 130, cy), (cx - 60, cy)], fill=YEL, outline=INK)
    return L

HEROES = dict(score=h_score, counter=h_counter, place=h_place, redcard=h_redcard, big=h_big, items=h_items, player=h_player,
              badges=h_badges, clock=h_clock, tactic=h_tactic, stamp=h_stamp, final=h_final)

def hero_layer(card, t, D):
    v = card.get("hero")
    if not v: return None
    if v["type"] == "quiz": return h_quiz(v, t, D, card)
    return HEROES[v["type"]](v, t, D)

# ---------------------------------------------------------------- tiempos
def card_duration(c):
    n = nchars(c["text"])
    if c.get("_dur"):  # con relato: lo que dura la voz + un respiro
        D = T0 + c["_dur"] + c.get("pad", 0.35)
    else:
        te = T0 + n / TYPE_CPS; D = te + max(1.2, n / 26)
    if c.get("d"): D = max(D, float(c["d"])) if c.get("_dur") else float(c["d"])
    v = c.get("hero") or {}
    ty = v.get("type")
    if ty == "quiz" and v.get("reveal") is None: D = max(D, quiz_cstart(c) + 3.3)
    if ty == "counter": D = max(D, v.get("st", 0.2) + v.get("dur", 1.4) + 0.9)
    if ty == "score" and v.get("roll"): D = max(D, v["roll"] + 1.0)
    if ty == "score" and v.get("steps"): D = max(D, v["steps"][-1][0] + 1.3)
    if ty == "tactic": D = max(D, 0.3 + len(v["path"]) * v.get("step", 0.7) + 1.0)
    if ty == "badges": D = max(D, 0.25 + len(v["items"]) * 0.6 + 1.0)
    if ty == "final": D = max(D, 2.6)
    return round(D * FPS) / FPS

# ---------------------------------------------------------------- render
def frame(cards, ci, t, starts, total):
    c = cards[ci]; D = starts[ci + 1] - starts[ci]; tg = starts[ci] + t
    im = background(tg)
    hl = hero_layer(c, t, D)
    if hl is not None:
        if t < 0.22:  # entrada: pequeño zoom
            s = 0.9 + 0.1 * eo(t / 0.22)
            hl = hl.resize((int(W * s), int(HERO_H * s)), Image.BILINEAR)
            im.alpha_composite(hl, (int((W - hl.width) / 2), int(HERO_Y + (HERO_H - hl.height) / 2)))
        else:
            im.alpha_composite(hl, (0, HERO_Y))
    draw_text(im, c["text"], t, c.get("_cps", TYPE_CPS))
    topbar(im, tg, total)
    im = im.convert("RGB")
    if ci > 0 and t < 3 / FPS:  # destello al cambiar de tarjeta
        im = Image.blend(im, Image.new("RGB", (W, H), (255, 255, 255)), 0.28 * (1 - t * FPS / 3))
    return im

def render_card(args):
    vd, ci, out = args
    cards, starts, total = plan(vd)
    D = starts[ci + 1] - starts[ci]; n = int(round(D * FPS))
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(n): p.stdin.write(frame(cards, ci, i / FPS, starts, total).tobytes())
    p.stdin.close(); p.wait(); assert p.returncode == 0
    return out

def load(vd):
    ns = {}; exec(open(os.path.join(vd, "guion.py"), encoding="utf-8").read(), ns); return ns

def plain(text):
    return " ".join(wtext(w) for w in parse(text))

def word_time(c, word):
    """Momento (desde el inicio de la tarjeta) en que la voz dice esa palabra, por proporción de caracteres."""
    say = c.get("say") or plain(c["text"]); i = say.find(word)
    if i < 0: i = plain(c["text"]).find(word); total = len(plain(c["text"]))
    else: total = len(say)
    return T0 + max(0, i) / max(1, total) * c.get("_dur", total / TYPE_CPS)

def audio_path(vd, ci): return os.path.join(vd, "audio", f"c{ci:02d}.mp3")

def dur_of(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout)

def plan(vd):
    global CHANNEL
    ns = load(vd); cards = [dict(c) for c in ns["CARDS"]]; starts = [0.0]
    CHANNEL = ns.get("CHANNEL", CHANNEL)
    for ci, c in enumerate(cards):
        if ns.get("VOICE"):
            a = audio_path(vd, ci)
            c["_dur"] = dur_of(a) if os.path.exists(a) else len(c.get("say") or plain(c["text"])) / 15.0
            c["_cps"] = max(8.0, nchars(c["text"]) / max(0.5, c["_dur"] * 0.9))   # el texto termina un poco antes que la voz
            v = c.get("hero") or {}
            if v.get("steps"): v["steps"] = [(word_time(c, ts) if isinstance(ts, str) else ts, a_, b_) for ts, a_, b_ in v["steps"]]
            if isinstance(c.get("cut"), str): c["cut"] = word_time(c, c["cut"])
        starts.append(starts[-1] + card_duration(c))
    return cards, starts, starts[-1]

# ---------------------------------------------------------------- sonido (sintetizado)
def env_exp(n, tau): return np.exp(-np.arange(n) / (tau * SR))
RNG = np.random.default_rng(11)

def s_type():
    n = int(0.018 * SR); x = RNG.normal(0, 1, n) * env_exp(n, 0.003)
    return np.convolve(x, [0.6, -0.4], "same") * 0.5
def s_click():
    n = int(0.05 * SR); tt = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1800 * tt) * env_exp(n, 0.008) + 0.3 * RNG.normal(0, 1, n) * env_exp(n, 0.002)) * 0.6
def s_tick():
    n = int(0.03 * SR); tt = np.arange(n) / SR
    return np.sin(2 * np.pi * 1250 * tt) * env_exp(n, 0.006) * 0.5
def s_tock():
    n = int(0.12 * SR); tt = np.arange(n) / SR
    return (np.sin(2 * np.pi * 820 * tt) + 0.5 * np.sin(2 * np.pi * 1640 * tt)) * env_exp(n, 0.03) * 0.8
def s_boom():
    n = int(0.7 * SR); tt = np.arange(n) / SR
    x = np.sin(2 * np.pi * (75 * tt - 30 * tt ** 2)) * np.exp(-tt * 6) + 0.3 * RNG.normal(0, 1, n) * np.exp(-tt * 35)
    return x / np.max(np.abs(x)) * 0.9
def s_whoosh():
    n = int(0.45 * SR); tt = np.arange(n) / SR; x = RNG.normal(0, 1, n); y = np.zeros(n); a = 0.0
    for i in range(n): a += (0.03 + 0.3 * i / n) * (x[i] - a); y[i] = a
    y *= np.sin(np.pi * tt / 0.45) ** 2; return y / np.max(np.abs(y)) * 0.45
def s_whistle(dur=0.5):
    n = int(dur * SR); tt = np.arange(n) / SR
    f = 3100 + 60 * np.sin(2 * np.pi * 9 * tt)
    ph = 2 * np.pi * np.cumsum(f) / SR
    trill = 0.65 + 0.35 * np.sign(np.sin(2 * np.pi * 34 * tt))
    x = (np.sin(ph) + 0.25 * np.sin(2 * ph)) * trill + 0.08 * RNG.normal(0, 1, n)
    e = np.minimum(1, tt / 0.02) * np.minimum(1, (dur - tt) / 0.05)
    return x * e * 0.45
def s_final_whistle():
    a, b = s_whistle(0.28), s_whistle(0.9); gap = np.zeros(int(0.14 * SR))
    return np.concatenate([a, gap, a, gap, b])
def s_cash():
    n = int(0.9 * SR); tt = np.arange(n) / SR
    bell = sum(np.sin(2 * np.pi * f * tt) * np.exp(-tt * d) for f, d in [(2093, 5), (2637, 6), (3136, 7), (4186, 9)])
    x = np.zeros(n); m = int(0.06 * SR); x[:m] += RNG.normal(0, 1, m) * env_exp(m, 0.01) * 0.8
    x[int(0.05 * SR):] += bell[: n - int(0.05 * SR)] * 0.35
    return x * 0.8
def s_ding():
    n = int(0.8 * SR); tt = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1318 * tt) + 0.6 * np.sin(2 * np.pi * 1975 * tt)) * np.exp(-tt * 5) * 0.45
def s_buzz():
    n = int(0.35 * SR); tt = np.arange(n) / SR
    return np.sign(np.sin(2 * np.pi * 150 * tt)) * 0.2 * np.minimum(1, (0.35 - tt) / 0.05)
def crowd(seconds, seed=5):
    n = int(seconds * SR); x = np.random.default_rng(seed).normal(0, 1, n)
    y = np.zeros(n); a = b = 0.0
    for i in range(n):  # paso banda casero
        a += 0.18 * (x[i] - a); b += 0.02 * (a - b); y[i] = a - b
    tt = np.arange(n) / SR
    y *= 0.75 + 0.25 * np.sin(2 * np.pi * 0.6 * tt) * np.sin(2 * np.pi * 0.23 * tt + 1)
    return y / np.max(np.abs(y)) * 0.5

def sfx_and_env(cards, starts, total):
    n = int((total + 1.5) * SR); fx = np.zeros(n); mus = np.ones(n); crd = np.zeros(n)
    def put(sig, at, vol=1.0):
        i = int(at * SR); j = min(n, i + len(sig))
        if 0 <= i < n: fx[i:j] += sig[: j - i] * vol
    typ = s_type(); clk = s_click(); tick = s_tick(); boom = s_boom(); wh = s_whoosh()
    crowd_bed = None
    for ci, c in enumerate(cards):
        t0 = starts[ci]; D = starts[ci + 1] - t0; v = c.get("hero") or {}; ty = v.get("type")
        if ci > 0: put(wh, t0 - 0.12, 0.5)
        # tecleo
        nn = nchars(c["text"]); rr = np.random.default_rng(ci); cps = c.get("_cps", TYPE_CPS)
        tv = 0.12 if c.get("_dur") else 0.35          # con relato, el tecleo va muy por debajo de la voz
        for k in range(nn):
            if rr.random() < (0.6 if c.get("_dur") else 0.85): put(typ, t0 + T0 + k / cps, tv + 0.1 * rr.random())
        for ht in hl_times(c["text"], cps): put(clk, t0 + ht, 0.35 if c.get("_dur") else 0.55)
        # animaciones
        if ty == "score":
            if v.get("roll"):
                k = 0.15
                while k < 0.15 + v["roll"] * 0.85: put(tick, t0 + k, 0.5); k += 0.06
                put(boom, t0 + 0.15 + v["roll"] * 0.9, 0.9)
            for (ts, _, _) in v.get("steps", []): put(boom, t0 + ts, 0.9)
        if ty == "counter":
            st, du = v.get("st", 0.2), v.get("dur", 1.4); k = st
            if v["to"] != v.get("frm", 0):
                while k < st + du * 0.8: put(tick, t0 + k, 0.45); k += 0.055
                put(s_cash() if v.get("style") == "tag" else boom, t0 + st + du * 0.85, 0.9)
        if ty == "quiz":
            if v.get("reveal") is None:
                cs = quiz_cstart(c)
                for s in range(3): put(s_tock(), t0 + cs + s, 0.8)
                put(s_buzz(), t0 + cs + 3, 0.6)
            else:
                put(s_ding(), t0 + 0.05, 0.9); put(boom, t0 + 0.05, 0.7)
        if ty == "place": put(boom[: int(0.25 * SR)], t0 + 0.4, 0.7)
        if ty == "redcard": put(s_whistle(0.55), t0 + 0.05, 0.9)
        if ty in ("big", "stamp"): put(boom, t0 + 0.12, 0.9)
        if ty == "items":
            for i in range(len(v["items"])): put(clk, t0 + 0.3 + i * 0.55, 0.7)
        if ty == "player": put(wh, t0, 0.4)
        if ty == "badges":
            for i in range(len(v["items"])): put(boom, t0 + 0.3 + i * 0.6, 0.75)
        if ty == "clock":
            k = 0.2
            while k < 0.2 + v.get("dur", 1.1): put(tick, t0 + k, 0.5); k += 0.09
            put(s_tock(), t0 + 0.25 + v.get("dur", 1.1), 0.8)
        if ty == "tactic":
            st = v.get("step", 0.7)
            for i, seg in enumerate(v["path"]):
                put(wh[: int(0.3 * SR)], t0 + 0.3 + i * st, 0.35)
                if seg[4] == "tiro": put(boom[: int(0.35 * SR)], t0 + 0.3 + i * st, 0.7); put(boom, t0 + 0.3 + (i + 0.8) * st, 0.8)
        if ty == "final": put(s_final_whistle(), t0 + 0.2, 0.8)
        for (name, at) in c.get("sfx", []):
            put({"whistle": s_whistle(0.5), "boom": boom, "cash": s_cash(), "ding": s_ding()}[name], t0 + at, 0.8)
        # hinchada y silencio
        if c.get("crowd"):
            if crowd_bed is None: crowd_bed = crowd(total + 1.5)
            i, j = int(t0 * SR), int((t0 + D) * SR); crd[i:j] = 1.0
            for (ts, _, _) in v.get("steps", []):  # rugido en cada gol
                a = int((t0 + ts) * SR); b = min(n, a + int(1.6 * SR)); crd[a:b] = np.maximum(crd[a:b], 1 + 1.6 * np.exp(-np.arange(b - a) / (0.6 * SR)))
        if c.get("cut"):
            ht = hl_times(c["text"], c.get("_cps", TYPE_CPS)); at = t0 + (ht[-1] if ht else 0.3)
            if c.get("_dur"): at = t0 + T0 + c["_dur"]
            if isinstance(c["cut"], (int, float)) and not isinstance(c["cut"], bool): at = t0 + c["cut"]
            i, j = int(at * SR), int((t0 + D) * SR)
            mus[i:j] = 0.0; crd[i:j] = 0.0
            put(boom, at, 0.6)
    # suavizar envolventes (20 ms) para que los cortes no hagan clic
    k = int(0.02 * SR); ker = np.ones(k) / k
    mus = np.convolve(mus, ker, "same"); crd = np.convolve(crd, ker, "same")
    crowd_sig = (crowd_bed[:n] * crd * 0.55) if crowd_bed is not None else 0
    return fx, mus, crowd_sig

def decode(path, seconds):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-t", f"{seconds:.3f}", "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2)

def build_audio(vd, cards, starts, total, out):
    ns = load(vd); n = int((total + 1.5) * SR)
    fx, mus, crowd_sig = sfx_and_env(cards, starts, total)
    tracks = sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(vd)), "music", "*.mp3")))
    music = np.zeros((n, 2)); voice = np.zeros((n, 2))
    if ns.get("VOICE"):  # relato: cada tarjeta empieza a hablar en T0
        for ci in range(len(cards)):
            a = decode(audio_path(vd, ci), 60); i = int((starts[ci] + T0) * SR); j = min(n, i + len(a))
            voice[i:j] += a[: j - i]
    if tracks and ns.get("MUSIC", 0) is not None:
        tr = tracks[ns.get("MUSIC", 0) % len(tracks)]
        m = decode(tr, total + ns.get("MUSIC_START", 0) + 2)[int(ns.get("MUSIC_START", 0) * SR):]
        m = m[:n]; music[: len(m)] = m
    tt = np.arange(n) / SR
    fade = np.minimum(1, tt / 0.3) * np.clip((total + 0.3 - tt) / 1.2, 0, 1)
    fxv = 0.75 if ns.get("VOICE") else 1.0
    mix = music * (mus * fade * float(ns.get("MUSIC_VOL", 0.5)))[:, None] + ((fx + crowd_sig) * fxv)[:, None] + voice
    mix = np.clip(mix[: int(total * SR)], -1, 1)
    tmp = out + ".raw.wav"
    with wave.open(tmp, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", str(SR), out], check=True)
    os.remove(tmp)

# ---------------------------------------------------------------- paquete de subida
def subir(vd, total):
    M = load(vd)["META"]; E = os.path.join(vd, "entrega"); os.makedirs(E, exist_ok=True)
    ns = load(vd)
    aviso = "Gráficos y animación hechos para este canal. Relato con voz generada por IA." if ns.get("VOICE") else \
        "Gráficos y animación hechos para este canal. Música de fondo generada con IA para el canal."
    desc = M["description"].rstrip() + "\n\nFuentes:\n" + "\n".join("• " + s for s in M["sources"]) + \
        "\n\n" + aviso + "\n" + " ".join(M.get("hashtags", ["#futbol", "#shorts"]))
    L = [f"# 📱 SUBIR · {ns.get('CHANNEL', CHANNEL).title().replace(' De ', ' de ')} · Short {M['code']} — `{M['code']}.mp4` ({total:.0f} s)", "",
         "**Título**", "```", M["title"], "```", "**Descripción**", "```", desc, "```",
         "**Etiquetas**", "```", ", ".join(M["tags"]), "```",
         "**Ajustes al subir**",
         "- Contenido para niños: **No**",
         "- Contenido alterado o sintético: **No** (gráficos animados, nada realista" + ("; el relato es una voz de IA genérica, avisada en la descripción)" if ns.get("VOICE") else ")"),
         "- Categoría: **Deportes** · Idioma: **Español**",
         "- Listas de reproducción: " + (" + ".join(f"**{x}**" for x in M.get("playlists", [])) or "—"),
         f"- Comentario fijado: `{M.get('pinned', M.get('question', ''))}`",
         "- Miniatura: en la app, elige el fotograma donde ya se ve completa la cifra o el marcador grande (hacia el segundo 2).",
         "- Publicar **un Short al día como máximo**, idealmente entre las 18:00 y las 21:00 (hora de Argentina).", ""]
    open(os.path.join(E, "SUBIR.md"), "w", encoding="utf-8").write("\n".join(L))

def sheet(vd, cards, starts, total):
    B = os.path.join(vd, "build"); os.makedirs(B, exist_ok=True); ims = []
    for ci, c in enumerate(cards):
        D = starts[ci + 1] - starts[ci]
        ims.append(frame(cards, ci, D - 0.35, starts, total).resize((270, 480)))
    o = Image.new("RGB", (270 * len(ims), 480))
    for i, im in enumerate(ims): o.paste(im, (i * 270, 0))
    o.save(os.path.join(B, "hoja.png")); print(os.path.join(B, "hoja.png"), f"{total:.1f} s")

def tts_cards(vd):
    """Relato: genera audio/cNN.mp3 de cada tarjeta que no lo tenga (say o el texto sin marcas; PRONUNCIA solo para la voz)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import tts, concurrent.futures as cf
    ns = load(vd); os.makedirs(os.path.join(vd, "audio"), exist_ok=True); say = tts.pronounce(ns.get("PRONUNCIA") or {})
    todo = [(ci, say(c.get("say") or plain(c["text"]))) for ci, c in enumerate(ns["CARDS"]) if not os.path.exists(audio_path(vd, ci))]
    with cf.ThreadPoolExecutor(4) as ex:
        fs = {ex.submit(tts.tts, txt, ns["VOICE"], audio_path(vd, ci), float(ns.get("SPEED", 1.05))): ci for ci, txt in todo}
        for f in cf.as_completed(fs): f.result(); print("voz", f"c{fs[f]:02d}", flush=True)

def main(vd, frames_only=False):
    if load(vd).get("VOICE") and not frames_only: tts_cards(vd)
    cards, starts, total = plan(vd)
    if frames_only: return sheet(vd, cards, starts, total)
    B = os.path.join(vd, "build"); os.makedirs(B, exist_ok=True)
    jobs = [(vd, ci, os.path.join(B, f"c{ci:02d}.mp4")) for ci in range(len(cards))]
    with ProcessPoolExecutor(max_workers=4) as ex:
        for o in ex.map(render_card, jobs): print("tarjeta", os.path.basename(o), flush=True)
    lst = os.path.join(B, "lista.txt"); open(lst, "w").write("".join(f"file '{os.path.abspath(j[2])}'\n" for j in jobs))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", os.path.join(B, "video.mp4")], check=True)
    build_audio(vd, cards, starts, total, os.path.join(B, "audio.wav"))
    M = load(vd)["META"]; E = os.path.join(vd, "entrega"); os.makedirs(E, exist_ok=True)
    out = os.path.join(E, f"{M['code']}.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(B, "video.mp4"), "-i", os.path.join(B, "audio.wav"),
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", "-movflags", "+faststart", out], check=True)
    subir(vd, total); print(out, f"{total:.1f} s")

if __name__ == "__main__":
    main(sys.argv[1], "--frames" in sys.argv)
