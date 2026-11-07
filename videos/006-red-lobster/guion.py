# Vídeo 006 — Red Lobster: la oferta de 20 dólares que la hundió… ¿o no?
# Datos de tema (API de YouTube, 6-nov-2026): EN "The rise and fall of Red Lobster" (Michael Girdley) 218k, E. Warren 1M,
# Short "Red Lobster Was Used… Then Killed" 1,86M; ES: solo Insider Español (2024) 546k → hueco en español.
# Lecciones aplicadas: arranque en plena acción con la cifra, sin gráficas en los primeros 30 s, giro adelantado (la demanda
# de 2026), mini-cliffhangers cada 60–90 s, Shorts de 20–25 s. Visuales: tomas de Pexels vía vidIQ (nada reutilizado).
# Hechos verificados (6/7-nov-2026):
# - Declaración del CEO Jonathan Tibus en la quiebra (mayo 2024; KSL/Deseret/Fortune/Yahoo/NBC): ~30 % menos clientes desde
#   2019; pérdida de 76 M$ en el ejercicio 2023; Ultimate Endless Shrimp permanente decidido por el ex-CEO Paul Kenny pese a la
#   oposición de otros directivos; coste 11 M$; Thai Union con "influencia desmedida" en las compras de camarón; dos
#   proveedores de camarón empanizado apartados "con la excusa de una revisión de calidad". Thai Union: contrademanda por
#   22,9 M$ de inventario sobrante.
# - Precio 20 $ (permanente desde mayo/junio 2023), subido a 22 y 25 $ sin frenar las pérdidas (NBC/CBS); CFO de Thai Union:
#   eligieron la promoción muchos más clientes de lo esperado. Ene-2024: Thai Union anuncia su salida (pérdida de 19 M$ en
#   9 meses de 2023; "no esperamos sacar mucho de la venta").
# - 2014: Darden vende Red Lobster a Golden Gate Capital por 2.100 M$ (CNN/Fox Business); a la vez, sale-leaseback de más de
#   500 restaurantes por ~1.500 M$ a American Realty Capital Properties (8-K en la SEC): contratos de más de 24 años de media,
#   subidas del 2 % anual, el inquilino paga impuestos, mantenimiento y obras. Starboard (activista) estimaba los inmuebles
#   en hasta 4.000 M$; Darden: la venta no necesitaba aprobación de los accionistas.
# - Quiebra (capítulo 11): 19-may-2024; ~100 cierres; más de 230 contratos rechazados; sept-2024 la compran sus prestamistas
#   encabezados por Fortress (puja de crédito de 376 M$), ~545 restaurantes. Portavoz: el mayor problema de alquiler son
#   contratos heredados por encima del mercado, sobre todo del sale-leaseback de 2014.
# - Damola Adamolekun: CEO desde agosto de 2024 con 35 años (nacido feb-1989), el más joven de su historia; antes CEO de
#   P.F. Chang's. Jul-2026: "Cuando llegué, el negocio principal no funcionaba". Bloomberg (mar-2026): pérdidas en 4 de los
#   últimos 5 trimestres. Sept-2026 (Restaurant Business): 484 locales en EE. UU.
# - Demanda de 2026 (Red Lobster GUC Trust, tribunal federal de Florida; NRN/Fortune/CNBC/Restaurant Dive/SeafoodSource):
#   contra Thai Union, su CEO y Paul Kenny; alega que Thai Union controlaba 3 de 5 puestos del consejo desde 2020, apartó a
#   proveedores y llegó al 46 % de las compras de camarón, y usó la promoción para exprimir a la empresa. Thai Union lo niega:
#   "implausible" arriesgar su inversión de 575 M$ por compras de camarón de menos de 33 M$; "intento cínico" de culparla.
# - Origen: Lakeland (Florida), 1968, Bill Darden y Charley Woodsby; Darden empezó a los 19 años (1938) con un restaurante de
#   25 asientos en Waycross (Georgia). General Mills la compró en 1970. Galletas Cheddar Bay: principios de los 90.
VOICE = "i4Kar2uamCWyas8TAu31"  # ElevenLabs "Adán - Narration"
SPEED = 1.0

