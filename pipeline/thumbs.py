"""Miniaturas 1280x720 a partir de THUMBS en guion.py.
Uso: python3 pipeline/thumbs.py <carpeta_video>

Cada miniatura en THUMBS es un dict:
  img, zoom, cx, cy, bright        -> encuadre de la imagen de fondo (img/<img>.png)
  shade: [lado, intensidad, ancho] -> degradado oscuro ("left"/"right") para que el texto se lea
  items: lista de elementos:
    ["text", x, y, "TEXTO", tamaño, color, anchor]      color: white|yellow|red ; anchor PIL (la, mt, mm, ra...)
    ["stamp", "TEXTO", x, y, ángulo, tamaño]
    ["arrow", x, y, ancho, alto]                        flecha roja hacia abajo
    ["crash", x0, y0, x1, y1]                           línea de gráfica que se desploma
    ["badge", x0, y0, x1, y1, "TEXTO", tamaño]           etiqueta roja
THUMBS_TOP = [i, j, k]  (1-based) -> se copian como TOP1/TOP2/TOP3
"""
import os, sys, shutil
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANTON = os.path.join(ROOT, "assets", "fonts", "Anton.ttf")
INTER_B = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "fonts", "InterDisplay-Black.otf")
W, H = 1280, 720
COL = {"white": (255, 255, 255), "yellow": (255, 210, 60), "red": (230, 40, 55), "black": (0, 0, 0),
       "pink": (255, 56, 150), "cyan": (80, 230, 235)}

def F(size, path=ANTON): return ImageFont.truetype(path, size)

def synth_bg(seed=0):
    """Fondo de reserva cuando falta la imagen: rejilla oscura con un foco rojo y otro frío."""
    import numpy as np
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    img = np.zeros((H, W, 3), np.float32) + np.array([11, 15, 23], np.float32)
    for cx, cy, r, col in ((0.18, 0.75, 0.55, (230, 57, 70)), (0.85, 0.25, 0.5, (90, 130, 200))):
        g = np.exp(-(((xx / W - cx) ** 2 + (yy / H - cy) ** 2) / (r ** 2)) * 3.0)[..., None]
        img += g * np.array(col, np.float32) * 0.55
    im = Image.fromarray(np.clip(img, 0, 255).astype("uint8"))
    d = ImageDraw.Draw(im)
    for x in range(0, W, 48): d.line([(x, 0), (x, H)], fill=(28, 34, 46))
    for y in range(0, H, 48): d.line([(0, y), (W, y)], fill=(28, 34, 46))
    return im

def base(vd, key, zoom=1.0, cx=0.5, cy=0.5, bright=1.0, sat=1.15):
    path = os.path.join(vd, "img", f"{key}.png")
    if not os.path.exists(path):
        print(f"sin img/{key}.png -> fondo de reserva"); return synth_bg()
    im = Image.open(path).convert("RGB")
    sw, sh = im.size; s = max(W / sw, H / sh) * zoom
    im = im.resize((int(sw * s), int(sh * s)), Image.LANCZOS)
    x = int((im.width - W) * cx); y = int((im.height - H) * cy)
    im = im.crop((x, y, x + W, y + H))
    im = ImageEnhance.Brightness(im).enhance(bright)
    im = ImageEnhance.Contrast(im).enhance(1.15)
    return ImageEnhance.Color(im).enhance(sat)

def shade(im, side="left", amount=200, width=0.6):
    g = Image.new("L", (W, 1))
    for x in range(W):
        r = x / W if side == "left" else 1 - x / W
        g.putpixel((x, 0), int(amount * max(0, 1 - r / width)))
    return Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), im, g.resize((W, H)))

def stamp(im, s, x, y, angle=-12, size=150, col=COL["red"]):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    tw = d.textlength(s, font=F(size))
    d.rectangle([x - tw / 2 - 30, y - size * 0.62, x + tw / 2 + 30, y + size * 0.62], outline=col + (255,), width=14)
    d.text((x, y), s, font=F(size), fill=col + (255,), anchor="mm")
    layer = layer.rotate(angle, center=(x, y), resample=Image.BICUBIC)
    im.paste(layer, (0, 0), layer)

