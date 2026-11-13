# Dato de Tribuna · 003 · «Adivina en 3 segundos» (quiz). Aprobado el 13-nov-2026; relato en voseo.
# Hechos: Hakan Şükür marcó a los 11 segundos (algunas fuentes: 10,8) ante Corea del Sur, partido por el tercer puesto del Mundial
# 2002. Corea sacó del medio; Hong Myung-bo perdió la pelota, İlhan Mansız se la dio a Şükür. En el Mundial 2026 nadie lo superó.
CHANNEL = "DATO DE TRIBUNA"
VOICE = "D09EpJbk4um1HKSpeTSc"   # PENDIENTE de que el usuario elija entre futbol/muestras_voz (1 Agustín enérgico, 2 Agustín rápido, 3 Agus, 4 Renzo)
SPEED = 1.08
MUSIC = None                     # pedido del usuario (13-nov): sin música, con relato de IA
PRONUNCIA = {"Şükür": "Shukur", "Hakan": "Jakan"}
CARDS = [
    dict(text="¿Cuánto tardó el *gol más rápido* de la historia de los Mundiales? Tenés 3 segundos.",
         say="¿Cuánto tardó el gol más rápido de la historia de los Mundiales? Tenés tres segundos.",
         hero=dict(type="quiz", opts=["11 SEGUNDOS", "27 SEGUNDOS", "45 SEGUNDOS"])),
    dict(text="*¡11 segundos!*", say="¡Once segundos!",
         hero=dict(type="quiz", opts=["11 SEGUNDOS", "27 SEGUNDOS", "45 SEGUNDOS"], reveal=0), d=1.6),
    dict(text="Hakan Şükür, Turquía, contra Corea del Sur, por el tercer puesto del Mundial 2002.",
         say="Hakan Şükür, Turquía, contra Corea del Sur, por el tercer puesto del Mundial dos mil dos.",
         hero=dict(type="clock", to="00:11", dur=1.2, label="TURQUÍA – COREA DEL SUR · 2002")),
    dict(text="Corea sacó del medio, perdió la pelota… y Şükür la empujó.",
         hero=dict(type="tactic", step=0.6,
                   players=[(0.5, 0.94, "x"), (0.6, 0.56, "x"), (0.45, 0.44, "o"), (0.62, 0.24, "o")],
                   path=[[0.5, 0.94, 0.6, 0.56, "pase"], [0.6, 0.56, 0.45, 0.44, "pase"], [0.45, 0.44, 0.62, 0.24, "pase"], [0.62, 0.24, 0.5, 0.0, "tiro"]])),
    dict(text="Pasaron 24 años y *ni el Mundial 2026* pudo superarlo.",
         say="Pasaron veinticuatro años y ni el Mundial dos mil veintiséis pudo superarlo.",
         hero=dict(type="stamp", text="RÉCORD VIGENTE")),
    dict(text="¿Acertaste? Comentá A, B o C, sin hacer trampa.",
         hero=dict(type="final", text="COMENTÁ")),
]
META = dict(
    code="003",
    title="¿Cuánto tardó el gol más rápido de un Mundial? Tenés 3 segundos",
    description="El récord que ni el Mundial 2026 pudo romper: Hakan Şükür, Turquía contra Corea del Sur, partido por el tercer puesto de 2002.",
    sources=["ESPN: «Who scored the fastest goal in men's World Cup history?»",
             "El Gráfico (2026): los goles más rápidos de la historia de la Copa del Mundo"],
    tags=["gol más rápido", "hakan şükür", "mundial 2002", "récords mundiales", "quiz de fútbol", "mundial 2026", "fútbol", "shorts"],
    hashtags=["#futbol", "#mundial", "#quiz", "#shorts"],
    pinned="¿Acertaste? A, B o C 👇 (sin hacer trampa)",
)
