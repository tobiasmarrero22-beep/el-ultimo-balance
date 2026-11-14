# 70x7 · Vídeo 004 — Todo el mapa de GTA 6 explicado: las 6 regiones de Leonida (guion del 14-nov-2026)
# Tema por datos (API de YouTube, 6–14 nov): "GTA 6: Full MAP GUIDE (Watch Before Launch Day)" 4,43 M (RoddyGames, EN);
# "GTA 6 - GUÍA DEFINITIVA DEL MAPA" 341 k (jumaboi, ES, 13-nov). Sigue al 70x7-001 (solo Vice City). Elegido por el usuario.
# Voz: Adán. Sin Shorts. Visual: mapa de Leonida dibujado por código (escena «leonida») + fotos reales de los lugares de Florida
# que inspiran cada región (Wikimedia Commons, pendiente del OK del usuario) + imágenes del 003.
#
# Hechos verificados (WebSearch, 14-nov-2026; textos de Rockstar citados por la prensa):
# - GTA 6 sale el 19-nov-2026 en PS5 y Xbox Series X|S. Leonida, estado ficticio inspirado en Florida, con seis regiones
#   (Game Informer, 6-may-2025, y la web oficial): Vice City, Leonida Keys, Grassrivers, Port Gellhorn, Ambrosia y Mount Kalaga.
# - Vice City: metrópolis costera densa (vida nocturna, compras, playas, entretenimiento y negocios del puerto). Inspirada en Miami.
# - Leonida Keys: islas tropicales (viajes por agua, pueblos pequeños, aguas peligrosas). Jason, exmilitar, trabaja para
#   narcotraficantes locales en los Cayos (web de Rockstar, vía GamesRadar). Lucía acaba de salir de la Penitenciaría de Leonida.
# - Grassrivers: humedales de manglares inspirados en los Everglades. Rockstar: los caimanes quizá sean la atracción más famosa,
#   pero entre los manglares hay depredadores mucho más letales y descubrimientos más raros (Beebom / TheGamesWiki).
# - Port Gellhorn: «la costa olvidada de Leonida», un antiguo destino de vacaciones en decadencia: moteles baratos, atracciones
#   cerradas, centros comerciales vacíos (prensa). Inspiración probable (comunidad): Panama City, costa del Golfo.
# - Ambrosia: zona industrial alrededor de la refinería de azúcar Allied Crystal, junto al lago Leonida; según Rockstar, la refinería
#   da los empleos y la banda de moteros The Final Chapter, «casi todo lo demás» (PC Gamer). Inspiración (comunidad): el cinturón
#   azucarero del lago Okeechobee (Clewiston).
# - Mount Kalaga: parque nacional en el límite norte; caza, pesca y caminos todoterreno; en los bosques viven «místicos montañeses y
#   radicales paranoicos» (PC Gamer, citando a Rockstar).
# - Tamaño: Rockstar no publicó una cifra en kilómetros; las estimaciones de fans van de algo menos del doble a más del doble de GTA 5.
VOICE = "i4Kar2uamCWyas8TAu31"  # Adán (voz de 70x7 desde el 002)
SPEED = 1.0
THEME = {"RED": (255, 56, 150), "YEL": (80, 230, 235)}  # rosa y celeste Vice City

def I(key, cap=None, pop=None, **kw):
    d = dict(type="img", key=key)
    if cap: d["cap"] = cap
    if pop: d["pop"] = pop
    d.update(kw); return d

def M(hl=None, sub=None, all_=False):
    """Mapa de Leonida dibujado por código; hl = región resaltada."""
    d = dict(type="leonida")
    if hl: d["hl"] = hl
    if sub: d["sub"] = sub
    if all_: d["all"] = True
    return d

# Fotos reales (Wikimedia Commons, solo dominio público / CC0 / CC BY, con crédito) de los lugares de Florida que inspiran cada región
COMMONS = {
    "miami_beach": "Miami Beach Ocean Drive Art Deco",
    "keys_bridge": "Seven Mile Bridge Florida Keys aerial",
    "keys_island": "Florida Keys island mangrove aerial",
    "everglades": "Everglades National Park sawgrass",
    "airboat": "Everglades airboat",
    "alligator": "American alligator Everglades",
    "gulf_motel": "Panama City Beach motel",
    "sugar_mill": "Clewiston sugar mill",
    "okeechobee": "Lake Okeechobee",
    "forest_north": "Ocala National Forest",
    "canyon": "Providence Canyon State Park",
}

