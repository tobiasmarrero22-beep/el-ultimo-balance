# Guion vídeo 001 — La caída de iRobot (Roomba)
# Cada escena: id, texto narrado (pensado para TTS), visual.
# Tipos de visual:
#   img: imagen IA con movimiento (key de IMAGES), "cap" = texto en pantalla opcional
#   title: tarjeta de capítulo
#   num: número grande animado (from -> to), con etiqueta
#   year: sello de fecha
#   bars: gráfico de barras animado
#   quote: frase grande en pantalla

TITLE = "La CAÍDA de Roomba: de valer 1.700 millones a valer CERO"

IMAGES = {
    "roomba_dark": "A single round robot vacuum cleaner sitting alone on a dark hardwood living room floor at night, one dramatic overhead spotlight, dust particles in the air, cinematic documentary still, shallow depth of field, muted teal and orange color grade, no text, no logos",
    "roomba_broken": "A round robot vacuum cleaner cracked in half lying on a cold concrete floor, scattered plastic pieces, moody low-key lighting, cinematic documentary still, muted teal and orange color grade, no text, no logos",
    "mit_lab": "A cluttered university robotics laboratory in 1990, three young researchers seen from behind working at a bench full of circuit boards, cables and small six-legged insect-like robots, warm tungsten light, retro film grain, cinematic, no text, no logos",
    "insect_robot": "Macro photo of a small six-legged insect-like walking robot made of aluminum and circuit boards on a laboratory table, 1990s technology, warm light, film grain, cinematic, no text, no logos",
    "packbot_cave": "A small tracked military ground robot with an articulated arm and camera driving into a dusty cave entrance in a desert mountain, soldier silhouette far in the background, cinematic war documentary still, muted colors, no text, no logos",
    "rubble_robot": "A small tracked rescue robot with headlights climbing over the rubble of a collapsed concrete building, dust in the air, emergency lights in the distance, cinematic documentary still, muted colors, no text, no logos",
    "nuclear_robot": "A small tracked robot with camera arm moving through a dim industrial nuclear power plant corridor, yellow radiation hazard signs, flashing warning lights, steam, cinematic documentary still, no readable text, no logos",
    "family_2002": "A round robot vacuum cleaning a beige carpet in an early 2000s living room with a boxy CRT television in the background, warm nostalgic film photo, cinematic, no text, no logos",
    "cat_roomba": "A fluffy orange cat sitting on top of a round robot vacuum cleaner on a kitchen floor, warm cinematic light, no text, no logos",
    "shenzhen_factory": "Long assembly line in a huge modern electronics factory producing round robot vacuum cleaners, cool blue industrial light, cinematic wide shot, no readable text, no logos",
    "lidar_map": "A robot vacuum on a floor emitting glowing blue laser scan lines that draw a precise holographic floor plan map of the apartment around it, futuristic, dark room, cinematic, no text, no logos",
    "smart_home": "Isometric cutaway view of a modern two-story house at night with glowing rooms, a small robot vacuum on the floor and a glowing smart speaker on a shelf, cinematic, no text, no logos",
    "eu_building": "A modern glass government building with many blue flags with a circle of yellow stars waving in front of it, grey overcast sky, serious mood, cinematic documentary still, no readable text",
    "empty_office": "An empty corporate open-plan office after mass layoffs, cardboard boxes on desks, chairs pushed away, grey cold morning light, cinematic documentary still, no readable text, no logos",
    "unsold_boxes": "A dim warehouse with tall stacks of unsold robot vacuum cleaner boxes covered in dust, single light beam, cinematic documentary still, no readable text, no logos",
    "gavel": "A wooden gavel lying on a stack of paper documents on a dark desk, dramatic side light, cinematic still, no readable text, no logos",
}

