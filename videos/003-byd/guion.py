# Vídeo 003 — BYD: de baterías de móvil a superar a Tesla (vídeo de prueba con todas las mejoras)
VOICE = "i4Kar2uamCWyas8TAu31"  # ElevenLabs "Adán - Narration" (latinoamericano)
SPEED = 1.0
IMAGE_MODEL = "nano-banana-2"
# Hechos verificados (2026-11-01): CNBC/InsideEVs/SCMP (Musk 2011 y 2023), Electrek/CnEVPost (ventas 2025),
# Wikipedia/Telltales/Validea-Fortune (fundación, Qinchuan, Buffett), ChargedEVs/BatteryDesign (Blade),
# AP/BNN Bloomberg (ingresos 2024), CnEVPost/Bloomberg (barcos ene-2024), JATO vía Silicon/iTiger (Europa abr-2025),
# Fortune/CleanTechnica/CarNewsChina (guerra de precios, 60 días, cero km), TipRanks/Bloomberg (GMT Research),
# AP/Euronews (Brasil dic-2024), Liga (Berkshire), CnEVPost/Automotive World (H1 2026), Heise/BI (México en pausa).

IMAGES = {
    "robot_line": "A modern electric car factory with dozens of orange robotic arms welding car bodies on an assembly line, sparks flying, cool blue light, wide cinematic shot, no logos, no readable text",
    "battery_lab_1995": "A 1990s Chinese battery workshop, rows of workers in uniforms assembling small rechargeable mobile phone batteries by hand on long tables, fluorescent light, film grain, documentary photo, no logos, no readable text",
    "phones_90s": "Close-up of a pile of old 1990s mobile phones and rectangular rechargeable batteries on a workbench, warm light, shallow depth of field, no logos, no readable text",
    "old_car_factory": "An old dated car assembly plant in northwest China in the early 2000s, a few boxy sedans on the line, dusty light beams, documentary photo, no logos, no readable text",
    "blade_battery": "A long thin blade-shaped battery cell clamped in a laboratory test rig while a steel nail pierces it, clean lab, dramatic lighting, cinematic macro shot, no logos, no readable text",
    "car_ship": "A giant roll-on roll-off car carrier ship docked at a port at night, thousands of new electric cars lined up on the pier waiting to be loaded, cinematic aerial view, no logos, no readable text",
    "showroom_price": "A bright modern car showroom in China full of sleek electric cars and customers, large red discount banners with no readable text, cinematic, no logos",
    "empty_lot": "A vast parking lot full of thousands of identical new cars covered in dust under an overcast sky, aerial drone view, cinematic, no logos, no readable text",
    "europe_road": "A sleek modern electric SUV driving on a European city street at dusk, wet road reflections, old buildings, cinematic, no logos, no readable text",
    "latam_street": "A busy avenue in Mexico City at golden hour with modern electric cars and taxis in traffic, cinematic, no logos, no readable text",
    "night_car": "A sleek generic electric sedan parked alone under a single streetlight at night in the rain, reflections, cinematic and moody, no logos, no readable text",
    "boardroom": "An empty corporate boardroom with a long table, scattered financial reports and a city skyline at dusk behind glass, tense mood, cinematic, no readable text, no logos",
}
# Fondos de miniatura con el modelo Pro
THUMB_IMAGES = {
    "thumb_car": "A sleek futuristic electric sedan in a dark studio with dramatic red rim lighting and light smoke, hyper-detailed, cinematic product shot, no logos, no text",
    "thumb_vs": "Two sleek electric cars facing each other head-on in a dark arena, the left one lit with red light and the right one lit with cold white light, dramatic standoff, cinematic, no logos, no text",
}
# Escenas que se animan con vídeo IA (imagen → vídeo). Prompt de movimiento para cada imagen.
CLIPS = {
    "robot_line": "the robotic arms move and weld, sparks fly, the assembly line slowly advances, camera slowly pushes in",
    "battery_lab_1995": "workers assemble batteries with their hands, subtle natural movement, camera slowly pans right",
    "blade_battery": "the steel nail slowly pierces the battery cell, no fire, no smoke, camera slowly pushes in",
    "car_ship": "cars slowly drive up the ramp into the ship, port lights flicker, camera slowly flies forward",
    "showroom_price": "customers walk around the cars, banners sway slightly, camera slowly tracks left",
    "empty_lot": "slow aerial drone flight over the endless rows of parked cars, clouds moving",
    "europe_road": "the SUV drives toward the camera along the wet street, lights reflecting, camera tracks backward",
    "night_car": "rain falls, puddles ripple, the streetlight flickers slightly, camera slowly pushes in toward the car",
}