SCENES = [
    # --- GANCHO ---
    dict(id="s01", text="El diecinueve vas a prender GTA seis y casi todos van a hacer lo mismo: ir directo a Vice City. Y se van a perder la mitad del juego.",
         visual=I("highway_neon", pop=["NO VAYAS DIRECTO"])),
    dict(id="s02", text="Porque Leonida, el estado donde transcurre GTA seis, tiene seis regiones. Y en una de ellas, según Rockstar, los caimanes son lo menos peligroso que te vas a cruzar.",
         visual=M(all_=True, sub="6 REGIONES"), abre="P1: ¿Qué hay en la región donde los caimanes son lo menos peligroso?"),
    dict(id="s03", text="Te llevo región por región, con lo que confirmó Rockstar y con los lugares reales de Florida en los que se inspira cada una.",
         visual=dict(type="timeline", title="EL RECORRIDO", points=[["1", "Vice City"], ["2", "Los Cayos"], ["3", "Grassrivers"], ["4", "Port Gellhorn"], ["5", "Ambrosia"], ["6", "Mount Kalaga"]], hl=0)),
    dict(id="s04", text="Y al final te digo por dónde conviene arrancar a explorar el primer día. Spoiler: no es Vice City.",
         visual=I("controller", pop=["¿POR DÓNDE ARRANCAR?"]), abre="P2: ¿Por qué región conviene arrancar a explorar el día uno?"),

    # --- 01 LEONIDA ---
    dict(id="s05", text="Capítulo uno. Leonida.", bloque="desarrollo",
         visual=dict(type="title", num="01", text="LEONIDA", name="Leonida, el estado")),
    dict(id="s06", text="Leonida es la versión de Florida que inventó Rockstar. Un estado entero, con ciudad, islas, pantanos, playas olvidadas, fábricas y montañas.",
         visual=M(all_=True)),
    dict(id="s07", text="Rockstar confirmó las seis regiones en mayo de dos mil veinticinco, con el segundo tráiler: Vice City, los Cayos de Leonida, Grassrivers, Port Gellhorn, Ambrosia y el Parque Nacional Mount Kalaga.",
         visual=dict(type="quote", text="VICE CITY · LEONIDA KEYS · GRASSRIVERS\nPORT GELLHORN · AMBROSIA · MOUNT KALAGA")),
    dict(id="s07b", text="Y es un regreso con historia: la saga no volvía a Vice City desde Vice City Stories, en dos mil seis.",
         visual=dict(type="year", year="2006", sub="ÚLTIMA VEZ EN VICE CITY")),
    dict(id="s08", text="¿Qué tan grande es? Rockstar no dio una cifra en kilómetros. Los fans que midieron los tráileres calculan que ronda el doble del mapa de GTA cinco, aunque las estimaciones varían bastante.",
         visual=dict(type="bars", title="TAMAÑO DEL MAPA (ESTIMACIÓN DE FANS, GTA 5 = 1)", data=[["GTA 5", 1], ["GTA 6 (ESTIMADO)", 2]], suffix="x")),
    dict(id="s09", text="Y lo vas a recorrer con dos protagonistas: Jason y Lucía. Ya vas a ver que cada uno tiene su propia región en esta historia.",
         visual=dict(type="versus", title="LOS PROTAGONISTAS", left=["JASON", "EXMILITAR"], right=["LUCÍA", "RECIÉN SALIDA DE PRISIÓN"], mid="&", lcol="yellow", rcol="red")),
    dict(id="s10", text="Pero hay una región a la que Rockstar describe con dos palabras que dan un poco de miedo: la costa olvidada. ¿Cuál es? Ya vamos a llegar.",
         visual=M(sub="LA COSTA OLVIDADA"), abre="P3: ¿Cuál es la región que Rockstar llama «la costa olvidada»?"),

    # --- 02 VICE CITY ---
    dict(id="s11", text="Capítulo dos. Vice City.",
         visual=dict(type="title", num="02", text="VICE CITY", name="Vice City")),
    dict(id="s12", text="Vice City es la gran ciudad de Leonida. Rockstar la presenta como una metrópolis costera densa: vida nocturna, compras, playas, entretenimiento y los negocios del puerto.",
         visual=M(hl="vice")),
    dict(id="s13", text="Se inspira en Miami, y se nota: los edificios art decó, las palmeras, el neón y las playas llenas.",
         visual=I("miami_beach", cap="MIAMI BEACH (FOTO REAL)")),
    dict(id="s13b", text="El distrito art decó de Miami Beach tiene más de ochocientos edificios históricos, con esos colores pastel que en los tráileres de GTA seis aparecen por todos lados.",
         visual=I("miami_neon", pop=["+800 EDIFICIOS ART DECÓ"])),
    dict(id="s14", text="Si te interesa la ciudad a fondo, ya tenemos un video entero recorriéndola, barrio por barrio. Te lo dejo arriba.",
         visual=I("neon_city", pop=["VIDEO COMPLETO ARRIBA"])),
    dict(id="s15", text="Pero la ciudad es solo el sur del mapa. Apenas salís de Vice City, empieza otro juego.",
         visual=I("highway_neon")),

    # --- 03 LOS CAYOS ---
    dict(id="s16", text="Capítulo tres. Los Cayos de Leonida.",
         visual=dict(type="title", num="03", text="LOS CAYOS", name="Los Cayos de Leonida")),
    dict(id="s17", text="Al sur de la península hay una cadena de islas tropicales: los Cayos de Leonida. Pueblos chicos, viajes en barco y aguas peligrosas.",
         visual=M(hl="keys")),
    dict(id="s18", text="Se inspiran en los Cayos de Florida, esas islas unidas por puentes larguísimos sobre el mar turquesa.",
         visual=I("keys_bridge", cap="CAYOS DE FLORIDA (FOTO REAL)")),
    dict(id="s18b", text="El más famoso, el puente de las Siete Millas, cruza el mar durante casi once kilómetros. Si Rockstar hizo su versión, va a ser la mejor ruta del juego para manejar.",
         visual=I("keys_bridge", pop=["CASI 11 KM SOBRE EL MAR"])),
    dict(id="s19", text="Y acá está la primera conexión con la historia: según Rockstar, Jason, un exmilitar, terminó en los Cayos trabajando para narcotraficantes de la zona.",
         visual=dict(type="quote", text="JASON\nEXMILITAR · VIVE EN LOS CAYOS\nTRABAJA PARA NARCOS LOCALES")),
    dict(id="s20", text="O sea: las islas no son solo para sacar fotos. Es su territorio, y probablemente donde arranca a meterse en problemas.",
         visual=I("keys_island", cap="CAYOS DE FLORIDA (FOTO REAL)")),
    dict(id="s21", text="Y Lucía, la otra protagonista, acaba de salir de la Penitenciaría de Leonida. Dos vidas complicadas que se cruzan en este mapa.",
         visual=dict(type="stamp", text="PENITENCIARÍA\nDE LEONIDA", stamp="LUCÍA", col="red")),
    dict(id="s22", text="Pero si en los Cayos hay narcos, esperá a ver quién manda en el pueblo de la refinería. Eso viene más adelante.",
         visual=M(sub="¿QUIÉN MANDA?"), abre="P4: ¿Quién manda en el pueblo de la refinería?"),

    # --- 04 GRASSRIVERS ---
    dict(id="s23", text="Capítulo cuatro. Grassrivers.",
         visual=dict(type="title", num="04", text="GRASSRIVERS", name="Grassrivers")),
    dict(id="s24", text="Grassrivers son los pantanos de Leonida: kilómetros de manglares, pasto alto y agua quieta. Se inspiran en los Everglades, el gran humedal del sur de Florida.",
         visual=M(hl="grass")),
    dict(id="s25", text="En los Everglades reales hay pasto que llega a la cintura y canales por los que solo se puede pasar en hidrodeslizador.",
         visual=I("everglades", cap="EVERGLADES (FOTO REAL)")),
    dict(id="s25b", text="Es el humedal subtropical más grande de Estados Unidos, y está lleno de vida salvaje: caimanes, garzas, serpientes y hasta panteras de Florida.",
         visual=I("everglades", pop=["CAIMANES · GARZAS · PANTERAS"])),
    dict(id="s26", text="Y acá está la región del principio. Rockstar escribió que los caimanes quizás sean la atracción más famosa… pero que entre los manglares hay depredadores mucho más letales.",
         visual=I("alligator", pop=["MÁS LETALES QUE LOS CAIMANES"]), cierra="P1"),
    dict(id="s27", text="Y descubrimientos todavía más raros. Rockstar no dijo cuáles. Algunos fans apuntan a serpientes pitón y a pumas; otros, a la gente que vive escondida ahí. Nadie lo sabe todavía.",
         visual=dict(type="quote", text="«DEPREDADORES MÁS LETALES\nY DESCUBRIMIENTOS MÁS RAROS»")),
    dict(id="s28", text="Para moverte, preparate para el hidrodeslizador: en los tráileres aparece cruzando el pasto a toda velocidad.",
         visual=I("airboat", cap="HIDRODESLIZADOR EN LOS EVERGLADES (FOTO REAL)")),
    dict(id="s29", text="Ahora, si el pantano te parece abandonado, esperá a conocer el lugar que Rockstar llama la costa olvidada.",
         visual=I("swamp_airboat")),

    # --- 05 PORT GELLHORN ---
    dict(id="s30", text="Capítulo cinco. Port Gellhorn.",
         visual=dict(type="title", num="05", text="PORT GELLHORN", name="Port Gellhorn")),
    dict(id="s31", text="Port Gellhorn es la costa olvidada de Leonida. Así la llama Rockstar.",
         visual=M(hl="port"), cierra="P3"),
    dict(id="s32", text="Fue un destino de vacaciones que se vino abajo: moteles baratos, atracciones cerradas, centros comerciales vacíos y rutas llenas de paradores.",
         visual=dict(type="quote", text="MOTELES BARATOS\nATRACCIONES CERRADAS\nCENTROS COMERCIALES VACÍOS")),
    dict(id="s33", text="La comunidad lo compara con la costa del golfo de Florida, con ciudades como Panama City: playas que en otra época estaban llenas y hoy viven de recuerdos.",
         visual=I("gulf_motel", cap="COSTA DEL GOLFO, FLORIDA (FOTO REAL)")),
    dict(id="s33b", text="Panama City Beach fue durante años una de las capitales del spring break, las vacaciones de los universitarios de Estados Unidos. Port Gellhorn parece lo que queda después de la fiesta.",
         visual=I("gulf_motel", cap="PANAMA CITY BEACH (FOTO REAL)")),
    dict(id="s34", text="Es el tipo de lugar donde GTA siempre esconde las mejores historias secundarias. Ojo con los moteles.",
         visual=I("gulf_motel", pop=["OJO CON LOS MOTELES"])),
    dict(id="s35", text="Y si seguís hacia el interior, el paisaje cambia de golpe: chimeneas, humo y una fábrica que lo controla todo.",
         visual=M(sub="HACIA EL INTERIOR")),

    # --- 06 AMBROSIA ---
    dict(id="s36", text="Capítulo seis. Ambrosia.",
         visual=dict(type="title", num="06", text="AMBROSIA", name="Ambrosia")),
    dict(id="s37", text="Ambrosia es la zona industrial de Leonida. Todo gira alrededor de una refinería de azúcar enorme, Allied Crystal, a orillas del lago Leonida.",
         visual=M(hl="ambrosia")),
    dict(id="s38", text="Se parece mucho al cinturón azucarero de Florida, alrededor del lago Okeechobee, donde pueblos como Clewiston viven del azúcar.",
         visual=I("sugar_mill", cap="INGENIO EN CLEWISTON, FLORIDA (FOTO REAL)")),
    dict(id="s38b", text="Clewiston, de hecho, se hace llamar «el pueblo más dulce de Estados Unidos». Y el Okeechobee es el lago de agua dulce más grande de Florida.",
         visual=I("okeechobee", pop=["EL PUEBLO MÁS DULCE"])),
    dict(id="s39", text="¿Y quién manda ahí? Según Rockstar, la refinería da los empleos… y una banda de motoqueros, The Final Chapter, da casi todo lo demás.",
         visual=dict(type="versus", title="AMBROSIA", left=["LA REFINERÍA", "DA EL TRABAJO"], right=["LOS MOTOQUEROS", "TODO LO DEMÁS"], mid="VS", lcol="yellow", rcol="red"), cierra="P4"),
    dict(id="s40", text="Un pueblo obrero, una fábrica gigante y una banda que controla la calle. Suena a la región con más misiones de todo el mapa.",
         visual=I("okeechobee", cap="LAGO OKEECHOBEE, FLORIDA (FOTO REAL)")),
    dict(id="s41", text="Pero todavía falta la región más salvaje. Y según Rockstar, la gente que vive ahí es todavía más rara que los motoqueros.",
         visual=M(sub="EL NORTE"), abre="P5: ¿Quiénes viven en los bosques del norte?"),

    # --- 07 MOUNT KALAGA ---
    dict(id="s42", text="Capítulo siete. Mount Kalaga.",
         visual=dict(type="title", num="07", text="MOUNT KALAGA", name="Mount Kalaga")),
    dict(id="s43", text="En el límite norte de Leonida está el Parque Nacional Mount Kalaga: bosques, colinas, ríos y caminos de tierra.",
         visual=M(hl="kalaga")),
    dict(id="s44", text="Rockstar lo presenta como un lugar para cazar, pescar y andar fuera de la ruta. Los tráileres muestran motos de cross y botes.",
         visual=I("forest_north", cap="BOSQUE DEL NORTE DE FLORIDA (FOTO REAL)")),
    dict(id="s45", text="¿Y quién vive en esos bosques? Según Rockstar, místicos de montaña y radicales paranoicos. Sí, así, textual.",
         visual=dict(type="quote", text="«MÍSTICOS DE MONTAÑA\nY RADICALES PARANOICOS»"), cierra="P5"),
    dict(id="s46", text="La comunidad cree que algunos cañones del parque se parecen a Providence Canyon, en el sur de Georgia, justo arriba de Florida.",
         visual=I("canyon", cap="PROVIDENCE CANYON, GEORGIA (FOTO REAL)")),
    dict(id="s46b", text="Le dicen el pequeño Gran Cañón de Georgia, y se formó en parte por la erosión que dejaron las malas prácticas agrícolas del siglo diecinueve.",
         visual=I("canyon", cap="PROVIDENCE CANYON, GEORGIA (FOTO REAL)")),
    dict(id="s47", text="Montañas en Florida no hay, así que Rockstar se tomó sus libertades. Y eso, para explorar, es una gran noticia.",
         visual=I("canyon", pop=["LIBERTADES DE ROCKSTAR"])),

    dict(id="s47b", text="Porque en Florida, montañas de verdad no hay: su punto más alto, Britton Hill, mide apenas unos ciento cinco metros.",
         visual=dict(type="num", start=0, end=105, suffix=" m", label="PUNTO MÁS ALTO DE FLORIDA (BRITTON HILL)")),

    # --- CIERRE ---
    dict(id="s48", text="Repasemos el mapa completo.", bloque="cierre",
         visual=M(all_=True, sub="LEONIDA COMPLETA")),
    dict(id="s49", text="Vice City, la ciudad. Los Cayos, las islas de Jason. Grassrivers, el pantano de los depredadores. Port Gellhorn, la costa olvidada. Ambrosia, la refinería y los motoqueros. Y Mount Kalaga, el bosque de los radicales.",
         visual=dict(type="timeline", title="LAS 6 REGIONES", points=[["1", "Vice City"], ["2", "Los Cayos"], ["3", "Grassrivers"], ["4", "Port Gellhorn"], ["5", "Ambrosia"], ["6", "Mount Kalaga"]], hl=5)),
    dict(id="s50", text="¿Y por dónde arrancar a explorar el primer día? La historia te va a llevar por donde quiera Rockstar, eso no lo podemos cambiar.",
         visual=I("controller")),
    dict(id="s51", text="Pero apenas tengas un rato libre, nuestro consejo es Grassrivers. Es la región que Rockstar más escondió, y la única donde nos avisaron que hay cosas raras sin decirnos cuáles.",
         visual=M(hl="grass", sub="NUESTRO CONSEJO"), cierra="P2"),
    dict(id="s52", text="Y vos, ¿a qué región vas primero? Contalo en los comentarios, que el diecinueve comparamos.",
         visual=I("swamp_airboat", pop=["¿VOS A CUÁL VAS?"])),
    dict(id="s53", text="Suscribite, porque el diecinueve arranca el gameplay en el canal y vamos a recorrer estas seis regiones de verdad. Todas las veces que haga falta.",
         visual=I("neon_city", pop=["EL 19 ARRANCA EL GAMEPLAY"])),
]

