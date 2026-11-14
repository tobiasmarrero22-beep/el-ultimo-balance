# Stoppage Time Facts · 001 · «149–0». Adaptación al inglés del Short 001 de Dato de Tribuna (mismos hechos verificados).
# AS Adema 149–0 SO l'Emyrne, liga de Madagascar, 31-oct-2002: protesta por un penal polémico en el partido anterior;
# entrenador suspendido 3 años. Guinness: récord de goles en contra en un partido de liga.
CHANNEL = "STOPPAGE TIME FACTS"
LANG = "en"
THOUSANDS = ","
VOICE = "hbdLfaIj2uL2NimPQh6e"   # Ben, sports narrator (americano), elegida por el usuario el 14-nov
SPEED = 1.05
MUSIC = None
THEME = {"GREEN_D": (9, 30, 46), "GREEN_L": (12, 39, 58), "YEL": (255, 152, 32)}   # partido de noche: azul y naranja
PRONUNCIA = {"SO l'Emyrne": "S.O. Lemirn", "AS Adema": "A.S. Adema"}
CARDS = [
    dict(text="149–0! The most lopsided scoreline in football history.",
         say="A hundred and forty-nine… nil! The most lopsided scoreline in football history.",
         hero=dict(type="score", a=149, b=0, frm=(0, 0), roll=1.6, ta="AS ADEMA", tb="SO L'EMYRNE")),
    dict(text="And all 149 goals were scored by… *the team that lost*.",
         say="And all a hundred and forty-nine goals were scored by… the team that lost!",
         hero=dict(type="score", a=149, b=0, ta="AS ADEMA", tb="SO L'EMYRNE")),
    dict(text="Madagascar, 2002: AS Adema vs SO l'Emyrne, a league match.",
         say="Madagascar, two thousand and two. AS Adema versus SO l'Emyrne, a league match.",
         hero=dict(type="place", name="MADAGASCAR", sub="31 OCTOBER 2002")),
    dict(text="In their previous game, a *controversial penalty* late on had cost them the title.",
         hero=dict(type="big", text="CONTROVERSIAL\nPENALTY"), sfx=[("whistle", 0.1)]),
    dict(text="So how did they protest? From kick-off, they kept shooting *into their own net*.",
         hero=dict(type="counter", to=149, dur=3.2, label="OWN GOALS", col="red")),
    dict(text="The punishment: their coach was ^banned for 3 years^.",
         say="The punishment: their coach was banned for three years.",
         hero=dict(type="redcard", text="3 YEARS")),
    dict(text="What's the craziest scoreline you've ever seen? *Comment below*.",
         hero=dict(type="final", text="COMMENT")),
]
META = dict(
    playlists=["Impossible Football Records"],
    code="001",
    title="149–0… and every goal was scored by the team that lost",
    description="Madagascar, 31 October 2002: AS Adema 149, SO l'Emyrne 0. The craziest record in football had one explanation: a protest.",
    sources=["Guinness World Records: most own goals in a domestic league match (AS Adema 149–0 SO l'Emyrne, 2002)",
             "ESPN and The Guardian (November 2002): SO l'Emyrne's protest and their coach's ban"],
    tags=["149-0", "biggest win in football", "football records", "madagascar football", "own goals", "football facts", "soccer facts", "shorts"],
    hashtags=["#football", "#soccer", "#records", "#shorts"],
    pinned="What's the craziest scoreline you've ever seen live? 👇",
)
