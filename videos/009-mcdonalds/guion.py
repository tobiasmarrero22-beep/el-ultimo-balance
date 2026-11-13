# Vídeo 009 — McDonald's: la foto de un menú, los clientes que se van… y el giro argentino (~9 min, sin Shorts)
# Tema con datos (API de YouTube, 13-nov-2026): EN "Why Nobody's Eating McDonald's Anymore" (Michael Girdley, jul-2026) 1,44 M,
# Michael Bordenaro 221k, "McDonald's Has (Finally) Cooked Itself" (Damon Cassidy, 12-nov-2026) 164k; ES: solo 95k (7 min,
# feb-2025) y 37k → hueco en español. Elegido por el usuario entre 5 marcas conocidas en Argentina.
# Hechos verificados (WebSearch, 13-nov-2026):
# - Jul-2023: foto viral del combo Big Mac a 17,59 $ en el área de servicio de Darien (Connecticut, I-95).
# - 29-may-2024: carta abierta de Joe Erlinger (presidente de McDonald's EE. UU.): Big Mac medio 4,39 $ (2019) → 5,29 $ (2024),
#   +21 %; menú medio +40 % desde 2019 (ingredientes, sueldos, papel); el combo de 18 $ era 1 local de más de 13.700; más del
#   95 % de los locales de EE. UU. son de franquiciados, que fijan sus precios (McDonald's corporativo / Restaurant Dive / Axios).
# - E. coli O157:H7 (CDC, informe final 3-dic-2024): 104 casos en 14 estados, 34 hospitalizados, 1 muerto (persona mayor de
#   Colorado); fuente probable: cebolla en tiras de Taylor Farms (California) en el Cuarto de Libra.
# - T1-2025: ventas comparables en EE. UU. -3,6 % (peor desde T2-2020); visitas de rentas bajas cerca de -10 % y clase media casi
#   igual; Kempczinski: "la economía de EE. UU. está dividida" (Benzinga / Restaurant Dive / eMarketer). T3-2025: visitas de rentas
#   bajas -"casi dos dígitos", las de rentas altas siguen creciendo; presión de súper, ropa, alquiler y guarderías (NACS).
# - Valor: combo de 5 $ (jun-2024) → McValue (ene-2025) → vuelven los Extra Value Meals (8-sep-2025; eliminados en 2019; 15 % de
#   descuento; combo Big Mac a 8 $) (McDonald's corporativo / Restaurant Dive).
# - 2026: T2 ventas EE. UU. +0,8 % con menos visitas; T3 (4-nov-2026) -0,2 %; visitas -4,6 % según Placer.ai (Reuters); tráfico de
#   la comida rápida -2,6 % (Revenue Management Solutions); Kempczinski: demasiadas campañas y un cambio desacertado en la oferta
#   barata; prueba de combos baratos en 1.900 locales, lanzamiento nacional previsto a principios de 2027; ventas mundiales +1,5 %
#   (NRN / Business Chief / 24/7 Wall St. / McDonald's).
# - Argentina: primer McDonald's el 24-nov-1986, Av. Cabildo 2254 (Belgrano). Woods Staton (nacido en Medellín) fue socio de
#   McDonald's en Argentina más de 20 años y presidente de la división Sur de América Latina (2004-2007); el 3-ago-2007 un grupo de
#   inversores reunido por él compra el negocio latinoamericano → Arcos Dorados, el mayor franquiciado de McDonald's del mundo:
#   2.428 restaurantes en 20 países y territorios a 31-dic-2024 (20-F en la SEC / WEF / El Cronista).
# - Índice Big Mac (The Economist, ene-2026, según iProUP / Noticias NQN / iProfesional): Argentina 7,37 $, segundo más caro del
#   mundo tras Suiza (7,99 $) y más caro que en EE. UU.
VOICE = "i4Kar2uamCWyas8TAu31"  # ElevenLabs "Adán - Narration"
SPEED = 1.0
IMAGE_MODEL = "nano-banana-2-lite"

