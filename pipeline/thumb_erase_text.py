# Borra el texto de la miniatura del usuario (máscara por color + difusión del fondo) y guarda base_sin_texto.png
import numpy as np
from PIL import Image, ImageFilter
D = "/home/user/el-ultimo-balance/videos/010-nasa-spacex/entrega/miniatura_usuario/"
im = np.asarray(Image.open(D + "original_es.jpg").convert("RGB")).astype(np.float32)
H, W, _ = im.shape
R, G, B = im[..., 0], im[..., 1], im[..., 2]
mask = np.zeros((H, W), bool)
# palabra amarilla "SALVAVIDAS"
y0, y1, x0, x1 = 88, 262, 352, 1035
reg = np.zeros((H, W), bool); reg[y0:y1, x0:x1] = True
yellow = (R > 140) & (G > 70) & (R - B > 80) & (G - B > 30)
mask |= reg & yellow
# palabra blanca "EL"
reg2 = np.zeros((H, W), bool); reg2[8:128, 570:712] = True
white = (R > 120) & (G > 120) & (B > 120) & (np.abs(R - B) < 60)
mask |= reg2 & white
# dilatar (incluye bordes, antialias y la sombra pegada)
m = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(25)).filter(ImageFilter.GaussianBlur(2))
mask = np.asarray(m) > 40
# no tocar la parte de abajo (techo del coche)
mask[262:, :] = False
mask[:, :372] = False  # no tocar el logo de la izquierda
Image.fromarray((mask * 255).astype(np.uint8)).save(D + "mascara.png")
# difusión: los píxeles tapados toman el promedio de sus vecinos, de grueso a fino
out = im.copy()
ys, xs = np.where(mask)
by0, by1, bx0, bx1 = max(ys.min() - 20, 0), min(ys.max() + 20, H), max(xs.min() - 20, 0), min(xs.max() + 20, W)
sub = out[by0:by1, bx0:bx1].copy(); msub = mask[by0:by1, bx0:bx1]
known = ~msub
# relleno inicial: media de fila de los conocidos
for c in range(3):
    ch = sub[..., c]
    for r in range(ch.shape[0]):
        k = known[r]
        if k.any(): ch[r, ~k] = np.interp(np.where(~k)[0], np.where(k)[0], ch[r, k])
for it in range(1500):
    p = np.pad(sub, ((1, 1), (1, 1), (0, 0)), mode="edge")
    avg = (p[:-2, 1:-1] + p[2:, 1:-1] + p[1:-1, :-2] + p[1:-1, 2:]) / 4
    sub[msub] = avg[msub]
out[by0:by1, bx0:bx1] = sub
# ruido suave para que no quede "lavado"
rng = np.random.default_rng(1)
noise = rng.normal(0, 1.6, out.shape).astype(np.float32)
out[mask] += noise[mask]
Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(D + "base_sin_texto.png")
print("máscara px:", mask.sum())
