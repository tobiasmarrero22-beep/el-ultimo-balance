"""Subtítulos traducidos (sin generar audio) sincronizados con la voz española del vídeo largo.
Uso: python3 pipeline/i18n_srt.py <carpeta_video> en pt ...
Lee los textos de <carpeta>/i18n.py (EN, PT, ...) y los tiempos de build/long_plan.json; cada escena traducida ocupa
el mismo hueco que la narración española. Salida: entrega/idiomas/subtitulos_<idioma>.srt y TRADUCCIONES.md
(título y descripción de META_I18N para «Subtítulos > Añadir idioma» en YouTube Studio).
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from meta import write_srt

def pieces_of(text, maxlen=84):
    out = []
    for p in re.split(r"(?<=[\.\?\!:])\s+", text):
        cur = ""
        for w in p.split():
            if len(cur) + len(w) + 1 > maxlen and cur: out.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        if cur: out.append(cur)
    return out

def main(vd, langs):
    ns = {}; exec(open(os.path.join(vd, "i18n.py")).read(), ns)
    plan = json.load(open(os.path.join(vd, "build", "long_plan.json")))
    E = os.path.join(vd, "entrega", "idiomas"); os.makedirs(E, exist_ok=True)
    for lang in langs:
        texts = ns[lang.upper()]
        missing = [sid for sid, *_ in plan if sid not in texts]
        if missing: sys.exit(f"{lang}: faltan traducciones: {missing}")
        cues, t = [], 0.0
        for sid, pre, a, d in plan:
            ps = pieces_of(texts[sid]); tot = sum(len(p) for p in ps); tt = t + pre
            for p in ps:
                dd = a * len(p) / tot; cues.append((tt, tt + dd, p)); tt += dd
            t += d
        out = os.path.join(E, f"subtitulos_{lang}.srt"); write_srt(out, cues)
        print(f"{lang}: {out} ({len(cues)} subtítulos)")
    meta = ns.get("META_I18N", {})
    if meta:
        names = {"en": "Inglés", "pt": "Portugués (Brasil)"}
        with open(os.path.join(E, "TRADUCCIONES.md"), "w") as f:
            f.write("# Traducciones para YouTube Studio\n\nYouTube Studio → Subtítulos → el vídeo → «Añadir idioma» → "
                    "título y descripción (y el SRT en «Subtítulos»).\n")
            for lang in langs:
                m = meta.get(lang)
                if not m: continue
                f.write(f"\n## {names.get(lang, lang)}\n\n**Título**\n```\n{m['title']}\n```\n**Descripción**\n```\n{m['description']}\n```\n"
                        f"**Subtítulos:** `subtitulos_{lang}.srt`\n")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
