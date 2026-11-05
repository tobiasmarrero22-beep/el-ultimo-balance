"""Animador de escenas: genera cada escena como MP4 (sin audio) y monta el vídeo final.
Uso: python3 pipeline/render.py <carpeta_video> long
     python3 pipeline/render.py <carpeta_video> short <nombre>   (nombre: clave de SHORTS en guion.py)
"""
import glob, math, os, subprocess, sys, json, random
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTS = os.path.join(ROOT, "assets", "fonts")
VD = os.environ.get("VD", "")  # carpeta del vídeo (se fija en main)
ANTON = os.path.join(FONTS, "Anton.ttf")
INTER_B = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "fonts", "InterDisplay-Black.otf")
INTER_SB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "fonts", "InterDisplay-SemiBold.otf")
FPS = 30
BG = (11, 15, 23)
RED = (230, 57, 70)
YEL = (255, 209, 102)
WHITE = (245, 245, 240)
GREY = (150, 158, 170)

_font_cache = {}
def font(path, size):
    k = (path, size)
    if k not in _font_cache: _font_cache[k] = ImageFont.truetype(path, size)
    return _font_cache[k]

def ease_out(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def ease_io(x): x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)

def dur_of(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                capture_output=True, text=True).stdout)

def fmt_num(v, prefix="", suffix=""):
    neg = v < 0; v = abs(int(round(v)))
    s = f"{v:,}".replace(",", ".")
    return ("-" if neg else "") + prefix + s + suffix

# ---------- utilidades de dibujo ----------
_BG = None  # (imagen desenfocada, duración, semilla) — fondo en movimiento de las escenas de gráficos

def bg_source(key):
    """Imagen de la escena anterior, pequeña, desenfocada y oscurecida: sirve de fondo vivo detrás del texto."""
    im = load_img(key).resize((640, 360), Image.BILINEAR).filter(ImageFilter.GaussianBlur(5))
    im = ImageEnhance.Brightness(im).enhance(0.42)
    return Image.blend(im, Image.new("RGB", im.size, BG), 0.25)

def bg_canvas(W, H, t=0.0, tint=(0, 0, 0)):
    if _BG is not None:
        src, D, seed = _BG
        im = kenburns(src, W, H, min(1.0, t / max(D, 0.1)), "in" if seed % 2 else "out", seed, Image.BILINEAR)
    else:
        im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # rejilla sutil que se desplaza
    off = int((t * 12) % 60)
    for x in range(-60 + off, W, 60): d.line([(x, 0), (x, H)], fill=(18, 24, 35))
    for y in range(-60 + off, H, 60): d.line([(0, y), (W, y)], fill=(18, 24, 35))
    return im

def text_center(d, cx, y, txt, f, fill, anchor="mt"):
    d.text((cx, y), txt, font=f, fill=fill, anchor=anchor)

def tag(im, x, y, txt, p, scale=1.0):
    """Etiqueta roja que entra desde la izquierda. p = progreso 0..1"""
    if p <= 0: return
    f = font(INTER_B, int(40 * scale))
    d = ImageDraw.Draw(im)
    w = d.textlength(txt, font=f) + 44 * scale
    h = 70 * scale
    ww = int(w * ease_out(p))
    if ww < 4: return
    d.rectangle([x, y, x + ww, y + h], fill=RED)
    d.rectangle([x, y, x + int(8 * scale), y + h], fill=YEL)
    if p > 0.5:
        a = ease_out((p - 0.5) * 2)
        layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(layer).text((x + 26 * scale, y + h / 2), txt, font=f, fill=WHITE + (int(255 * a),), anchor="lm")
        im.paste(layer, (0, 0), layer)

# ---------- tipos de escena ----------
_img_cache = {}
def load_img(key):
    if key not in _img_cache:
        _img_cache[key] = Image.open(os.path.join(VD, "img", f"{key}.png")).convert("RGB")
    return _img_cache[key]

def kenburns(src, W, H, p, motion="in", seed=0, resample=Image.BICUBIC):
    sw, sh = src.size
    base = max(W / sw, H / sh)
    rnd = random.Random(seed)
    dx, dy = rnd.choice([-1, 1]) * 0.04, rnd.choice([-1, 1]) * 0.025
    z0, z1 = (1.0, 1.14) if motion == "in" else (1.14, 1.0)
    z = z0 + (z1 - z0) * ease_io(p)
    s = base * z
    cx = sw / 2 + dx * sw * (ease_io(p) - 0.5)
    cy = sh / 2 + dy * sh * (ease_io(p) - 0.5)
    # mapeo inverso: punto de salida (u,v) -> fuente
    a = 1 / s; e = 1 / s
    c = cx - (W / 2) * a; f = cy - (H / 2) * e
    return src.transform((W, H), Image.AFFINE, (a, 0, c, 0, e, f), resample=resample)

