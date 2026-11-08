"""Paquete de subida (entrega/SUBIR.md) + subtítulos SRT a partir de META en guion.py y los planes de render.
Uso: python3 pipeline/meta.py <carpeta_video>
"""
import json, os, re, sys, shutil

def ts(sec):
    m, s = divmod(int(sec), 60); return f"{m}:{s:02d}"

def srt_time(sec):
    h = int(sec // 3600); m = int(sec % 3600 // 60); s = sec % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)) % 1000:03d}"

def cues_and_chapters(plan, scenes, intro):
    by = {s["id"]: s for s in scenes}
    t = 0.0; chapters = [(0.0, intro)]; cues = []
    for sid, pre, A, D in plan:
        sc = by[sid]; v = sc.get("visual", {})
        if v.get("type") == "title":
            chapters.append((t, f"{v['num']}. {v.get('name', v['text'].capitalize())}"))
        parts = re.split(r"(?<=[\.\?\!:])\s+", sc["text"]); pieces = []
        for p in parts:
            cur = ""
            for w in p.split():
                if len(cur) + len(w) + 1 > 84 and cur: pieces.append(cur); cur = w
                else: cur = (cur + " " + w).strip()
            if cur: pieces.append(cur)
        tot = sum(len(p) for p in pieces); tt = t + pre
        for p in pieces:
            d = A * len(p) / tot; cues.append((tt, tt + d, p)); tt += d
        t += D
    return chapters, cues, t

def write_srt(path, cues):
    with open(path, "w") as f:
        for i, (a, b, txt) in enumerate(cues, 1):
            f.write(f"{i}\n{srt_time(a)} --> {srt_time(b)}\n{txt}\n\n")

def main(vd):
    ns = {}; exec(open(os.path.join(vd, "guion.py")).read(), ns)
    M = ns["META"]; E = os.path.join(vd, "entrega"); os.makedirs(E, exist_ok=True)
    plan = json.load(open(os.path.join(vd, "build", "long_plan.json")))
    chapters, cues, total = cues_and_chapters(plan, ns["SCENES"], M["intro_chapter"])
    write_srt(os.path.join(E, "subtitulos_largo.srt"), cues)
    cap = "\n".join(f"{ts(a)} {name}" for a, name in chapters)
    fuentes = "\n".join(f"• {s}" for s in M["sources"])
    con_img = any(os.path.exists(os.path.join(vd, "img", f"{sc['visual']['key']}.png"))
                  for sc in ns["SCENES"] if sc["visual"]["type"] == "img")
    aviso = ("Las imágenes de este vídeo son ilustraciones generadas con IA y no muestran a personas ni productos reales. "
             "La narración está hecha con voz sintética." if con_img else "La narración de este vídeo está hecha con voz sintética.")
    aviso = M.get("disclosure", aviso)
    desc = f"""{M['description']}

📌 Capítulos
{cap}

📚 Fuentes
{fuentes}

{aviso}

{M['hashtags']}"""
    L = []
    L.append(f"# {M['code']} — {M['name']} · Paquete de subida\n")
    L.append(f"## 🎬 VÍDEO LARGO — `{M['code']}_largo.mp4` ({ts(total)})\n")
    L.append("**Título** (el primero es el recomendado)\n```\n" + M["titles"][0] + "\n```")
    for alt in M["titles"][1:]: L.append(f"- Alternativa: `{alt}`")
    L.append("\n**Miniatura:** `TOP1_miniatura.jpg` → si tienes \"Probar y comparar\", sube `TOP1`, `TOP2` y `TOP3`.\n")
    L.append("**Descripción**\n```\n" + desc + "\n```\n")
    L.append("**Etiquetas**\n```\n" + ", ".join(M["tags"]) + "\n```\n")
    L.append("**Ajustes al subir**\n- Contenido para niños: **No**\n" f"- Contenido alterado o sintético: **{M.get('altered', 'Sí')}**\n"
             f"- Subtítulos: `subtitulos_largo.srt` (Español)\n- Categoría: **{M.get('category', 'Educación')}** · Idioma: **Español**\n"
             f"- Pantalla final (últimos 10 s): \"Suscribirse\" + \"Vídeo más reciente\"\n- Lista de reproducción: **{M['playlist']}**\n")
    L.append("**Comentario fijado**\n```\n" + M["pinned"] + "\n```\n\n---\n")
    shorts = ns["SHORTS"] if "SHORTS" in ns else {"a": {"scenes": ns.get("SHORT", [])}}
    for name, sh in shorts.items():
        sm = M["shorts"][name]
        sp = os.path.join(vd, "build", f"short_{name}_plan.json")
        if os.path.exists(sp):
            _, scues, stot = cues_and_chapters(json.load(open(sp)), sh["scenes"], "")
            write_srt(os.path.join(E, f"subtitulos_short_{name}.srt"), scues)
        else:
            stot = 0
        L.append(f"## 📱 SHORT {name.upper()} — `{M['code']}_short_{name}.mp4` ({int(stot)} s)\n")
        L.append("**Título**\n```\n" + sm["title"] + "\n```")
        L.append("**Descripción**\n```\n" + sm["description"] + "\n```")
        L.append("**Etiquetas**\n```\n" + ", ".join(sm["tags"]) + "\n```")
        L.append("**Miniatura:** en la app de YouTube elige el fotograma del segundo 0.\n"
                 "**Vídeo relacionado:** enlaza el vídeo largo de esta historia.\n\n---\n")
    if shorts:
        L.append("## 📅 Orden de publicación\n1. Vídeo largo a la hora fija del canal.\n"
                 "2. Short A a las 2–3 h; los demás Shorts en días siguientes (uno al día entre vídeos largos).\n"
                 "3. A las 48 h: captura de YouTube Studio → Analytics del vídeo (retención y CTR) para ajustar guiones.\n")
    else:
        L.append("## 📅 Publicación\n1. Vídeo largo a la hora fija del canal (sin Shorts).\n"
                 "2. A las 48 h: captura de YouTube Studio → Analytics del vídeo (retención y CTR) para ajustar guiones.\n")
    open(os.path.join(E, "SUBIR.md"), "w").write("\n".join(L))
    for src, dst in [("final_largo.mp4", f"{M['code']}_largo.mp4")] + [(f"final_short_{n}.mp4", f"{M['code']}_short_{n}.mp4") for n in shorts]:
        p = os.path.join(vd, "build", src)
        if os.path.exists(p): shutil.copy(p, os.path.join(E, dst))
    print(cap); print("duración", ts(total))

if __name__ == "__main__":
    main(os.path.abspath(sys.argv[1]))
