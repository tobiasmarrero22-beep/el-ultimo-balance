"""Animador de escenas: genera cada escena como MP4 (sin audio) y monta el vídeo final.
Uso: python3 pipeline/render.py <carpeta_video> long
     python3 pipeline/render.py <carpeta_video> short <nombre>   (nombre: clave de SHORTS en guion.py)
"""
import math, os, subprocess, sys, json, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTS = os.path.join(ROOT, "assets", "fonts")
VD = os.environ.get("VD", "")  # carpeta del vídeo (se fija en main)
ANTON = os.path.join(FONTS, "Anton.ttf")
INTER_B = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
INTER_SB = "/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf"
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
def bg_canvas(W, H, t=0.0, tint=(0, 0, 0)):
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

def kenburns(src, W, H, p, motion="in", seed=0):
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
    return src.transform((W, H), Image.AFFINE, (a, 0, c, 0, e, f), resample=Image.BICUBIC)

def scene_img(v, t, D, W, H, seed):
    p = t / D
    im = kenburns(load_img(v["key"]), W, H, p, v.get("motion", "in"), seed)
    # oscurecer bordes inferiores para legibilidad
    if v.get("cap"):
        tag(im, int(W * 0.05), int(H * 0.80), v["cap"], (t - 0.35) / 0.6, scale=W / 1920)
    return im

def scene_title(v, t, D, W, H, seed):
    im = bg_canvas(W, H, t)
    d = ImageDraw.Draw(im)
    sc = W / 1920
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
    im = bg_canvas(W, H, t); d = ImageDraw.Draw(im); sc = W / 1920
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
    im = bg_canvas(W, H, t); d = ImageDraw.Draw(im); sc = W / 1920
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
    im = bg_canvas(W, H, t); d = ImageDraw.Draw(im); sc = W / 1920
    d.text((W * 0.08, H * 0.09), v["title"], font=font(INTER_B, int(52 * sc)), fill=WHITE, anchor="lt")
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
    im = bg_canvas(W, H, t); sc = W / 1920
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

RENDER = dict(img=scene_img, title=scene_title, num=scene_num, year=scene_year, bars=scene_bars, quote=scene_quote)

def encode(frames_fn, n, W, H, out):
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(frames_fn(i).tobytes())
    p.stdin.close(); p.wait()
    assert p.returncode == 0, out

def render_scene(args):
    sc, D, W, H, out, seed = args
    v = sc["visual"]; fn = RENDER[v["type"]]
    n = int(round(D * FPS))
    encode(lambda i: fn(v, i / FPS, D, W, H, seed), n, W, H, out)
    return out

# ---------- Short vertical ----------
def short_frame(sc, t, D, W, H, seed, words_timing, title):
    src = load_img(sc["key"])
    bg = kenburns(src, W, H, t / D, "in", seed).filter(ImageFilter.GaussianBlur(28))
    bg = Image.blend(bg, Image.new("RGB", (W, H), (0, 0, 0)), 0.45)
    fg = kenburns(src, W, int(W * 9 / 16 * 1.25), t / D, "in", seed + 1)
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
    sc, D, A, out, seed, title = args
    W, H = 1080, 1920
    timing = chunks_for(sc["text"], A)
    n = int(round(D * FPS))
    encode(lambda i: short_frame(sc, i / FPS, D, W, H, seed, timing, title), n, W, H, out)
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

def main(vd, mode, sname=None):
    global VD
    VD = os.path.abspath(vd); os.environ["VD"] = VD
    ns = {}; exec(open(os.path.join(VD, "guion.py")).read(), ns)
    os.makedirs(os.path.join(VD, "build"), exist_ok=True)
    B = lambda *p: os.path.join(VD, "build", *p)
    if mode == "long":
        scenes = ns["SCENES"]; W, H = 1920, 1080
        jobs, plan = [], []
        for i, sc in enumerate(scenes):
            A = dur_of(os.path.join(VD, "audio", f"{sc['id']}.mp3"))
            pre = 0.6 if sc["visual"]["type"] == "title" else 0.0
            post = 0.9 if sc["visual"]["type"] == "title" else 0.35
            D = pre + A + post
            plan.append((sc["id"], pre, A, D))
            out = B(f"{sc['id']}.mp4")
            jobs.append((sc, D, W, H, out, i))
        todo = [j for j in jobs if not (os.path.exists(j[4]) and abs(dur_of(j[4]) - round(j[1] * FPS) / FPS) < 0.05)]
        print("escenas por renderizar:", [os.path.basename(j[4]) for j in todo], flush=True)
        with ProcessPoolExecutor(4) as ex:
            for o in ex.map(render_scene, todo): print("escena", os.path.basename(o), flush=True)
        build_audio(plan, B, "long")
        concat([j[4] for j in jobs], B("long_video.mp4"))
        mux(B("long_video.mp4"), B("long_audio.wav"), B("final_largo.mp4"), grain=True)
    else:
        sh = shorts_of(ns)[sname]; scenes = sh["scenes"]
        todo, plan = [], []
        for i, sc in enumerate(scenes):
            A = dur_of(os.path.join(VD, "audio", f"{sc['id']}.mp3"))
            D = A + 0.15
            plan.append((sc["id"], 0.0, A, D))
            todo.append((sc, D, A, B(f"{sc['id']}.mp4"), i * 3, sh.get("bar", "EL ÚLTIMO BALANCE")))
        with ProcessPoolExecutor(4) as ex:
            for o in ex.map(render_short_scene, todo): print("escena", os.path.basename(o), flush=True)
        build_audio(plan, B, f"short_{sname}")
        concat([j[3] for j in todo], B(f"short_{sname}_video.mp4"))
        mux(B(f"short_{sname}_video.mp4"), B(f"short_{sname}_audio.wav"), B(f"final_short_{sname}.mp4"), grain=False)

def build_audio(plan, B, tag_):
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
    ambient_pad(total + 1, B("pad.wav"))
    # mezcla: música baja con ducking bajo la voz + normalización a -14 LUFS
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", B(f"{tag_}_narr.wav"), "-i", B("pad.wav"), "-filter_complex",
                    "[1:a]volume=0.22,afade=t=in:d=2[m];[m][0:a]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
                    "[0:a][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[out]",
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
                    "-crf", "21", "-maxrate", "8M", "-bufsize", "16M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], check=True)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