ANGLES = [  # (zoom inicial, zoom final, desplazamiento x, desplazamiento y) — planos de la misma foto
    (1.00, 1.10, 0.00, 0.00),    # general, acercándose
    (1.40, 1.48, -0.20, -0.12),  # detalle arriba-izquierda
    (1.40, 1.48, 0.20, 0.12),    # detalle abajo-derecha
    (1.22, 1.08, 0.00, 0.06),    # medio, alejándose
]
SEG = 4.0  # segundos por plano

def kb_angle(src, W, H, p, angle, seed):
    z0, z1, ox, oy = angle
    sw, sh = src.size; s = max(W / sw, H / sh) * (z0 + (z1 - z0) * ease_io(p))
    drift = random.Random(seed).choice([-1, 1]) * 0.04
    hw, hh = W / 2 / s, H / 2 / s
    cx = min(max(sw / 2 + ox * sw * 0.5 + drift * sw * (ease_io(p) - 0.5), hw), sw - hw)
    cy = min(max(sh / 2 + oy * sh * 0.5, hh), sh - hh)
    a = 1 / s
    return src.transform((W, H), Image.AFFINE, (a, 0, cx - (W / 2) * a, 0, a, cy - (H / 2) * a), resample=Image.BICUBIC)

def scene_img(v, t, D, W, H, seed):
    n = max(1, int(round(D / SEG))) if D >= 6 else 1
    if n == 1:
        im = kenburns(load_img(v["key"]), W, H, t / D, v.get("motion", "in"), seed)
    else:
        L = D / n; k = min(int(t / L), n - 1); tl = t - k * L
        order = [0, 1, 2, 3] if v.get("motion", "in") == "in" else [3, 2, 1, 0]
        im = kb_angle(load_img(v["key"]), W, H, tl / L, ANGLES[order[1 + (k - 1 + seed) % 3] if k else order[0]], seed + k)
        if k: im = punch(im, int(tl * FPS), frames=5, amount=0.045)  # corte entre planos
    if v.get("cap"):
        tag(im, int(W * 0.05), int(H * 0.80), v["cap"], (t - 0.35) / 0.6, scale=W / 1920)
    return im

def scene_title(v, t, D, W, H, seed):
    im = bg_canvas(W, H, t)
    d = ImageDraw.Draw(im)
    sc = W / 1920 * v.get("zoom", 1)
    # número de capítulo
    a = ease_out(t / 0.6)
    fn = font(ANTON, int(300 * sc))
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    ld.text((W / 2, H * 0.40 + (1 - a) * 60 * sc), v["num"], font=fn, fill=RED + (int(255 * a),), anchor="mm")
    im.paste(layer, (0, 0), layer)
    # línea
    lw = int(W * 0.5 * ease_out((t - 0.3) / 0.7))
    if lw > 0: d.rectangle([W / 2 - lw / 2, H * 0.58, W / 2 + lw / 2, H * 0.58 + 6 * sc], fill=YEL)
    # título
    b = ease_out((t - 0.5) / 0.6)
    if b > 0:
        ft = font(ANTON, int(110 * sc))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
        lines = wrap(v["text"], ft, W * 0.85)
        y = H * 0.63 + (1 - b) * 40 * sc
        for ln in lines:
            ld.text((W / 2, y), ln, font=ft, fill=WHITE + (int(255 * b),), anchor="mt"); y += 125 * sc
        im.paste(layer, (0, 0), layer)
    # fundido de entrada desde negro
    if t < 0.25: im = Image.blend(Image.new("RGB", (W, H), (0, 0, 0)), im, t / 0.25)
    return im

def wrap(txt, f, maxw):
    words, lines, cur = txt.split(), [], ""
    dd = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    for w in words:
        test = (cur + " " + w).strip()
        if dd.textlength(test, font=f) <= maxw: cur = test
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def scene_num(v, t, D, W, H, seed):
    im = bg_canvas(W, H, t); d = ImageDraw.Draw(im); sc = W / 1920 * v.get("zoom", 1)
    p = ease_out(t / min(D * 0.7, 2.5))
    val = v["start"] + (v["end"] - v["start"]) * p
    down = v["end"] < v["start"] or v["end"] < 0
    col = RED if down else YEL
    txt = fmt_num(val, v.get("prefix", ""), v.get("suffix", "") if round(val) != 0 else "")
    fs = int(260 * sc) if len(txt) < 9 else int(200 * sc)
    d.text((W / 2, H * 0.45), txt, font=font(ANTON, fs), fill=col, anchor="mm")
    a = ease_out((t - 0.3) / 0.5)
    if a > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(layer).text((W / 2, H * 0.68), v["label"], font=font(INTER_B, int(54 * sc)), fill=WHITE + (int(255 * a),), anchor="mm")
        im.paste(layer, (0, 0), layer)
    return im