FALLBACK = {
    "s13": dict(type="quote", text="VICE CITY = MIAMI"),
    "s18": dict(type="quote", text="LEONIDA KEYS = CAYOS DE FLORIDA"),
    "s20": M(hl="keys"),
    "s25": dict(type="quote", text="GRASSRIVERS = EVERGLADES"),
    "s26": dict(type="quote", text="LOS CAIMANES SON\nLO DE MENOS"),
    "s28": I("swamp_airboat"),
    "s33": dict(type="quote", text="PORT GELLHORN ≈ COSTA DEL GOLFO"),
    "s34": M(hl="port"),
    "s38": dict(type="quote", text="AMBROSIA ≈ LAGO OKEECHOBEE"),
    "s40": M(hl="ambrosia"),
    "s44": M(hl="kalaga"),
    "s46": dict(type="quote", text="MOUNT KALAGA ≈ NORTE DE FLORIDA\nY SUR DE GEORGIA"),
    "s47": M(hl="kalaga"),
    "s13b": dict(type="num", start=0, end=800, prefix="+", label="EDIFICIOS ART DECÓ EN MIAMI BEACH"),
    "s18b": dict(type="num", start=0, end=11, suffix=" km", label="PUENTE DE LAS SIETE MILLAS"),
    "s25b": M(hl="grass"),
    "s33b": dict(type="quote", text="SPRING BREAK"),
    "s38b": dict(type="quote", text="«EL PUEBLO MÁS DULCE\nDE ESTADOS UNIDOS»"),
    "s46b": dict(type="quote", text="«EL PEQUEÑO GRAN CAÑÓN\nDE GEORGIA»"),
}