N = ", photorealistic, cinematic lighting, 16:9, no text, no logos, no brand names"
IMAGES = {
    "highway_stop": "Highway service plaza at dusk with a fast-food restaurant glowing red and yellow, cars parked, travelers walking, American interstate" + N,
    "menu_board": "Close-up of a glowing digital fast-food menu board above a counter, prices and words completely blurred and unreadable, warm red and yellow light" + N,
    "drive_night": "Fast-food drive-thru lane at night, red and yellow glow reflecting on wet asphalt, a single car at the order window, moody" + N,
    "receipt_hand": "Close-up of a hand holding a long paper receipt in a fast-food restaurant, receipt text unreadable, restaurant blurred behind" + N,
    "phone_scroll": "Person scrolling social media on a smartphone in a dark room, screen glow on the face, screen content blurred and unreadable" + N,
    "onions": "Slivered raw onions piled on a stainless steel table in an industrial food processing plant, workers in hairnets blurred behind" + N,
    "empty_restaurant": "Empty fast-food restaurant interior with red and yellow chairs and tables, no customers, afternoon light, quiet atmosphere" + N,
    "family_bills": "Worried parents at a kitchen table at night going through bills and a calculator, children's drawings on the fridge, warm lamp light" + N,
    "grocery_cart": "Half-empty supermarket shopping cart in a grocery aisle, shopper seen from behind checking prices, fluorescent light" + N,
    "value_meal": "Fast-food combo meal on a red tray: a cheeseburger, a small paper box of french fries and a soda cup, bright and appetizing, unbranded packaging" + N,
    "kitchen_crew": "Busy fast-food kitchen with crew members in caps preparing burgers at a grill, seen from behind, steam and warm light" + N,
    "boardroom": "Corporate boardroom with executives seen from behind looking at a large screen with a falling red chart, no readable text, night city view" + N,
    "burger_closeup": "Macro close-up of a classic double-patty burger with sesame bun, lettuce and sauce on a dark background, dramatic studio light" + N,
    "ba_80s": "1980s film photograph of a busy avenue in Buenos Aires, Argentina, with old cars, buses and pedestrians, faded colors, film grain, no readable signs" + N,
    "office_80s": "Silhouette of a businessman seen from behind standing at the window of a 1980s office overlooking a South American city, warm afternoon light" + N,
    "ba_night": "Buenos Aires street at night with traditional buildings and a glowing fast-food restaurant on a corner, people walking, no readable signs" + N,
}

def I(key, cap=None, pop=None, **kw):
    d = dict(type="img", key=key)
    if cap: d["cap"] = cap
    if pop: d["pop"] = pop
    d.update(kw); return d

LATAM = dict(type="route", title="ARCOS DORADOS: 2.428 RESTAURANTES EN 20 PAÍSES (2024)",
             points={"Ciudad de México": [0.22, 0.22], "San Juan": [0.66, 0.26], "Bogotá": [0.42, 0.44], "São Paulo": [0.64, 0.68],
                     "Santiago": [0.36, 0.80], "Buenos Aires": [0.52, 0.86]},
             routes=[["Buenos Aires", "São Paulo"], ["Buenos Aires", "Santiago"], ["Buenos Aires", "Bogotá"], ["Buenos Aires", "Ciudad de México"],
                     ["Buenos Aires", "San Juan"]])

