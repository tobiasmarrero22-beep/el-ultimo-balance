"""Clips de vídeo IA a partir de las imágenes (imagen → vídeo) con DubVoice.
Uso: python3 pipeline/vid.py <carpeta_video> [modelo] [claves...]     (modelo por defecto: meta, 2.000 cr/clip)
Lee CLIPS = {clave_imagen: "prompt de movimiento"} de guion.py y guarda clips/<clave>.mp4.
DubVoice devuelve los créditos de vídeo si la generación falla.
"""
import base64, io, json, os, subprocess, sys, time

B = "https://www.dubvoice.ai"

def call(method, path, body=None, timeout=300):
    cmd = ["curl", "-sS", "-m", str(timeout), "-X", method, B + path, "-H", "Content-Type: application/json", "-w", "\n%{http_code}"]
    if body is not None:
        tmp = "/tmp/_vid_body.json"; json.dump(body, open(tmp, "w")); cmd += ["--data-binary", "@" + tmp]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    txt, _, code = out.rpartition("\n")
    try: return int(code), json.loads(txt)
    except Exception: return int(code or 0), {"raw": txt[:400]}

def data_uri(path, maxw=1280):
    from PIL import Image
    im = Image.open(path).convert("RGB")
    if im.width > maxw: im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=88)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def find_url(j):
    for k in ("video_url", "file_url", "result", "url", "output"):
        v = j.get(k)
        if isinstance(v, str) and v.startswith(("http", "/")): return v
    return None

def gen(vd, key, motion, model):
    out = os.path.join(vd, "clips", f"{key}.mp4")
    if os.path.exists(out): return out
    body = {"prompt": f"Cinematic documentary shot. {motion}. Realistic, smooth subtle motion, no text, no logos.",
            "model": model, "aspect_ratio": "16:9", "resolution": "720p"}
    img = data_uri(os.path.join(vd, "img", f"{key}.png"))
    if model == "meta": body["start_frame"] = img
    elif model == "google-vids": body.update(ref_images=[img], mode_image="frame", duration=5)
    else: body["ref_images"] = [img]
    st, j = call("POST", "/api/v1/video", body)
    print(key, "→", st, json.dumps(j)[:300], flush=True)
    url = find_url(j)
    jid = j.get("task_id") or j.get("job_id") or j.get("id")
    t0 = time.time()
    while not url and jid and time.time() - t0 < 900:
        time.sleep(10)
        for path in (f"/api/v1/video?task_id={jid}", f"/api/v1/video/{jid}", f"/api/v1/video?job_id={jid}"):
            s2, j2 = call("GET", path, timeout=60)
            if s2 == 200 and isinstance(j2, dict) and ("status" in j2 or find_url(j2)):
                if j2.get("status") == "failed": raise RuntimeError(f"{key}: {j2}")
                url = find_url(j2)
                break
    if not url: raise RuntimeError(f"{key}: sin URL ({st} {j})")
    if url.startswith("/"): url = B + url
    os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run(["curl", "-sS", "-m", "300", "-o", out, url], check=True)
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip()
    if not d: os.remove(out); raise RuntimeError(f"{key}: el archivo descargado no es un vídeo")
    print(key, "OK", d, "s", flush=True)
    return out

if __name__ == "__main__":
    vd = os.path.abspath(sys.argv[1]); model = sys.argv[2] if len(sys.argv) > 2 else "meta"; only = set(sys.argv[3:])
    ns = {}; exec(open(os.path.join(vd, "guion.py")).read(), ns)
    for key, motion in ns.get("CLIPS", {}).items():
        if only and key not in only: continue
        if not os.path.exists(os.path.join(vd, "img", f"{key}.png")): print(key, "sin imagen, se salta"); continue
        try: gen(vd, key, motion, model)
        except Exception as e: print("FAIL", key, e, flush=True)
