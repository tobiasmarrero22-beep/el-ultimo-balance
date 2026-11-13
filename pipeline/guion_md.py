"""Guion para revisar con el usuario ANTES de producir (voz, imágenes, render): guion_revision.md + comprobación de las reglas fijas.

Uso: python3 pipeline/guion_md.py <carpeta_del_vídeo>
  - El Último Balance / 70x7: lee guion.py (SCENES con text, visual).
  - Anacron: lee script.json (scenes con narration, chapter).

Reglas fijas de guion (todos los canales, pedido del usuario 13-nov-2026):
  1. Gancho fuerte en los primeros segundos: qué va a ver, por qué le importa y por qué quedarse.
  2. Estructura por bloques: GANCHO → DESARROLLO → CIERRE.
  3. Preguntas abiertas: dudas que no se resuelven en el momento, sino más adelante.
  4. Regla de oro: cuando se cierra una pregunta, se abre otra (el espectador nunca piensa "ya me puedo ir").
  5. Sin saludos ni relleno: el gancho empieza en el segundo 0 contando la historia.

Marcas opcionales por escena (en guion.py como claves del dict; en script.json como campos):
  bloque="desarrollo" | "cierre"   → primera escena de ese bloque (el gancho va desde el principio hasta la primera
                                     de "desarrollo"; si no se marca, el desarrollo empieza en el primer capítulo)
  abre="P1: ¿Por qué...?"           → abre una pregunta (P1, P2, ...); puede ser lista
  cierra="P1"                       → la resuelve; puede ser lista
"""
import json, os, re, sys

SALUDOS = re.compile(r"^\s*(hola|buenas|bienvenid|qué tal|que tal|hey|en este v[ií]deo|en el v[ií]deo de hoy|hoy (vamos|te voy|les voy)|"
                     r"antes de empezar|no olvides|suscr[ií]bete)", re.I)


def as_list(v):
    if not v: return []
    return v if isinstance(v, list) else [v]


def load(vd):
    if os.path.exists(os.path.join(vd, "guion.py")):
        ns = {}; exec(open(os.path.join(vd, "guion.py"), encoding="utf-8").read(), ns)
        out = []
        for s in ns["SCENES"]:
            v = s.get("visual", {})
            chap = v.get("name") or v.get("text") if v.get("type") == "title" else None
            out.append({"id": s["id"], "text": s["text"], "chapter": chap, "bloque": s.get("bloque"),
                        "abre": as_list(s.get("abre")), "cierra": as_list(s.get("cierra")), "vis": v.get("type", "")})
        M = ns.get("META", {}); title = (M.get("titles") or [""])[0]
        extra = {"sources": M.get("sources", []), "disclosure": M.get("disclosure", ""), "altered": M.get("altered")}
        return out, title, 15.0, extra  # ~15 caracteres por segundo (voz Adán)
    s = json.load(open(os.path.join(vd, "script.json"), encoding="utf-8"))
    cfg = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(vd))), "config.json"), encoding="utf-8"))
    cps = cfg.get("voice", {}).get("chars_per_sec", 15)
    out = [{"id": f"{i + 1:03d}", "text": sc["narration"].replace("**", ""), "chapter": sc.get("chapter"), "bloque": sc.get("bloque"),
            "abre": as_list(sc.get("abre")), "cierra": as_list(sc.get("cierra")), "vis": sc.get("bg", "")} for i, sc in enumerate(s["scenes"])]
    y = s.get("youtube", {})
    extra = {"sources": y.get("sources", []), "disclosure": "Anacron: voz sintética (aviso fijo en canal/disclaimer.txt)", "altered": "No"}
    return out, s.get("title", ""), cps, extra


