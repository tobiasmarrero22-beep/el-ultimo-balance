# Dato de Tribuna · 004 · «173.850» (cifra y silencio). Aprobado el 13-nov-2026; relato en voseo.
# Hechos: 16-jul-1950, Maracaná (Río de Janeiro), último partido de la ronda final del Mundial: a Brasil le bastaba el empate.
# Friaça 1-0 (47'), Schiaffino 1-1 (66'), Ghiggia 1-2 (79'). Público oficial: 173.850 (récord de un partido de Mundial).
CHANNEL = "DATO DE TRIBUNA"
VOICE = "D09EpJbk4um1HKSpeTSc"   # Agustín enérgico (ElevenLabs vía DubVoice), elegida por el usuario el 14-nov
SPEED = 1.08
MUSIC = None                     # pedido del usuario (13-nov): sin música, con relato de IA
PRONUNCIA = {}
CARDS = [
    dict(text="173.850 personas en un estadio… y de golpe, *silencio*.",
         say="¡Ciento setenta y tres mil ochocientas cincuenta personas en un estadio!… Y de golpe… silencio.",
         hero=dict(type="counter", to=173850, dur=1.5, label="ESPECTADORES"), crowd=True, cut=True, pad=1.2),
    dict(text="Río de Janeiro, 1950. Brasil contra Uruguay: el partido que decidía el Mundial.",
         say="Río de Janeiro, mil novecientos cincuenta. Brasil contra Uruguay: el partido que decidía el Mundial.",
         hero=dict(type="place", name="RÍO DE JANEIRO", sub="16 DE JULIO DE 1950")),
    dict(text="A Brasil le alcanzaba con *empatar*.",
         hero=dict(type="score", a=0, b=0, ta="BRASIL", tb="URUGUAY")),
    dict(text="¡Brasil se puso 1 a 0!", say="¡Brasil se puso uno a cero!",
         hero=dict(type="score", a=1, b=0, frm=(0, 0), steps=[("uno", 1, 0)], ta="BRASIL", tb="URUGUAY"), crowd=True, pad=0.8),
    dict(text="Pero Uruguay lo dio vuelta: empate… y *2 a 1 para Uruguay*.",
         say="Pero Uruguay lo dio vuelta: empate… ¡y dos a uno para Uruguay!",
         hero=dict(type="score", a=1, b=2, frm=(1, 0), steps=[("empate", 1, 1), ("dos a uno", 1, 2)], ta="BRASIL", tb="URUGUAY"),
         cut="dos a uno", pad=1.0),
    dict(text="Sigue siendo el *récord de público* de un partido de Mundial.",
         hero=dict(type="stamp", text="RÉCORD DE PÚBLICO")),
    dict(text="Lo llamaron el *Maracanazo*. ¿Cuál fue la derrota más dolorosa de tu selección?",
         hero=dict(type="final", text="COMENTÁ")),
]
META = dict(
    playlists=['Historias de los Mundiales', 'Récords imposibles del fútbol'],
    code="004",
    title="173.850 personas… y de golpe, silencio",
    description="Río de Janeiro, 16 de julio de 1950. A Brasil le alcanzaba con empatar contra Uruguay. Lo que pasó después tiene nombre propio: el Maracanazo.",
    sources=["Guinness World Records: mayor asistencia en un partido de la Copa Mundial (173.850, Maracaná 1950)",
             "El Observador (Uruguay): «Maracaná 1950, el origen del mito del Maracanazo»",
             "History.com: «The Maracanã Blow: Brazil's stunning World Cup defeat»"],
    tags=["maracanazo", "uruguay", "brasil", "mundial 1950", "ghiggia", "récord de público", "fútbol", "historia del fútbol", "shorts"],
    hashtags=["#futbol", "#maracanazo", "#mundial", "#shorts"],
    pinned="¿Cuál fue la derrota más dolorosa de tu selección? 👇",
)
