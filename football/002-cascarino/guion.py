# Stoppage Time Facts · 002 · Cascarino. Adaptación al inglés del Short 002 de Dato de Tribuna (mismos hechos verificados).
CHANNEL = "STOPPAGE TIME FACTS"
LANG = "en"
THOUSANDS = ","
VOICE = "gU0LNdkMOQCOrPrwtbee"   # PENDIENTE de que el usuario elija entre football/voice_samples (1 British Football Announcer, 2 Connor, 3 Ben)
SPEED = 1.05
MUSIC = None
THEME = {"GREEN_D": (9, 30, 46), "GREEN_L": (12, 39, 58), "YEL": (255, 152, 32)}   # partido de noche: azul y naranja
PRONUNCIA = {"Gillingham": "Jillingum", "Millwall": "Mill-wall"}
CARDS = [
    dict(text="This club signed a striker… and paid for him with *training kit*.",
         hero=dict(type="counter", style="tag", frm=0, to=0, pre="£", label="TRANSFER FEE")),
    dict(text="England, 1982. Tony Cascarino was playing for Crockenhill, a tiny non-league club in Kent.",
         say="England, nineteen eighty-two. Tony Cascarino was playing for Crockenhill, a tiny non-league club in Kent.",
         hero=dict(type="player", name="TONY CASCARINO", sub="ENGLAND · 1982", num=9)),
    dict(text="Gillingham wanted him. The fee? *Tracksuits and training equipment*.",
         hero=dict(type="items", items=["TRACKSUITS", "TRAINING EQUIPMENT"])),
    dict(text="Five years later, they sold him to Millwall for *£225,000*.",
         say="Five years later, they sold him to Millwall for… two hundred and twenty-five thousand pounds!",
         hero=dict(type="counter", style="tag", frm=0, to=225000, pre="£", label="MILLWALL · 1987", dur=1.6)),
    dict(text="And he went on to play at *two World Cups* for Ireland!",
         hero=dict(type="badges", items=["WORLD CUP\n1990", "WORLD CUP\n1994"])),
    dict(text="88 caps and 19 goals for his country.",
         say="Eighty-eight caps and nineteen goals for his country.",
         hero=dict(type="counter", to=88, dur=1.2, label="IRELAND CAPS", col="white")),
    dict(text="Which player turned out to be worth way more than he cost? *Comment below*.",
         hero=dict(type="final", text="COMMENT")),
]
META = dict(
    playlists=["Strangest Transfers Ever"],
    code="002",
    title="Signed for some tracksuits… then he played at two World Cups",
    description="England, 1982: Gillingham signed Tony Cascarino from Crockenhill and paid with tracksuits and training equipment. Five years later he was worth £225,000.",
    sources=["Gillingham FC: «Past Masters – Tony Cascarino» (2013)",
             "FourFourTwo: Tony Cascarino on his start at Gillingham",
             "The Irish Times: «Cascarino, the hard facts» (88 caps, 19 goals for Ireland)"],
    tags=["tony cascarino", "strangest transfers", "cheapest transfer ever", "gillingham", "millwall", "ireland", "football facts", "soccer facts", "shorts"],
    hashtags=["#football", "#transfers", "#shorts"],
    pinned="Which player turned out to be worth way more than he cost? 👇",
)