def check(scenes, cps, extra=None):
    warn = []
    extra = extra or {}
    # reglas anti-desmonetización que se pueden comprobar solas
    if len(extra.get("sources") or []) < 2: warn.append("faltan fuentes citadas (mínimo 2) para la descripción: regla anti-desmonetización 1")
    if not extra.get("disclosure"): warn.append("falta el aviso de IA en la descripción (META[\"disclosure\"]): regla anti-desmonetización 4")
    # bloques
    blk, cur = [], "gancho"
    first_chap = next((i for i, s in enumerate(scenes) if s["chapter"]), None)
    has_dev = any(s["bloque"] == "desarrollo" for s in scenes)
    for i, s in enumerate(scenes):
        if s["bloque"] in ("desarrollo", "cierre"): cur = s["bloque"]
        elif not has_dev and cur == "gancho" and first_chap is not None and i >= first_chap: cur = "desarrollo"
        blk.append(cur)
    if "cierre" not in blk: warn.append("falta marcar el bloque de CIERRE (bloque=\"cierre\" en su primera escena)")
    g = [s for s, b in zip(scenes, blk) if b == "gancho"]
    gsec = sum(len(s["text"]) for s in g) / cps
    if not g: warn.append("no hay GANCHO antes del desarrollo")
    elif gsec > 75: warn.append(f"el gancho dura ~{gsec:.0f} s: que no pase de ~60 s")
    # saludo / relleno al principio
    if scenes and SALUDOS.match(scenes[0]["text"]): warn.append("la primera frase es un saludo o relleno: empezar contando la historia")
    for s in scenes[:4]:
        if re.search(r"bienvenid|suscr[ií]bete|dale like|activa la campana", s["text"], re.I):
            warn.append(f"{s['id']}: saludo o petición de suscripción en el gancho")
    # preguntas abiertas y regla de oro
    abiertas, cuando, timeline = {}, {}, []
    for i, (s, b) in enumerate(zip(scenes, blk)):
        for a in s["abre"]:
            k = a.split(":")[0].strip(); abiertas[k] = a; cuando[k] = s["id"]
        for c in s["cierra"]:
            k = c.split(":")[0].strip()
            if k not in abiertas: warn.append(f"{s['id']}: cierra {k}, que no estaba abierta")
            else: abiertas.pop(k)
            if b != "cierre" and not abiertas:
                warn.append(f"{s['id']}: al cerrar {k} no queda ninguna pregunta abierta (regla de oro: abrir otra)")
        timeline.append(len(abiertas))
    for k, a in abiertas.items(): warn.append(f"queda sin cerrar {a} (abierta en {cuando[k]})")
    n_abre = sum(len(s["abre"]) for s in scenes)
    if n_abre < 3: warn.append(f"solo {n_abre} preguntas abiertas marcadas: ir dejando dudas que se resuelvan más adelante")
    # tramos largos sin ninguna pregunta abierta (fuera del cierre)
    run = 0
    for s, b, n in zip(scenes, blk, timeline):
        run = run + len(s["text"]) / cps if (n == 0 and b == "desarrollo") else 0
        if run > 90: warn.append(f"hacia {s['id']}: más de 90 s de desarrollo sin ninguna pregunta abierta"); run = -1e9
    return blk, timeline, warn


def write(vd):
    scenes, title, cps, extra = load(vd)
    blk, timeline, warn = check(scenes, cps, extra)
    tot = sum(len(s["text"]) for s in scenes)
    L = [f"# Guion para revisar · {title}", "",
         f"{len(scenes)} escenas · {tot:,} caracteres · ~{tot / cps / 60:.1f} min de narración".replace(",", "."), "",
         "Reglas: gancho en el segundo 0 (qué va a ver, por qué le importa, por qué quedarse) · GANCHO → DESARROLLO → CIERRE · "
         "preguntas abiertas que se resuelven más adelante · al cerrar una, se abre otra · sin saludos ni relleno.",
         "Anti-desmonetización: guion original con fuentes · variedad frente a los vídeos anteriores · nada de material ajeno sin "
         "comentario · aviso de IA · calidad antes que cantidad.", ""]
    L += ["## Comprobación automática", ""] + ([f"- ⚠️ {w}" for w in warn] or ["- ✅ Cumple las reglas que se pueden comprobar solas."]) + [""]
    qs = [(s["id"], a) for s in scenes for a in s["abre"]]
    if qs:
        L += ["## Preguntas abiertas", ""]
        for sid, a in qs:
            k = a.split(":")[0].strip()
            cierre = next((s["id"] for s in scenes if any(c.split(":")[0].strip() == k for c in s["cierra"])), "—")
            L.append(f"- **{a}** · se abre en {sid} · se cierra en {cierre}")
        L.append("")
    cur = None; t = 0.0
    for s, b, n in zip(scenes, blk, timeline):
        if b != cur:
            cur = b; L += ["", f"## {b.upper()}", ""]
        if s["chapter"]: L += [f"### {s['chapter']}", ""]
        mm = f"{int(t // 60)}:{int(t % 60):02d}"
        tags = "".join([f" ❓**abre {a}**" for a in s["abre"]] + [f" ✅**cierra {c}**" for c in s["cierra"]])
        L.append(f"`{mm}` **{s['id']}** {s['text']}{tags}")
        L.append("")
        t += len(s["text"]) / cps + 0.4
    out = os.path.join(vd, "guion_revision.md")
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    return out, warn


if __name__ == "__main__":
    out, warn = write(sys.argv[1])
    print(out); [print("  ⚠️", w) for w in warn]