def render(vd, spec):
    im = base(vd, spec["img"], spec.get("zoom", 1.0), spec.get("cx", 0.5), spec.get("cy", 0.5), spec.get("bright", 1.0))
    if spec.get("shade"): im = shade(im, *spec["shade"])
    d = ImageDraw.Draw(im)
    for it in spec["items"]:
        k = it[0]
        if k == "text":
            _, x, y, s, size, col, anchor = it
            d.text((x, y), s, font=F(size), fill=COL[col], anchor=anchor, stroke_width=max(6, size // 18), stroke_fill=(0, 0, 0))
        elif k == "stamp":
            _, s, x, y, ang, size = it; stamp(im, s, x, y, ang, size); d = ImageDraw.Draw(im)
        elif k == "arrow":
            _, x, y, w, h = it
            d.polygon([(x, y), (x + w, y), (x + w, y + h * .6), (x + w * 1.5, y + h * .6), (x + w / 2, y + h), (x - w / 2, y + h * .6), (x, y + h * .6)], fill=COL["red"], outline=(0, 0, 0))
        elif k == "crash":
            _, x0, y0, x1, y1 = it
            pts = [(x0, y0), (x0 + (x1 - x0) * .25, y0 + 20), (x0 + (x1 - x0) * .4, y0 - 15), (x0 + (x1 - x0) * .55, y0 + 60), (x0 + (x1 - x0) * .7, y0 + 40), (x1, y1)]
            d.line(pts, fill=(0, 0, 0), width=24, joint="curve"); d.line(pts, fill=COL["red"], width=14, joint="curve")
        elif k == "badge":
            _, x0, y0, x1, y1, s, size = it
            d.rounded_rectangle([x0, y0, x1, y1], 24, fill=COL["red"], outline=(0, 0, 0), width=6)
            d.text(((x0 + x1) / 2, (y0 + y1) / 2), s, font=F(size), fill=COL["white"], anchor="mm")
    return im

def main(vd):
    ns = {}; exec(open(os.path.join(vd, "guion.py")).read(), ns)
    out = os.path.join(vd, "entrega", "miniaturas"); os.makedirs(out, exist_ok=True)
    paths = []
    for i, spec in enumerate(ns["THUMBS"], 1):
        p = os.path.join(out, f"mini_{i:02d}.jpg"); render(vd, spec).save(p, quality=92); paths.append(p)
    n = len(paths); rows = (n + 1) // 2
    sheet = Image.new("RGB", (2 * 640 + 30, rows * 370 + 10), (30, 30, 30)); dd = ImageDraw.Draw(sheet)
    for i, p in enumerate(paths):
        x = 10 + (i % 2) * 650; y = 10 + (i // 2) * 370
        sheet.paste(Image.open(p).resize((640, 360)), (x, y))
        dd.text((x + 12, y + 8), str(i + 1), font=F(48, INTER_B), fill=COL["yellow"], stroke_width=4, stroke_fill=(0, 0, 0))
    sheet.save(os.path.join(out, "00_todas.jpg"), quality=85)
    small = Image.new("RGB", (5 * 180 + 20, ((n + 4) // 5) * 105 + 20), (255, 255, 255))
    for i, p in enumerate(paths):
        small.paste(Image.open(p).resize((168, 94), Image.LANCZOS), (10 + (i % 5) * 180, 10 + (i // 5) * 105))
    small.save(os.path.join(out, "00_tamano_movil.png"))
    for rank, idx in enumerate(ns.get("THUMBS_TOP", [1, 2, 3]), 1):
        shutil.copy(paths[idx - 1], os.path.join(vd, "entrega", f"TOP{rank}_miniatura.jpg"))
    print("miniaturas:", n)

if __name__ == "__main__":
    main(os.path.abspath(sys.argv[1]))