SCENES = [
    # --- GANCHO ---
    dict(id="s01", text="Diecisiete dólares con cincuenta y nueve. Eso costaba un combo Big Mac en un McDonald's de una autopista de Connecticut, en Estados Unidos.",
         visual=I("highway_stop", cap="CONNECTICUT · JULIO DE 2023", pop=["17,59 $"])),
    dict(id="s02", text="En julio de dos mil veintitrés, un viajero le sacó una foto al menú y la subió a las redes. En pocos días, esa imagen dio la vuelta al mundo.",
         visual=dict(type="num", start=0, end=17.59, dec=2, suffix=" $", label="UN COMBO BIG MAC EN UN ÁREA DE SERVICIO DE CONNECTICUT")),
    dict(id="s03", text="Era un caso aislado. Pero tocó un nervio: millones de personas sentían que McDonald's ya no era barato.",
         visual=I("menu_board", pop=["YA NO ES BARATO"])),
    dict(id="s04", text="Tres años después, McDonald's está perdiendo clientes en su propio país. Entre julio y septiembre de dos mil veintiséis, las visitas a sus restaurantes de Estados Unidos cayeron un cuatro coma seis por ciento.",
         visual=dict(type="num", start=0, end=-4.6, dec=1, suffix=" %", label="VISITAS A McDONALD'S EN EE. UU. · JULIO A SEPTIEMBRE DE 2026")),
    dict(id="s05", text="Y el giro más curioso de esta historia llega desde Argentina: el país donde el Big Mac llegó a ser el segundo más caro del planeta… y donde empezó el mayor franquiciado de McDonald's del mundo.",
         visual=I("ba_night", pop=["ARGENTINA"])),
    dict(id="s06", text="Esta es la historia de cómo el rey de la comida barata se olvidó de ser barato. Y de lo que está haciendo para recuperar a los que se fueron.",
         visual=I("drive_night")),

    # --- 01 ---
    dict(id="s07", text="Capítulo uno: la foto de los dieciocho dólares.",
         visual=dict(type="title", num="01", text="LA FOTO DE LOS 18 DÓLARES", name="La foto de los 18 dólares")),
    dict(id="s08", text="Volvamos a esa foto. El local estaba en un área de servicio de la autopista, en Darien. Y en esos sitios los precios suelen ser más altos: el viajero tiene hambre y pocas opciones.",
         visual=I("highway_stop", pop=["ÁREA DE SERVICIO"], motion="out")),
    dict(id="s09", text="Además, hay un detalle que mucha gente no sabe: McDonald's casi no es dueño de sus restaurantes en Estados Unidos. Más del noventa y cinco por ciento son de franquiciados.",
         visual=dict(type="num", start=0, end=95, suffix=" %", label="LOCALES DE McDONALD'S EN EE. UU. EN MANOS DE FRANQUICIADOS")),
    dict(id="s10", text="Cada franquiciado pone sus propios precios. La empresa gana, sobre todo, con el alquiler de los locales y un porcentaje de lo que vende cada uno.",
         visual=dict(type="versus", title="CÓMO FUNCIONA McDONALD'S EN EE. UU.", left=["FRANQUICIADO", "PONE LOS PRECIOS"], right=["McDONALD'S", "COBRA ALQUILER\nY UN %"], mid="+", lcol="yellow", rcol="red")),
    dict(id="s11", text="Pero la foto ya había hecho su trabajo. Durante meses circularon en redes comparaciones que aseguraban que McDonald's había duplicado sus precios.",
         visual=I("phone_scroll", pop=["¿EL DOBLE?"])),
    dict(id="s12", text="Hasta que en mayo de dos mil veinticuatro, el presidente de McDonald's en Estados Unidos, Joe Erlinger, publicó una carta abierta para defenderse.",
         visual=dict(type="headline", kicker="29 de mayo de 2024", text="El presidente de McDonald's en EE. UU. responde: las subidas de precio que circulan son exageradas", mark="exageradas", source="Fuente: McDonald's (carta abierta de Joe Erlinger)")),
    dict(id="s13", text="Según la empresa, el Big Mac costaba de media cuatro dólares con treinta y nueve en dos mil diecinueve. En dos mil veinticuatro, cinco con veintinueve. Un veintiuno por ciento más.",
         visual=dict(type="bars", title="PRECIO MEDIO DEL BIG MAC EN EE. UU. (USD)", data=[["2019", 4.39], ["2024", 5.29]], dec=2, note="+21 %")),
    dict(id="s14", text="Y el menú en conjunto, un cuarenta por ciento más caro que en dos mil diecinueve. Lo atribuía a lo que habían subido los ingredientes, los sueldos y hasta el papel.",
         visual=dict(type="num", start=0, end=40, prefix="+", suffix=" %", label="SUBIDA MEDIA DEL MENÚ DESDE 2019, SEGÚN McDONALD'S")),
    dict(id="s15", text="Y aquel combo de dieciocho dólares, decía, era un solo local entre más de trece mil setecientos.",
         visual=dict(type="quote", text="1 LOCAL\nDE MÁS DE 13.700")),
    dict(id="s16", text="Los números tenían su lógica. Pero no cambiaban lo que sentía la gente. Cuando tu marca es sinónimo de barato, no basta con ser solo un poco más caro que antes.",
         visual=I("receipt_hand", pop=["LO QUE SIENTE LA GENTE"])),
    dict(id="s16b", text="Y lo peor de ese año todavía no había llegado. Porque unos meses después, el problema ya no fue el precio. Fue la comida.",
         visual=I("burger_closeup", shake=True)),

    # --- 02 ---
    dict(id="s17", text="Capítulo dos: el susto de las cebollas.",
         visual=dict(type="title", num="02", text="EL SUSTO DE LAS CEBOLLAS", name="El susto de las cebollas")),
    dict(id="s18", text="Octubre de dos mil veinticuatro. Las autoridades sanitarias de Estados Unidos anuncian un brote de la bacteria E. coli relacionado con una de las hamburguesas más vendidas de McDonald's: el Cuarto de Libra.",
         visual=dict(type="headline", kicker="Octubre de 2024", text="Brote de E. coli vinculado al Cuarto de Libra de McDonald's en varios estados", mark="E. coli", source="Fuente: CDC (Centros para el Control de Enfermedades)")),
    dict(id="s19", text="Ciento cuatro personas enfermaron en catorce estados.",
         visual=dict(type="num", start=0, end=104, suffix=" PERSONAS", label="ENFERMAS EN 14 ESTADOS (CDC)")),
    dict(id="s20", text="Treinta y cuatro tuvieron que ser hospitalizadas. Y una persona mayor de Colorado murió.",
         visual=dict(type="quote", text="34 HOSPITALIZADOS\n1 MUERTO")),
    dict(id="s21", text="Según los investigadores, el origen más probable fueron unas cebollas cortadas en tiras finas de un proveedor de California. McDonald's las retiró de sus restaurantes.",
         visual=I("onions", pop=["CEBOLLA EN TIRAS"])),
    dict(id="s22", text="En diciembre, el brote se dio por terminado. Pero durante semanas, muchos clientes se lo pensaron dos veces antes de pedir una hamburguesa.",
         visual=I("empty_restaurant")),
    dict(id="s22b", text="Precios que asustaban, un brote que asustaba todavía más… y en dos mil veinticinco llegó la factura.",
         visual=I("empty_restaurant", pop=["LA FACTURA"], pop_col="red", motion="out")),

    # --- 03 ---
    dict(id="s23", text="Capítulo tres: los clientes que se van.",
         visual=dict(type="title", num="03", text="LOS CLIENTES QUE SE VAN", name="Los clientes que se van")),
    dict(id="s24", text="En el primer trimestre de dos mil veinticinco, las ventas comparables de McDonald's en Estados Unidos cayeron un tres coma seis por ciento. Su peor caída desde dos mil veinte, en plena pandemia.",
         visual=dict(type="num", start=0, end=-3.6, dec=1, suffix=" %", label="VENTAS COMPARABLES EN EE. UU. · 1.ER TRIMESTRE DE 2025")),
    dict(id="s25", text="Y la empresa explicó quién se estaba yendo. Las visitas de los clientes con menos ingresos se acercaban a una caída del diez por ciento. Las de la clase media bajaban casi lo mismo.",
         visual=dict(type="versus", title="VISITAS A McDONALD'S EN EE. UU. (1.ER TRIMESTRE DE 2025)", left=["MENOS INGRESOS", "CERCA DE -10 %"], right=["CLASE MEDIA", "CASI IGUAL"], mid="·", lcol="red", rcol="red")),
    dict(id="s26", text="Justo el público que había hecho grande a McDonald's: familias que quieren comer fuera sin gastar mucho.",
         visual=I("family_bills")),
    dict(id="s27", text="Su director ejecutivo, Chris Kempczinski, lo resumió así: la economía de Estados Unidos está dividida. A los que más tienen les va bien. Los demás recortan.",
         visual=dict(type="quote", text="\"LA ECONOMÍA\nESTÁ DIVIDIDA\"\n— CHRIS KEMPCZINSKI")),
    dict(id="s28", text="Y en otoño, nada había cambiado. Las visitas de los clientes con menos ingresos caían casi un diez por ciento, mientras las de los que más ganan seguían subiendo.",
         visual=dict(type="versus", title="VISITAS A McDONALD'S EN EE. UU. (3.ER TRIMESTRE DE 2025)", left=["MENOS INGRESOS", "CASI -10 %"], right=["MÁS INGRESOS", "SUBEN"], mid="VS", lcol="red", rcol="yellow")),
    dict(id="s29", text="Comer fuera compite con el supermercado, el alquiler, la ropa o la guardería de los chicos. Y una hamburguesa es de lo primero que se recorta.",
         visual=I("grocery_cart", pop=["SÚPER", "ALQUILER", "GUARDERÍA"])),
    dict(id="s29b", text="McDonald's tenía claro el diagnóstico: había dejado de parecer barato. Así que decidió pelear con la única arma que de verdad entiende su cliente. El precio.",
         visual=I("menu_board", motion="out")),

    # --- 04 ---
    dict(id="s30", text="Capítulo cuatro: la guerra del menú barato.",
         visual=dict(type="title", num="04", text="LA GUERRA DEL MENÚ BARATO", name="La guerra del menú barato")),
    dict(id="s31", text="En junio de dos mil veinticuatro lanzó un combo de cinco dólares: una hamburguesa sencilla o un sándwich de pollo, papas pequeñas y un refresco.",
         visual=dict(type="stamp", text="JUNIO DE 2024\nUN COMBO POR 5 DÓLARES", stamp="OFERTA", col="yellow")),
    dict(id="s32", text="En enero de dos mil veinticinco lo amplió con una plataforma llamada McValue. Y en septiembre recuperó algo que había eliminado en dos mil diecinueve: los menús Extra Value.",
         visual=dict(type="timeline", title="LA VUELTA A LO BARATO", points=[["JUN 2024", "Combo de 5 $"], ["ENE 2025", "McValue"], ["SEP 2025", "Extra Value"]], hl=2)),
    dict(id="s33", text="Ocho combos con un quince por ciento de descuento frente a comprar cada cosa por separado. El combo Big Mac, por ejemplo, salía a ocho dólares en su lanzamiento.",
         visual=I("value_meal", pop=["-15 %", "BIG MAC: 8 $"])),
    dict(id="s34", text="Menos de la mitad que aquella foto de Connecticut.",
         visual=dict(type="versus", title="EL COMBO BIG MAC", left=["CONNECTICUT 2023", "17,59 $"], right=["EXTRA VALUE 2025", "8 $"], mid="VS", lcol="red", rcol="yellow")),
    dict(id="s35", text="Sus rivales respondieron con sus propios menús baratos, y en Estados Unidos se empezó a hablar de una guerra de precios en la comida rápida.",
         visual=I("kitchen_crew", pop=["GUERRA DE PRECIOS"])),
    dict(id="s35b", text="Por un momento, pareció que la estrategia funcionaba. Pero McDonald's estaba a punto de descubrir que bajar precios no alcanza si el cliente no se entera… o no se lo cree.",
         visual=I("drive_night", motion="out")),

    # --- 05 ---
    dict(id="s36", text="Capítulo cinco: el tropiezo de dos mil veintiséis.",
         visual=dict(type="title", num="05", text="EL TROPIEZO DE 2026", name="El tropiezo de 2026")),
    dict(id="s37", text="En el segundo trimestre de dos mil veintiséis, las ventas en Estados Unidos subieron un cero coma ocho por ciento. Pero solo porque cada cliente gastaba más. Las visitas seguían bajando.",
         visual=dict(type="versus", title="McDONALD'S EE. UU. · 2.º TRIMESTRE DE 2026", left=["VENTAS", "+0,8 %"], right=["VISITAS", "BAJAN"], mid="·", lcol="yellow", rcol="red")),
    dict(id="s38", text="Y el cuatro de noviembre llegó el informe del tercer trimestre: las ventas comparables en Estados Unidos, un cero coma dos por ciento abajo. Y unas visitas que, según Placer.ai, caían un cuatro coma seis por ciento.",
         visual=dict(type="headline", kicker="4 de noviembre de 2026", text="Las ventas de McDonald's en EE. UU. bajan por la caída de clientes", mark="caída de clientes", source="Fuente: Nation's Restaurant News / Reuters")),
    dict(id="s39", text="No era solo McDonald's. Según la consultora Revenue Management Solutions, las visitas a la comida rápida en todo el país cayeron un dos coma seis por ciento. Pero nadie tiene tanto que perder como el líder.",
         visual=dict(type="num", start=0, end=-2.6, dec=1, suffix=" %", label="VISITAS A LA COMIDA RÁPIDA EN EE. UU. · 3.ER TRIMESTRE DE 2026 (RMS)")),
    dict(id="s40", text="Lo sorprendente fue la explicación de Kempczinski. Esta vez no culpó solo a la economía. Reconoció errores propios: demasiadas campañas de marketing a la vez… y un cambio poco acertado en su oferta barata.",
         visual=dict(type="quote", text="ERRORES PROPIOS:\nDEMASIADAS CAMPAÑAS\nUNA OFERTA BARATA\nMAL PLANTEADA")),
    dict(id="s41", text="Ahora prueba nuevos combos económicos en unos mil novecientos restaurantes, con la idea de llevarlos a todo el país a principios de dos mil veintisiete.",
         visual=dict(type="num", start=0, end=1900, suffix=" LOCALES", label="PRUEBAN NUEVOS COMBOS BARATOS · LANZAMIENTO PREVISTO EN 2027")),
    dict(id="s42", text="El mayor vendedor de hamburguesas del mundo intenta recuperar a sus clientes con la misma arma que lo hizo famoso: ser barato. Pero para entender la otra cara de McDonald's hay que irse muy lejos de Estados Unidos.",
         visual=I("boardroom")),

    # --- 06 ---
    dict(id="s43", text="Capítulo seis: el giro argentino.",
         visual=dict(type="title", num="06", text="EL GIRO ARGENTINO", name="El giro argentino")),
    dict(id="s44", text="Buenos Aires, veinticuatro de noviembre de mil novecientos ochenta y seis. En la avenida Cabildo, en el barrio de Belgrano, abre el primer McDonald's de Argentina.",
         visual=I("ba_80s", cap="BUENOS AIRES · 1986")),
    dict(id="s45", text="Detrás está un empresario nacido en Medellín, Colombia: Woods Staton, el socio de McDonald's en el país.",
         visual=dict(type="stamp", text="24 DE NOVIEMBRE DE 1986\nAV. CABILDO 2254 · BELGRANO", stamp="PRIMER McDONALD'S DE ARGENTINA", col="yellow")),
    dict(id="s46", text="Durante dos décadas hace crecer la marca en Argentina y, más tarde, dirige todo el sur de América Latina para McDonald's.",
         visual=I("office_80s")),
    dict(id="s47", text="Y en dos mil siete da el gran golpe: con un grupo de inversores, le compra a McDonald's todo su negocio en América Latina.",
         visual=dict(type="year", year="2007", sub="STATON COMPRA EL NEGOCIO DE McDONALD'S EN AMÉRICA LATINA")),
    dict(id="s48", text="Así nace Arcos Dorados, el mayor franquiciado de McDonald's del mundo. Según su último informe anual, dos mil cuatrocientos veintiocho restaurantes en veinte países y territorios de América Latina y el Caribe.",
         visual=LATAM),
    dict(id="s49", text="Mientras el McDonald's de Estados Unidos pelea por no perder clientes, el mayor operador de la marca en el planeta tiene su origen en aquella aventura argentina.",
         visual=I("ba_80s", motion="out")),
    dict(id="s50", text="Y Argentina tiene otra conexión con esta historia: el precio. En enero de dos mil veintiséis, según el índice Big Mac de la revista The Economist, un Big Mac en Argentina costaba siete dólares con treinta y siete.",
         visual=dict(type="num", start=0, end=7.37, dec=2, suffix=" $", label="BIG MAC EN ARGENTINA, EN DÓLARES · ÍNDICE BIG MAC (ENE-2026)")),
    dict(id="s51", text="Solo Suiza lo tenía más caro, con siete dólares con noventa y nueve. Y era más caro que en el propio Estados Unidos.",
         visual=dict(type="bars", title="LOS BIG MAC MÁS CAROS DEL MUNDO (USD, ENE-2026)", data=[["SUIZA", 7.99], ["ARGENTINA", 7.37]], dec=2, note="2.º DEL MUNDO")),
    dict(id="s52", text="El índice no mide si la comida es buena o mala: compara precios para saber si una moneda está cara o barata. Pero dice mucho de lo que se siente al pagar.",
         visual=dict(type="quote", text="ÍNDICE BIG MAC:\n¿ESTÁ CARA O BARATA\nUNA MONEDA?")),
    dict(id="s53", text="Para muchos argentinos, la queja de aquel combo de dieciocho dólares no suena tan lejana.",
         visual=I("ba_night", motion="out")),

    # --- CIERRE ---
    dict(id="s54", text="Entonces, ¿se está muriendo McDonald's? No. En el resto del mundo, sus ventas comparables crecieron un uno coma cinco por ciento en el último trimestre.",
         visual=dict(type="num", start=0, end=1.5, dec=1, prefix="+", suffix=" %", label="VENTAS COMPARABLES EN TODO EL MUNDO · 3.ER TRIMESTRE DE 2026")),
    dict(id="s55", text="Pero su historia reciente deja una lección. Cuando tu marca es sinónimo de barato, el precio no es un número. Es una promesa.",
         visual=dict(type="quote", text="EL PRECIO\nNO ES UN NÚMERO.\nES UNA PROMESA.")),
    dict(id="s56", text="Y cuando la gente siente que esa promesa se rompió, basta una foto de un menú para que millones de personas se pregunten si vale la pena volver.",
         visual=I("menu_board")),
    dict(id="s57", text="¿Cuánto pagaste por tu último combo? ¿Sentiste que valía lo que costaba? Cuéntamelo en los comentarios, y dime desde qué país lo pagaste.",
         visual=I("value_meal", motion="out")),
    dict(id="s58", text="Y si te gustan estas historias, suscríbete: cada semana, el último balance de una empresa. Gracias por llegar hasta el final. Nos vemos en el próximo balance.",
         visual=I("drive_night")),
]