def scene_year(v, t, D, W, H, seed):
    im = bg_canvas(W, H, t); d = ImageDraw.Draw(im); sc = W / 1920 * v.get("zoom", 1)
    # línea de tiempo
    d.rectangle([0, H * 0.5 - 2 * sc, W, H * 0.5 + 2 * sc], fill=(40, 48, 62))
    k = ease_out(t / 0.45)
    s = 1.35 - 0.35 * k
    fy = font(ANTON, int(230 * sc * s if len(v["year"]) <= 4 else 170 * sc * s))
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    bw = ld.textlength(v["year"], font=fy) + 80 * sc
    ld.rectangle([W / 2 - bw / 2, H * 0.5 - 150 * sc * s, W / 2 + bw / 2, H * 0.5 + 150 * sc * s], fill=BG + (int(255 * k),))
    ld.text((W / 2, H * 0.5), v["year"], font=fy, fill=YEL + (int(255 * k),), anchor="mm")
    im.paste(layer, (0, 0), layer)
    a = ease_out((t - 0.4) / 0.5)
    if a > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(layer).text((W / 2, H * 0.78), v["sub"], font=font(INTER_B, int(60 * sc)), fill=WHITE + (int(255 * a),), anchor="mm")
        im.paste(layer, (0, 0), layer)
    return im

def scene_bars(v, t, D, W, H, seed):
    im = bg_canvas(W, H, t); d = ImageDraw.Draw(im); sc = W / 1920 * v.get("zoom", 1)
    d.text((W * 0.08, H * 0.09), v["title"], font=fit_font(INTER_B, int(52 * sc), v["title"], W * (0.58 if v.get("note") else 0.84)), fill=WHITE, anchor="lt")
    data = v["data"]; n = len(data)
    vmax = max(x[1] for x in data) * 1.12
    x0, x1 = W * 0.12, W * 0.88
    base_y, top_y = H * 0.86, H * 0.24
    slot = (x1 - x0) / max(n, 2)
    bw = slot * 0.62
    per = min(D * 0.75, 1.0 + 0.9 * n) / n
    for i, (lab, val) in enumerate(data):
        p = ease_out((t - i * per * 0.8) / per)
        if p <= 0: continue
        cx = x0 + slot * (i + 0.5) if n > 1 else W / 2
        h = (base_y - top_y) * (val / vmax) * p
        col = YEL if i == 0 else RED
        d.rectangle([cx - bw / 2, base_y - h, cx + bw / 2, base_y], fill=col)
        d.text((cx, base_y + 18 * sc), lab, font=font(INTER_B, int(46 * sc)), fill=GREY, anchor="mt")
        d.text((cx, base_y - h - 14 * sc), fmt_num(val * p), font=font(ANTON, int(78 * sc)), fill=WHITE, anchor="mb")
    if v.get("note"):
        a = ease_out((t - per * n) / 0.5)
        if a > 0:
            layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
            ld.rounded_rectangle([W * 0.70, H * 0.08, W * 0.92, H * 0.22], radius=int(18 * sc), fill=RED + (int(255 * a),))
            ld.text((W * 0.81, H * 0.15), v["note"], font=font(ANTON, int(96 * sc)), fill=WHITE + (int(255 * a),), anchor="mm")
            im.paste(layer, (0, 0), layer)
    d.line([(x0 - 20 * sc, base_y), (x1 + 20 * sc, base_y)], fill=GREY, width=max(2, int(3 * sc)))
    return im

def scene_quote(v, t, D, W, H, seed):
    im = bg_canvas(W, H, t); sc = W / 1920 * v.get("zoom", 1)
    lines = v["text"].split("\n")
    fs = int((130 if len(lines) <= 3 else 100) * sc)
    f = font(ANTON, fs)
    lh = fs * 1.18
    y0 = H / 2 - lh * len(lines) / 2 + lh / 2
    step = min(0.55, D * 0.6 / max(1, len(lines)))
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    for i, ln in enumerate(lines):
        a = ease_out((t - i * step) / 0.45)
        if a <= 0: continue
        col = YEL if (i == len(lines) - 1 and len(lines) > 1) else WHITE
        if ln.startswith("ERROR") or ln.startswith("→"): col = RED
        ld.text((W / 2, y0 + i * lh + (1 - a) * 30 * sc), ln, font=f, fill=col + (int(255 * a),), anchor="mm")
    im.paste(layer, (0, 0), layer)
    return im

