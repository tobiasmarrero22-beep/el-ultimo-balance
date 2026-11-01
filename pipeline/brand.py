"""Identidad del canal: logo (3 opciones), banner, marca de agua y previsualizaciones.
Uso: python3 brand.py "EL ÚLTIMO BALANCE"
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ANTON = os.path.join(HERE, "..", "fonts", "Anton.ttf")
INTER_SB = "/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf"
INTER_B = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
BG, GRID = (11, 15, 23), (22, 29, 42)
RED, YEL, WHITE, GREY = (230, 57, 70), (255, 209, 102), (245, 245, 240), (150, 158, 170)
NAME = sys.argv[1] if len(sys.argv) > 1 else "EL ÚLTIMO BALANCE"
TAGLINE = "Cómo se construyen y se hunden las grandes marcas"
OUT = os.path.join(HERE, "entrega"); os.makedirs(OUT, exist_ok=True)
SS = 4  # supermuestreo para bordes suaves

def F(path, size): return ImageFont.truetype(path, size)

def grid(d, w, h, step, col=GRID, width=1):
    for x in range(0, w, step): d.line([(x, 0), (x, h)], fill=col, width=width)
    for y in range(0, h, step): d.line([(0, y), (w, y)], fill=col, width=width)

def arrow(d, pts, col, width, head):
    d.line(pts, fill=col, width=width, joint="curve")
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    p1 = (x1 + head * math.cos(a), y1 + head * math.sin(a))
    p2 = (x1 + head * 0.9 * math.cos(a + 2.3), y1 + head * 0.9 * math.sin(a + 2.3))
    p3 = (x1 + head * 0.9 * math.cos(a - 2.3), y1 + head * 0.9 * math.sin(a - 2.3))
    d.polygon([p1, p2, p3], fill=col)

def icon_bars(size):
    """Opción A: barras que caen + flecha."""
    S = size * SS; im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([0, 0, S - 1, S - 1], fill=BG)
    u = S / 100
    bars = [(24, 30, YEL), (39, 42, YEL), (54, 56, (240, 140, 80)), (69, 72, RED)]
    for x, top, col in bars:
        d.rounded_rectangle([x * u, top * u, (x + 11) * u, 74 * u], radius=2 * u, fill=col)
    d.rectangle([20 * u, 75 * u, 84 * u, 77.5 * u], fill=GREY)
    arrow(d, [(22 * u, 22 * u), (45 * u, 33 * u), (58 * u, 30 * u), (80 * u, 60 * u)], WHITE, int(4.5 * u), 9 * u)
    return im.resize((size, size), Image.LANCZOS)

def icon_crash(size):
    """Opción B: gráfica que sube y se desploma, sobre rejilla."""
    S = size * SS; im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    base = Image.new("RGBA", (S, S), BG + (255,)); d = ImageDraw.Draw(base)
    u = S / 100
    grid(d, S, S, int(12.5 * u), GRID, int(0.6 * u))
    pts = [(18 * u, 66 * u), (32 * u, 54 * u), (44 * u, 58 * u), (56 * u, 32 * u)]
    d.line(pts, fill=YEL, width=int(6 * u), joint="curve")
    arrow(d, [(56 * u, 32 * u), (64 * u, 50 * u), (71 * u, 47 * u), (77 * u, 66 * u)], RED, int(6 * u), 10 * u)
    mask = Image.new("L", (S, S), 0); ImageDraw.Draw(mask).ellipse([0, 0, S - 1, S - 1], fill=255)
    im.paste(base, (0, 0), mask)
    return im.resize((size, size), Image.LANCZOS)

def icon_mono(size):
    """Opción C: monograma con iniciales y barra roja."""
    S = size * SS; im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([0, 0, S - 1, S - 1], fill=BG)
    u = S / 100
    words = [w for w in NAME.split() if len(w) > 2]
    ini = "".join(w[0] for w in words[-2:])
    d.text((50 * u, 46 * u), ini, font=F(ANTON, int(52 * u)), fill=YEL, anchor="mm")
    d.rectangle([28 * u, 74 * u, 72 * u, 79 * u], fill=RED)
    return im.resize((size, size), Image.LANCZOS)

def banner():
    W, H = 2560, 1440
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    grid(d, W, H, 80)
    # gráfica de fondo a todo el ancho (solo se ve en TV / escritorio grande)
    pts = [(0, 1150), (300, 1020), (520, 1080), (800, 860), (1050, 940), (1300, 640), (1500, 700), (1700, 420), (1900, 520), (2080, 900), (2250, 860), (2560, 1300)]
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    ld.line(pts[:8], fill=YEL + (70,), width=14, joint="curve"); ld.line(pts[7:], fill=RED + (90,), width=14, joint="curve")
    layer = layer.filter(ImageFilter.GaussianBlur(2)); im.paste(layer, (0, 0), layer)
    # oscurecer zona central para legibilidad
    shade = Image.new("L", (W, H), 0); ImageDraw.Draw(shade).rounded_rectangle([450, 560, 2110, 880], radius=40, fill=170)
    shade = shade.filter(ImageFilter.GaussianBlur(60))
    im = Image.composite(Image.new("RGB", (W, H), BG), im, shade); d = ImageDraw.Draw(im)
    # zona segura 1546x423 centrada
    sx0, sy0, sx1, sy1 = (W - 1546) // 2, (H - 423) // 2, (W + 1546) // 2, (H + 423) // 2
    ic = icon_bars(330)
    # título ajustado al ancho disponible
    maxw = (sx1 - sx0) - 330 - 70
    size = 190
    while d.textlength(NAME, font=F(ANTON, size)) > maxw: size -= 4
    tw = d.textlength(NAME, font=F(ANTON, size))
    block = 330 + 60 + tw
    x0 = (W - block) / 2
    im.paste(ic, (int(x0), (H - 330) // 2 - 10), ic)
    tx = x0 + 330 + 60
    d.text((tx, H / 2 - 40), NAME, font=F(ANTON, size), fill=WHITE, anchor="ls")
    ts = 44
    while d.textlength(TAGLINE, font=F(INTER_SB, ts)) > tw: ts -= 2
    d.text((tx + 4, H / 2 + 10), TAGLINE, font=F(INTER_SB, ts), fill=GREY, anchor="lt")
    pill = "NUEVO VÍDEO CADA DÍA"
    pw = d.textlength(pill, font=F(INTER_B, 34)) + 56
    d.rounded_rectangle([tx, H / 2 + 80, tx + pw, H / 2 + 140], radius=30, fill=RED)
    d.text((tx + pw / 2, H / 2 + 110), pill, font=F(INTER_B, 34), fill=WHITE, anchor="mm")
    p = os.path.join(OUT, "banner_2560x1440.png"); im.save(p, optimize=True)
    # previsualización con las zonas que ve cada dispositivo
    pv = im.copy(); dv = ImageDraw.Draw(pv)
    dv.rectangle([sx0, sy0, sx1, sy1], outline=(0, 255, 120), width=6)          # móvil (siempre visible)
    dv.rectangle([(W - 2560) // 2, (H - 423) // 2, (W + 2560) // 2, (H + 423) // 2], outline=(80, 160, 255), width=6)  # escritorio
    dv.text((sx0 + 10, sy0 - 50), "zona visible en móvil", font=F(INTER_B, 36), fill=(0, 255, 120))
    dv.text((20, (H - 423) // 2 - 50), "zona visible en ordenador", font=F(INTER_B, 36), fill=(80, 160, 255))
    pv.resize((1280, 720)).save(os.path.join(HERE, "preview_banner_zonas.jpg"), quality=88)
    # cómo se ve en escritorio (franja 2560x423)
    im.crop((0, (H - 423) // 2, W, (H + 423) // 2)).resize((1280, 212)).save(os.path.join(HERE, "preview_banner_escritorio.jpg"), quality=88)
    return p

def main():
    icons = {"A_barras": icon_bars, "B_grafica": icon_crash, "C_iniciales": icon_mono}
    prev = Image.new("RGB", (3 * 360 + 40, 470), (255, 255, 255)); dp = ImageDraw.Draw(prev)
    for i, (k, fn) in enumerate(icons.items()):
        big = fn(800); big.save(os.path.join(OUT, f"logo_{k}_800.png"))
        x = 10 + i * 370
        prev.paste(fn(320), (x + 20, 20), fn(320))
        prev.paste(fn(98), (x + 60, 360), fn(98))      # tamaño real en el canal
        prev.paste(fn(40), (x + 200, 390), fn(40))      # tamaño en comentarios
        dp.text((x + 180, 450), k, font=F(INTER_B, 22), fill=(40, 40, 40), anchor="mb")
    prev.save(os.path.join(HERE, "preview_logos.png"))
    banner()
    # marca de agua 150x150 (se sube en Studio > Personalización > Marca)
    wm = icon_bars(150); wm.save(os.path.join(OUT, "marca_de_agua_150.png"))
    print("ok")

if __name__ == "__main__":
    main()
