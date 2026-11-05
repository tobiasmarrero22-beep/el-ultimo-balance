# Vídeo 005 — Volkswagen: la mentira del diésel… y por qué hoy cierra fábricas
# Lecciones aplicadas (datos del 5-nov): arranque en plena acción, sin gráficas en los primeros 30 s, mini-cliffhangers
# cada 60–90 s, Shorts de 20–25 s, título que no lo revela todo. Visuales: tomas de stock vía vidIQ (Pexels), nada reutilizado.
VOICE = "i4Kar2uamCWyas8TAu31"  # ElevenLabs "Adán - Narration"
SPEED = 1.0
# Hechos verificados (2026-11-05): CarAdvice/Bloomberg/WVU/IEEE (estudio de WVU para el ICCT, ~50.000 $, Jetta y Passat,
# 15–35 veces el límite de NOx), CityAM/Ratchet+Wrench (VW supera a Toyota en el 1er semestre de 2015: 5,04 vs 5,02 M),
# Asiae/ara.cat/techxplore (10,7 M de coches; coste > 30.000–33.000 M€), IndustryWeek/Fortune/TheLocal (Oliver Schmidt,
# 7 años, dic-2017), OCCRP/Fortune/Carscoops (Braunschweig 26-may-2025: Hadler 4,5 años, Jelden 2 años y 7 meses, dos
# condenas suspendidas; 31 acusados pendientes), TimesLive/BusinessDay (juicio de Winterkorn sept-2024, suspendido por
# salud; él lo niega), Bloomberg/CarNewsChina (BYD supera a VW en China en 2023, VW lideraba desde al menos 2008),
# electrive/AP-US News/OSW (acuerdo de 2024: 35.000 empleos para 2030; Dresde deja de fabricar coches; Osnabrück vendida;
# 3-sept-2026: 50.000 empleos más y fin de producción en 4 plantas), El Universal/Xataka/CarAdvice (último vocho:
# Puebla, 30-jul-2003, unidad 21.529.464, hoy en Wolfsburgo).

BROLL = {  # clave → búsqueda en vidIQ (vidiq_generate_broll); el clip se guarda en clips/<clave>.mp4
    "road_test": "car driving on highway usa daytime",
    "exhaust": "car exhaust pipe smoke close up",
    "beetle": "classic volkswagen beetle",
    "assembly": "car factory assembly line robots",
    "factory_empty": "empty factory hall dark",
    "lab": "car emissions test laboratory dynamometer",
    "code": "computer code on screen dark",
    "boardroom": "business meeting boardroom serious",
    "stock_crash": "stock market chart falling red screen",
    "money": "euro banknotes counting",
    "court": "courtroom judge gavel",
    "prison": "prison corridor bars",
    "china_ev": "electric car charging city china",
    "workers": "factory workers walking shift",
    "mexico_street": "mexico city street traffic",
    "highway_night": "highway traffic at night",
}