def scene_lines(v, t, D, W, H, seed):
    """Gráfica de líneas que se dibuja de izquierda a derecha. series: [[nombre, valores, color], ...]"""
    im = bg_canvas(W, H, t); d = ImageDraw.Draw(im); sc = W / 1920 * v.get("zoom", 1)
    d.text((W * 0.08, H * 0.08), v["title"], font=font(INTER_B, int(48 * sc)), fill=WHITE, anchor="lt")
    xs = v["x"]; n = len(xs)
    vmax = max(max(s[1]) for s in v["series"]) * 1.15
    x0, x1, y0, y1 = W * 0.10, W * 0.80, H * 0.85, H * 0.22
    step = 10 ** int(math.log10(vmax)); step = step / 2 if vmax / step < 4 else step
    k = 0.0
    while k <= vmax:
        yy = y0 - (y0 - y1) * k / vmax
        d.line([(x0, yy), (x1, yy)], fill=(30, 38, 52), width=max(1, int(2 * sc)))
        d.text((x0 - 16 * sc, yy), fmt_num(k), font=font(INTER_SB, int(30 * sc)), fill=GREY, anchor="rm"); k += step
    px = lambda i: x0 + (x1 - x0) * i / (n - 1)
    py = lambda val: y0 - (y0 - y1) * val / vmax
    for i, lab in enumerate(xs):
        d.text((px(i), y0 + 18 * sc), lab, font=font(INTER_B, int(38 * sc)), fill=GREY, anchor="mt")
    p = ease_io(t / max(1.0, min(D * 0.8, 5.0))) * (n - 1)
    cols = {"red": RED, "white": WHITE, "yellow": YEL}
    for name, vals, c in v["series"]:
        col = cols.get(c, WHITE)
        pts = [(px(i), py(vals[i])) for i in range(int(p) + 1)]
        if int(p) < n - 1:
            f = p - int(p); a, b = vals[int(p)], vals[int(p) + 1]
            pts.append((px(p), py(a + (b - a) * f)))
        if len(pts) > 1: d.line(pts, fill=col, width=int(10 * sc), joint="curve")
        ex, ey = pts[-1]
        d.ellipse([ex - 14 * sc, ey - 14 * sc, ex + 14 * sc, ey + 14 * sc], fill=col)
        cur = vals[min(int(round(p)), n - 1)] if p >= n - 1 else (vals[int(p)] + (vals[min(int(p) + 1, n - 1)] - vals[int(p)]) * (p - int(p)))
        d.text((ex + 30 * sc, ey), f"{name} {fmt_num(cur)}", font=font(ANTON, int(56 * sc)), fill=col, anchor="lm")
    return im

def fit_font(path, size, txt, maxw):
    dd = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    while size > 20 and dd.textlength(txt, font=font(path, size)) > maxw: size -= 4
    return font(path, size)

def scene_versus(v, t, D, W, H, seed):
    """Antes / después (o A vs B): left=[cifra, texto], right=[cifra, texto], mid="→" o "VS", title opcional."""
    im = bg_canvas(W, H, t); sc = W / 1920 * v.get("zoom", 1)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    if v.get("title"):
        ld.text((W / 2, H * 0.12), v["title"], font=fit_font(INTER_B, int(50 * sc), v["title"], W * 0.9), fill=GREY + (255,), anchor="mt")
    cols = {"yellow": YEL, "red": RED, "white": WHITE}
    for side, (top, bottom), col, delay in (("l", v["left"], cols[v.get("lcol", "yellow")], 0.0),
                                            ("r", v["right"], cols[v.get("rcol", "red")], v.get("delay", 0.6))):
        a = ease_out((t - delay) / 0.5)
        if a <= 0: continue
        sgn = -1 if side == "l" else 1
        cx = W / 2 + sgn * W * 0.24 + sgn * (1 - a) * W * 0.12
        ft = fit_font(ANTON, int(170 * sc), top, W * 0.40)
        ld.text((cx, H * 0.45), top, font=ft, fill=col + (int(255 * a),), anchor="mm")
        fb = font(INTER_B, int(46 * sc))
        for k, ln in enumerate(bottom.split("\n")):
            ld.text((cx, H * 0.62 + k * 66 * sc), ln, font=fit_font(INTER_B, int(56 * sc), ln, W * 0.44), fill=WHITE + (int(255 * a),), anchor="mt")
    m = ease_out((t - 0.35) / 0.4)
    if m > 0:
        ld.text((W / 2, H * 0.45), v.get("mid", "→"), font=font(ANTON, int(130 * sc)), fill=WHITE + (int(255 * m),), anchor="mm")
    im.paste(layer, (0, 0), layer)
    return im

def scene_stamp(v, t, D, W, H, seed):
    """Titular arriba + sello rojo que cae encima. text="línea1\nlínea2", stamp="TEXTO"."""
    im = bg_canvas(W, H, t); sc = W / 1920 * v.get("zoom", 1)
    lines = v["text"].split("\n")
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    fs = int(96 * sc); lh = fs * 1.2
    y0 = H * 0.30 - lh * (len(lines) - 1) / 2
    for i, ln in enumerate(lines):
        a = ease_out((t - i * 0.25) / 0.45)
        if a > 0:
            ld.text((W / 2, y0 + i * lh + (1 - a) * 25 * sc), ln, font=fit_font(ANTON, fs, ln, W * 0.9), fill=WHITE + (int(255 * a),), anchor="mm")
    im.paste(layer, (0, 0), layer)
    t0 = v.get("at", 0.5 + 0.25 * len(lines))
    if t >= t0:
        k = ease_out((t - t0) / 0.22)
        s = 1.7 - 0.7 * k
        size = int(v.get("size", 190) * sc * s)
        txt = v["stamp"]
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        f = font(ANTON, size); tw = d2.textlength(txt, font=f)
        cx, cy = W / 2, H * 0.66
        col = RED + (int(255 * min(1, k * 1.5)),)
        d2.rectangle([cx - tw / 2 - 34 * sc * s, cy - size * 0.64, cx + tw / 2 + 34 * sc * s, cy + size * 0.64], outline=col, width=max(4, int(16 * sc * s)))
        d2.text((cx, cy), txt, font=f, fill=col, anchor="mm")
        lay = lay.rotate(v.get("angle", -7), center=(cx, cy), resample=Image.BICUBIC)
        im.paste(lay, (0, 0), lay)
    return im

