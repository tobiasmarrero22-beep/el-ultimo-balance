import json, ssl, urllib.request, urllib.parse, os, time
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
BASE = "https://www.googleapis.com/youtube/v3/"
UNITS = {"n": 0}
def get(endpoint, **params):
    url = BASE + endpoint + "?" + urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(url, headers={"X-goog-api-key": "dummy"})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
                UNITS["n"] += 100 if endpoint == "search" else 1
                return json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:500]
            if e.code in (500, 503) and i < 2:
                time.sleep(2 ** i); continue
            raise RuntimeError(f"{e.code} {body}")
def search(q, lang, after, duration=None, n=50, order="viewCount"):
    p = dict(part="snippet", q=q, type="video", maxResults=n, order=order,
             publishedAfter=after, relevanceLanguage=lang)
    if duration: p["videoDuration"] = duration
    return [it["id"]["videoId"] for it in get("search", **p).get("items", [])]
def videos(ids):
    out = []
    for i in range(0, len(ids), 50):
        out += get("videos", part="snippet,statistics,contentDetails", id=",".join(ids[i:i+50])).get("items", [])
    return out
def channels(ids):
    out = {}
    ids = list(dict.fromkeys(ids))
    for i in range(0, len(ids), 50):
        for c in get("channels", part="snippet,statistics", id=",".join(ids[i:i+50])).get("items", []):
            out[c["id"]] = c
    return out
ES_MARK = [" de ", " la ", " el ", " que ", " los ", " las ", " por ", " para ", " con ", " una ", " es ", " del ", " qué ", " cómo ", " así "]
EN_MARK = [" the ", " of ", " and ", " to ", " you ", " is ", " in ", " how ", " why ", " what ", " this ", " was ", " his ", " her "]
def lang_of(v):
    sn = v["snippet"]
    l = (sn.get("defaultAudioLanguage") or sn.get("defaultLanguage") or "")[:2].lower()
    t = " " + sn["title"].lower() + " "
    es = sum(t.count(m) for m in ES_MARK) + sum(t.count(c) for c in "ñáéíóú¿¡")
    en = sum(t.count(m) for m in EN_MARK)
    if es > en: return "es"
    if en > es: return "en"
    return l or "?"