SCENES = [
    # --- GANCHO (en plena acción, sin gráficas) ---
    dict(id="s01", text="Dos mil trece. Un pequeño equipo de una universidad de Estados Unidos sale a la carretera con dos Volkswagen diésel y una máquina que mide lo que sale por el tubo de escape.",
         visual=dict(type="img", key="road_test", cap="EE. UU., 2013")),
    dict(id="s02", text="Lo que ven no tiene sentido. Uno de los coches contamina hasta treinta y cinco veces más de lo que permite la ley.",
         visual=dict(type="img", key="exhaust", cap="HASTA 35 VECES EL LÍMITE")),
    dict(id="s02b", text="Para comparar, también midieron un BMW diésel. Ese salió limpio. El problema era solo de Volkswagen.",
         visual=dict(type="img", key="highway_night", cap="EL BMW: LIMPIO")),
    dict(id="s03", text="Esa prueba costó unos cincuenta mil dólares. A Volkswagen le acabaría costando más de treinta mil millones de euros.",
         visual=dict(type="img", key="money", cap="50.000 $ → MÁS DE 30.000 M€")),
    dict(id="s04", text="Esta es la historia de la mayor trampa de la industria del automóvil: cómo la empresa del vocho engañó a millones de conductores…",
         visual=dict(type="img", key="beetle", cap="VOLKSWAGEN")),
    dict(id="s05", text="y por qué, diez años después, Volkswagen está cerrando fábricas en Alemania por primera vez en su historia. Y de paso, te cuento por qué el último vocho del mundo se fabricó en México.",
         visual=dict(type="img", key="factory_empty", cap="ALEMANIA, 2026")),

    # --- CAPÍTULO 1 ---
    dict(id="s06", text="Capítulo uno. El coche del pueblo.",
         visual=dict(type="title", num="01", text="EL COCHE DEL PUEBLO", name="El coche del pueblo")),
    dict(id="s07", text="Volkswagen significa eso: el coche del pueblo. Su modelo más famoso, el escarabajo, se convirtió en uno de los coches más vendidos de la historia.",
         visual=dict(type="img", key="beetle", motion="out", cap="EL ESCARABAJO")),
    dict(id="s08", text="Se fabricaron más de veintiún millones y medio, casi un millón setecientos mil solo en México. Y el último de todos no salió de Alemania. Salió de México.",
         visual=dict(type="num", start=0, end=21529464, label="ESCARABAJOS FABRICADOS EN TOTAL")),
    dict(id="s09", text="El treinta de julio de dos mil tres, en la planta de Puebla, terminó el último vocho. No se vendió: lo mandaron directo a un museo en Wolfsburgo, la ciudad de Volkswagen. De aquella última edición solo se hicieron tres mil unidades, en azul y en beige.",
         visual=dict(type="year", year="30 JUL 2003", sub="EL ÚLTIMO VOCHO SALE DE PUEBLA")),
    dict(id="s10", text="En México el vocho fue taxi, coche familiar y leyenda. Pero en Alemania, Volkswagen ya tenía la mirada puesta en algo mucho más grande.",
         visual=dict(type="img", key="mexico_street", cap="EL VOCHO, UNA LEYENDA EN MÉXICO")),

    # --- CAPÍTULO 2 ---
    dict(id="s11", text="Capítulo dos. Ser el número uno.",
         visual=dict(type="title", num="02", text="SER EL NÚMERO UNO", name="Ser el número uno")),
    dict(id="s12", text="En dos mil siete llega a la presidencia Martin Winterkorn, un ingeniero obsesionado con un objetivo: superar a Toyota y convertir a Volkswagen en el mayor fabricante de coches del mundo. El plan tenía hasta fecha: lograrlo en dos mil dieciocho.",
         visual=dict(type="quote", text="OBJETIVO:\nSUPERAR\nA TOYOTA")),
    dict(id="s13", text="Para conquistar Estados Unidos, la apuesta fue el diésel. Volkswagen lo vendía como diésel limpio: coches que gastaban poco, corrían mucho y casi no contaminaban.",
         visual=dict(type="img", key="highway_night", cap="\"DIÉSEL LIMPIO\"")),
    dict(id="s14", text="Había un problema. Las normas de Estados Unidos sobre los óxidos de nitrógeno, unos gases muy dañinos para los pulmones, eran mucho más estrictas que las europeas.",
         visual=dict(type="img", key="exhaust", motion="out", cap="ÓXIDOS DE NITRÓGENO")),
    dict(id="s15", text="Cumplirlas de verdad era caro y complicado. Así que alguien dentro de Volkswagen encontró un atajo.",
         visual=dict(type="stamp", text="CUMPLIR LA LEY\nERA CARO", stamp="ATAJO")),
    dict(id="s16", text="Y durante años, funcionó. En el primer semestre de dos mil quince, Volkswagen vendió cinco millones cuarenta mil coches. Toyota, cinco millones veinte mil. Por fin era el número uno.",
         visual=dict(type="versus", title="VENTAS EN EL 1er SEMESTRE DE 2015", left=["5,04 M", "VOLKSWAGEN"], right=["5,02 M", "TOYOTA"], mid="VS", lcol="yellow", rcol="white")),
    dict(id="s17", text="Le duró muy poco. Porque aquella prueba en la carretera ya había llegado a la mesa de las autoridades.",
         visual=dict(type="img", key="boardroom", cap="JULIO DE 2015")),

    # --- CAPÍTULO 3 ---
    dict(id="s18", text="Capítulo tres. La trampa.",
         visual=dict(type="title", num="03", text="LA TRAMPA", name="La trampa")),
    dict(id="s19", text="El truco estaba en el software del motor. El programa era capaz de detectar cuándo el coche estaba en un laboratorio, haciendo la prueba oficial de emisiones. Se fijaba en detalles como la velocidad, el tiempo que llevaba encendido el motor o si el volante se movía.",
         visual=dict(type="img", key="lab", cap="LA PRUEBA OFICIAL")),
    dict(id="s20", text="En el laboratorio, el coche activaba todos sus sistemas de limpieza y aprobaba sin problemas. En la carretera, los apagaba, y contaminaba muchísimo más.",
         visual=dict(type="versus", left=["LABORATORIO", "APRUEBA\nSIN PROBLEMAS"], right=["CARRETERA", "HASTA 35 VECES\nEL LÍMITE"], mid="VS", lcol="white", rcol="red")),
    dict(id="s21", text="Por eso nadie lo había notado. Hasta que el equipo de la Universidad de Virginia Occidental decidió medir los coches en la calle, no en el laboratorio.",
         visual=dict(type="img", key="road_test", motion="out", cap="UNIVERSIDAD DE VIRGINIA OCCIDENTAL")),
    dict(id="s21b", text="El Jetta superaba el límite entre quince y treinta y cinco veces. El Passat, entre cinco y veinte. El BMW cumplía la norma.",
         visual=dict(type="bars", title="VECES POR ENCIMA DEL LÍMITE DE NOx (MÁXIMO MEDIDO)", data=[["JETTA", 35], ["PASSAT", 20], ["BMW X5", 1]], reveal=3)),
    dict(id="s21c", text="Y no era la primera vez que ese laboratorio pillaba una trampa. En mil novecientos noventa y ocho ya había ayudado a destapar algo parecido en motores de camiones.",
         visual=dict(type="year", year="1998", sub="EL MISMO LABORATORIO YA HABÍA PILLADO OTRA TRAMPA")),
    dict(id="s22", text="En septiembre de dos mil quince, la agencia medioambiental de Estados Unidos lo hace público. Y Volkswagen admite lo impensable: el programa trampa estaba en millones de coches de todo el mundo.",
         visual=dict(type="img", key="code", cap="SEPTIEMBRE DE 2015")),
    dict(id="s23", text="En total, unos diez millones setecientos mil vehículos.",
         visual=dict(type="num", start=0, end=10700000, label="COCHES CON EL PROGRAMA TRAMPA")),
    dict(id="s24", text="Y lo peor para la empresa todavía no había empezado.",
         visual=dict(type="stamp", text="SEPTIEMBRE DE 2015", stamp="DIESELGATE")),

    # --- CAPÍTULO 4 ---
    dict(id="s25", text="Capítulo cuatro. La factura.",
         visual=dict(type="title", num="04", text="LA FACTURA", name="La factura")),
    dict(id="s26", text="Las acciones de Volkswagen se desploman en la bolsa. Y a los pocos días, Martin Winterkorn dimite. Asegura que no sabía nada.",
         visual=dict(type="img", key="stock_crash", cap="WINTERKORN DIMITE")),
    dict(id="s26b", text="Y el trono le dura un suspiro. Ese año, Toyota recupera el primer puesto: diez millones ciento cincuenta mil coches vendidos, frente a nueve millones novecientos treinta mil de Volkswagen.",
         visual=dict(type="versus", title="VENTAS MUNDIALES EN 2015", left=["10,15 M", "TOYOTA"], right=["9,93 M", "VOLKSWAGEN"], mid="VS", lcol="white", rcol="red")),
    dict(id="s27", text="Llegan las multas, las demandas y las recompras de coches en medio mundo. Solo en Estados Unidos, en dos mil diecisiete, Volkswagen se declaró culpable y aceptó pagar cuatro mil trescientos millones de dólares en el acuerdo penal. La factura total supera los treinta mil millones de euros.",
         visual=dict(type="num", start=0, end=30000, prefix="+", suffix=" M€", label="LO QUE LE HA COSTADO EL ESCÁNDALO A VOLKSWAGEN")),
    dict(id="s28", text="Y también hay cárcel. En diciembre de dos mil diecisiete, un juez de Estados Unidos condena a Oliver Schmidt, un directivo de Volkswagen, a siete años de prisión. Se había declarado culpable.",
         visual=dict(type="img", key="prison", cap="OLIVER SCHMIDT: 7 AÑOS")),
    dict(id="s29", text="En Alemania el proceso fue mucho más lento. En mayo de dos mil veinticinco, casi diez años después, un tribunal de Braunschweig condena a cuatro exdirectivos e ingenieros. El jefe de desarrollo de motores diésel recibe cuatro años y medio de cárcel.",
         visual=dict(type="img", key="court", cap="BRAUNSCHWEIG, MAYO DE 2025")),
    dict(id="s29b", text="Aquel juicio había empezado en septiembre de dos mil veintiuno y necesitó ciento setenta y cinco sesiones. Y todavía quedan treinta y un acusados más pendientes de juicio.",
         visual=dict(type="num", start=0, end=175, suffix=" SESIONES", label="EL JUICIO DE BRAUNSCHWEIG (2021–2025)")),
    dict(id="s30", text="¿Y Winterkorn? La fiscalía sostiene que, como muy tarde en mayo de dos mil catorce, ya sabía lo del programa. Su juicio empezó en dos mil veinticuatro, pero se suspendió por su salud. Él sigue negando las acusaciones.",
         visual=dict(type="quote", text="WINTERKORN:\nJUICIO\nSUSPENDIDO")),
    dict(id="s31", text="El escándalo dejó a Volkswagen herida. Pero el golpe que de verdad la puso contra las cuerdas llegó desde el otro lado del mundo.",
         visual=dict(type="img", key="factory_empty", motion="out", cap="EL SIGUIENTE GOLPE")),

    # --- CAPÍTULO 5 ---
    dict(id="s32", text="Capítulo cinco. El golpe de China.",
         visual=dict(type="title", num="05", text="EL GOLPE DE CHINA", name="El golpe de China")),
    dict(id="s33", text="China era el gran mercado de Volkswagen. Llevaba años siendo la marca que más coches vendía allí.",
         visual=dict(type="img", key="china_ev", cap="CHINA")),
    dict(id="s34", text="Pero en dos mil veintitrés, por primera vez, una marca china le quita el trono: BYD, la empresa que empezó haciendo baterías para móviles. Sí, la misma de la que te hablé en otro vídeo.",
         visual=dict(type="stamp", text="CHINA, 2023\nBYD SUPERA A VOLKSWAGEN", stamp="Nº1 PERDIDO")),
    dict(id="s34b", text="En el primer trimestre de aquel año, BYD vendió en China más de cuatrocientos cuarenta mil coches. Volkswagen, cuatrocientos veintisiete mil. Desde al menos dos mil ocho, nadie le había quitado el primer puesto.",
         visual=dict(type="bars", title="COCHES VENDIDOS EN CHINA · 1er TRIMESTRE 2023 (MILES)", data=[["BYD", 440], ["VOLKSWAGEN", 427]], reveal=2)),
    dict(id="s35", text="Volkswagen llegó tarde a los coches eléctricos, y los chinos los fabrican más baratos. Las ventas caen, y en Alemania sobran fábricas.",
         visual=dict(type="img", key="assembly", cap="SOBRAN FÁBRICAS")),
    dict(id="s36", text="En diciembre de dos mil veinticuatro, Volkswagen pacta con los sindicatos recortar treinta y cinco mil empleos en Alemania hasta dos mil treinta. La planta de Dresde deja de fabricar coches, y la de Osnabrück se pone a la venta.",
         visual=dict(type="num", start=0, end=35000, suffix=" EMPLEOS", label="RECORTE PACTADO EN ALEMANIA HASTA 2030")),
    dict(id="s37", text="Y en septiembre de dos mil veintiséis, el consejo aprueba ir todavía más lejos: cincuenta mil empleos más y el fin de la producción en cuatro plantas.",
         visual=dict(type="img", key="workers", cap="50.000 EMPLEOS MÁS · 4 PLANTAS")),
    dict(id="s38", text="Es la primera vez en su historia que Volkswagen deja de fabricar coches en fábricas alemanas. Para una empresa que nació como símbolo de la industria de su país, es un golpe enorme.",
         visual=dict(type="stamp", text="ALEMANIA, 2026", stamp="HISTÓRICO")),

    # --- CAPÍTULO 6 / CIERRE ---
    dict(id="s39", text="Capítulo seis. ¿Qué queda del coche del pueblo?",
         visual=dict(type="title", num="06", text="¿QUÉ QUEDA DEL COCHE DEL PUEBLO?", name="¿Qué queda del coche del pueblo?")),
    dict(id="s40", text="Volkswagen sigue siendo uno de los fabricantes más grandes del mundo. Pero en diez años pasó de presumir de ser el número uno a pagar la mayor multa de la historia del automóvil y a cerrar fábricas en casa.",
         visual=dict(type="versus", left=["2015", "Nº1 DEL\nMUNDO"], right=["2026", "CIERRA FÁBRICAS\nEN ALEMANIA"], lcol="yellow", rcol="red")),
    dict(id="s41", text="Todo empezó con un atajo para ahorrar dinero. Y con un pequeño equipo que, en lugar de fiarse del laboratorio, decidió salir a la carretera a comprobarlo. Y queda una pregunta incómoda: si un equipo tan pequeño pudo descubrirlo, ¿cómo es posible que nadie dentro de la empresa lo frenara antes?",
         visual=dict(type="img", key="road_test", cap="LA PRUEBA DE 50.000 $")),
    dict(id="s42", text="¿Tú volverías a comprar un Volkswagen? ¿O ya te pasaste a una marca china? Te leo en los comentarios. Y suscríbete: la próxima historia ya está en camino.",
         visual=dict(type="quote", text="¿VOLVERÍAS A\nCOMPRAR UN\nVOLKSWAGEN?")),
]