RENDER = dict(img=scene_img, title=scene_title, num=scene_num, year=scene_year, bars=scene_bars, quote=scene_quote, lines=scene_lines, versus=scene_versus, stamp=scene_stamp)

def punch(im, i, frames=7, amount=0.06):
    """Entrada de escena: pequeño zoom que se asienta (simula un corte con transición)."""
    if i >= frames: return im
    s = 1 + amount * (1 - ease_out(i / frames))
    W, H = im.size; cw, ch = W / s, H / s
    return im.crop((int((W - cw) / 2), int((H - ch) / 2), int((W + cw) / 2), int((H + ch) / 2))).resize((W, H), Image.BILINEAR)

def clip_path(key):
    p = os.path.join(VD, "clips", f"{key}.mp4")
    return p if os.path.exists(p) else None

def clip_frames(key, D, W, H, seed=0):
    """Fotogramas de un clip ajustado a D segundos (ida y vuelta + ralentí si hace falta), recortado a WxH.
    Si el clip es más largo que la escena, empieza en un punto distinto según la semilla (tomas de stock largas)."""
    src = clip_path(key); c = max(0.5, dur_of(src)); n = int(round(D * FPS))
    ss = ((seed * 5.3) % (c - D - 0.5)) if c > D + 1.0 else 0.0
    c -= ss
    if D <= c * 1.6:
        chain = f"[0:v]setpts=PTS*{max(D / c, 1.0):.4f}"
    else:
        chain = f"[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0,setpts=PTS*{max(D / (2 * c), 1.0):.4f}"
    vf = f"{chain},fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}[v]"
    p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-ss", f"{ss:.2f}", "-i", src, "-filter_complex", vf, "-map", "[v]", "-frames:v", str(n),
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    last = None; size = W * H * 3
    for _ in range(n):
        buf = p.stdout.read(size)
        if len(buf) == size: last = Image.frombytes("RGB", (W, H), buf)
        yield last.copy() if last is not None else Image.new("RGB", (W, H), BG)
    p.stdout.close(); p.wait()

def encode(frames_fn, n, W, H, out):
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(frames_fn(i).tobytes())
    p.stdin.close(); p.wait()
    assert p.returncode == 0, out

def render_scene(args):
    sc, D, W, H, out, seed = args
    v = sc["visual"]; n = int(round(D * FPS))
    if v["type"] == "img" and clip_path(v["key"]) and v.get("clip", True):
        reader = clip_frames(v["key"], D, W, H, seed)
        def frame(i):
            im = next(reader)
            if v.get("cap"): tag(im, int(W * 0.05), int(H * 0.80), v["cap"], (i / FPS - 0.35) / 0.6, scale=W / 1920)
            return punch(im, i)
    else:
        global _BG
        bgk = v.get("bg")
        _BG = (bg_source(bgk), D, seed) if (v["type"] != "img" and bgk and os.path.exists(os.path.join(VD, "img", f"{bgk}.png"))) else None
        fn = RENDER[v["type"]]
        if v["type"] == "img":
            frame = lambda i: punch(fn(v, i / FPS, D, W, H, seed), i)
        else:
            frame = lambda i: punch(push_in(fn(v, i / FPS, D, W, H, seed), i / FPS / D), i)
    encode(frame, n, W, H, out)
    return out

def push_in(im, p, amount=0.03):
    """Acercamiento lento y continuo para que los gráficos no se queden quietos."""
    W, H = im.size; a = 1 / (1 + amount * ease_io(p))
    return im.transform((W, H), Image.AFFINE, (a, 0, (W - W * a) / 2, 0, a, (H - H * a) / 2), resample=Image.BILINEAR)