LINES_DATA = dict(title="COCHES 100 % ELÉCTRICOS VENDIDOS (MILES)", x=["2021", "2022", "2023", "2024", "2025"],
                  series=[["BYD", [321, 911, 1575, 1765, 2255], "red"], ["TESLA", [936, 1314, 1809, 1789, 1636], "white"]])

SCENES = [
    # --- GANCHO ---
    dict(id="s01", text="En dos mil once, un periodista le preguntó a Elon Musk si le preocupaba una empresa china llamada BYD. Musk se echó a reír.",
         visual=dict(type="img", key="robot_line", cap="2011 · BYD")),
    dict(id="s02", text="¿Has visto sus coches?, respondió. Dijo que su tecnología no era muy fuerte, y que no la veía como competencia.",
         visual=dict(type="quote", text="\"¿HAS VISTO\nSUS COCHES?\"\n— ELON MUSK, 2011")),
    dict(id="s03", text="Catorce años después, en dos mil veinticinco, BYD vendió más de dos millones doscientos mil coches cien por cien eléctricos. Tesla, un millón seiscientos mil.",
         visual=dict(type="lines", **LINES_DATA)),
    dict(id="s04", text="Esta es la historia de cómo un químico que fabricaba baterías para teléfonos móviles construyó la empresa que destronó a Tesla.",
         visual=dict(type="img", key="night_car")),
    dict(id="s05", text="Y también de las dudas que la persiguen: una guerra de precios brutal, proveedores asfixiados, y un informe que asegura que su deuda real es muchísimo mayor de lo que parece.",
         visual=dict(type="quote", text="Y LAS DUDAS\nQUE LA\nPERSIGUEN")),

    # --- CAPÍTULO 1 ---
    dict(id="s06", text="Capítulo uno. El químico de las baterías.",
         visual=dict(type="title", num="01", text="EL QUÍMICO DE LAS BATERÍAS", name="El químico de las baterías")),
    dict(id="s07", text="Febrero de mil novecientos noventa y cinco. Shenzhen, en el sur de China. Wang Chuanfu, un químico especializado en baterías, funda una pequeña empresa con dinero prestado por un primo. La llama BYD.",
         visual=dict(type="year", year="1995", sub="NACE BYD EN SHENZHEN")),
    dict(id="s08", text="Las baterías recargables para móviles las dominaban empresas japonesas, con fábricas llenas de máquinas carísimas. Wang decide hacerlo de otra forma: con mucha mano de obra, herramientas sencillas y costes mucho más bajos.",
         visual=dict(type="img", key="battery_lab_1995", cap="MANOS EN VEZ DE MÁQUINAS")),
    dict(id="s09", text="Funciona. BYD acaba fabricando baterías y componentes para gigantes de los móviles como Nokia y Motorola.",
         visual=dict(type="img", key="phones_90s", cap="NOKIA · MOTOROLA")),
    dict(id="s10", text="En dos mil dos sale a bolsa en Hong Kong. Wang ya era un empresario de éxito. Pero lo que hizo al año siguiente casi nadie lo entendió.",
         visual=dict(type="year", year="2002", sub="SALE A BOLSA EN HONG KONG")),

    # --- CAPÍTULO 2 ---
    dict(id="s11", text="Capítulo dos. La apuesta que nadie entendía.",
         visual=dict(type="title", num="02", text="LA APUESTA QUE NADIE ENTENDÍA", name="La apuesta que nadie entendía")),
    dict(id="s12", text="En enero de dos mil tres, BYD compra un pequeño fabricante de coches con problemas: Qinchuan Auto. Su propio consejo de administración no estaba de acuerdo.",
         visual=dict(type="img", key="old_car_factory", cap="2003 · QINCHUAN AUTO")),
    dict(id="s13", text="¿Una empresa de baterías fabricando coches? A los inversores no les gustó nada. Pero Wang tenía una idea fija: si el futuro eran los coches eléctricos, quien dominara las baterías dominaría los coches.",
         visual=dict(type="quote", text="QUIEN DOMINE\nLAS BATERÍAS\nDOMINARÁ LOS COCHES")),
    dict(id="s14", text="Y en dos mil ocho, alguien muy famoso le da la razón. Berkshire Hathaway, la empresa de Warren Buffett, compra cerca del diez por ciento de BYD por unos doscientos treinta millones de dólares.",
         visual=dict(type="year", year="2008", sub="WARREN BUFFETT COMPRA EL 10 %")),
    dict(id="s15", text="Según la revista Fortune, Buffett quería una cuarta parte de la empresa. Wang solo aceptó venderle el diez por ciento.",
         visual=dict(type="quote", text="BUFFETT QUERÍA EL 25 %.\nWANG SOLO LE\nDEJÓ EL 10 %.")),
    dict(id="s16", text="Durante años, BYD vende coches baratos de gasolina, híbridos y autobuses eléctricos. No era glamuroso. Pero estaba aprendiendo algo que casi nadie tenía: a fabricar casi todo ella misma.",
         visual=dict(type="img", key="old_car_factory", motion="out")),

    # --- CAPÍTULO 3 ---
    dict(id="s17", text="Capítulo tres. Adiós a la gasolina.",
         visual=dict(type="title", num="03", text="ADIÓS A LA GASOLINA", name="Adiós a la gasolina")),
    dict(id="s18", text="En marzo de dos mil veinte, BYD presenta la batería Blade: una batería de litio ferrofosfato, larga y delgada como una cuchilla. Para demostrar que es segura, la atraviesan con un clavo.",
         visual=dict(type="img", key="blade_battery", cap="BATERÍA BLADE · 2020")),
    dict(id="s19", text="Según BYD, no echó humo ni fuego, y su superficie se quedó entre treinta y sesenta grados. Una batería convencional de las más usadas, en la misma prueba, superó los quinientos grados y ardió.",
         visual=dict(type="bars", title="TEMPERATURA EN LA PRUEBA DEL CLAVO (°C)", data=[["BLADE (máx.)", 60], ["BATERÍA CONVENCIONAL", 500]], reveal=2)),
    dict(id="s20", text="Y en marzo de dos mil veintidós da un paso que ningún gran fabricante se había atrevido a dar: deja de fabricar coches solo de gasolina. A partir de ahí, solo eléctricos e híbridos enchufables.",
         visual=dict(type="year", year="MARZO 2022", sub="FIN DE LOS COCHES DE GASOLINA")),
    dict(id="s21", text="Su gran ventaja es que fabrica casi todo ella misma: las baterías, los motores, muchos de sus chips. Cuando el resto del mundo sufría por la falta de piezas, BYD tenía las suyas.",
         visual=dict(type="img", key="robot_line", motion="out", cap="BATERÍAS · MOTORES · CHIPS")),

    # --- CAPÍTULO 4 ---
    dict(id="s22", text="Capítulo cuatro. El día que adelantó a Tesla.",
         visual=dict(type="title", num="04", text="EL DÍA QUE ADELANTÓ A TESLA", name="El día que adelantó a Tesla")),
    dict(id="s23", text="En el último trimestre de dos mil veintitrés pasa lo impensable: por primera vez, BYD vende más coches eléctricos que Tesla en un trimestre.",
         visual=dict(type="year", year="T4 2023", sub="BYD SUPERA A TESLA POR PRIMERA VEZ")),
    dict(id="s24", text="En dos mil veinticuatro factura setecientos setenta y siete mil millones de yuanes, unos ciento siete mil millones de dólares. Por primera vez, más que Tesla.",
         visual=dict(type="bars", title="INGRESOS 2024 (MILES DE MILLONES $)", data=[["BYD", 107], ["TESLA", 98]], reveal=2)),
    dict(id="s25", text="Y para vender fuera de China, monta algo que casi ninguna marca de coches tenía: su propia flota de barcos. En enero de dos mil veinticuatro zarpa el primero, con capacidad para unos siete mil coches, rumbo a Europa.",
         visual=dict(type="img", key="car_ship", cap="SU PROPIA FLOTA DE BARCOS")),
    dict(id="s26", text="En abril de dos mil veinticinco, según la consultora JATO, BYD vende en Europa más coches eléctricos que Tesla por primera vez.",
         visual=dict(type="img", key="europe_road", cap="EUROPA · ABRIL 2025")),
    dict(id="s27", text="Y en dos mil veinticinco llega el golpe definitivo: más de dos millones doscientos cincuenta mil eléctricos para BYD, contra un millón seiscientos mil de Tesla. Es el mayor vendedor de coches eléctricos del mundo.",
         visual=dict(type="num", start=0, end=2254714, prefix="", suffix="", label="ELÉCTRICOS VENDIDOS POR BYD EN 2025")),
    dict(id="s28", text="Y Elon Musk, el mismo que se había reído en dos mil once, ya en dos mil veintitrés reconocía que sus coches eran muy competitivos.",
         visual=dict(type="quote", text="\"SUS COCHES SON\nMUY COMPETITIVOS\"\n— ELON MUSK, 2023")),

    # --- CAPÍTULO 5 ---
    dict(id="s29", text="Capítulo cinco. El lado oscuro.",
         visual=dict(type="title", num="05", text="EL LADO OSCURO", name="El lado oscuro")),
    dict(id="s30", text="Pero para llegar ahí, BYD aprieta. En mayo de dos mil veinticinco baja el precio de veintidós modelos, algunos hasta un treinta y cuatro por ciento. Su coche más barato, el Seagull, se queda en unos siete mil setecientos dólares.",
         visual=dict(type="img", key="showroom_price", cap="HASTA -34 %")),
    dict(id="s31", text="La guerra de precios es tan dura que el propio gobierno chino interviene: pide a los fabricantes que no vendan por debajo del coste, y más tarde lo prohíbe.",
         visual=dict(type="quote", text="EL GOBIERNO CHINO:\nPROHIBIDO VENDER\nPOR DEBAJO DEL COSTE")),
    dict(id="s32", text="También pone la lupa en los proveedores, que tardaban demasiado en cobrar. En junio, BYD promete reducir sus plazos de pago a la mitad: sesenta días.",
         visual=dict(type="num", start=120, end=60, prefix="", suffix=" DÍAS", label="PLAZO DE PAGO A PROVEEDORES")),
    dict(id="s33", text="Y en toda la industria china aparece un fenómeno extraño: coches nuevos que se registran como vendidos y acaban en el mercado de segunda mano con cero kilómetros. Los reguladores sospechan que sirven para inflar las cifras de ventas.",
         visual=dict(type="img", key="empty_lot", cap="\"DE SEGUNDA MANO\" CON 0 KM")),
    dict(id="s34", text="En enero de dos mil veinticinco, la firma de análisis GMT Research publica un informe explosivo: calcula que la deuda neta real de BYD, contando lo que debe a sus proveedores, rondaría los trescientos veintitrés mil millones de yuanes, unos cuarenta y cuatro mil millones de dólares. BYD sostiene que sus cuentas siguen las normas contables.",
         visual=dict(type="img", key="boardroom", cap="GMT RESEARCH: 323.000 MILLONES DE YUANES")),
    dict(id="s35", text="Y en diciembre de dos mil veinticuatro, en Brasil, la fiscalía rescata a ciento sesenta y tres trabajadores chinos en la obra de su nueva fábrica, en condiciones que describió como análogas a la esclavitud. Los había contratado una constructora, Jinjiang. BYD rompió el contrato con ella.",
         visual=dict(type="quote", text="BRASIL, DIC. 2024:\n163 TRABAJADORES\nRESCATADOS")),
    dict(id="s36", text="Mientras tanto, Warren Buffett, el inversor que había creído en BYD en dos mil ocho, empieza a vender sus acciones en dos mil veintidós, hasta deshacerse de todas.",
         visual=dict(type="quote", text="BUFFETT\nVENDIÓ\nTODO")),

    # --- CAPÍTULO 6 ---
    dict(id="s37", text="Capítulo seis. ¿Y ahora qué?",
         visual=dict(type="title", num="06", text="¿Y AHORA QUÉ?", name="¿Y ahora qué?")),
    dict(id="s38", text="Dos mil veintiséis empieza mal. En el primer semestre, BYD vende un millón ochocientos mil vehículos, casi un dieciséis por ciento menos que un año antes. En China, sus ventas caen con fuerza.",
         visual=dict(type="bars", title="VEHÍCULOS VENDIDOS EN EL 1er SEMESTRE (MILES)", data=[["2025", 2146], ["2026", 1809]], reveal=2, note="-16 %")),
    dict(id="s39", text="Y su beneficio del semestre baja más de un veinte por ciento.",
         visual=dict(type="num", start=0, end=-20, prefix="", suffix=" %", label="BENEFICIO · 1er SEMESTRE 2026")),
    dict(id="s40", text="Pero fuera de China pasa lo contrario. Sus ventas en el extranjero se disparan, y por primera vez más de la mitad de sus ingresos llegan de fuera: de Europa, del sudeste asiático y de América Latina, donde ya pisa fuerte en México y en Brasil.",
         visual=dict(type="img", key="latam_street", cap="53 % DE SUS INGRESOS, FUERA DE CHINA")),
    dict(id="s41", text="Su objetivo para dos mil veintiséis: vender un millón y medio de coches fuera de China. Wang Chuanfu dice que puede superarlo.",
         visual=dict(type="quote", text="META 2026:\n1,5 MILLONES\nFUERA DE CHINA")),
    dict(id="s42", text="Aunque el mundo le pone frenos: Europa cobra aranceles extra a sus eléctricos fabricados en China, y su fábrica en México quedó en pausa por miedo a la política comercial de Estados Unidos.",
         visual=dict(type="img", key="europe_road", motion="out", cap="ARANCELES EN EUROPA · MÉXICO EN PAUSA")),

    # --- CIERRE ---
    dict(id="s43", text="Entonces, ¿BYD es el nuevo rey del automóvil, o una burbuja inflada por precios imposibles y deudas que no se ven?",
         visual=dict(type="quote", text="¿NUEVO REY\nO BURBUJA?")),
    dict(id="s44", text="Lo que es seguro es esto: una empresa que empezó haciendo baterías para móviles aprendió a fabricar casi todo ella misma, apostó por los eléctricos antes que nadie, y obligó a Tesla a mirar por el retrovisor.",
         visual=dict(type="quote", text="1. BATERÍAS PROPIAS\n2. TODO EN CASA\n3. ELÉCTRICOS ANTES QUE NADIE\n4. PRECIOS IMBATIBLES")),
    dict(id="s45", text="Puede que en dos mil once Musk tuviera razón y aquellos coches no fueran buenos. Lo que no vio venir fue lo rápido que podían mejorar.",
         visual=dict(type="img", key="night_car", motion="out")),
    dict(id="s46", text="¿Comprarías un BYD? Te leo en los comentarios. Y suscríbete, porque la próxima historia ya está en camino.",
         visual=dict(type="quote", text="¿COMPRARÍAS\nUN BYD?")),
]