BROLL = {  # clave → búsqueda en vidIQ (vidiq_generate_broll); elegidas en broll.json
    "shrimp": "fried shrimp plate restaurant", "platter": "fried shrimp plate restaurant", "lobster": "live lobster tank restaurant",
    "lobster2": "live lobster tank restaurant", "dinner": "family eating seafood dinner restaurant", "lake": "florida lake sunset",
    "sunset": "florida lake sunset", "kitchen": "chef cooking seafood restaurant kitchen", "money": "counting dollar bills hands",
    "signing": "signing contract business deal", "for_rent": "for lease sign commercial building",
    "shrimp_market": "shrimp processing seafood factory workers", "shrimp_bag": "shrimp processing seafood factory workers",
    "empty_rest": "empty restaurant chairs on tables closed", "empty_tables": "empty restaurant chairs on tables closed",
    "lawyers": "lawyer reading legal documents desk", "documents": "lawyer reading legal documents desk",
    "boats": "fishing boat at sea asia", "bread": "fresh bread rolls out of oven", "parking": "restaurant exterior evening parking lot america",
    "worried": "calculator bills expenses desk", "calculator": "calculator bills expenses desk", "crayfish": "cooked lobster dinner plate",
}

SCENES = [
    # --- GANCHO (en plena acción, sin gráficas) ---
    dict(id="s01", text="Veinte dólares. Camarones sin límite, todas las veces que quisieras. En dos mil veintitrés, Red Lobster, la mayor cadena de marisquerías de Estados Unidos, convirtió esa oferta en permanente.",
         visual=dict(type="img", key="shrimp", cap="CAMARONES SIN LÍMITE · 20 $")),
    dict(id="s02", text="La gente respondió como era de esperar: pidió, y pidió, y pidió. Según los documentos de su quiebra, la oferta le costó once millones de dólares.",
         visual=dict(type="img", key="platter")),
    dict(id="s03", text="Menos de un año después, Red Lobster estaba en bancarrota. Y todo el mundo culpó a los camarones.",
         visual=dict(type="img", key="empty_rest", cap="MAYO DE 2024")),
    dict(id="s04", text="Pero en esos mismos papeles aparece otra historia. Un alquiler que empezó diez años antes, por sus propios restaurantes. Y un socio que, además, era quien le vendía los camarones.",
         visual=dict(type="img", key="for_rent")),
    dict(id="s05", text="Y en dos mil veintiséis, una demanda asegura algo todavía más fuerte: que la oferta no fue un error. Que fue un plan. Esta es la historia.",
         visual=dict(type="img", key="lawyers", cap="¿ERROR… O PLAN?")),

    # --- 01 ---
    dict(id="s06", text="Capítulo uno: un restaurante junto al lago.",
         visual=dict(type="title", num="01", text="UN RESTAURANTE JUNTO AL LAGO", name="Un restaurante junto al lago")),
    dict(id="s07", text="Lakeland, Florida, mil novecientos sesenta y ocho. Bill Darden y Charley Woodsby abren un restaurante de mariscos a orillas de un lago.",
         visual=dict(type="img", key="lake", cap="LAKELAND, FLORIDA · 1968")),
    dict(id="s08", text="Darden no era un novato: había empezado a los diecinueve años, con un local de veinticinco asientos en Georgia.",
         visual=dict(type="year", year="1938", sub="DARDEN COMPRA SU PRIMER RESTAURANTE: 25 ASIENTOS")),
    dict(id="s09", text="La idea era simple: llevar el marisco, que parecía un lujo de la costa, a la familia estadounidense de clase media, a un precio razonable.",
         visual=dict(type="img", key="dinner")),
    dict(id="s10", text="Funcionó tan bien que, en mil novecientos setenta, el gigante General Mills compró la cadena. Y Red Lobster se multiplicó por todo el país.",
         visual=dict(type="img", key="kitchen", cap="1970: LA COMPRA GENERAL MILLS")),
    dict(id="s11", text="A principios de los noventa llegó su arma secreta: unos panecillos de queso cheddar y ajo que se volvieron casi tan famosos como las langostas.",
         visual=dict(type="img", key="bread", cap="PANECILLOS CHEDDAR BAY")),
    dict(id="s12", text="Llegó a tener unos setecientos restaurantes. Parecía imposible que algo así se hundiera. Pero en dos mil catorce firmó un contrato que lo cambiaría todo.",
         visual=dict(type="img", key="lobster")),

    # --- 02 ---
    dict(id="s13", text="Capítulo dos: inquilino de sí mismo.",
         visual=dict(type="title", num="02", text="INQUILINO DE SÍ MISMO", name="Inquilino de sí mismo")),
    dict(id="s14", text="En dos mil catorce, su dueño, Darden, decidió venderla. El comprador fue un fondo de inversión, Golden Gate Capital.",
         visual=dict(type="img", key="signing", cap="2014")),
    dict(id="s15", text="El precio: dos mil cien millones de dólares.",
         visual=dict(type="num", start=0, end=2100, prefix="", suffix=" M$", label="LO QUE PAGÓ GOLDEN GATE CAPITAL POR RED LOBSTER")),
    dict(id="s16", text="Pero en la misma operación pasó algo clave. Los edificios y terrenos de más de quinientos restaurantes se vendieron por separado, por unos mil quinientos millones, a una empresa inmobiliaria.",
         visual=dict(type="img", key="money")),
    dict(id="s17", text="Desde ese día, Red Lobster pasó a pagar alquiler por los restaurantes que antes eran suyos.",
         visual=dict(type="stamp", text="DE DUEÑO DE SUS LOCALES\nA INQUILINO", stamp="ALQUILER")),
    dict(id="s18", text="Y no era un alquiler cualquiera. Contratos de más de veinticuatro años de media, con subidas del dos por ciento cada año. Y encima, Red Lobster pagaba los impuestos, el mantenimiento y las obras.",
         visual=dict(type="img", key="for_rent", cap="+2 % CADA AÑO")),
    dict(id="s19", text="Hubo quien avisó. Un fondo activista calculaba que esos inmuebles podían valer hasta cuatro mil millones. Pero la venta no necesitaba la aprobación de los accionistas, y se hizo igual.",
         visual=dict(type="versus", title="LOS INMUEBLES DE RED LOBSTER", left=["1.500 M$", "LO QUE SE PAGÓ"], right=["4.000 M$", "LO QUE VALÍAN\nSEGÚN UN ACTIVISTA"], mid="VS", lcol="yellow", rcol="red")),
    dict(id="s20", text="La cadena tenía ahora una factura fija que subía cada año, vendiera o no vendiera. Y pronto iba a llegar alguien que vendía otra cosa: camarones.",
         visual=dict(type="img", key="calculator")),

    # --- 03 ---
    dict(id="s21", text="Capítulo tres: el socio de los camarones.",
         visual=dict(type="title", num="03", text="EL SOCIO DE LOS CAMARONES", name="El socio de los camarones")),
    dict(id="s22", text="Thai Union es uno de los mayores productores de mariscos del mundo. Y en esos años se convirtió en socio de Red Lobster.",
         visual=dict(type="img", key="boats", cap="THAI UNION · TAILANDIA")),
    dict(id="s23", text="En dos mil veinte, según la demanda posterior, Thai Union encabezó la compra del control con un grupo de inversores, y se quedó con tres de los cinco puestos del consejo.",
         visual=dict(type="stamp", text="3 DE 5 PUESTOS\nEN EL CONSEJO", stamp="CONTROL")),
    dict(id="s24", text="Es decir: el que mandaba en Red Lobster también era uno de los que le vendía el producto estrella.",
         visual=dict(type="img", key="shrimp_market")),
    dict(id="s25", text="Y al frente de la empresa terminó Paul Kenny, un ejecutivo vinculado a Thai Union. En la quiebra, el director general que la llevó declaró que Thai Union tuvo una influencia desmedida en las compras de camarón.",
         visual=dict(type="img", key="documents", cap="DECLARACIÓN EN LA QUIEBRA")),
    dict(id="s26", text="Según esa declaración, dos proveedores de camarón empanizado fueron apartados con la excusa de una revisión de calidad. Thai Union lo niega todo. Pero lo que vino después lo conoce todo el mundo.",
         visual=dict(type="img", key="shrimp_bag")),

    # --- 04 ---
    dict(id="s27", text="Capítulo cuatro: camarones sin fin.",
         visual=dict(type="title", num="04", text="CAMARONES SIN FIN", name="Camarones sin fin")),
    dict(id="s28", text="Red Lobster ya hacía la promoción de camarones ilimitados de vez en cuando, para atraer clientes. En dos mil veintitrés, Paul Kenny decidió hacerla permanente, a veinte dólares.",
         visual=dict(type="img", key="platter", cap="PERMANENTE · 20 $")),
    dict(id="s29", text="Según la declaración de la quiebra, lo decidió pese a la oposición de otros directivos.",
         visual=dict(type="quote", text="«PESE A LA\nOPOSICIÓN DE\nOTROS DIRECTIVOS»")),
    dict(id="s30", text="Y pasó lo que temían. Muchos más clientes de lo previsto pidieron la oferta, lo reconoció el propio director financiero de Thai Union. Y cuantos más platos repetían, más perdía la cadena.",
         visual=dict(type="img", key="shrimp")),
    dict(id="s31", text="Subieron el precio a veintidós dólares. Después, a veinticinco. No alcanzó.",
         visual=dict(type="versus", title="EL PRECIO DE LOS CAMARONES SIN LÍMITE", left=["20 $", "2023"], right=["25 $", "Y AUN ASÍ, PÉRDIDAS"], mid="→", lcol="yellow", rcol="red")),
    dict(id="s32", text="Once millones de dólares de pérdida por la promoción. Y mientras tanto, el problema de fondo seguía ahí: desde dos mil diecinueve, Red Lobster había perdido cerca del treinta por ciento de sus clientes.",
         visual=dict(type="num", start=0, end=-30, suffix=" %", label="CLIENTES DE RED LOBSTER DESDE 2019")),
    dict(id="s33", text="En dos mil veintitrés perdió setenta y seis millones de dólares. Y en enero de dos mil veinticuatro, Thai Union anunció que se iba. Su director general dijo que no esperaba sacar mucho de la venta.",
         visual=dict(type="img", key="worried", cap="−76 M$ EN 2023")),

    # --- 05 ---
    dict(id="s34", text="Capítulo cinco: la quiebra.",
         visual=dict(type="title", num="05", text="LA QUIEBRA", name="La quiebra")),
    dict(id="s35", text="Primero llegaron los cierres. De un día para otro, cerca de cien restaurantes apagaron las luces. Y eso fue antes incluso de declararse en quiebra.",
         visual=dict(type="img", key="empty_tables", cap="CERCA DE 100 CIERRES")),
    dict(id="s36", text="El diecinueve de mayo de dos mil veinticuatro, Red Lobster se declaró en quiebra.",
         visual=dict(type="year", year="19 MAY 2024", sub="RED LOBSTER SE DECLARA EN QUIEBRA")),
    dict(id="s37", text="En el proceso rechazó más de doscientos treinta contratos de alquiler. Y su portavoz lo dijo claro: el mayor problema eran los alquileres heredados, por encima del mercado, firmados sobre todo en la venta de dos mil catorce.",
         visual=dict(type="img", key="parking")),
    dict(id="s38", text="Ahí está la otra mitad de la historia. Los camarones fueron el golpe que todo el mundo vio. El alquiler llevaba diez años apretando en silencio.",
         visual=dict(type="versus", title="LO QUE HUNDIÓ A RED LOBSTER", left=["11 M$", "CAMARONES\n(UNA PROMOCIÓN)"], right=["10 AÑOS", "DE ALQUILERES\nQUE SUBÍAN"], mid="+", lcol="yellow", rcol="red")),
    dict(id="s39", text="En septiembre, sus propios prestamistas, encabezados por el fondo Fortress, se quedaron con la empresa. Salió de la quiebra con unos quinientos cuarenta y cinco restaurantes. Y con un director general muy distinto.",
         visual=dict(type="img", key="signing", cap="SEPTIEMBRE DE 2024")),

    # --- 06 ---
    dict(id="s40", text="Capítulo seis: un capitán de treinta y cinco años.",
         visual=dict(type="title", num="06", text="UN CAPITÁN DE 35 AÑOS", name="Un capitán de 35 años")),
    dict(id="s41", text="Damola Adamolekun llegó en agosto de dos mil veinticuatro, con treinta y cinco años. Es el director general más joven en la historia de Red Lobster. Antes había dirigido la cadena P. F. Chang's.",
         visual=dict(type="img", key="kitchen", cap="CEO DESDE AGOSTO DE 2024")),
    dict(id="s42", text="Su diagnóstico fue directo: cuando llegó, el negocio principal no funcionaba.",
         visual=dict(type="quote", text="«CUANDO LLEGUÉ,\nEL NEGOCIO PRINCIPAL\nNO FUNCIONABA»")),
    dict(id="s43", text="Su plan: cerrar los restaurantes que pierden dinero, recortar el menú, y apostar por la nostalgia: los platos de siempre y los famosos panecillos.",
         visual=dict(type="img", key="crayfish")),
    dict(id="s44", text="Pero el camino es lento. Según Bloomberg, la cadena tuvo pérdidas en cuatro de cinco trimestres. Y en septiembre de dos mil veintiséis ya le quedaban cuatrocientos ochenta y cuatro locales en Estados Unidos.",
         visual=dict(type="num", start=0, end=484, label="RESTAURANTES EN EE. UU. (SEPTIEMBRE DE 2026)")),
    dict(id="s45", text="Y aun así, este año volvió a ofrecer los camarones sin límite. Solo en algunos mercados, y con mucho cuidado. Porque mientras tanto, en un juzgado de Florida, esa oferta estaba siendo juzgada.",
         visual=dict(type="img", key="shrimp", cap="2026: VUELVEN… CON LÍMITES")),

    # --- 07 ---
    dict(id="s46", text="Capítulo siete: ¿error o plan?",
         visual=dict(type="title", num="07", text="¿ERROR O PLAN?", name="¿Error o plan?")),
    dict(id="s47", text="En dos mil veintiséis, el fideicomiso que representa a los acreedores de Red Lobster demandó a Thai Union, a su director general y a Paul Kenny.",
         visual=dict(type="img", key="lawyers", cap="TRIBUNAL FEDERAL · FLORIDA")),
    dict(id="s48", text="La demanda sostiene que Thai Union usó su control para apartar a otros proveedores, que llegó a vender el cuarenta y seis por ciento de todos los camarones que compraba la cadena, y que la promoción sirvió para exprimir a la empresa.",
         visual=dict(type="num", start=0, end=46, suffix=" %", label="DE LOS CAMARONES DE RED LOBSTER (SEGÚN LA DEMANDA)")),
    dict(id="s49", text="Thai Union responde que es absurdo: que había invertido quinientos setenta y cinco millones en Red Lobster, y que no lo iba a arriesgar por compras de camarón de menos de treinta y tres millones.",
         visual=dict(type="versus", title="LA DEFENSA DE THAI UNION", left=["575 M$", "LO QUE INVIRTIÓ\nEN RED LOBSTER"], right=["< 33 M$", "SUS VENTAS\nDE CAMARÓN"], mid="VS", lcol="white", rcol="yellow")),
    dict(id="s50", text="Y lo llama un intento cínico de culparla por los errores de gestión de la propia Red Lobster. El caso sigue abierto. Ningún tribunal ha dado todavía la razón a nadie.",
         visual=dict(type="img", key="documents", cap="CASO ABIERTO")),
    dict(id="s51", text="Lo que sí está escrito en los documentos es esto: una cadena que vendió sus propios restaurantes, que quedó en manos de su proveedor, y que regaló su producto más caro a veinte dólares.",
         visual=dict(type="img", key="lobster2")),
    dict(id="s52", text="Los camarones no hundieron solos a Red Lobster. Fueron la última ola, sobre un barco que llevaba diez años haciendo agua.",
         visual=dict(type="quote", text="LOS CAMARONES\nFUERON LA ÚLTIMA OLA")),
    dict(id="s53", text="¿Tú crees que fue un error o un plan? Te leo en los comentarios. Y si te gustan estas historias, suscríbete: cada semana, el último balance de una empresa.",
         visual=dict(type="img", key="sunset")),
]