# ---------- Short vertical ----------
_bg_cache = {}
def short_frame(sc, t, D, W, H, seed, words_timing, title, fg=None):
    if sc.get("alt"):
        bg = bg_canvas(W, H, t)
        PH = int(W * 9 / 16 * 1.25)
        fg = RENDER[sc["alt"]["type"]](sc["alt"], t, D, W, PH, seed)
        ImageDraw.Draw(bg).rectangle([0, int(H * 0.30) - 6, W, int(H * 0.30) + PH + 5], fill=(40, 48, 62))
    elif fg is None:
        src = load_img(sc["key"])
        bg = kenburns(src, W, H, t / D, "in", seed).filter(ImageFilter.GaussianBlur(28))
        bg = Image.blend(bg, Image.new("RGB", (W, H), (0, 0, 0)), 0.45)
        fg = kenburns(src, W, int(W * 9 / 16 * 1.25), t / D, "in", seed + 1)
    else:
        src = load_img(sc["key"])
        if sc["key"] not in _bg_cache:
            b = kenburns(src, W, H, 0.5, "in", seed).filter(ImageFilter.GaussianBlur(28))
            _bg_cache[sc["key"]] = Image.blend(b, Image.new("RGB", (W, H), (0, 0, 0)), 0.45)
        bg = _bg_cache[sc["key"]].copy()
    y = int(H * 0.30); bg.paste(fg, (0, y))
    d = ImageDraw.Draw(bg)
    # cabecera
    d.rectangle([0, int(H * 0.12), W, int(H * 0.12) + 120], fill=RED)
    d.text((W / 2, int(H * 0.12) + 60), title, font=font(ANTON, 78), fill=WHITE, anchor="mm")
    # subtítulo palabra a palabra (bloques de hasta 3 palabras)
    chunk = None
    for (t0, t1, txt) in words_timing:
        if t0 <= t < t1: chunk = txt; break
    if chunk:
        f = font(ANTON, 104)
        lines = wrap(chunk.upper(), f, W * 0.86)
        yy = int(H * 0.72)
        for ln in lines:
            d.text((W / 2, yy), ln, font=f, fill=YEL, anchor="mt", stroke_width=8, stroke_fill=(0, 0, 0)); yy += 120
    return bg

def chunks_for(text, D, k=3):
    words = text.split()
    groups = [" ".join(words[i:i + k]) for i in range(0, len(words), k)]
    weights = [len(g) + 2 for g in groups]; tot = sum(weights)
    out, t = [], 0.0
    for g, w in zip(groups, weights):
        dt = D * w / tot; out.append((t, t + dt, g)); t += dt
    return out

def render_short_scene(args):
    global _BG
    _BG = None
    sc, D, A, out, seed, title = args
    W, H = 1080, 1920
    timing = chunks_for(sc["text"], A)
    n = int(round(D * FPS))
    if not sc.get("alt") and clip_path(sc["key"]):
        reader = clip_frames(sc["key"], D, W, int(W * 9 / 16 * 1.25), seed)
        encode(lambda i: punch(short_frame(sc, i / FPS, D, W, H, seed, timing, title, fg=next(reader)), i), n, W, H, out)
    else:
        encode(lambda i: punch(short_frame(sc, i / FPS, D, W, H, seed, timing, title), i), n, W, H, out)
    return out

