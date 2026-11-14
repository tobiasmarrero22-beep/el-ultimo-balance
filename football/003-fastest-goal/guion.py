# Stoppage Time Facts · 003 · Quiz del gol más rápido. Adaptación al inglés del Short 003 de Dato de Tribuna.
CHANNEL = "STOPPAGE TIME FACTS"
LANG = "en"
THOUSANDS = ","
VOICE = "hbdLfaIj2uL2NimPQh6e"   # Ben, sports narrator (americano), elegida por el usuario el 14-nov
SPEED = 1.05
MUSIC = None
THEME = {"GREEN_D": (9, 30, 46), "GREEN_L": (12, 39, 58), "YEL": (255, 152, 32)}   # partido de noche: azul y naranja
PRONUNCIA = {"Şükür": "Shukur", "Hakan": "Hakan"}
CARDS = [
    dict(text="How long did the *fastest goal* in World Cup history take? You've got 3 seconds.",
         say="How long did the fastest goal in World Cup history take? You've got three seconds.",
         hero=dict(type="quiz", opts=["11 SECONDS", "27 SECONDS", "45 SECONDS"])),
    dict(text="*11 seconds!*", say="Eleven seconds!",
         hero=dict(type="quiz", opts=["11 SECONDS", "27 SECONDS", "45 SECONDS"], reveal=0), d=1.6),
    dict(text="Hakan Şükür, Turkey, against South Korea, in the 2002 World Cup third-place match.",
         say="Hakan Şükür, Turkey, against South Korea, in the two thousand and two World Cup third-place match.",
         hero=dict(type="clock", to="00:11", dur=1.2, label="TURKEY – SOUTH KOREA · 2002")),
    dict(text="Korea kicked off, lost the ball… and Şükür tucked it away.",
         hero=dict(type="tactic", step=0.6,
                   players=[(0.5, 0.94, "x"), (0.6, 0.56, "x"), (0.45, 0.44, "o"), (0.62, 0.24, "o")],
                   path=[[0.5, 0.94, 0.6, 0.56, "pase"], [0.6, 0.56, 0.45, 0.44, "pase"], [0.45, 0.44, 0.62, 0.24, "pase"], [0.62, 0.24, 0.5, 0.0, "tiro"]])),
    dict(text="24 years later, *not even the 2026 World Cup* could beat it.",
         say="Twenty-four years later, not even the twenty twenty-six World Cup could beat it.",
         hero=dict(type="stamp", text="STILL THE RECORD")),
    dict(text="Did you get it right? Comment A, B or C… no cheating.",
         hero=dict(type="final", text="COMMENT")),
]
META = dict(
    playlists=["Football Quiz: 3 Seconds", "World Cup Stories"],
    code="003",
    title="How long did the fastest World Cup goal take? You've got 3 seconds",
    description="The record not even the 2026 World Cup could break: Hakan Şükür, Turkey vs South Korea, 2002 third-place match.",
    sources=["ESPN: «Who scored the fastest goal in men's World Cup history?»",
             "El Gráfico (2026): the fastest goals in World Cup history"],
    tags=["fastest goal", "hakan sukur", "world cup 2002", "world cup records", "football quiz", "world cup 2026", "soccer facts", "shorts"],
    hashtags=["#football", "#worldcup", "#quiz", "#shorts"],
    pinned="Did you get it right? A, B or C 👇 (no cheating)",
)
