# Stoppage Time Facts · 004 · Maracanazo. Adaptación al inglés del Short 004 de Dato de Tribuna (mismos hechos verificados).
CHANNEL = "STOPPAGE TIME FACTS"
LANG = "en"
THOUSANDS = ","
VOICE = "hbdLfaIj2uL2NimPQh6e"   # Ben, sports narrator (americano), elegida por el usuario el 14-nov
SPEED = 1.05
MUSIC = None
THEME = {"GREEN_D": (9, 30, 46), "GREEN_L": (12, 39, 58), "YEL": (255, 152, 32)}   # partido de noche: azul y naranja
PRONUNCIA = {"Maracanazo": "Maracanaso"}
CARDS = [
    dict(text="173,850 people in one stadium… and then, *silence*.",
         say="A hundred and seventy-three thousand, eight hundred and fifty people in one stadium!… And then… silence.",
         hero=dict(type="counter", to=173850, dur=1.5, label="SPECTATORS"), crowd=True, cut=True, pad=1.2),
    dict(text="Rio de Janeiro, 1950. Brazil vs Uruguay: the match that decided the World Cup.",
         say="Rio de Janeiro, nineteen fifty. Brazil versus Uruguay: the match that decided the World Cup.",
         hero=dict(type="place", name="RIO DE JANEIRO", sub="16 JULY 1950")),
    dict(text="Brazil only needed *a draw*.",
         hero=dict(type="score", a=0, b=0, ta="BRAZIL", tb="URUGUAY")),
    dict(text="Brazil went 1–0 up!", say="Brazil went one-nil up!",
         hero=dict(type="score", a=1, b=0, frm=(0, 0), steps=[("one", 1, 0)], ta="BRAZIL", tb="URUGUAY"), crowd=True, pad=0.8),
    dict(text="But Uruguay turned it around: 1–1… and *2–1 to Uruguay*.",
         say="But Uruguay turned it around: one-all… and two-one to Uruguay!",
         hero=dict(type="score", a=1, b=2, frm=(1, 0), steps=[("one-all", 1, 1), ("two-one", 1, 2)], ta="BRAZIL", tb="URUGUAY"),
         cut="two-one", pad=1.0),
    dict(text="It's still the *biggest crowd* ever at a World Cup match.",
         hero=dict(type="stamp", text="RECORD CROWD")),
    dict(text="They called it the *Maracanazo*. What's your country's most painful defeat?",
         hero=dict(type="final", text="COMMENT")),
]
META = dict(
    playlists=["World Cup Stories", "Impossible Football Records"],
    code="004",
    title="173,850 people… and then, silence",
    description="Rio de Janeiro, 16 July 1950. Brazil only needed a draw against Uruguay. What happened next has its own name: the Maracanazo.",
    sources=["Guinness World Records: largest attendance at a FIFA World Cup match (173,850, Maracanã 1950)",
             "El Observador (Uruguay): «Maracaná 1950, el origen del mito del Maracanazo»",
             "History.com: «The Maracanã Blow: Brazil's stunning World Cup defeat»"],
    tags=["maracanazo", "uruguay", "brazil", "world cup 1950", "ghiggia", "record attendance", "football history", "soccer facts", "shorts"],
    hashtags=["#football", "#worldcup", "#maracanazo", "#shorts"],
    pinned="What's your country's most painful defeat? 👇",
)
