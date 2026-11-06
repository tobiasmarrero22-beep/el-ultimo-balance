import json, ssl, sys, time, urllib.request, concurrent.futures as cf
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
B = "https://www.dubvoice.ai"
def req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(B + path, data=data, method=method, headers={"Content-Type": "application/json", "Authorization": "Bearer dummy"})
    with urllib.request.urlopen(r, context=CTX, timeout=60) as resp:
        return json.load(resp)
def tts_clone(text, voice, out, tries=3):
    """Voz clonada de la cuenta (GET /api/voice-clone → voice_id numérico): POST /api/minimax-tts devuelve el MP3 directo."""
    import os
    for k in range(tries):
        try:
            r = urllib.request.Request(B + "/api/minimax-tts", data=json.dumps({"text": text, "voice_id": voice, "language": "es"}).encode(),
                                       method="POST", headers={"Content-Type": "application/json", "Authorization": "Bearer dummy"})
            with urllib.request.urlopen(r, context=CTX, timeout=180) as resp:
                data = resp.read(); ct = resp.headers.get("Content-Type", "")
            if "audio" in ct and len(data) > 1000:
                open(out + ".part", "wb").write(data); os.replace(out + ".part", out); return out
            raise RuntimeError(data[:300])
        except Exception as e:
            err = e; time.sleep(3 * (k + 1))
    raise RuntimeError(f"TTS clon falló: {err}")
def tts(text, voice, out, speed=1.0, model=None, tries=2):
    if str(voice).isdigit(): return tts_clone(text, str(voice), out)
    for attempt in range(tries):
        body = {"text": text, "voice_id": voice, "language": "es", "voice_settings": {"speed": speed}}
        if model: body["model_id"] = model
        j = req("POST", "/api/v1/tts", body); tid = j["task_id"]
        for _ in range(90):
            time.sleep(2); s = req("GET", f"/api/v1/tts/{tid}")
            if s["status"] in ("completed", "failed"): break
        if s["status"] == "completed":
            u = s["result"]
            for k in range(4):  # reintentar solo la DESCARGA (la generación ya está cobrada)
                try:
                    with urllib.request.urlopen(urllib.request.Request(u), context=CTX, timeout=60) as r:
                        data = r.read()
                    if len(data) > 1000:
                        open(out + ".part", "wb").write(data); import os; os.replace(out + ".part", out)
                        return out
                except Exception:
                    time.sleep(2 * (k + 1))
            raise RuntimeError(f"descarga fallida: {u}")
    raise RuntimeError(f"TTS failed: {s.get('error')}")
def pronounce(table):
    """PRONUNCIA = {"Vice City": "Vais Síti", ...} en guion.py: cambia la escritura solo para la voz (frases largas primero)."""
    import re
    if not table: return lambda t: t
    rx = re.compile(r"\b(" + "|".join(re.escape(k) for k in sorted(table, key=len, reverse=True)) + r")\b")
    return lambda t: rx.sub(lambda m: table[m.group(1)], t)
VOZ = "fishaudio_a48e73d4fb124c689357e88b04c9db30"  # "Narrador Cálido Español" (Fish Audio)
if __name__ == "__main__":
    # Uso: python3 pipeline/tts.py <carpeta_video> [ids...]   (voz y velocidad: VOICE / SPEED en guion.py)
    import os
    os.chdir(sys.argv[1]); os.makedirs("audio", exist_ok=True)
    ns = {}; exec(open("guion.py").read(), ns)
    voice, speed = ns.get("VOICE", VOZ), float(ns.get("SPEED", 1.05))
    say = pronounce(ns.get("PRONUNCIA") or {})
    shorts = ns["SHORTS"] if "SHORTS" in ns else {"a": {"scenes": ns.get("SHORT", [])}}
    items = [(s["id"], s["text"]) for s in ns["SCENES"]] + [(s["id"], s["text"]) for sh in shorts.values() for s in sh["scenes"]]
    only = set(sys.argv[2:])
    if only: items = [i for i in items if i[0] in only]
    import os
    items = [i for i in items if not os.path.exists(f"audio/{i[0]}.mp3")]
    with cf.ThreadPoolExecutor(8) as ex:
        futs = {ex.submit(tts, say(t), voice, f"audio/{i}.mp3", speed): i for i, t in items}
        for f in cf.as_completed(futs):
            try: f.result(); print("ok", futs[f], flush=True)
            except Exception as e: print("FAIL", futs[f], e, flush=True)