SHORTS = {
    "a": {"bar": "CAMARONES SIN LÍMITE", "scenes": [
        dict(id="a01", text="Camarones sin límite por veinte dólares. Esta oferta ayudó a hundir a la mayor cadena de marisquerías de Estados Unidos.", key="shrimp"),
        dict(id="a02", text="La pidió mucha más gente de lo previsto, y le costó once millones de dólares. Subieron el precio a veinticinco… y no alcanzó.", key="platter"),
        dict(id="a03", text="Red Lobster quebró en dos mil veinticuatro. La historia completa, en mi canal.", key="empty_rest"),
    ]},
    "b": {"bar": "¿ERROR O PLAN?", "scenes": [
        dict(id="b01", text="Una demanda dice que la oferta que hundió a Red Lobster no fue un error.", key="lawyers"),
        dict(id="b02", text="Su socio, Thai Union, era también quien le vendía los camarones. Los acreedores lo acusan de usar la promoción para exprimir a la empresa. Thai Union lo niega.", key="shrimp_market"),
        dict(id="b03", text="El juicio sigue abierto en Florida, y todavía nadie lo ha ganado. Toda la historia, en mi canal.", key="documents"),
    ]},
}

THUMBS = [
    dict(img="shrimp", zoom=1.1, cx=0.5, cy=0.5, shade=["left", 225, 0.62], items=[
        ["text", 45, 40, "20 $", 230, "yellow", "la"], ["text", 45, 300, "CAMARONES", 120, "white", "la"], ["text", 45, 440, "SIN LÍMITE", 120, "white", "la"],
        ["badge", 45, 590, 430, 690, "QUIEBRA", 80]]),
    dict(img="lobster2", zoom=1.05, cx=0.6, cy=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 70, "¿ERROR", 200, "white", "la"], ["text", 45, 320, "O PLAN?", 200, "red", "la"]]),
    dict(img="empty_rest", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "QUEBRÓ", 210, "white", "la"], ["text", 45, 320, "POR 20 $", 170, "yellow", "la"], ["stamp", "¿SEGURO?", 950, 560, -10, 110]]),
    dict(img="for_rent", zoom=1.0, cx=0.5, cy=0.5, shade=["left", 230, 0.65], items=[
        ["text", 45, 60, "PAGABA", 150, "white", "la"], ["text", 45, 250, "ALQUILER", 150, "yellow", "la"], ["text", 45, 440, "DE SUS LOCALES", 105, "white", "la"]]),
    dict(img="crayfish", zoom=1.0, cx=0.5, cy=0.5, shade=["left", 230, 0.62], items=[
        ["text", 45, 60, "11 M$", 220, "yellow", "la"], ["text", 45, 330, "EN CAMARONES", 115, "white", "la"], ["badge", 45, 520, 520, 630, "UNA SOLA OFERTA", 66]]),
    dict(img="lobster", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 210, 0.6], items=[
        ["text", 45, 60, "RED", 200, "red", "la"], ["text", 45, 300, "LOBSTER", 200, "white", "la"], ["stamp", "QUIEBRA", 960, 560, -12, 120]]),
    dict(img="platter", zoom=1.1, cx=0.5, cy=0.5, shade=["left", 225, 0.6], items=[
        ["text", 45, 70, "UNA OFERTA", 140, "white", "la"], ["text", 45, 260, "LA HUNDIÓ", 170, "red", "la"], ["text", 45, 480, "¿O NO?", 130, "yellow", "la"]]),
    dict(img="money", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 70, "VENDIÓ SUS", 140, "white", "la"], ["text", 45, 260, "RESTAURANTES", 130, "yellow", "la"], ["text", 45, 440, "Y SE HUNDIÓ", 130, "red", "la"]]),
]
THUMBS_TOP = [1, 3, 2]

