# Fútbol Sin Relato · 001 · «149 a 0» (formato: historia en tarjetas). Guion aprobado por el usuario el 13-nov-2026.
# Hechos: AS Adema 149–0 SO l'Emyrne, liga de Madagascar, 31-oct-2002. SOE metió todos los goles en contra como protesta por un
# penal polémico (a favor de DSA Antananarivo) en el partido anterior, que les costó el título. La federación suspendió 3 años al
# entrenador (Ratsimandresy Ratsarazaka). Guinness: récord de goles en contra en un partido de liga.
MUSIC = 0
CARDS = [
    dict(text="El resultado más abultado de la historia del fútbol.",
         hero=dict(type="score", a=149, b=0, frm=(0, 0), roll=1.4, ta="AS ADEMA", tb="SO L'EMYRNE")),
    dict(text="Y los 149 goles los metió… *el equipo que perdió*.",
         hero=dict(type="score", a=149, b=0, ta="AS ADEMA", tb="SO L'EMYRNE")),
    dict(text="Un partido de liga: AS Adema contra SO l'Emyrne.",
         hero=dict(type="place", name="MADAGASCAR", sub="31 DE OCTUBRE DE 2002")),
    dict(text="En el partido anterior, un *penal polémico* en el final los había dejado sin el título.",
         hero=dict(type="big", text="PENAL\nPOLÉMICO"), sfx=[("whistle", 0.1)]),
    dict(text="Su protesta: desde el saque inicial, patearon una y otra vez *a su propio arco*.",
         hero=dict(type="counter", to=149, dur=3.2, label="GOLES EN CONTRA", col="red")),
    dict(text="El castigo: su entrenador, ^suspendido 3 años^.",
         hero=dict(type="redcard", text="3 AÑOS")),
    dict(text="¿Cuál es el resultado más loco que viste?",
         hero=dict(type="final")),
]
META = dict(
    code="001",
    title="149 a 0… y los goles los metió el equipo que perdió",
    description="Madagascar, 31 de octubre de 2002: AS Adema 149, SO l'Emyrne 0. El récord más loco del fútbol tuvo una explicación: una protesta.",
    sources=["Guinness World Records: más goles en contra en un partido de liga (AS Adema 149–0 SO l'Emyrne, 2002)",
             "ESPN y The Guardian (noviembre de 2002): la protesta de SO l'Emyrne y la sanción a su entrenador"],
    tags=["149 a 0", "resultado más abultado", "récord fútbol", "madagascar", "goles en contra", "fútbol", "curiosidades del fútbol", "shorts"],
    hashtags=["#futbol", "#records", "#shorts"],
    pinned="¿Cuál es el resultado más loco que viste en vivo? 👇",
)