SCENES = [
    # --- GANCHO (0-30 s) ---
    dict(id="s01", text="En 2022, Amazon quiso pagar mil setecientos millones de dólares por la empresa que inventó este robot.",
         visual=dict(type="img", key="roomba_dark", cap="AMAZON: 1.700 MILLONES $")),
    dict(id="s02", text="Tres años después, sus accionistas se quedaron con cero. Ni un centavo.",
         visual=dict(type="num", start=1700, end=0, prefix="$", suffix=" M", label="VALOR PARA SUS ACCIONISTAS")),
    dict(id="s03", text="Esta es la historia de iRobot, la empresa que metió el primer robot en millones de casas, y que terminó en manos de la fábrica china que se los construía.",
         visual=dict(type="img", key="roomba_broken")),
    dict(id="s04", text="Y no la mató un solo error. La mataron cuatro. El último llegó desde Bruselas.",
         visual=dict(type="quote", text="4 ERRORES.\nUNO LLEGÓ DESDE BRUSELAS.")),

    # --- CAPÍTULO 1 ---
    dict(id="s05", text="Capítulo uno. Robots para ir a la guerra.",
         visual=dict(type="title", num="01", text="ROBOTS PARA IR A LA GUERRA")),
    dict(id="s06", text="Mil novecientos noventa. Laboratorio de Inteligencia Artificial del MIT. Tres investigadores, Rodney Brooks, Colin Angle y Helen Greiner, fundan una pequeña empresa con una idea que entonces sonaba a ciencia ficción: robots que sirvan para algo de verdad.",
         visual=dict(type="img", key="mit_lab", cap="1990 · MIT")),
    dict(id="s07", text="Al principio construyen lo que paga las facturas: robots experimentales para laboratorios, universidades y el ejército de Estados Unidos.",
         visual=dict(type="img", key="mit_lab", motion="out")),
    dict(id="s08", text="En mil novecientos noventa y ocho llega el contrato que lo cambia todo. DARPA, la agencia de investigación del Pentágono, financia un robot militar. Se llamará PackBot.",
         visual=dict(type="year", year="1998", sub="CONTRATO CON DARPA → PACKBOT")),
    dict(id="s09", text="PackBot es un pequeño tanque con un brazo, que entra donde un soldado no debería entrar: cuevas, edificios a punto de caerse, artefactos explosivos.",
         visual=dict(type="img", key="packbot_cave", cap="PACKBOT")),
    dict(id="s10", text="Tras los atentados del once de septiembre, robots PackBot buscaron entre los escombros del World Trade Center. Y en dos mil once entraron en la central nuclear de Fukushima, donde ningún humano podía entrar.",
         visual=dict(type="img", key="nuclear_robot", cap="2011 · FUKUSHIMA")),
    dict(id="s11", text="iRobot se había ganado una reputación: si había que mandar un robot a un sitio imposible, se lo pedías a ellos.",
         visual=dict(type="img", key="rubble_robot")),
    dict(id="s12", text="Pero los contratos militares tienen un problema. Dependes de un solo cliente. Y ese cliente es el gobierno.",
         visual=dict(type="quote", text="UN SOLO CLIENTE:\nEL GOBIERNO")),

    # --- CAPÍTULO 2 ---
    dict(id="s13", text="Capítulo dos. El robot que barría.",
         visual=dict(type="title", num="02", text="EL ROBOT QUE BARRÍA")),
    dict(id="s14", text="Así que en septiembre de dos mil dos hacen una apuesta rarísima para una empresa de robots de guerra: un disco que aspira el suelo él solo. Lo llaman Roomba.",
         visual=dict(type="year", year="2002", sub="NACE ROOMBA")),
    dict(id="s15", text="Cuesta unos doscientos dólares. Nada de pantallas, nada de aplicaciones. Pulsas un botón, y el robot se pone a recorrer tu casa.",
         visual=dict(type="num", start=0, end=200, prefix="$", suffix="", label="PRECIO DEL PRIMER ROOMBA")),
    dict(id="s16", text="La idea venía de lo que habían aprendido con sus robots insecto: no hace falta un cerebro perfecto. Basta con reaccionar rápido a cada choque.",
         visual=dict(type="img", key="insect_robot", cap="ROBOTS INSECTO → ROOMBA")),
    dict(id="s17", text="El éxito los pilla por sorpresa. En dos mil cuatro ya han vendido un millón de Roombas.",
         visual=dict(type="num", start=0, end=1000000, prefix="", suffix="", label="ROOMBAS VENDIDOS EN 2004")),
    dict(id="s18", text="Y entonces pasa algo que ningún departamento de marketing puede comprar: internet se enamora del robot. Gatos montados en Roombas, perros persiguiéndolos, gente que les pone nombre.",
         visual=dict(type="quote", text="GATOS MONTADOS EN ROOMBAS.\nPERROS PERSIGUIÉNDOLOS.\nROBOTS CON NOMBRE.")),
    dict(id="s19", text="Roomba deja de ser una marca y se convierte en una palabra. Mucha gente empieza a llamar roomba a cualquier robot aspirador.",
         visual=dict(type="quote", text="\"ROOMBA\"\nYA NO ERA UNA MARCA.\nERA UNA PALABRA.")),
    dict(id="s20", text="Con los años, iRobot vende más de cuarenta millones de robots en todo el mundo. Y en dos mil dieciséis toma una decisión que parece lógica: vende su división militar y se queda solo con los robots de casa.",
         visual=dict(type="year", year="2016", sub="VENDE LA DIVISIÓN MILITAR")),
    dict(id="s21", text="A partir de ese momento, todo su futuro depende de una sola cosa: que la gente siga comprando Roombas.",
         visual=dict(type="quote", text="ERROR Nº 1:\nTODO A UN SOLO PRODUCTO")),

    # --- CAPÍTULO 3 ---
    dict(id="s22", text="Capítulo tres. El ataque desde China.",
         visual=dict(type="title", num="03", text="EL ATAQUE DESDE CHINA")),
    dict(id="s23", text="Mientras tanto, en China, decenas de fabricantes miran el Roomba y piensan: esto lo podemos hacer nosotros. Más barato. Y mejor.",
         visual=dict(type="quote", text="CHINA:\nMÁS BARATO.\nY MEJOR.")),
    dict(id="s24", text="Marcas como Roborock, Ecovacs o Dreame sacan robots con navegación láser, que dibujan un mapa exacto de tu casa, y que además friegan. A menudo, por menos dinero.",
         visual=dict(type="img", key="lidar_map", cap="ROBOROCK · ECOVACS · DREAME")),
    dict(id="s25", text="Y iRobot comete el error de manual: confiar en su nombre. Durante años sigue apostando por su propio sistema de navegación con cámara, mientras sus rivales usan láser. No incorpora el láser a su gama hasta dos mil veinticinco.",
         visual=dict(type="quote", text="ERROR Nº 2:\nCREER QUE NADIE\nPODÍA ALCANZARLOS")),
    dict(id="s26", text="Los números cuentan la historia. En dos mil veintiuno, iRobot factura mil quinientos sesenta y cinco millones de dólares. Su récord.",
         visual=dict(type="bars", title="VENTAS DE iROBOT (MILLONES $)", data=[["2021", 1565]], reveal=1)),
    dict(id="s27", text="En dos mil veintidós baja a mil ciento ochenta y tres. En dos mil veintitrés, a ochocientos noventa. Y en dos mil veinticuatro, a seiscientos ochenta y uno. En tres años pierde más de la mitad de sus ventas.",
         visual=dict(type="bars", title="VENTAS DE iROBOT (MILLONES $)", data=[["2021", 1565], ["2022", 1183], ["2023", 891], ["2024", 682]], reveal=4, note="-57 %")),
    dict(id="s28", text="La pandemia había disparado las compras para el hogar. Cuando pasó, el golpe fue doble: menos clientes, y los que quedaban se iban a la competencia.",
         visual=dict(type="img", key="unsold_boxes")),

    # --- CAPÍTULO 4 ---
    dict(id="s29", text="Capítulo cuatro. El salvavidas de Amazon.",
         visual=dict(type="title", num="04", text="EL SALVAVIDAS DE AMAZON")),
    dict(id="s30", text="Agosto de dos mil veintidós. Cuando todo empieza a torcerse, aparece el comprador perfecto: Amazon. Ofrece sesenta y un dólares por acción. Unos mil setecientos millones en total.",
         visual=dict(type="num", start=0, end=1700, prefix="$", suffix=" M", label="OFERTA DE AMAZON · AGOSTO 2022")),
    dict(id="s31", text="Para Amazon tenía sentido: Alexa, cámaras, timbres inteligentes, y ahora un robot que recorre tu casa cada día. Los críticos lo vieron enseguida: Amazon tendría el mapa de millones de hogares.",
         visual=dict(type="img", key="lidar_map", cap="EL MAPA DE TU CASA", motion="out")),
    dict(id="s32", text="Pero a los reguladores les preocupaba otra cosa. La Comisión Europea temía que Amazon, que también es la tienda donde se venden los robots de la competencia, pudiera hundirlos en su web para favorecer a Roomba.",
         visual=dict(type="quote", text="COMISIÓN EUROPEA:\n¿AMAZON HUNDIRÍA\nA LA COMPETENCIA?")),
    dict(id="s33", text="La investigación se alarga. Meses. Más de un año. Y una empresa que pierde dinero cada trimestre no puede permitirse esperar.",
         visual=dict(type="quote", text="ERROR Nº 3:\nAPOSTARLO TODO\nA QUE AMAZON LA SALVARÍA")),
    dict(id="s34", text="En julio de dos mil veintitrés, iRobot pide un préstamo de doscientos millones de dólares al fondo Carlyle para aguantar. Un préstamo carísimo. Y como ahora tiene más deuda, Amazon baja su oferta: de sesenta y un dólares por acción a cincuenta y uno setenta y cinco. Unos mil cuatrocientos millones.",
         visual=dict(type="num", start=1700, end=1400, prefix="$", suffix=" M", label="NUEVA OFERTA · JULIO 2023")),
    dict(id="s35", text="iRobot ya no negociaba. Solo esperaba.",
         visual=dict(type="quote", text="YA NO NEGOCIABA.\nSOLO ESPERABA.")),

    # --- CAPÍTULO 5 ---
    dict(id="s36", text="Capítulo cinco. Bruselas dice no.",
         visual=dict(type="title", num="05", text="BRUSELAS DICE NO")),
    dict(id="s37", text="Veintinueve de enero de dos mil veinticuatro. Amazon e iRobot anuncian que cancelan el acuerdo. El motivo: no había forma de conseguir la aprobación de la Unión Europea.",
         visual=dict(type="year", year="29·01·2024", sub="SE CANCELA LA COMPRA")),
    dict(id="s38", text="Amazon paga una indemnización de noventa y cuatro millones de dólares. Parece mucho. No lo es: buena parte se va directa a devolver el préstamo.",
         visual=dict(type="num", start=0, end=94, prefix="$", suffix=" M", label="INDEMNIZACIÓN DE AMAZON")),
    dict(id="s39", text="Ese mismo día, iRobot despide a unas trescientas cincuenta personas, el treinta y uno por ciento de la plantilla. Y Colin Angle, el cofundador que la había dirigido durante décadas, deja el cargo.",
         visual=dict(type="img", key="empty_office", cap="-31 % DE LA PLANTILLA")),
    dict(id="s40", text="La empresa ahora tenía que sobrevivir sin el dinero de Amazon, con una deuda cara, y con competidores más baratos que mejoraban cada año.",
         visual=dict(type="quote", text="SIN AMAZON.\nCON DEUDA.\nY SIN VENTAJA.")),

    # --- CAPÍTULO 6 ---
    dict(id="s41", text="Capítulo seis. Cero.",
         visual=dict(type="title", num="06", text="CERO")),
    dict(id="s42", text="Marzo de dos mil veinticinco. iRobot publica sus resultados y escribe la frase que ninguna empresa quiere escribir: hay dudas sustanciales sobre su capacidad para seguir funcionando. La acción se desploma un treinta y cinco por ciento en un día.",
         visual=dict(type="num", start=0, end=-35, prefix="", suffix=" %", label="LA ACCIÓN, EN UN SOLO DÍA")),
    dict(id="s43", text="En el último trimestre de dos mil veinticuatro vendió ciento setenta y dos millones de dólares. Un año antes, había vendido trescientos siete.",
         visual=dict(type="bars", title="VENTAS 4º TRIMESTRE (MILLONES $)", data=[["T4 2023", 307], ["T4 2024", 172]], reveal=2)),
    dict(id="s44", text="Durante dos mil veinticinco lanza nuevos modelos, ahora sí con láser, para pelear con Roborock y Ecovacs. Pero llega tarde.",
         visual=dict(type="img", key="unsold_boxes", motion="out")),
    dict(id="s45", text="Y aquí viene el giro final. ¿Quién fabricaba los Roomba? Una empresa china: Shenzhen Picea Robotics. Su principal fabricante.",
         visual=dict(type="quote", text="¿QUIÉN FABRICABA\nLOS ROOMBA?\n→ PICEA ROBOTICS")),
    dict(id="s46", text="En noviembre de dos mil veinticinco, una filial de Picea compra la deuda de iRobot. Su fabricante pasaba a ser también su acreedor.",
         visual=dict(type="quote", text="SU FABRICANTE\nAHORA TAMBIÉN ERA\nSU ACREEDOR")),
    dict(id="s47", text="El catorce de diciembre de dos mil veinticinco, iRobot se declara en quiebra en Estados Unidos, con un acuerdo ya cerrado: Picea se queda con el cien por cien de la empresa.",
         visual=dict(type="year", year="14·12·2025", sub="iROBOT SE DECLARA EN QUIEBRA")),
    dict(id="s48", text="¿Y los accionistas? Los mismos a los que en dos mil veintidós les ofrecían sesenta y un dólares por acción. Se quedan con cero.",
         visual=dict(type="num", start=61, end=0, prefix="$", suffix="", label="POR ACCIÓN")),

    # --- CIERRE ---
    dict(id="s49", text="Entonces, ¿quién mató a Roomba?",
         visual=dict(type="quote", text="¿QUIÉN MATÓ\nA ROOMBA?")),
    dict(id="s50", text="No hubo un solo culpable. Fue depender de un solo producto. Fue creer que nadie podía alcanzarlos. Fue apostarlo todo a que Amazon los rescataría. Y fue un regulador que dijo no, cuando ya no quedaba plan B.",
         visual=dict(type="quote", text="1. UN SOLO PRODUCTO\n2. EXCESO DE CONFIANZA\n3. TODO A AMAZON\n4. BRUSELAS DICE NO")),
    dict(id="s51", text="La empresa que inventó el robot de casa acabó siendo propiedad de la fábrica que se los construía. Roomba sigue existiendo. Pero ya no es aquella empresa nacida en el MIT.",
         visual=dict(type="img", key="roomba_dark")),
    dict(id="s52", text="Si quieres que analicemos otra marca que está cometiendo ahora mismo los mismos errores, dímelo en los comentarios. Y suscríbete, porque la próxima historia ya está en camino.",
         visual=dict(type="quote", text="¿QUÉ MARCA\nANALIZAMOS AHORA?")),
]

# --- SHORT (vertical, ~50 s) ---
SHORT = [
    dict(id="h01", text="Amazon iba a pagar mil setecientos millones de dólares por la empresa de Roomba.", key="roomba_dark"),
    dict(id="h02", text="Hoy sus accionistas tienen cero. ¿Qué pasó?", key="roomba_broken"),
    dict(id="h03", text="iRobot nació en el MIT haciendo robots militares. En dos mil dos lanzó Roomba y se volvió un fenómeno.", key="packbot_cave"),
    dict(id="h04", text="Pero se lo jugó todo a un solo producto, y las marcas chinas sacaron robots más baratos y con mejor tecnología.", key="lidar_map"),
    dict(id="h05", text="Sus ventas cayeron más de la mitad en tres años. Su salvación era Amazon.", key="unsold_boxes"),
    dict(id="h06", text="Pero la Unión Europea no lo aprobó, y en enero de dos mil veinticuatro la compra se canceló.", key="empty_office"),
    dict(id="h07", text="Al final, iRobot quebró, y se la quedó la fábrica china que construía sus robots.", key="roomba_broken"),
    dict(id="h08", text="La historia completa, en el vídeo de mi canal.", key="roomba_dark"),
]