META = {
    "code": "006",
    "name": "Red Lobster",
    "intro_chapter": "Intro: camarones sin límite por 20 dólares",
    "titles": [
        "Una oferta de 20 $ hundió a Red Lobster… o eso nos contaron",
        "Red Lobster: camarones sin límite, quiebra y una demanda (¿error o plan?)",
        "Así se hundió la mayor cadena de mariscos de EE. UU. (no fueron solo los camarones)",
    ],
    "description": "En 2023, Red Lobster convirtió en permanente su oferta de camarones sin límite por 20 dólares. Según los documentos de su quiebra, le costó 11 millones, y en mayo de 2024 la cadena se declaró en bancarrota. Pero la historia empieza diez años antes, cuando vendió los edificios de más de 500 restaurantes y pasó a pagar alquiler por ellos, y sigue con un socio que también era su proveedor de camarones. En 2026, una demanda de los acreedores asegura que la oferta no fue un error; Thai Union lo niega y el caso sigue abierto.",
    "sources": [
        "Declaración de Jonathan Tibus en la quiebra de Red Lobster (mayo de 2024) — KSL / Deseret News / Fortune / NBC News / Yahoo Finance",
        "NBC News / CBS News: precio de Ultimate Endless Shrimp (20, 22 y 25 dólares) y declaraciones de Thai Union",
        "CNN Money / Fox Business (mayo de 2014): Darden vende Red Lobster a Golden Gate Capital por 2.100 millones",
        "SEC — formularios 8-K de American Realty Capital Properties (2014): sale-leaseback de más de 500 restaurantes",
        "Bisnow / Restaurant Business / BNN Bloomberg: cierres, contratos de alquiler y venta a Fortress (2024)",
        "Fortune (febrero de 2026), Rolling Out (julio de 2026), Restaurant Business (septiembre de 2026): Damola Adamolekun y el plan de rescate",
        "Nation's Restaurant News / Fortune / CNBC / Restaurant Dive / SeafoodSource (2026): demanda del Red Lobster GUC Trust contra Thai Union",
        "Wikipedia / LAL Today: origen de Red Lobster en Lakeland (1968)",
        "Vídeos de archivo: Pexels (vía vidIQ) — Bonus Studio, FU GUYI, Glenn Langhorst, Ivan S, Jaxon Matthew Willis, Kindel Media, Los Muertos Crew, Magda Ehlers, Mikhail Nilov, olia danilevich, Pavel Danilyuk, Scott Portier, Shutter Break, Thirdman, WeStarMoney Rec, Zuzanna Musial, cottonbro studio, kaboompics, khanhhoangminh",
    ],
    "disclosure": "La narración de este vídeo está hecha con voz sintética. Las imágenes son vídeos de archivo de Pexels que ilustran la historia; no muestran a las personas, los restaurantes ni los hechos reales. Las acusaciones de la demanda de 2026 no han sido probadas en un tribunal y Thai Union las niega.",
    "hashtags": "#RedLobster #Negocios #Quiebra #Empresas",
    "tags": ["red lobster", "red lobster quiebra", "camarones ilimitados", "endless shrimp", "thai union", "quiebra",
             "historia de empresas", "restaurantes", "fondos de inversión", "sale leaseback", "negocios", "el último balance"],
    "pinned": "¿Error o plan? 🦐 ¿Qué crees que hundió de verdad a Red Lobster? 👇 Y dime qué empresa quieres para el próximo vídeo.",
    "playlist": "Auges y caídas",
    "shorts": {
        "a": {"title": "Camarones sin límite por 20 $… y la cadena quebró 🦐",
              "description": "La oferta que ayudó a hundir a Red Lobster. Historia completa en el canal. #RedLobster #shorts",
              "tags": ["red lobster", "camarones", "quiebra", "negocios", "shorts"]},
        "b": {"title": "¿La oferta que hundió a Red Lobster fue un plan? 🤔",
              "description": "Una demanda de 2026 acusa a su antiguo socio y proveedor; Thai Union lo niega. Historia completa en el canal. #RedLobster #shorts",
              "tags": ["red lobster", "thai union", "demanda", "negocios", "shorts"]},
    },
}
