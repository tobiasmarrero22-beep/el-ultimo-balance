# Escribe el texto nuevo sobre base_sin_texto.png imitando el estilo de la miniatura del usuario (cursiva, degradado, sombra).
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D = "/home/user/el-ultimo-balance/videos/010-nasa-spacex/entrega/miniatura_usuario/"
FONT = "/home/user/el-ultimo-balance/assets/fonts/Anton.ttf"
SHEAR = 0.19

def word_layer(text, cap_h, top_col, bot_col, max_w):
    f = ImageFont.truetype(FONT, 100); ch = f.getbbox("H")[3] - f.getbbox("H")[1]
    size = int(100 * cap_h / ch); f = ImageFont.truetype(FONT, size)
    l, t, r, b = f.getbbox(text)
    if r - l > max_w:
        size = int(size * max_w / (r - l)); f = ImageFont.truetype(FONT, size); l, t, r, b = f.getbbox(text)
    capt = f.getbbox("H")[1]; pad = 60
    w, h = r - l + pad * 2, b - min(t, capt) + pad * 2
    mask = Image.new("L", (w, h), 0); d = ImageDraw.Draw(mask)
    ox, oy = pad - l, pad - min(t, capt)
    d.text((ox, oy), text, font=f, fill=255)
    # degradado vertical sobre la altura de las mayúsculas
    grad = Image.new("RGB", (w, h)); gd = ImageDraw.Draw(grad)
    y_top, y_bot = oy + capt, oy + f.getbbox("H")[3]
    for y in range(h):
        k = min(1, max(0, (y - y_top) / max(1, y_bot - y_top)))
        gd.line([(0, y), (w, y)], fill=tuple(int(top_col[i] + (bot_col[i] - top_col[i]) * k) for i in range(3)))
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0)); lay.paste(grad, (0, 0), mask)
    # cursiva: inclinar hacia la derecha
    extra = int(h * SHEAR)
    lay = lay.transform((w + extra, h), Image.AFFINE, (1, SHEAR, -extra, 0, 1, 0), resample=Image.BICUBIC)
    capbox = (y_top, y_bot)
    return lay, capbox, pad

def place(base, lay, capbox, cx, cap_top):
    a = lay.split()[3]
    sh = Image.new("RGBA", lay.size, (0, 0, 0, 0)); sh.putalpha(a.point(lambda v: int(v * 0.75)))
    sh = sh.filter(ImageFilter.GaussianBlur(7))
    x = int(cx - lay.width / 2); y = int(cap_top - capbox[0])
    base.alpha_composite(sh, (x - 5, y + 7)); base.alpha_composite(lay, (x, y))

def make(small, big, out, big_cx=695, big_top=103, big_cap=150, big_max=670, small_cx=642, small_top=20, small_cap=98):
    base = Image.open(D + "base_sin_texto.png").convert("RGBA")
    lay, cb, _ = word_layer(big, big_cap, (255, 233, 70), (255, 150, 0), big_max); place(base, lay, cb, big_cx, big_top)
    lay, cb, _ = word_layer(small, small_cap, (255, 255, 255), (196, 196, 200), 400); place(base, lay, cb, small_cx, small_top)
    base.convert("RGB").save(out, quality=95); print(out)

make("THE", "LIFELINE", D + "miniatura_en.jpg")
make("A", "SALVAÇÃO", D + "miniatura_pt.jpg", big_top=106, big_cap=146)
make("EL", "SALVAVIDAS", D + "prueba_es_recreada.jpg")
