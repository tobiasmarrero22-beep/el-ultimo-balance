"""Identidad de Stoppage Time Facts (canal de Shorts de fútbol en inglés): avatar, banner, vista en el móvil y marca de agua.
Paleta propia de «partido de noche» (azul y naranja) para no ser una copia de Dato de Tribuna.
Uso: python3 football/canal/brand.py"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "pipeline"))
import sinvoz
from PIL import Image, ImageDraw, ImageFilter
F = sinvoz.font; ANTON, BLACK = sinvoz.ANTON, sinvoz.BLACK
OUT = os.path.dirname(os.path.abspath(__file__))
D1, D2, BG = (9, 30, 46), (13, 44, 66), (6, 20, 32)
ACC, INK, WHITE, RED = (255, 152, 32), (10, 14, 20), (245, 245, 240), (230, 57, 70)
TITLE, BADGE = "STOPPAGE TIME FACTS", "90+'"

def badge_box(w, h, l1, l2=None, s1=None, s2=None, rot=-6):
    box = Image.new("RGBA", (w, h), (0, 0, 0, 0)); b = ImageDraw.Draw(box)
    b.rounded_rectangle([0, 0, w - 1, h - 1], int(h * 0.11), fill=ACC + (255,), outline=INK + (255,), width=max(4, w // 55))
    if l2:
        b.text((w / 2, h * 0.38), l1, font=sinvoz.fit(ANTON, s1, l1, w * 0.86), fill=INK, anchor="mm")
        b.text((w / 2, h * 0.78), l2, font=sinvoz.fit(ANTON, s2, l2, w * 0.86), fill=INK, anchor="mm")
    else:
        b.text((w / 2, h / 2), l1, font=sinvoz.fit(ANTON, s1, l1, w * 0.86), fill=INK, anchor="mm")
    return box.rotate(rot, expand=True, resample=Image.BICUBIC) if rot else box

# avatar 800x800
S = 800; im = Image.new("RGB", (S, S), D1); d = ImageDraw.Draw(im)
for i in range(0, S, 100):
    if (i // 100) % 2: d.rectangle([i, 0, i + 99, S], fill=D2)
d.ellipse([60, 60, S - 60, S - 60], outline=WHITE, width=10); d.line([S / 2, 60, S / 2, S - 60], fill=WHITE, width=8)
box = badge_box(580, 440, BADGE, "FACTS", 250, 120)
im.paste(box, (int(S / 2 - box.width / 2), int(S / 2 - box.height / 2)), box); im.save(os.path.join(OUT, "avatar.png"))

# marca de agua 150x150 (YouTube: Personalización → Marca de agua)
wm = badge_box(150, 150, BADGE, None, 90, rot=0); wm.save(os.path.join(OUT, "watermark.png"))

# banner 2560x1440: el campo entero cabe en la franja del móvil (1546x423)
BW, BH = 2560, 1440; CX, CY = BW // 2, BH // 2; K = 14.0
PL, PW = 105 * K, 68 * K; x0, x1 = CX - PL / 2, CX + PL / 2; y0, y1 = CY - PW / 2, CY + PW / 2
im = Image.new("RGB", (BW, BH), BG); d = ImageDraw.Draw(im)
n = 14; sw = PL / n
for i in range(n): d.rectangle([x0 + i * sw, y0, x0 + (i + 1) * sw, y1], fill=(16, 54, 80) if i % 2 else (12, 44, 66))
for i in range(0, BW, 160):
    if (i // 160) % 2: d.rectangle([i, 0, i + 159, y0 - 1], fill=(8, 26, 40)); d.rectangle([i, y1 + 1, i + 159, BH], fill=(8, 26, 40))
L = WHITE; w = 9; r = 9.15 * K
d.rectangle([x0, y0, x1, y1], outline=L, width=w); d.line([CX, y0, CX, y1], fill=L, width=w)
d.ellipse([CX - r, CY - r, CX + r, CY + r], outline=L, width=w); d.ellipse([CX - 9, CY - 9, CX + 9, CY + 9], fill=L)
for side in (-1, 1):
    gx = x0 if side < 0 else x1; s_ = -side
    for dd, hh in [(16.5 * K, 40.32 * K), (5.5 * K, 18.32 * K)]:
        d.rectangle([min(gx, gx + s_ * dd), CY - hh / 2, max(gx, gx + s_ * dd), CY + hh / 2], outline=L, width=w)
    px = gx + s_ * 11 * K
    d.arc([px - r, CY - r, px + r, CY + r], -53 if side < 0 else 127, 53 if side < 0 else 233, fill=L, width=w)
    d.ellipse([px - 7, CY - 7, px + 7, CY + 7], fill=L)
    d.rectangle([min(gx, gx - s_ * 2.4 * K), CY - 3.66 * K, max(gx, gx - s_ * 2.4 * K), CY + 3.66 * K], outline=L, width=w)
# focos del estadio (partido de noche) en las esquinas
glow = Image.new("RGBA", (BW, BH), (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
for (fx, fy) in [(x0 - 60, y0 - 60), (x1 + 60, y0 - 60), (x0 - 60, y1 + 60), (x1 + 60, y1 + 60)]:
    g.ellipse([fx - 260, fy - 260, fx + 260, fy + 260], fill=(255, 240, 200, 60))
im = im.convert("RGBA"); im.alpha_composite(glow.filter(ImageFilter.GaussianBlur(90))); d = ImageDraw.Draw(im)
def dashed(a, b, col, wd=7, seg=24):
    l_ = math.hypot(b[0] - a[0], b[1] - a[1]); k = max(2, int(l_ // seg))
    for j in range(0, k, 2):
        p = (a[0] + (b[0] - a[0]) * j / k, a[1] + (b[1] - a[1]) * j / k); q = (a[0] + (b[0] - a[0]) * (j + 1) / k, a[1] + (b[1] - a[1]) * (j + 1) / k)
        d.line([p, q], fill=col, width=wd)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    d.polygon([b, (b[0] - 28 * math.cos(ang - 0.45), b[1] - 28 * math.sin(ang - 0.45)), (b[0] - 28 * math.cos(ang + 0.45), b[1] - 28 * math.sin(ang + 0.45))], fill=col)
def X(x, y): d.line([x - 19, y - 19, x + 19, y + 19], fill=RED, width=9); d.line([x - 19, y + 19, x + 19, y - 19], fill=RED, width=9)
def O(x, y): d.ellipse([x - 21, y - 21, x + 21, y + 21], outline=ACC, width=9)
O(x0 + 175, CY - 150); O(x0 + 125, CY + 150); X(x0 + 70, CY - 75)
dashed((x0 + 168, CY - 122), (x0 + 130, CY + 118), ACC); dashed((x0 + 105, CY + 135), (x0 + 14, CY + 25), ACC, 8)
X(x1 - 175, CY + 150); X(x1 - 125, CY - 150); O(x1 - 70, CY + 75)
dashed((x1 - 168, CY + 122), (x1 - 130, CY - 118), WHITE); dashed((x1 - 105, CY - 135), (x1 - 14, CY - 25), WHITE, 8)
ft = F(ANTON, 118); tw = ft.getlength(TITLE); bw_, gap = 170, 30; tot = tw + gap + bw_; tx, ty = CX - tot / 2, CY
sh = Image.new("RGBA", (BW, BH), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle([tx - 40, ty - 100, tx + tot + 40, ty + 100], 34, fill=(0, 0, 0, 160))
im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18))); d = ImageDraw.Draw(im)
d.text((tx, ty), TITLE, font=ft, fill=WHITE, anchor="lm", stroke_width=6, stroke_fill=(0, 0, 0))
d.rounded_rectangle([tx + tw + gap, ty - 70, tx + tot, ty + 68], 22, fill=ACC, outline=INK, width=5)
d.text((tx + tw + gap + bw_ / 2, ty), BADGE, font=F(ANTON, 96), fill=INK, anchor="mm")
im = im.convert("RGB"); im.save(os.path.join(OUT, "banner.png"))
im.crop((CX - 773, CY - 211, CX + 773, CY + 212)).save(os.path.join(OUT, "banner_mobile_view.png"))
print("ok")