SHORTS = {
    "a": {"bar": "MUSK SE RIÓ DE ELLOS", "scenes": [
        dict(id="a01", text="En dos mil once, Elon Musk se rió de esta empresa china en plena entrevista.", key="robot_line"),
        dict(id="a02", text="¿Has visto sus coches?, dijo. No la veía como competencia.", key="night_car"),
        dict(id="a03", text="En dos mil veinticinco, BYD vendió más de dos millones doscientos mil coches eléctricos. Tesla, un millón seiscientos mil.", key="car_ship"),
        dict(id="a04", text="Hoy es el mayor vendedor de coches eléctricos del mundo. La historia completa, en mi canal.", key="europe_road"),
    ]},
    "b": {"bar": "DE BATERÍAS DE MÓVIL A TESLA", "scenes": [
        dict(id="b01", text="Esta empresa empezó en mil novecientos noventa y cinco haciendo baterías para teléfonos móviles.", key="battery_lab_1995"),
        dict(id="b02", text="Fabricaba para Nokia y Motorola, con mucha mano de obra y costes bajísimos.", key="phones_90s"),
        dict(id="b03", text="En dos mil tres compró una pequeña fábrica de coches. A sus inversores no les gustó nada.", key="old_car_factory"),
        dict(id="b04", text="Hoy BYD vende más coches eléctricos que Tesla. Cómo lo hizo, en el vídeo de mi canal.", key="robot_line"),
    ]},
    "c": {"bar": "LA PRUEBA DEL CLAVO", "scenes": [
        dict(id="c01", text="Para demostrar que su batería era segura, BYD la atravesó con un clavo.", key="blade_battery"),
        dict(id="c02", text="Según la empresa, no echó humo ni fuego. Una batería convencional, en la misma prueba, superó los quinientos grados y ardió.", key="blade_battery"),
        dict(id="c03", text="Esa batería, la Blade, es una de las claves de cómo BYD superó a Tesla.", key="robot_line"),
        dict(id="c04", text="La historia completa, en mi canal.", key="night_car"),
    ]},
    "d": {"bar": "SU PROPIA FLOTA DE BARCOS", "scenes": [
        dict(id="d01", text="Esta marca de coches tiene su propia flota de barcos.", key="car_ship"),
        dict(id="d02", text="En dos mil veinticuatro, BYD puso a navegar el primero, con capacidad para unos siete mil coches, rumbo a Europa.", key="car_ship"),
        dict(id="d03", text="En abril de dos mil veinticinco, por primera vez, vendió en Europa más eléctricos que Tesla.", key="europe_road"),
        dict(id="d04", text="Y ahora va a por América Latina. La historia completa, en mi canal.", key="latam_street"),
    ]},
    "e": {"bar": "¿NUEVO REY O BURBUJA?", "scenes": [
        dict(id="e01", text="BYD bajó el precio de sus coches hasta un treinta y cuatro por ciento.", key="showroom_price"),
        dict(id="e02", text="La guerra de precios fue tan dura que el gobierno chino tuvo que intervenir.", key="empty_lot"),
        dict(id="e03", text="Y un informe calcula que su deuda real rondaría los cuarenta y cuatro mil millones de dólares. BYD dice que sus cuentas cumplen las normas.", key="boardroom"),
        dict(id="e04", text="¿Nuevo rey o burbuja? Te lo cuento todo en mi canal.", key="night_car"),
    ]},
}