PRONUNCIA = {
    "GTA seis": "ge te a seis", "GTA cinco": "ge te a cinco", "GTA": "ge te a", "Rockstar": "Rokstar", "Vice City": "Vais Síti",
    "Leonida": "Leónida", "Grassrivers": "Grasríverz", "Port Gellhorn": "Port Guélhorn", "Mount Kalaga": "Maunt Kalága",
    "Allied Crystal": "Álaid Crístal", "The Final Chapter": "De Fáinal Chápter", "Everglades": "Évergleids", "Okeechobee": "Okichóbi",
    "Clewiston": "Clúiston", "Panama City": "Pánama Síti", "Providence Canyon": "Próvidens Cánion", "Jason": "Yéison", "Miami": "Maiámi", "Vice City Stories": "Vais Síti Stóris", "Panama City Beach": "Pánama Síti Bich", "spring break": "spring breik", "Britton Hill": "Británjil",
    "art decó": "ar decó",
}

SHORTS = {}  # sin Shorts (como el 002 y el 003)

THUMBS = [
    dict(img="leonida_map", zoom=1.0, cx=0.62, cy=0.5, shade=["left", 220, 0.55], items=[
        ["text", 45, 60, "6 REGIONES", 190, "yellow", "la"], ["text", 45, 300, "DE LEONIDA", 130, "white", "la"], ["badge", 45, 520, 470, 640, "GTA 6", 100]]),
    dict(img="swamp_airboat", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "NO VAYAS", 190, "pink", "la"], ["text", 45, 300, "A VICE CITY", 150, "white", "la"], ["badge", 45, 540, 470, 660, "GTA 6", 100]]),
    dict(img="alligator", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "LO DE MENOS", 160, "yellow", "la"], ["text", 45, 270, "SON LOS CAIMANES", 105, "white", "la"], ["badge", 45, 500, 470, 620, "GTA 6", 100]]),
    dict(img="highway_neon", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "EL MAPA", 200, "yellow", "la"], ["text", 45, 320, "COMPLETO", 160, "white", "la"], ["badge", 45, 560, 470, 680, "GTA 6", 100]]),
]
THUMBS_TOP = [1, 2, 3]

