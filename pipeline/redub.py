# Rehace escenas de una pista de idioma con la voz más rápida (para no acelerar con atempo). Uso: redub.py <vídeo> <idioma> <velocidad> s01 s02 ...
import os, sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/el-ultimo-balance/pipeline")
import dub
vd, lang, speed, ids = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4:]
ns = {}; exec(open(os.path.join(vd, "i18n.py")).read(), ns)
voice = ns["VOICES"][lang][0]; texts = ns[lang.upper()]
A = os.path.join(vd, f"audio_{lang}")
for sid in ids:
    p = os.path.join(A, f"{sid}.mp3")
    if os.path.exists(p): os.replace(p, p + ".old")
with cf.ThreadPoolExecutor(4) as ex:
    futs = {ex.submit(dub.gen, texts[sid], voice, lang, speed, os.path.join(A, f"{sid}.mp3")): sid for sid in ids}
    for f in cf.as_completed(futs):
        try: f.result(); print("ok", futs[f], flush=True)
        except Exception as e:
            print("FALLO", futs[f], e, flush=True); p = os.path.join(A, f"{futs[f]}.mp3")
            if os.path.exists(p + ".old"): os.replace(p + ".old", p)
for sid in ids:
    p = os.path.join(A, f"{sid}.mp3.old")
    if os.path.exists(p) and os.path.exists(os.path.join(A, f"{sid}.mp3")): os.remove(p)