# Escenas de reserva (solo se usan si falta img/<clave>.png, p. ej. si la generación de imágenes está caída)
_Z = dict(zoom=1.5)  # en los Shorts el panel es más pequeño: texto más grande
FALLBACK = {
    "s01": dict(type="year", year="2011", sub="ELON MUSK SE RÍE DE BYD"),
    "s04": dict(type="versus", left=["1995", "BATERÍAS\nDE MÓVIL"], right=["2025", "Nº1 MUNDIAL\nEN ELÉCTRICOS"]),
    "s08": dict(type="versus", title="BATERÍAS RECARGABLES EN LOS AÑOS 90", left=["JAPÓN", "MÁQUINAS\nCARÍSIMAS"],
                right=["BYD", "MANO DE OBRA\nY COSTES BAJOS"], mid="VS", lcol="white", rcol="yellow"),
    "s09": dict(type="quote", text="SUS CLIENTES:\nNOKIA\nMOTOROLA"),
    "s12": dict(type="stamp", text="UNA EMPRESA DE BATERÍAS\nCOMPRA UNA FÁBRICA DE COCHES", stamp="2003"),
    "s16": dict(type="stamp", text="COCHES BARATOS, HÍBRIDOS\nY AUTOBUSES ELÉCTRICOS", stamp="TODO EN CASA"),
    "s18": dict(type="quote", text="BATERÍA BLADE:\nLARGA Y DELGADA\nCOMO UNA CUCHILLA"),
    "s21": dict(type="quote", text="BATERÍAS\nMOTORES\nCHIPS"),
    "s25": dict(type="num", start=0, end=7000, suffix=" COCHES", label="CAPACIDAD APROXIMADA DE SU PRIMER BARCO (2024)"),
    "s26": dict(type="year", year="ABRIL 2025", sub="EN EUROPA, BYD VENDE MÁS ELÉCTRICOS QUE TESLA"),
    "s30": dict(type="num", start=0, end=-34, suffix=" %", label="BAJADA DE PRECIO MÁXIMA · MAYO 2025"),
    "s33": dict(type="stamp", text="COCHES NUEVOS VENDIDOS\nCOMO \"DE SEGUNDA MANO\"", stamp="0 KM"),
    "s34": dict(type="num", start=0, end=323000, label="DEUDA NETA SEGÚN GMT RESEARCH (MILLONES DE YUANES)"),
    "s40": dict(type="versus", left=["CHINA", "VENTAS\nEN CAÍDA"], right=["53 %", "DE SUS INGRESOS,\nFUERA DE CHINA"],
                mid="VS", lcol="red", rcol="yellow"),
    "s42": dict(type="stamp", text="EUROPA: ARANCELES EXTRA\nMÉXICO: FÁBRICA EN PAUSA", stamp="FRENOS"),
    "s45": dict(type="versus", left=["2011", "\"¿HAS VISTO\nSUS COCHES?\""], right=["2025", "EL QUE MÁS\nELÉCTRICOS VENDE"],
                lcol="white", rcol="yellow"),
    # Shorts
    "a01": dict(type="year", year="2011", sub="MUSK SE RÍE DE BYD", **_Z),
    "a02": dict(type="quote", text="\"¿HAS VISTO\nSUS COCHES?\"", **_Z),
    "a03": dict(type="bars", title="ELÉCTRICOS VENDIDOS EN 2025 (MILES)", data=[["BYD", 2255], ["TESLA", 1636]], **_Z),
    "a04": dict(type="stamp", text="EL QUE MÁS COCHES\nELÉCTRICOS VENDE", stamp="Nº1", **_Z),
    "b01": dict(type="year", year="1995", sub="BATERÍAS PARA MÓVILES", **_Z),
    "b02": dict(type="quote", text="CLIENTES:\nNOKIA\nMOTOROLA", **_Z),
    "b03": dict(type="stamp", text="COMPRA UNA FÁBRICA\nDE COCHES", stamp="2003", **_Z),
    "b04": dict(type="versus", left=["1995", "BATERÍAS\nDE MÓVIL"], right=["2025", "MÁS ELÉCTRICOS\nQUE TESLA"], zoom=1.8),
    "c01": dict(type="quote", text="LA ATRAVESÓ\nCON UN CLAVO", **_Z),
    "c02": dict(type="bars", title="TEMPERATURA EN LA PRUEBA (°C)", data=[["BLADE", 60], ["CONVENCIONAL", 500]], **_Z),
    "c03": dict(type="quote", text="BATERÍA BLADE:\nLA CLAVE PARA\nSUPERAR A TESLA", **_Z),
    "c04": dict(type="quote", text="LA HISTORIA\nCOMPLETA,\nEN MI CANAL", **_Z),
    "d01": dict(type="stamp", text="UNA MARCA DE COCHES\nCON FLOTA PROPIA DE", stamp="BARCOS", **_Z),
    "d02": dict(type="num", start=0, end=7000, suffix=" COCHES", label="POR BARCO · RUMBO A EUROPA", **_Z),
    "d03": dict(type="year", year="ABRIL 2025", sub="EN EUROPA SUPERA A TESLA", **_Z),
    "d04": dict(type="quote", text="PRÓXIMA PARADA:\nAMÉRICA LATINA", **_Z),
    "e01": dict(type="num", start=0, end=-34, suffix=" %", label="BAJADA DE PRECIOS", **_Z),
    "e02": dict(type="quote", text="TAN DURA QUE\nINTERVINO EL\nGOBIERNO CHINO", **_Z),
    "e03": dict(type="num", start=0, end=44, suffix=" MIL MILL. $", label="DEUDA REAL SEGÚN GMT RESEARCH", **_Z),
    "e04": dict(type="quote", text="¿NUEVO REY\nO BURBUJA?", **_Z),
}