# Shorts de 20–25 s (los que mejor retienen), cada uno con un gancho distinto
SHORTS = {
    "a": {"bar": "LA PRUEBA DE 50.000 $", "scenes": [
        dict(id="a01", text="Una prueba de cincuenta mil dólares le costó a Volkswagen más de treinta mil millones de euros.", key="road_test"),
        dict(id="a02", text="Unos investigadores midieron sus coches en la carretera, no en el laboratorio. Contaminaban hasta treinta y cinco veces más de lo permitido.", key="exhaust"),
        dict(id="a03", text="Así cayó la mayor trampa del automóvil. La historia completa, en mi canal.", key="code"),
    ]},
    "b": {"bar": "EL ÚLTIMO VOCHO", "scenes": [
        dict(id="b01", text="El último vocho del mundo no se fabricó en Alemania. Se fabricó en México.", key="beetle"),
        dict(id="b02", text="Salió de Puebla el treinta de julio de dos mil tres, y nunca se vendió: está en un museo en Alemania. De esa última edición solo se hicieron tres mil.", key="mexico_street"),
        dict(id="b03", text="Hoy Volkswagen cierra fábricas en Alemania. Por qué, en mi canal.", key="factory_empty"),
    ]},
    "c": {"bar": "EL COCHE QUE SABÍA", "scenes": [
        dict(id="c01", text="Estos coches sabían cuándo los estaban examinando.", key="lab"),
        dict(id="c02", text="En el laboratorio aprobaban. En la carretera apagaban los filtros y contaminaban muchísimo más. Eran más de diez millones, y los descubrió una prueba de cincuenta mil dólares.", key="highway_night"),
        dict(id="c03", text="Fue el escándalo diésel de Volkswagen. La historia completa, en mi canal.", key="stock_crash"),
    ]},
}