# Escenas de reserva (solo si falta img/<clave>.png: la generación de imágenes de DubVoice falla a menudo)
FALLBACK = {
    "s01": dict(type="year", year="17,59 $", sub="UN COMBO BIG MAC · CONNECTICUT, JULIO DE 2023"),
    "s03": dict(type="quote", text="«McDONALD'S\nYA NO ES BARATO»"),
    "s05": dict(type="versus", title="EL GIRO ARGENTINO", left=["BIG MAC", "2.º MÁS CARO\nDEL MUNDO"], right=["ARCOS DORADOS", "MAYOR FRANQUICIADO\nDEL MUNDO"], mid="+", lcol="yellow", rcol="yellow"),
    "s06": dict(type="stamp", text="EL REY DE LA COMIDA BARATA\nSE OLVIDÓ DE SER BARATO", stamp="McDONALD'S", col="red"),
    "s08": dict(type="quote", text="ÁREA DE SERVICIO\n= PRECIOS MÁS ALTOS"),
    "s11": dict(type="chat", title="# redes sociales", kicker="lo que se repetía en 2023-2024", msgs=[
        ["usuario_1", "¿McDonald's cuesta el doble que antes?", "alert"], ["usuario_2", "Ya no es comida barata", "alert"]]),
    "s16": dict(type="quote", text="LOS NÚMEROS\nVS.\nLO QUE SIENTE LA GENTE"),
    "s16b": dict(type="stamp", text="UNOS MESES DESPUÉS…", stamp="EL PROBLEMA FUE LA COMIDA", col="red"),
    "s21": dict(type="stamp", text="ORIGEN MÁS PROBABLE:\nCEBOLLA EN TIRAS FINAS", stamp="RETIRADA", col="red"),
    "s22": dict(type="year", year="DIC 2024", sub="EL BROTE SE DA POR TERMINADO"),
    "s22b": dict(type="stamp", text="2025", stamp="LLEGA LA FACTURA", col="red"),
    "s26": dict(type="quote", text="EL PÚBLICO QUE HIZO\nGRANDE A McDONALD'S"),
    "s29": dict(type="quote", text="SÚPER\nALQUILER\nROPA\nGUARDERÍA"),
    "s29b": dict(type="stamp", text="DIAGNÓSTICO:\nYA NO PARECE BARATO", stamp="ARMA: EL PRECIO", col="yellow"),
    "s33": dict(type="num", start=0, end=8, suffix=" $", label="EL COMBO BIG MAC EXTRA VALUE EN SU LANZAMIENTO (SEP-2025)"),
    "s35": dict(type="stamp", text="EE. UU. · 2024-2025", stamp="GUERRA DE PRECIOS", col="red"),
    "s35b": dict(type="quote", text="BAJAR PRECIOS\nNO ALCANZA\nSI NADIE SE ENTERA"),
    "s42": dict(type="quote", text="LA MISMA ARMA\nQUE LO HIZO FAMOSO:\nSER BARATO"),
    "s44": dict(type="year", year="1986", sub="BUENOS AIRES · ABRE EL PRIMER McDONALD'S DE ARGENTINA"),
    "s46": dict(type="timeline", title="WOODS STATON", points=[["1986", "Primer local en Argentina"], ["2004", "Dirige el sur de América Latina"], ["2007", "Compra todo el negocio"]], hl=2),
    "s49": dict(type="versus", title="DOS CARAS DE McDONALD'S", left=["EE. UU.", "PIERDE CLIENTES"], right=["ARCOS DORADOS", "NACIÓ EN ARGENTINA"], mid="VS", lcol="red", rcol="yellow"),
    "s53": dict(type="quote", text="18 DÓLARES\nNO SUENA TAN LEJOS"),
    "s56": dict(type="quote", text="UNA FOTO\nDE UN MENÚ"),
    "s57": dict(type="quote", text="¿CUÁNTO PAGASTE\nTU ÚLTIMO COMBO?"),
    "s58": dict(type="stamp", text="EL ÚLTIMO BALANCE", stamp="SUSCRÍBETE", col="yellow"),
}

