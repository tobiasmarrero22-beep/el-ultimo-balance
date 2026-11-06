"""Clips de una grabación propia (gameplay, cámara...) para cada escena, cortados en el segundo "at" de cada una.
Uso: python3 pipeline/gameplay.py <carpeta_video>

En guion.py:
  SRC  = ruta del vídeo fuente           CROP = "w:h:x:y" opcional (quitar franjas negras)
  BAN  = [(desde, hasta), ...]  tramos que no se usan (notificaciones, auto parado...)
  escenas largas: visual=dict(type="img", key=..., at=SEG)   Shorts: dict(id, text, key, at=SEG)
Necesita audio/ (la duración de cada clip = la de su escena). Si el tramo pisa un BAN, se corre hacia adelante.
Deja clips/<key>.mp4 (1920x1080, 30 fps, sin audio, un poco más largo que la escena → el render lo usa desde 0)
e img/<key>.png (fotograma central: fondo de los gráficos y de las miniaturas).
"""
import json, os, subprocess, sys

def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]))

def main(vd):
    ns = {}; exec(open(os.path.join(vd, "guion.py")).read(), ns)
    src, ban = ns["SRC"], ns.get("BAN", [])
    vf = (f"crop={ns['CROP']}," if ns.get("CROP") else "") + "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30"
    items = []
    for sc in ns["SCENES"]:
        v = sc["visual"]
        if v["type"] == "img" and "at" in v:
            items.append((sc["id"], v["key"], v["at"], dur(os.path.join(vd, "audio", f"{sc['id']}.mp3")) + 0.35))
    for sh in (ns.get("SHORTS") or {}).values():
        for sc in sh["scenes"]:
            if "at" in sc:
                items.append((sc["id"], sc["key"], sc["at"], dur(os.path.join(vd, "audio", f"{sc['id']}.mp3")) + 0.15))
    os.makedirs(os.path.join(vd, "clips"), exist_ok=True); os.makedirs(os.path.join(vd, "img"), exist_ok=True)
    idx_p = os.path.join(vd, "clips", "index.json")
    idx = json.load(open(idx_p)) if os.path.exists(idx_p) else {}
    used = []
    for sid, key, at, D in items:
        L = round(D + 0.6, 2); t = float(at)
        for _ in range(50):
            bad = [b for b in ban if t < b[1] and t + L > b[0]]
            if not bad: break
            t = max(b[1] for b in bad) + 0.2
        if t != at: print(f"  {sid}: {at} pisaba un tramo prohibido → {t:.1f}")
        if sid.startswith("s"):
            for (u0, u1, usid) in used:
                if t < u1 - 0.5 and t + L > u0 + 0.5: print(f"  aviso: {sid} ({t:.1f}-{t + L:.1f}) repite metraje de {usid} ({u0:.1f}-{u1:.1f})")
            used.append((t, t + L, sid))
        sig = f"{src}|{t:.2f}|{L}|{vf}"
        out = os.path.join(vd, "clips", f"{key}.mp4"); png = os.path.join(vd, "img", f"{key}.png")
        if idx.get(key) == sig and os.path.exists(out) and os.path.exists(png): continue
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.2f}", "-t", f"{L}", "-i", src, "-an", "-vf", vf,
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", out], check=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t + L / 2:.2f}", "-i", src, "-frames:v", "1", "-vf", vf, png], check=True)
        idx[key] = sig; json.dump(idx, open(idx_p, "w"), indent=1)
        print("clip", key, f"{t:.1f}s +{L}s", flush=True)

if __name__ == "__main__":
    main(sys.argv[1])