THUMBS = [
    dict(img="thumb_vs", zoom=1.05, cx=0.5, bright=1.0, items=[
        ["text", 640, 30, "BYD", 230, "red", "mt"], ["text", 640, 300, "VS", 120, "white", "mt"], ["text", 640, 440, "TESLA", 200, "white", "mt"]]),
    dict(img="thumb_car", zoom=1.05, cx=0.65, shade=["left", 230, 0.6], items=[
        ["text", 50, 70, "MUSK SE", 160, "white", "la"], ["text", 50, 250, "RIÓ DE", 160, "white", "la"], ["text", 50, 430, "ELLOS", 190, "red", "la"]]),
    dict(img="thumb_car", zoom=1.1, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 50, 80, "DE BATERÍAS", 125, "white", "la"], ["text", 50, 230, "DE MÓVIL", 125, "white", "la"], ["text", 50, 390, "A SUPERAR", 125, "yellow", "la"], ["text", 50, 530, "A TESLA", 125, "red", "la"]]),
    dict(img="car_ship", zoom=1.05, cx=0.5, shade=["left", 200, 0.7], items=[
        ["text", 50, 70, "2.250.000", 180, "red", "la"], ["text", 50, 300, "VS", 110, "white", "la"], ["text", 50, 430, "1.640.000", 180, "white", "la"]]),
    dict(img="thumb_vs", zoom=1.15, cx=0.5, items=[
        ["text", 640, 40, "¿CÓMO BYD", 150, "white", "mt"], ["text", 640, 230, "DESTRONÓ", 150, "yellow", "mt"], ["text", 640, 420, "A TESLA?", 170, "red", "mt"]]),
    dict(img="showroom_price", zoom=1.05, cx=0.5, shade=["left", 200, 0.7], items=[
        ["text", 50, 80, "¿REY O", 200, "white", "la"], ["text", 50, 320, "BURBUJA?", 210, "red", "la"]]),
    dict(img="thumb_car", zoom=1.0, cx=0.5, bright=0.9, items=[
        ["text", 640, 30, "EL NUEVO REY", 150, "yellow", "mt"], ["stamp", "BYD", 640, 500, -8, 170]]),
    dict(img="blade_battery", zoom=1.05, cx=0.6, shade=["left", 220, 0.65], items=[
        ["text", 50, 70, "LA BATERÍA", 150, "white", "la"], ["text", 50, 250, "QUE HUNDIÓ", 150, "yellow", "la"], ["text", 50, 430, "A TESLA", 170, "red", "la"]]),
    dict(img="europe_road", zoom=1.05, cx=0.5, shade=["right", 220, 0.6], items=[
        ["text", 1230, 90, "TESLA", 170, "white", "ra"], ["text", 1230, 290, "YA NO ES", 140, "white", "ra"], ["text", 1230, 460, "EL Nº1", 180, "red", "ra"]]),
    dict(img="thumb_car", zoom=1.1, cx=0.6, shade=["left", 230, 0.6], items=[
        ["text", 50, 90, "-34 %", 260, "red", "la"], ["text", 50, 400, "GUERRA DE PRECIOS", 90, "white", "la"], ["badge", 50, 540, 330, 670, "BYD", 110]]),
]
THUMBS_TOP = [2, 1, 5]

