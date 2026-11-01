import json, ssl, sys, time, urllib.request, concurrent.futures as cf
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
B = "https://www.dubvoice.ai"
def req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(B + path, data=data, method=method, headers={"Content-Type": "application/json", "Authorization": "Bearer dummy"})
    with urllib.request.urlopen(r, context=CTX, timeout=60) as resp:
        return json.load(resp)
def tts(text, voice, out, speed=1.0, model=None, tries=2):
    for attempt in range(tries):
        body = {"text": text, "voice_id": voice, "language": "es", "voice_settings": {"speed": speed}}
        if model: body["model_id"] = model
        j = req("POST", "/api/v1/tts", body); tid = j["task_id"]
        for _ in range(90):
            time.sleep(2); s = req("GET", f"/api/v1/tts/{tid}")
            if s["status"] in ("completed", "failed"): break
        if s["status"] == "completed":
            u = s["result"]
            with urllib.request.urlopen(urllib.request.Request(u), context=CTX, timeout=60) as r, open(out, "wb") as f:
                f.write(r.read())
            return out
    raise RuntimeError(f"TTS failed: {s.get('error')}")
VOZ = "fishaudio_a48e73d4fb124c689357e88b04c9db30"  # "Narrador Cálido Español" (Fish Audio)
if __name__ == "__main__":
    # Uso: python3 pipeline/tts.py <carpeta_video> [ids...]   (voz y velocidad: VOICE / SPEED en guion.py)
    import os
    os.chdir(sys.argv[1]); os.makedirs("audio", exist_ok=True)
    ns = {}; exec(open("guion.py").read(), ns)
    voice, speed = ns.get("VOICE", VOZ), float(ns.get("SPEED", 1.05))
    shorts = ns["SHORTS"] if "SHORTS" in ns else {"a": {"scenes": ns.get("SHORT", [])}}
    items = [(s["id"], s["text"]) for s in ns["SCENES"]] + [(s["id"], s["text"]) for sh in shorts.values() for s in sh["scenes"]]
    only = set(sys.argv[2:])
    if only: items = [i for i in items if i[0] in only]
    import os
    items = [i for i in items if not os.path.exists(f"audio/{i[0]}.mp3")]
    with cf.ThreadPoolExecutor(8) as ex:
        futs = {ex.submit(tts, t, voice, f"audio/{i}.mp3", speed): i for i, t in items}
        for f in cf.as_completed(futs):
            try: f.result(); print("ok", futs[f], flush=True)
            except Exception as e: print("FAIL", futs[f], e, flush=True)
