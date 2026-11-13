"""Banner de Fútbol Sin Relato (2560x1440). El campo entero (105 m a 14 px/m) cabe en la franja que se ve en el móvil (1546x423).
Uso: python3 futbol/canal/banner.py  → banner.png + banner_vista_movil.png"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "pipeline"))
import sinvoz
from PIL import Image, ImageDraw, ImageFilter
F = sinvoz.font; ANTON, BLACK = sinvoz.ANTON, sinvoz.BLACK
YEL, INK, WHITE, RED = sinvoz.YEL, sinvoz.INK, sinvoz.WHITE, sinvoz.RED
OUT = os.path.dirname(os.path.abspath(__file__))
BW, BH = 2560, 1440; CX, CY = BW // 2, BH // 2
S = 14.0
PL, PW = 105 * S, 68 * S
x0, x1 = CX - PL / 2, CX + PL / 2; y0, y1 = CY - PW / 2, CY + PW / 2
im = Image.new("RGB", (BW, BH), (9, 38, 24)); d = ImageDraw.Draw(im)
n = 14; sw = PL / n
for i in range(n):
    d.rectangle([x0 + i * sw, y0, x0 + (i + 1) * sw, y1], fill=(22, 92, 52) if i % 2 else (17, 76, 43))
for i in range(0, BW, 160):
    if (i // 160) % 2: d.rectangle([i, 0, i + 159, y0 - 1], fill=(11, 46, 29)); d.rectangle([i, y1 + 1, i + 159, BH], fill=(11, 46, 29))
L = (255, 255, 255); w = 9; r = 9.15 * S
d.rectangle([x0, y0, x1, y1], outline=L, width=w)
d.line([CX, y0, CX, y1], fill=L, width=w)
d.ellipse([CX - r, CY - r, CX + r, CY + r], outline=L, width=w); d.ellipse([CX - 9, CY - 9, CX + 9, CY + 9], fill=L)
for side in (-1, 1):
    gx = x0 if side < 0 else x1; s_ = -side  # hacia dentro del campo
    pa_d, pa_h, ga_d, ga_h = 16.5 * S, 40.32 * S, 5.5 * S, 18.32 * S
    d.rectangle(sorted([gx, gx + s_ * pa_d]) and [min(gx, gx + s_ * pa_d), CY - pa_h / 2, max(gx, gx + s_ * pa_d), CY + pa_h / 2], outline=L, width=w)
    d.rectangle([min(gx, gx + s_ * ga_d), CY - ga_h / 2, max(gx, gx + s_ * ga_d), CY + ga_h / 2], outline=L, width=w)
    px = gx + s_ * 11 * S
    d.arc([px - r, CY - r, px + r, CY + r], -53 if side < 0 else 127, 53 if side < 0 else 233, fill=L, width=w)
    d.ellipse([px - 7, CY - 7, px + 7, CY + 7], fill=L)
    d.rectangle([min(gx, gx - s_ * 2.4 * S), CY - 3.66 * S, max(gx, gx - s_ * 2.4 * S), CY + 3.66 * S], outline=L, width=w)

def dashed(a, b, col, wd=7, seg=24):
    l_ = math.hypot(b[0] - a[0], b[1] - a[1]); k = max(2, int(l_ // seg))
    for j in range(0, k, 2):
        p = (a[0] + (b[0] - a[0]) * j / k, a[1] + (b[1] - a[1]) * j / k); q = (a[0] + (b[0] - a[0]) * (j + 1) / k, a[1] + (b[1] - a[1]) * (j + 1) / k)
        d.line([p, q], fill=col, width=wd)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    d.polygon([b, (b[0] - 28 * math.cos(ang - 0.45), b[1] - 28 * math.sin(ang - 0.45)), (b[0] - 28 * math.cos(ang + 0.45), b[1] - 28 * math.sin(ang + 0.45))], fill=col)
def X(x, y): d.line([x - 19, y - 19, x + 19, y + 19], fill=RED, width=9); d.line([x - 19, y + 19, x + 19, y - 19], fill=RED, width=9)
def O(x, y): d.ellipse([x - 21, y - 21, x + 21, y + 21], outline=YEL, width=9)
# jugadas en las dos áreas, fuera de la zona del texto
O(x0 + 175, CY - 150); O(x0 + 125, CY + 150); X(x0 + 70, CY - 75)
dashed((x0 + 168, CY - 122), (x0 + 130, CY + 118), YEL); dashed((x0 + 105, CY + 135), (x0 + 14, CY + 25), YEL, 8)
X(x1 - 175, CY + 150); X(x1 - 125, CY - 150); O(x1 - 70, CY + 75)
dashed((x1 - 168, CY + 122), (x1 - 130, CY - 118), WHITE); dashed((x1 - 105, CY - 135), (x1 - 14, CY - 25), WHITE, 8)
d.ellipse([x0 + 4, CY + 8, x0 + 30, CY + 34], fill=WHITE, outline=INK, width=3)
v = Image.new("L", (BW, BH), 0); ImageDraw.Draw(v).ellipse([-500, -420, BW + 500, BH + 420], fill=255); v = v.filter(ImageFilter.GaussianBlur(240))
im = Image.composite(im, Image.new("RGB", (BW, BH), (0, 0, 0)), v)
title = "FÚTBOL SIN RELATO"; ft = F(ANTON, 128); tw = ft.getlength(title)
bw_, gap = 150, 30; tot = tw + gap + bw_; tx, ty = CX - tot / 2, CY
sh = Image.new("RGBA", (BW, BH), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle([tx - 40, ty - 105, tx + tot + 40, ty + 105], 34, fill=(0, 0, 0, 150))
im = im.convert("RGBA"); im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18))); d = ImageDraw.Draw(im)
d.text((tx, ty), title, font=ft, fill=WHITE, anchor="lm", stroke_width=6, stroke_fill=(0, 0, 0))
d.rounded_rectangle([tx + tw + gap, ty - 72, tx + tot, ty + 70], 22, fill=YEL, outline=INK, width=5)
d.text((tx + tw + gap + bw_ / 2, ty), "90'", font=F(ANTON, 100), fill=INK, anchor="mm")
im = im.convert("RGB"); im.save(os.path.join(OUT, "banner.png"))
im.crop((CX - 773, CY - 211, CX + 773, CY + 212)).save(os.path.join(OUT, "banner_vista_movil.png"))
print("ok")