META = {
    "code": "003",
    "name": "BYD",
    "intro_chapter": "Intro: Musk se rió de BYD",
    "titles": [
        "Elon Musk se RIÓ de BYD. Hoy vende más eléctricos que Tesla",
        "BYD: de baterías de móvil a superar a TESLA",
        "Cómo BYD destronó a Tesla (y las dudas que lo persiguen)",
    ],
    "description": "En 2011, Elon Musk se rió cuando le preguntaron por BYD. En 2025, BYD vendió más de 2,25 millones de coches 100 % eléctricos y superó a Tesla como el mayor vendedor del mundo. Esta es la historia del químico que fabricaba baterías para móviles y construyó un gigante del automóvil… y de las dudas que lo persiguen: la guerra de precios, los proveedores y su deuda.",
    "sources": [
        "CNBC / InsideEVs / SCMP: entrevista de Elon Musk en Bloomberg (2011) y su respuesta de 2023",
        "Electrek / CnEVPost: ventas de eléctricos de BYD y Tesla en 2025",
        "Fortune (vía Validea), Wikipedia: fundación de BYD, compra de Qinchuan (2003) e inversión de Berkshire (2008)",
        "BYD / ChargedEVs: presentación de la batería Blade y prueba del clavo (2020)",
        "AP / BNN Bloomberg: ingresos de BYD en 2024 frente a Tesla",
        "CnEVPost / Bloomberg: primer barco de transporte de BYD (enero 2024)",
        "JATO Dynamics (vía Silicon): ventas en Europa, abril 2025",
        "Fortune / CleanTechnica / CarNewsChina: guerra de precios, plazos a proveedores y coches de 0 km (2025)",
        "Bloomberg / TipRanks: informe de GMT Research sobre la deuda de BYD (enero 2025)",
        "AP / Euronews: trabajadores rescatados en la obra de Camaçari, Brasil (diciembre 2024)",
        "CnEVPost / Automotive World: resultados del primer semestre de 2026",
    ],
    "hashtags": "#BYD #Tesla #CochesEléctricos #Negocios #China",
    "tags": ["byd", "byd vs tesla", "tesla", "coches eléctricos", "autos eléctricos", "elon musk byd", "historia de byd",
             "byd méxico", "byd brasil", "batería blade", "guerra de precios", "china", "historia de empresas", "el último balance"],
    "pinned": "¿Comprarías un BYD o te quedas con Tesla? 👇 Y dime qué marca quieres que analicemos en el próximo vídeo.",
    "playlist": "Auges y gigantes",
    "shorts": {
        "a": {"title": "Elon Musk se rió de esta empresa… y le quitó el trono",
              "description": "La historia completa de BYD está en el canal. #BYD #Tesla #ElonMusk #shorts",
              "tags": ["byd", "tesla", "elon musk", "coches eléctricos", "shorts"]},
        "b": {"title": "Empezó haciendo baterías de móvil… hoy supera a Tesla",
              "description": "Cómo lo hizo BYD: vídeo completo en el canal. #BYD #negocios #shorts",
              "tags": ["byd", "baterías", "historia de empresas", "tesla", "shorts"]},
        "c": {"title": "Atravesaron su batería con un clavo… y no ardió",
              "description": "La batería Blade de BYD. Historia completa en el canal. #BYD #batería #shorts",
              "tags": ["byd", "batería blade", "coches eléctricos", "ciencia", "shorts"]},
        "d": {"title": "Esta marca de coches tiene su propia flota de barcos",
              "description": "Así conquista BYD el mundo. Vídeo completo en el canal. #BYD #barcos #shorts",
              "tags": ["byd", "barcos", "exportación", "coches eléctricos", "shorts"]},
        "e": {"title": "BYD: ¿nuevo rey de los coches o burbuja?",
              "description": "Guerra de precios y dudas sobre su deuda. Historia completa en el canal. #BYD #shorts",
              "tags": ["byd", "guerra de precios", "deuda", "china", "shorts"]},
    },
}
