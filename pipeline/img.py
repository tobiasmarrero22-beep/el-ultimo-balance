import json, ssl, sys, time, os, urllib.request, concurrent.futures as cf
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
B = "https://www.dubvoice.ai"
import subprocess
def call(method, path, body=None):
    cmd = ["curl", "-sS", "-m", "240", "-X", method, B + path, "-H", "Content-Type: application/json", "-w", "\n%{http_code}"]
    if body is not None: cmd += ["-d", json.dumps(body)]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    txt, _, code = out.rpartition("\n")
    try: return int(code), json.loads(txt)
    except Exception: return int(code or 0), {"raw": txt[:300]}
def gen(key, prompt, model, aspect="16:9", outdir="img"):
    out = f"{outdir}/{key}.png"
    if os.path.exists(out): return out
    for attempt in range(6):
        st, j = call("POST", "/api/image-generate", {"prompt": prompt, "model": model, "aspect_ratio": aspect})
        if st == 429:  # no se cobra: esperar y reintentar
            time.sleep(15); continue
        if st == 202 or j.get("status") == "processing":
            jid = j["job_id"]
            for _ in range(120):
                time.sleep(3); st2, j = call("GET", f"/api/image-generate/status?job_id={jid}")
                if j.get("status") in ("completed", "failed"): break
        url = j.get("image_url")
        if url:
            if url.startswith("/"): url = B + url
            subprocess.run(["curl", "-sS", "-m", "120", "-o", out, url], check=True)
            try:
                from PIL import Image; Image.open(out).verify()
            except Exception:
                os.remove(out); raise RuntimeError(f"{key}: la descarga no es una imagen válida ({url})")
            return out
        break  # cualquier otro error puede haberse cobrado: no reintentar a ciegas
    raise RuntimeError(f"{key}: {st} {j}")
if __name__ == "__main__":
    # Uso: python3 pipeline/img.py <carpeta_video> [modelo] [claves...]   (por defecto nano-banana-2-lite, 500 cr)
    os.chdir(sys.argv[1]); os.makedirs("img", exist_ok=True)
    model = sys.argv[2] if len(sys.argv) > 2 else "nano-banana-2-lite"; only = set(sys.argv[3:])
    ns = {}; exec(open("guion.py").read(), ns)
    items = [(k, p) for k, p in ns["IMAGES"].items() if not only or k in only]
    with cf.ThreadPoolExecutor(1) as ex:
        futs = {ex.submit(gen, k, p, model): k for k, p in items}
        for f in cf.as_completed(futs):
            try: print("ok", f.result(), flush=True)
            except Exception as e: print("FAIL", futs[f], e, flush=True)