SHORTS = {}

THUMBS = [
    dict(img="menu_board", zoom=1.05, cx=0.5, shade=["left", 225, 0.62], items=[
        ["text", 45, 60, "17,59 $", 220, "yellow", "la"], ["text", 45, 320, "UN COMBO", 130, "white", "la"], ["text", 45, 470, "BIG MAC", 130, "white", "la"]]),
    dict(img="empty_restaurant", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "SE ESTÁN", 150, "white", "la"], ["text", 45, 260, "YENDO", 200, "red", "la"], ["badge", 45, 520, 560, 640, "-4,6 % VISITAS", 70]]),
    dict(img="drive_night", zoom=1.05, cx=0.6, shade=["left", 225, 0.6], items=[
        ["text", 45, 60, "YA NO ES", 150, "white", "la"], ["text", 45, 260, "BARATO", 210, "yellow", "la"]]),
    dict(img="burger_closeup", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "LA FOTO", 160, "white", "la"], ["text", 45, 260, "QUE LO", 130, "white", "la"], ["text", 45, 410, "CAMBIÓ TODO", 120, "yellow", "la"]]),
    dict(img="ba_night", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "EL GIRO", 160, "white", "la"], ["text", 45, 260, "ARGENTINO", 150, "yellow", "la"]]),
    dict(img="receipt_hand", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "+40 %", 220, "red", "la"], ["text", 45, 320, "EN 5 AÑOS", 130, "white", "la"]]),
    dict(img="value_meal", zoom=1.05, cx=0.55, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "18 $", 230, "red", "la"], ["text", 45, 330, "VS", 110, "white", "la"], ["text", 45, 460, "8 $", 200, "yellow", "la"]]),
    dict(img="family_bills", zoom=1.05, cx=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "LOS QUE", 150, "white", "la"], ["text", 45, 260, "YA NO", 150, "white", "la"], ["text", 45, 440, "VUELVEN", 170, "red", "la"]]),
    dict(img="boardroom", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "McDONALD'S", 150, "yellow", "la"], ["stamp", "EN PROBLEMAS", 520, 470, -8, 110]]),
    dict(img="ba_80s", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "NACIÓ EN", 150, "white", "la"], ["text", 45, 260, "BELGRANO", 170, "yellow", "la"]]),
]
THUMBS_TOP = [1, 3, 7]