THUMBS = [  # se completan cuando estén los fotogramas de los clips (img/<clave>.png)
    dict(img="exhaust", zoom=1.1, cx=0.5, shade=["left", 230, 0.6], items=[
        ["text", 45, 70, "LA PRUEBA", 150, "white", "la"], ["text", 45, 250, "QUE HUNDIÓ", 130, "yellow", "la"], ["text", 45, 430, "A VOLKSWAGEN", 115, "red", "la"]]),
    dict(img="factory_empty", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 80, "CIERRA", 190, "white", "la"], ["text", 45, 320, "FÁBRICAS", 170, "red", "la"], ["badge", 45, 540, 520, 660, "POR 1ª VEZ", 95]]),
    dict(img="money", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 70, "50.000 $", 170, "white", "la"], ["text", 45, 280, "→ 30.000 M€", 150, "red", "la"]]),
    dict(img="beetle", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 80, "LA GRAN", 160, "white", "la"], ["text", 45, 280, "MENTIRA", 190, "red", "la"], ["text", 45, 500, "DEL DIÉSEL", 110, "yellow", "la"]]),
    dict(img="lab", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 80, "EL COCHE", 160, "white", "la"], ["text", 45, 280, "QUE SABÍA", 160, "yellow", "la"], ["text", 45, 470, "QUE LO VIGILABAN", 90, "red", "la"]]),
    dict(img="stock_crash", zoom=1.05, cx=0.5, items=[
        ["text", 640, 40, "¿CÓMO ENGAÑÓ", 140, "white", "mt"], ["text", 640, 230, "AL MUNDO?", 170, "red", "mt"]]),
]
THUMBS_TOP = [1, 2, 5]

