"""Pistas de audio en otros idiomas (YouTube "varios idiomas") + subtítulos SRT, sobre el MISMO vídeo.
Uso: python3 pipeline/dub.py <carpeta_video> <idioma>      (idioma: en, pt, ... definido en <carpeta>/i18n.py)

i18n.py define VOICES = {"en": (voice_id, velocidad)}, un dict por idioma (EN, PT, ...) {id_escena: texto}
y META_I18N (título/descripción traducidos). Cada escena se genera con DubVoice (ElevenLabs) y se coloca donde
empieza la escena española (build/long_plan.json); si no entra en su hueco se acelera hasta x1,25 (atempo).
Se mezcla con el mismo fondo (build/pad.wav o música) y los mismos efectos (build/long_sfx.wav), a -14 LUFS.
Salida: entrega/idiomas/<code>_audio_<idioma>.mp3 (misma duración que el vídeo) y subtitulos_<idioma>.srt.
"""
import json, os, re, subprocess, sys, time, glob, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tts as T
from meta import write_srt

def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout)

def gen(text, voice, lang, speed, out, tries=6):
    if os.path.exists(out): return out
    for k in range(tries):
        try:
            j = T.req("POST", "/api/v1/tts", {"text": text, "voice_id": voice, "language": lang, "voice_settings": {"speed": speed}})
            tid = j["task_id"]
            for _ in range(120):
                time.sleep(2); s = T.req("GET", f"/api/v1/tts/{tid}")
                if s["status"] in ("completed", "failed"): break
            if s["status"] != "completed":
                raise RuntimeError(s.get("error"))
            subprocess.run(["curl", "-sS", "-m", "120", "-o", out + ".part", s["result"]], check=True)
            if os.path.getsize(out + ".part") < 1000: raise RuntimeError("descarga vacía")
            os.replace(out + ".part", out); return out
        except Exception as e:
            err = e; time.sleep(8 * (k + 1))  # "Too many requests": esperar y reintentar
    raise RuntimeError(f"{out}: {err}")

def pieces_of(text):
    parts = re.split(r"(?<=[\.\?\!:])\s+", text); out = []
    for p in parts:
        cur = ""
        for w in p.split():
            if len(cur) + len(w) + 1 > 84 and cur: out.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        if cur: out.append(cur)
    return out

def main(vd, lang):
    ns = {}; exec(open(os.path.join(vd, "i18n.py")).read(), ns)
    texts = ns[lang.upper()]; voice, speed = ns["VOICES"][lang]
    g = {}; exec(open(os.path.join(vd, "guion.py")).read(), g); code = g["META"]["code"]
    B = lambda f: os.path.join(vd, "build", f)
    plan = json.load(open(B("long_plan.json")))
    missing = [sid for sid, *_ in plan if sid not in texts]
    if missing: sys.exit(f"faltan traducciones: {missing}")
    A = os.path.join(vd, f"audio_{lang}"); os.makedirs(A, exist_ok=True)
    with cf.ThreadPoolExecutor(4) as ex:
        futs = {ex.submit(gen, texts[sid], voice, lang, speed, os.path.join(A, f"{sid}.mp3")): sid for sid, *_ in plan}
        for f in cf.as_completed(futs):
            try: f.result()
            except Exception as e: sys.exit(f"FALLO {futs[f]}: {e}")
    print(f"{lang}: {len(plan)} escenas generadas", flush=True)
    # colocación en el tiempo del vídeo español
    t = 0.0; prev_end = 0.0; placed = []; fast = []
    for sid, pre, a_es, D in plan:
        src = os.path.join(A, f"{sid}.mp3"); d = dur(src)
        start = max(t + pre, prev_end + 0.08); room = (t + D) - start - 0.05
        tempo = 1.0
        if d > room + 0.25:
            tempo = min(1.25, d / max(0.5, room)); fast.append((sid, round(tempo, 2)))
        placed.append((sid, start, d / tempo, tempo, src)); prev_end = start + d / tempo; t += D
    total = t
    inputs, filt = [], []
    for k, (sid, start, dd, tempo, src) in enumerate(placed):
        inputs += ["-i", src]; ms = int(start * 1000)
        at = f",atempo={tempo:.4f}" if tempo > 1.0 else ""
        filt.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo{at},adelay={ms}|{ms}[a{k}]")
    filt.append("".join(f"[a{k}]" for k in range(len(placed))) + f"amix=inputs={len(placed)}:normalize=0,apad=whole_dur={total:.3f}[narr]")
    narr = B(f"{lang}_narr.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(filt), "-map", "[narr]", "-t", f"{total:.3f}", narr], check=True)
    mvol = float(os.environ.get("MUSIC_VOL", "0.10")) if glob.glob(os.path.join(vd, "music", "*.mp3")) else 0.22
    E = os.path.join(vd, "entrega", "idiomas"); os.makedirs(E, exist_ok=True)
    out = os.path.join(E, f"{code}_audio_{lang}.mp3")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", narr, "-i", B("pad.wav"), "-i", B("long_sfx.wav"), "-filter_complex",
                    f"[1:a]volume={mvol},afade=t=in:d=2[m];[m][0:a]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
                    "[2:a]aformat=channel_layouts=stereo[fx];"
                    "[0:a][md][fx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[out]",
                    "-map", "[out]", "-t", f"{total:.3f}", "-ar", "48000", "-c:a", "libmp3lame", "-b:a", "192k", out], check=True)
    cues = []
    for sid, start, dd, tempo, src in placed:
        ps = pieces_of(texts[sid]); tot = sum(len(p) for p in ps); tt = start
        for p in ps:
            d_ = dd * len(p) / tot; cues.append((tt, tt + d_, p)); tt += d_
    write_srt(os.path.join(E, f"subtitulos_{lang}.srt"), cues)
    over = prev_end - total
    print(f"{lang}: {out} ({total:.1f} s) · escenas aceleradas: {len(fast)} (máx. x{max([x[1] for x in fast], default=1.0)}) · "
          f"{'sobra ' + str(round(-over, 1)) + ' s al final' if over < 0 else 'se pasa ' + str(round(over, 1)) + ' s'}")
    if fast: print("  aceleradas:", fast)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