META = {
    "code": "70x7_004",
    "name": "GTA 6: el mapa de Leonida",
    "intro_chapter": "No vayas directo a Vice City",
    "titles": [
        "Todo el mapa de GTA 6 explicado: las 6 regiones de Leonida (antes del 19)",
        "GTA 6: no vayas directo a Vice City (las 6 regiones de Leonida)",
        "El mapa de GTA 6 región por región… y dónde se inspira cada una",
    ],
    "description": "Leonida, el estado de GTA 6, tiene seis regiones: Vice City, los Cayos de Leonida, Grassrivers, Port Gellhorn, Ambrosia y Mount Kalaga. Te las explico una por una con lo que confirmó Rockstar, los lugares reales de Florida en los que se inspiran y por dónde conviene arrancar a explorar el 19.",
    "sources": [
        "Game Informer (6-may-2025) y web oficial de Rockstar: las seis regiones de Leonida",
        "GamesRadar (2025): descripción oficial de Jason (trabaja para narcos locales en los Cayos) y de Lucía",
        "Beebom / TheGamesWiki: descripción oficial de Grassrivers (depredadores más letales que los caimanes)",
        "PC Gamer: Ambrosia (refinería Allied Crystal y la banda The Final Chapter) y Mount Kalaga («místicos de montaña y radicales paranoicos»)",
        "GTABase / GTABoom / Gfinity: comparación de Leonida con lugares reales de Florida y estimaciones del tamaño del mapa",
        "Tom's Guide / IBTimes (nov-2026): lanzamiento el 19 de noviembre en PS5 y Xbox Series X|S",
        "Fotos vía Wikimedia Commons (dominio público / CC0): NPS, Departamento de Transporte y Archivos Nacionales de EE. UU. y otros autores",
        "Fotos con licencia CC BY: «Airboat in the Everglades - panoramio», de qwesy qwesy (CC BY 3.0); «American Alligator - Alligator mississippiensis, Everglades National Park, Homestead, Florida - 23768845571», de judygva (back in town and trying to catch up) (CC BY 2.0); «Miami South Beach Art Deco Welcome Center by Don Ramey Logan», de Don Ramey Logan (CC BY 4.0); «Ocala National Forest, Ocala, Florida, US», de Trish Hartmann (CC BY 2.0); «Pahokee - Lake Okeechobee Scenic Trail», de RicoRico (CC BY 4.0)",
    ],
    "disclosure": "El mapa es una ilustración hecha para este video. Las fotos son de lugares reales de Florida y Georgia (Wikimedia Commons, créditos en las fuentes) y algunas imágenes son ilustraciones generadas con IA (de un video anterior del canal): nada de eso muestra el juego.",
    "hashtags": "#GTA6 #GTAVI #Leonida #70x7",
    "category": "Videojuegos",
    "playlist": "GTA 6: todo lo que sabemos",
    "tags": ["GTA 6", "GTA VI", "mapa GTA 6", "GTA 6 mapa", "Leonida", "GTA 6 Leonida", "GTA 6 regiones", "Vice City", "Grassrivers",
             "Port Gellhorn", "Ambrosia GTA 6", "Mount Kalaga", "Leonida Keys", "GTA 6 Florida", "GTA 6 19 de noviembre", "GTA 6 español", "70x7"],
    "pinned": "¿A qué región vas primero el 19? 👇 El 19/11 arranca el gameplay en el canal 🦁",
    "shorts": {},
}