META = {
    "code": "005",
    "name": "Volkswagen",
    "intro_chapter": "Intro: la prueba de 50.000 dólares",
    "titles": [
        "Una prueba de 50.000 $ hundió a Volkswagen… y aún paga las consecuencias",
        "El coche que sabía cuándo lo estaban vigilando: la caída de Volkswagen",
        "Volkswagen: la mayor trampa del automóvil y por qué hoy cierra fábricas",
    ],
    "description": "En 2013, un pequeño equipo de una universidad de EE. UU. midió dos Volkswagen diésel en la carretera y descubrió que contaminaban hasta 35 veces más de lo permitido. Esa prueba de unos 50.000 dólares destapó el escándalo diésel: un programa que detectaba el laboratorio, más de 10 millones de coches afectados y una factura de más de 30.000 millones de euros. Diez años después, con China comiéndole terreno, Volkswagen cierra fábricas en Alemania por primera vez en su historia.",
    "sources": [
        "CarAdvice / Bloomberg / WVU / IEEE Spectrum: el estudio de la Universidad de Virginia Occidental para el ICCT",
        "City A.M. / Ratchet+Wrench: Volkswagen supera a Toyota en el primer semestre de 2015",
        "Asiae / ARA / TechXplore: 10,7 millones de vehículos y coste del escándalo",
        "IndustryWeek / Fortune / The Local: condena de Oliver Schmidt (diciembre de 2017)",
        "OCCRP / Fortune / Carscoops: condenas del tribunal de Braunschweig (mayo de 2025)",
        "TimesLive / BusinessDay: juicio de Martin Winterkorn (2024)",
        "Bloomberg / CarNewsChina: BYD supera a Volkswagen en China (2023)",
        "electrive / AP (US News) / OSW: recortes de empleo y plantas en Alemania (2024–2026)",
        "El Universal / Xataka / CarAdvice: el último vocho, Puebla, 30 de julio de 2003",
        "Vídeos de archivo: Pexels (vía vidIQ) — ArtHouse Studio, Christopher Rodriguez, Eleonora Vokueva, Engin Altundağ, Gustavo Fring, Israyosoy S., K, MART PRODUCTION, Pixabay, Rafael Minguet Delgado, Teela Hudak, Teo Doulke, cottonbro studio, pickarick",
    ],
    "disclosure": "La narración de este vídeo está hecha con voz sintética. Las imágenes son vídeos de archivo de Pexels que ilustran la historia; no muestran a las personas ni los hechos reales.",
    "hashtags": "#Volkswagen #Dieselgate #Vocho #Negocios #Coches",
    "tags": ["volkswagen", "dieselgate", "escándalo volkswagen", "vocho", "volkswagen méxico", "volkswagen crisis",
             "volkswagen cierra fábricas", "byd", "historia de empresas", "coches", "diésel", "el último balance"],
    "pinned": "¿Volverías a comprar un Volkswagen o ya te pasaste a una marca china? 👇 Y dime qué empresa quieres para el próximo vídeo.",
    "playlist": "Auges y caídas",
    "shorts": {
        "a": {"title": "Una prueba de 50.000 $ le costó 30.000 millones a Volkswagen",
              "description": "El escándalo diésel. Historia completa en el canal. #Volkswagen #Dieselgate #shorts",
              "tags": ["volkswagen", "dieselgate", "coches", "shorts"]},
        "b": {"title": "El último vocho del mundo se hizo en México",
              "description": "Puebla, 2003. Historia completa de Volkswagen en el canal. #Vocho #Volkswagen #shorts",
              "tags": ["vocho", "volkswagen", "méxico", "puebla", "shorts"]},
        "c": {"title": "Estos coches sabían cuándo los estaban examinando",
              "description": "La trampa de Volkswagen. Historia completa en el canal. #Volkswagen #shorts",
              "tags": ["volkswagen", "dieselgate", "trampa", "shorts"]},
    },
}
