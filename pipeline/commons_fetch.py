# Busca fotos con licencia libre en Wikimedia Commons para las claves de IMAGES y guarda candidatas + créditos.
# Uso: python3 commons_fetch.py <carpeta_video> <json_consultas> <dir_salida>
import json, os, re, subprocess, sys, urllib.parse
UA = "ElUltimoBalanceVideoBot/1.0 (educational video production)"
OK = re.compile(r"^(public domain|pd|cc0|cc by (2\.0|2\.5|3\.0|4\.0)|cc-by-(2\.0|2\.5|3\.0|4\.0))", re.I)
import time
def api(**p):
    p.update(action="query", format="json", maxlag=5)
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(p)
    for k in range(6):
        time.sleep(3)  # sin prisas: límite de peticiones de Wikimedia
        out = subprocess.run(["curl", "-sS", "-m", "40", "-A", UA, url], capture_output=True, text=True).stdout
        try: return json.loads(out)
        except Exception: print("  (Wikimedia pide esperar; reintento)", flush=True); time.sleep(45 * (k + 1))
    return {}
def clean(h): return re.sub(r"<[^>]+>", "", h or "").strip()
vd, qfile, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(outdir, exist_ok=True)
queries = json.load(open(qfile))
cj = os.path.join(outdir, "candidatas.json")
res = json.load(open(cj)) if os.path.exists(cj) else {}
for key, qs in queries.items():
    cands = []
    for q in qs:
        j = api(generator="search", gsrsearch=q + " filetype:bitmap", gsrnamespace=6, gsrlimit=12, prop="imageinfo",
                iiprop="url|size|extmetadata|mime", iiurlwidth=1920)
        pages = sorted((j.get("query", {}) or {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
        for p in pages:
            ii = (p.get("imageinfo") or [{}])[0]; m = ii.get("extmetadata", {})
            lic = clean(m.get("LicenseShortName", {}).get("value", ""))
            if not OK.match(lic) or ii.get("width", 0) < 1200 or ii.get("mime") not in ("image/jpeg", "image/png"): continue
            cands.append({"title": p["title"], "lic": lic, "w": ii["width"], "h": ii["height"], "thumb": ii.get("thumburl") or ii["url"],
                          "page": ii.get("descriptionurl"), "artist": clean(m.get("Artist", {}).get("value", ""))[:120],
                          "credit": clean(m.get("Credit", {}).get("value", ""))[:120]})
        if len(cands) >= 3: break
    res[key] = cands[:4]
    for i, c in enumerate(res[key][:3]):
        f = os.path.join(outdir, f"{key}__{i}.jpg")
        time.sleep(2); subprocess.run(["curl", "-sS", "-m", "60", "-A", UA, "-o", f, c["thumb"]])
    json.dump(res, open(os.path.join(outdir, "candidatas.json"), "w"), ensure_ascii=False, indent=1)
    print(key, len(res[key]), "|", " || ".join(f"{c['title'][5:60]} [{c['lic']}]" for c in res[key][:3]), flush=True)
json.dump(res, open(os.path.join(outdir, "candidatas.json"), "w"), ensure_ascii=False, indent=1)
