# Fútbol Sin Relato · 002 · «Lo pagaron con ropa de entrenamiento» (formato: precio que sube). Aprobado por el usuario el 13-nov-2026.
# Hechos: Gillingham fichó a Tony Cascarino del Crockenhill (Kent League) en enero de 1982 a cambio de chándales y material de
# entrenamiento (Gillingham FC, «Past Masters», 2013; Cascarino). Vendido al Millwall en junio de 1987 por 225.000 £ (récord del
# Millwall entonces). Irlanda: Euro 88, Mundiales 1990 y 1994; 88 partidos y 19 goles.
MUSIC = 1
CARDS = [
    dict(text="Este club fichó a un delantero… y lo pagó con *ropa de entrenamiento*.",
         hero=dict(type="counter", style="tag", frm=0, to=0, suf=" £", label="PRECIO DEL FICHAJE")),
    dict(text="Tony Cascarino jugaba en el Crockenhill, un club modesto de Kent.",
         hero=dict(type="player", name="TONY CASCARINO", sub="INGLATERRA · 1982", num=9)),
    dict(text="El Gillingham lo quería. ¿El precio? *Ropa y material de entrenamiento*.",
         hero=dict(type="items", items=["CONJUNTOS DEPORTIVOS", "MATERIAL DE ENTRENAMIENTO"])),
    dict(text="Cinco años después, lo vendió al Millwall por *225.000 libras*.",
         hero=dict(type="counter", style="tag", frm=0, to=225000, suf=" £", label="MILLWALL · 1987", dur=1.6)),
    dict(text="Y terminó jugando *dos Mundiales* con Irlanda.",
         hero=dict(type="badges", items=["MUNDIAL\n1990", "MUNDIAL\n1994"])),
    dict(text="88 partidos con su selección y 19 goles.",
         hero=dict(type="counter", to=88, dur=1.2, label="PARTIDOS CON IRLANDA", col="white")),
    dict(text="¿Qué jugador valió muchísimo más de lo que costó?",
         hero=dict(type="final")),
]
META = dict(
    code="002",
    title="Lo ficharon a cambio de ropa de entrenamiento… y jugó dos Mundiales",
    description="Inglaterra, 1982: el Gillingham fichó a Tony Cascarino y le pagó al Crockenhill con ropa y material de entrenamiento. Cinco años después valía 225.000 libras.",
    sources=["Gillingham FC: «Past Masters – Tony Cascarino» (2013)",
             "FourFourTwo: entrevista a Tony Cascarino sobre sus comienzos en el Gillingham",
             "The Irish Times: «Cascarino, the hard facts» (88 partidos y 19 goles con Irlanda)"],
    tags=["tony cascarino", "fichajes raros", "fichaje más barato", "gillingham", "millwall", "irlanda", "fútbol", "curiosidades del fútbol", "shorts"],
    hashtags=["#futbol", "#fichajes", "#shorts"],
    pinned="¿Qué jugador valió muchísimo más de lo que costó? 👇",
)