# ---------- audio ----------
def ambient_pad(seconds, out):
    sr = 44100; t = np.arange(int(seconds * sr)) / sr
    chords = [[110.0, 164.81, 220.0, 261.63], [98.0, 146.83, 196.0, 233.08], [87.31, 130.81, 174.61, 220.0], [103.83, 155.56, 207.65, 246.94]]
    seg = 8.0; sig = np.zeros_like(t)
    for i, ch in enumerate(chords * int(seconds / (seg * 4) + 2)):
        s0 = i * seg
        if s0 > seconds: break
        m = (t >= s0 - 2) & (t < s0 + seg + 2)
        tt = t[m] - s0
        env = np.clip(np.minimum((tt + 2) / 2.5, (seg + 2 - tt) / 2.5), 0, 1)
        for f in ch:
            sig[m] += env * (np.sin(2 * np.pi * f * t[m]) + 0.3 * np.sin(2 * np.pi * f * 2.003 * t[m])) / len(ch)
    sig += 0.25 * np.sin(2 * np.pi * 55 * t) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.07 * t))
    pulse = (np.sin(2 * np.pi * 1.0 * t) > 0.97).astype(float)
    sig += 0.15 * np.convolve(pulse * np.random.default_rng(1).normal(0, 1, len(t)), np.exp(-np.arange(2000) / 300), "same")
    sig = sig / np.max(np.abs(sig)) * 0.5
    st = np.stack([sig, np.roll(sig, 300)], 1)
    import wave
    with wave.open(out, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((st * 32767).astype(np.int16).tobytes())

def whoosh(out):
    sr = 44100; n = int(0.7 * sr); t = np.arange(n) / sr
    noise = np.random.default_rng(7).normal(0, 1, n)
    env = np.sin(np.pi * t / 0.7) ** 2
    # filtro paso banda barrido simple
    y = np.zeros(n); a = 0.0
    for i in range(n):
        k = 0.02 + 0.25 * (i / n)
        a = a + k * (noise[i] - a); y[i] = a
    y = y * env; y = y / np.max(np.abs(y)) * 0.6
    import wave
    with wave.open(out, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((y * 32767).astype(np.int16).tobytes())

def shorts_of(ns):
    if "SHORTS" in ns: return ns["SHORTS"]
    return {"a": {"bar": ns.get("SHORT_BAR", "EL ÚLTIMO BALANCE"), "scenes": ns["SHORT"]}}

def has_img(key):
    return os.path.exists(os.path.join(VD, "img", f"{key}.png")) or bool(clip_path(key))

def with_fallback(scenes, fb, short=False):
    """Si falta la imagen de una escena, usa FALLBACK[id] (escena de código) en su lugar."""
    out = []
    for sc in scenes:
        key = sc["key"] if short else (sc["visual"].get("key") if sc["visual"]["type"] == "img" else None)
        if key and not has_img(key):
            if sc["id"] not in fb: raise SystemExit(f"falta img/{key}.png y no hay FALLBACK para {sc['id']}")
            print(f"{sc['id']}: sin img/{key}.png -> escena de reserva {fb[sc['id']]['type']}", flush=True)
            sc = dict(sc, alt=fb[sc["id"]]) if short else dict(sc, visual=fb[sc["id"]])
        out.append(sc)
    return out

def sig_of(sc):
    v = sc.get("visual") or {"key": sc.get("key"), "alt": sc.get("alt")}
    key = v.get("key") if isinstance(v, dict) else None
    stamp = [os.path.getmtime(p) for p in (os.path.join(VD, "img", f"{key}.png"), clip_path(key) or "") if key and p and os.path.exists(p)]
    return json.dumps([v, stamp], sort_keys=True, ensure_ascii=False, default=str)

def main(vd, mode, sname=None):
    global VD
    VD = os.path.abspath(vd); os.environ["VD"] = VD
    ns = {}; exec(open(os.path.join(VD, "guion.py")).read(), ns)
    os.makedirs(os.path.join(VD, "build"), exist_ok=True)
    B = lambda *p: os.path.join(VD, "build", *p)
    if mode == "long":
        scenes = with_fallback(ns["SCENES"], ns.get("FALLBACK", {})); W, H = 1920, 1080
        if ns.get("BG_BROLL", True):  # fondo en movimiento detrás de gráficos: la imagen anterior (o la siguiente)
            keys = [sc["visual"]["key"] if sc["visual"]["type"] == "img" else None for sc in scenes]
            out_sc = []
            for i, sc in enumerate(scenes):
                if keys[i] is None:
                    prev = [k for k in keys[:i] if k]; nxt = [k for k in keys[i + 1:] if k]
                    k = prev[-1] if prev else (nxt[0] if nxt else None)
                    if k: sc = dict(sc, visual=dict(sc["visual"], bg=k))
                out_sc.append(sc)
            scenes = out_sc
        jobs, plan = [], []
        for i, sc in enumerate(scenes):
            A = dur_of(os.path.join(VD, "audio", f"{sc['id']}.mp3"))
            pre = 0.6 if sc["visual"]["type"] == "title" else 0.0
            post = 0.9 if sc["visual"]["type"] == "title" else 0.35
            D = pre + A + post
            plan.append((sc["id"], pre, A, D))
            out = B(f"{sc['id']}.mp4")
            jobs.append((sc, D, W, H, out, i))
        fresh = lambda j: (os.path.exists(j[4]) and abs(dur_of(j[4]) - round(j[1] * FPS) / FPS) < 0.05
                           and os.path.exists(j[4] + ".sig") and open(j[4] + ".sig").read() == sig_of(j[0]))
        todo = [j for j in jobs if not fresh(j)]
        print("escenas por renderizar:", [os.path.basename(j[4]) for j in todo], flush=True)
        with ProcessPoolExecutor(4) as ex:
            by_out = {j[4]: j for j in todo}
            for o in ex.map(render_scene, todo):
                open(o + ".sig", "w").write(sig_of(by_out[o][0]))  # se guarda al momento: si se corta, se retoma
                print("escena", os.path.basename(o), flush=True)
        build_audio(plan, B, "long", {s["id"]: s["visual"]["type"] for s in scenes})
        concat([j[4] for j in jobs], B("long_video.mp4"))
        mux(B("long_video.mp4"), B("long_audio.wav"), B("final_largo.mp4"), grain=True)
    else:
        sh = shorts_of(ns)[sname]; scenes = with_fallback(sh["scenes"], ns.get("FALLBACK", {}), short=True)
        todo, plan = [], []
        for i, sc in enumerate(scenes):
            A = dur_of(os.path.join(VD, "audio", f"{sc['id']}.mp3"))
            D = A + 0.15
            plan.append((sc["id"], 0.0, A, D))
            todo.append((sc, D, A, B(f"{sc['id']}.mp4"), i * 3, sh.get("bar", "EL ÚLTIMO BALANCE")))
        with ProcessPoolExecutor(4) as ex:
            for o in ex.map(render_short_scene, todo): print("escena", os.path.basename(o), flush=True)
        build_audio(plan, B, f"short_{sname}", {s["id"]: s["alt"]["type"] if s.get("alt") else "img" for s in scenes})
        concat([j[3] for j in todo], B(f"short_{sname}_video.mp4"))
        mux(B(f"short_{sname}_video.mp4"), B(f"short_{sname}_audio.wav"), B(f"final_short_{sname}.mp4"), grain=False)

def music_bed(tracks, seconds, out):
    """Encadena las pistas de música (con fundidos cruzados) hasta cubrir la duración."""
    seq = []; tot = 0.0
    while tot < seconds:
        for t_ in tracks:
            seq.append(t_); tot += dur_of(t_) - 4
            if tot >= seconds: break
    inputs = sum([["-i", s] for s in seq], [])
    if len(seq) == 1:
        filt = "[0:a]aformat=channel_layouts=stereo[o]"
    else:
        chain = "[0:a]"; parts = []
        for k in range(1, len(seq)):
            lab = f"[x{k}]"
            parts.append(f"{chain}[{k}:a]acrossfade=d=4{lab}"); chain = lab
        filt = ";".join(parts) + f";{chain}aformat=channel_layouts=stereo[o]"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", filt, "-map", "[o]", "-t", f"{seconds:.3f}",
                    "-ar", "44100", out], check=True)

