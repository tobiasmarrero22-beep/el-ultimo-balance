# Copia fotos elegidas a img/<clave>.png en 1920x1080. Si la foto es vertical o cuadrada, la centra sobre un fondo
# desenfocado de la misma foto (para que el zoom no corte el cohete). Uso: install_photos.py <img_dir> clave=archivo ...
import sys
from PIL import Image, ImageFilter, ImageEnhance
out = sys.argv[1]
for arg in sys.argv[2:]:
    key, src = arg.split("=", 1)
    im = Image.open(src).convert("RGB"); W, H = 1920, 1080
    if im.width / im.height >= 1.6:
        s = max(W / im.width, H / im.height); im2 = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        x, y = (im2.width - W) // 2, (im2.height - H) // 2; res = im2.crop((x, y, x + W, y + H))
    else:
        s = max(W / im.width, H / im.height); bg = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        x, y = (bg.width - W) // 2, (bg.height - H) // 2
        bg = ImageEnhance.Brightness(bg.crop((x, y, x + W, y + H)).filter(ImageFilter.GaussianBlur(40))).enhance(0.45)
        s2 = min(W * 0.92 / im.width, H / im.height); fg = im.resize((round(im.width * s2), round(im.height * s2)), Image.LANCZOS)
        bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2)); res = bg
    res.save(f"{out}/{key}.png"); print(key, im.size, "->", res.size)