META = {
    "code": "009",
    "name": "McDonald's",
    "intro_chapter": "Intro: el combo de 17,59 dólares",
    "titles": [
        "McDonald's está perdiendo a sus clientes (y todo empezó con una foto)",
        "La foto de un menú que le costó millones de clientes a McDonald's",
        "Por qué la gente está dejando de ir a McDonald's",
    ],
    "description": "En julio de 2023, la foto de un combo Big Mac a 17,59 dólares en un área de servicio de Connecticut se hizo viral. Tres años después, McDonald's está perdiendo clientes en Estados Unidos: entre julio y septiembre de 2026 sus visitas cayeron un 4,6 % (Placer.ai). Repasamos la subida de precios (+40 % desde 2019, según la propia empresa), el brote de E. coli del Cuarto de Libra, la huida de los clientes con menos ingresos, la guerra del menú barato y los errores que reconoció su CEO. Y el giro argentino: el primer McDonald's de Belgrano (1986), el origen de Arcos Dorados, el mayor franquiciado de McDonald's del mundo, y un Big Mac argentino que llegó a ser el segundo más caro del planeta.",
    "sources": [
        "McDonald's (29-may-2024): carta abierta de Joe Erlinger sobre los precios (Big Mac 4,39 $ → 5,29 $; menú +40 % desde 2019)",
        "Scripps News / Mashed (jul-2023): la foto del combo Big Mac a 17,59 $ en Darien (Connecticut)",
        "CDC (3-dic-2024): brote de E. coli O157:H7 vinculado a la cebolla del Cuarto de Libra (104 casos, 14 estados)",
        "Restaurant Dive / Benzinga / eMarketer (mayo de 2025): ventas de McDonald's EE. UU. -3,6 % en el 1.er trimestre de 2025",
        "NACS (nov-2025): visitas de clientes con menos ingresos, casi -10 % en el 3.er trimestre de 2025",
        "McDonald's / Restaurant Dive (2024-2025): combo de 5 $, McValue y vuelta de los Extra Value Meals",
        "Nation's Restaurant News / Reuters / Business Chief (4-nov-2026): resultados del 3.er trimestre de 2026 (Placer.ai, RMS)",
        "Arcos Dorados, formulario 20-F 2024 (SEC); El Cronista; Foro Económico Mundial: Woods Staton y el primer McDonald's de Argentina",
        "iProUP / Noticias NQN (ene-2026): índice Big Mac de The Economist (Argentina 7,37 $, Suiza 7,99 $)",
    ],
    "disclosure": "Las imágenes de este vídeo son ilustraciones generadas con IA y no muestran restaurantes, productos ni personas reales. La narración está hecha con voz sintética.",
    "hashtags": "#McDonalds #Negocios #ComidaRápida #Argentina",
    "tags": ["mcdonalds", "mcdonald's", "por qué la gente deja de ir a mcdonald's", "mcdonald's crisis", "big mac", "índice big mac",
             "arcos dorados", "woods staton", "mcdonald's argentina", "comida rápida", "precios", "inflación", "historia de empresas",
             "negocios", "el último balance"],
    "pinned": "¿Cuánto pagaste por tu último combo y en qué país? 🍔 Te leo 👇 Y dime qué empresa quieres para el próximo vídeo.",
    "playlist": "Quiebras y caídas",
    "category": "Educación",
    "altered": "Sí",
    "shorts": {},
}