def _sfx_bank():
    sr = 44100; rng = np.random.default_rng(3)
    n = int(0.55 * sr); t = np.arange(n) / sr
    noise = rng.normal(0, 1, n); y = np.zeros(n); a = 0.0
    for i in range(n):
        a = a + (0.02 + 0.3 * (i / n)) * (noise[i] - a); y[i] = a
    wh = y * np.sin(np.pi * t / 0.55) ** 2; wh = wh / np.max(np.abs(wh)) * 0.5
    n2 = int(0.6 * sr); t2 = np.arange(n2) / sr
    imp = np.sin(2 * np.pi * (70 * t2 - 25 * t2 ** 2)) * np.exp(-t2 * 7) + 0.25 * rng.normal(0, 1, n2) * np.exp(-t2 * 40)
    imp = imp / np.max(np.abs(imp)) * 0.7
    return sr, wh, imp

def sfx_track(plan, types, total, out):
    """Whoosh al entrar en escenas de gráfico/texto y golpe grave en fechas, cifras y capítulos."""
    sr, wh, imp = _sfx_bank(); buf = np.zeros(int((total + 1) * sr)); t = 0.0
    def put(sig, at, vol):
        i = int(at * sr); j = min(len(buf), i + len(sig))
        if i < len(buf): buf[i:j] += sig[: j - i] * vol
    for sid, pre, A, D in plan:
        ty = types.get(sid, "img")
        if ty in ("title", "year", "quote", "num", "bars", "lines"): put(wh, max(0.0, t - 0.15), 0.35)
        elif ty == "img": put(wh, max(0.0, t - 0.15), 0.12)
        if ty in ("title", "year"): put(imp, t + 0.35, 0.55)
        if ty == "num": put(imp, t + min(D * 0.7, 2.5), 0.4)
        t += D
    st = np.stack([buf, buf], 1); st = np.clip(st, -1, 1)
    import wave
    with wave.open(out, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st * 32767).astype(np.int16).tobytes())

def build_audio(plan, B, tag_, types=None):
    # narración con huecos exactos según el plan
    parts, filt, t = [], [], 0.0
    inputs = []
    for k, (sid, pre, A, D) in enumerate(plan):
        inputs += ["-i", os.path.join(VD, "audio", f"{sid}.mp3")]
        ms = int((t + pre) * 1000)
        filt.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[a{k}]")
        t += D
    total = t
    mix = "".join(f"[a{k}]" for k in range(len(plan)))
    filt.append(f"{mix}amix=inputs={len(plan)}:normalize=0,apad=whole_dur={total:.3f}[narr]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(filt), "-map", "[narr]",
                    "-t", f"{total:.3f}", B(f"{tag_}_narr.wav")], check=True)
    tracks = sorted(glob.glob(os.path.join(VD, "music", "*.mp3")))
    if tracks:
        music_bed(tracks, total + 1, B("pad.wav")); mvol = 0.10
    else:
        ambient_pad(total + 1, B("pad.wav")); mvol = 0.22
    sfx_track(plan, types or {}, total, B(f"{tag_}_sfx.wav"))
    # mezcla: música con ducking bajo la voz + efectos + normalización a -14 LUFS
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", B(f"{tag_}_narr.wav"), "-i", B("pad.wav"), "-i", B(f"{tag_}_sfx.wav"), "-filter_complex",
                    f"[1:a]volume={mvol},afade=t=in:d=2[m];[m][0:a]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
                    "[2:a]aformat=channel_layouts=stereo[fx];"
                    "[0:a][md][fx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[out]",
                    "-map", "[out]", "-t", f"{total:.3f}", "-ar", "48000", B(f"{tag_}_audio.wav")], check=True)
    json.dump(plan, open(B(f"{tag_}_plan.json"), "w"))

def concat(files, out):
    lst = out + ".txt"
    with open(lst, "w") as f:
        for x in files: f.write(f"file '{x}'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out], check=True)

def mux(video, audio, out, grain):
    vf = "vignette=PI/5" if grain else "null"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", audio, "-vf", vf, "-c:v", "libx264", "-preset", "medium",
                    "-crf", os.environ.get("CRF", "21"), "-maxrate", os.environ.get("MAXRATE", "8M"), "-bufsize", "16M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], check=True)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
