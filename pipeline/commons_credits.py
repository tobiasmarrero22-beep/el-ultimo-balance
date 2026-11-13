
import json, subprocess, urllib.parse, re, time, sys
UA = "ElUltimoBalanceVideoBot/1.0 (educational video production)"
def clean(h): return re.sub(r"<[^>]+>", "", h or "").strip()
def api(**p):
    p.update(action="query", format="json")
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(p)
    for k in range(8):
        out = subprocess.run(["curl", "-sS", "-m", "40", "-A", UA, url], capture_output=True, text=True).stdout
        try: return json.loads(out)
        except Exception: time.sleep(60 * (k + 1))
    return {}
titles = sys.argv[2:]
pre = [t for t in titles if t.endswith("…")]
full = [t for t in titles if not t.endswith("…")]
for t in pre:
    j = api(list="prefixsearch", pssearch=t[:-1], psnamespace=6, pslimit=1)
    for r in j.get("query", {}).get("prefixsearch", []): full.append(r["title"])
    time.sleep(5)
j = api(titles="|".join(full), prop="imageinfo", iiprop="url|extmetadata")
out = {}
for p in j.get("query", {}).get("pages", {}).values():
    ii = (p.get("imageinfo") or [{}])[0]; m = ii.get("extmetadata", {})
    out[p["title"]] = {"lic": clean(m.get("LicenseShortName", {}).get("value")), "artist": clean(m.get("Artist", {}).get("value"))[:150],
                       "credit": clean(m.get("Credit", {}).get("value"))[:150], "page": ii.get("descriptionurl"), "url": ii.get("url")}
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1); print(len(out), "créditos")
