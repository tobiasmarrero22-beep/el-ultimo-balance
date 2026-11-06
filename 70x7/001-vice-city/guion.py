# 70x7 · Vídeo 001 — Recorrí toda Vice City antes de GTA 6 (con la grabación del usuario, 6-nov-2026)
# Canal 70x7 (@70veces7Oficial, AR): noticias y gameplay de GTA 6 en español, voseo. Visual: gameplay real (12:04),
# recorrido de noche al amanecer: Ocean Beach → Washington Beach → Vice Point → Leaf Links → Little Haiti →
# Little Havana → Viceport → Starfish Island → Washington Beach → Ocean Beach.
# Sin la radio del juego (canciones con licencia → reclamos de Content ID): música synthwave generada con vidIQ.
# Hechos verificados (2026-11-06): GTA 6 sale el 19-nov-2026 en PS5 y Xbox Series X|S, sin PC anunciado (GamesRadar,
# Tom's Guide); tráiler 1 (dic-2023) filtrado y publicado antes, 90.421.491 vistas en YouTube en 24 h, récord Guinness;
# tráiler 2 (6-may-2025): 475 M en 24 h en todas las plataformas según Rockstar (TechRadar, TweakTown); web oficial
# (Game Informer 6-may-2025): "the glamour, hustle, and greed of America captured in a single city", Ocean Beach
# ("pastel art deco hotels and bright white sands"), Little Cuba ("bustling panaderias"), Tisha-Wocka ("bootleg brands"),
# VC Port; seis regiones: Vice City, Leonida Keys, Grassrivers, Port Gellhorn, Ambrosia, Mount Kalaga.
# Vice City: octubre de 2002, ambientado en 1986; Tommy Vercetti con la voz de Ray Liotta; 17,5 M de copias a marzo de
# 2008 según Take-Two (6,2 M en EE. UU.); Starfish Island se iba a llamar Star Island (isla real de Miami); la mansión
# y la última misión, homenaje al final de Scarface; primer escondite de Tommy: hotel Ocean View, Ocean Beach.
VOICE = "2719189"  # voz clonada del usuario ("tobias", DubVoice → /api/minimax-tts). Antes: Adán i4Kar2uamCWyas8TAu31
SPEED = 1.0
SRC = "/tmp/claude-0/-home-user-el-ultimo-balance/8305f4cc-14d9-5014-b85d-03b0c591e58c/scratchpad/user_vid1/v.mp4"
SRC_URL = "https://youtu.be/yzCP-6Hwo9w"  # vídeo oculto del usuario (se baja con vidiq_video_upload)
CROP = "1570:884:177:1"  # quita las franjas negras de la captura del celular
BAN = [(0.0, 8.0),  # Centro de control (grabación de pantalla) y el "-10" del reproductor de YouTube
       (138.5, 148.0), (289.5, 298.0),  # notificaciones del celular (Filo.news, Claro)
       (317.5, 333.5), (374.0, 393.0), (453.5, 473.0), (513.5, 532.5), (573.0, 589.5), (636.0, 641.5),
       (650.0, 667.5), (698.0, 711.5)]  # auto parado
THEME = {"RED": (255, 56, 150), "YEL": (80, 230, 235)}  # rosa y celeste Vice City

def G(at, cap=None, key=None):
    return dict(type="img", key=key, at=at, **({"cap": cap} if cap else {}))

SCENES = [
    # --- GANCHO (en plena acción, sin gráficas) ---
    dict(id="s01", text="El diecinueve de noviembre, Rockstar nos devuelve a Vice City. Pero antes de que eso pase, vamos a recorrer la Vice City original entera, de punta a punta.",
         visual=G(4, "VICE CITY ORIGINAL")),
    dict(id="s02", text="Desde que se pone el sol hasta que vuelve a salir. Washington Beach, Vice Point, Little Havana, el puerto, Starfish Island.",
         visual=G(22, "DE NOCHE HASTA EL AMANECER")),
    dict(id="s03", text="Y en el camino me di cuenta de algo. De todos los lugares que Rockstar ya nombró oficialmente para GTA seis, solo uno vuelve con el mismo nombre exacto que tenía en dos mil dos.",
         visual=G(32)),
    dict(id="s04", text="Lo vas a ver al final, justo cuando amanece. Así que subite, que arrancamos.",
         visual=G(642, "¿CUÁL VUELVE?")),

    # --- 01 WASHINGTON BEACH ---
    dict(id="s05", text="Primera parada: Washington Beach.",
         visual=dict(type="title", num="01", text="WASHINGTON BEACH", name="Washington Beach")),
    dict(id="s06", text="Esta es la Vice City de dos mil dos. Rockstar la lanzó en octubre de ese año, pero la historia transcurre en mil novecientos ochenta y seis: neón, trajes claros, autos deportivos y mucha plata sucia.",
         visual=G(47, "OCTUBRE DE 2002")),
    dict(id="s07", text="La ciudad es inventada, pero cualquiera que haya pisado Miami la reconoce al instante.",
         visual=dict(type="year", year="1986", sub="EL AÑO EN QUE TRANSCURRE VICE CITY")),
    dict(id="s08", text="Y el que maneja es Tommy Vercetti. A diferencia del protagonista mudo de GTA tres, Tommy hablaba. Y lo hacía con la voz de Ray Liotta, el actor de Buenos muchachos.",
         visual=G(62, "TOMMY VERCETTI · VOZ DE RAY LIOTTA")),

    # --- 02 VICE POINT ---
    dict(id="s09", text="Segunda parada: Vice Point.",
         visual=dict(type="title", num="02", text="VICE POINT", name="Vice Point")),
    dict(id="s10", text="Vice Point es la zona de los hoteles altos y del shopping. Y mientras se hace de noche, vale la pena recordar lo que fue este juego.",
         visual=G(76, "VICE POINT")),
    dict(id="s10b", text="La historia arranca con Tommy recién salido de la cárcel. La mafia lo manda a Vice City a cerrar un negocio de drogas, y el negocio termina en una emboscada.",
         visual=G(88, "RECIÉN SALIDO DE LA CÁRCEL")),
    dict(id="s11", text="Según Take Two, hasta marzo de dos mil ocho había vendido diecisiete millones y medio de copias. Más de seis millones, solo en Estados Unidos.",
         visual=dict(type="num", start=0, end=17500000, label="COPIAS DE VICE CITY VENDIDAS HASTA 2008")),
    dict(id="s12", text="Y buena parte de la culpa la tuvo la radio: nueve emisoras llenas de canciones reales de los ochenta.",
         visual=G(101, "9 EMISORAS DE RADIO")),
    dict(id="s13", text="Por eso en este video no la vas a escuchar: esas canciones tienen dueño, y YouTube las reclama. La música que suena acá es original.",
         visual=G(113, "MÚSICA ORIGINAL")),
    dict(id="s14", text="Pero hay otra razón por la que este recorrido importa justo ahora.",
         visual=G(127)),
    dict(id="s15", text="En diciembre de dos mil veintitrés, el primer tráiler de GTA seis sumó más de noventa millones de vistas en YouTube en veinticuatro horas. Récord Guinness.",
         visual=dict(type="num", start=0, end=90421491, label="VISTAS EN 24 H · PRIMER TRÁILER DE GTA 6")),
    dict(id="s16", text="Y ni siquiera salió cuando Rockstar quería: se filtró, y tuvieron que publicarlo horas antes de lo previsto.",
         visual=G(149, "SE FILTRÓ")),
    dict(id="s17", text="El segundo tráiler, en mayo de dos mil veinticinco, fue todavía más lejos: según Rockstar, llegó a cuatrocientos setenta y cinco millones de vistas en un día, sumando todas las plataformas.",
         visual=dict(type="versus", title="TRÁILERS DE GTA 6 · PRIMERAS 24 HORAS", left=["90 M", "TRÁILER 1\nSOLO YOUTUBE"],
                     right=["475 M", "TRÁILER 2\nTODAS LAS REDES"], mid="VS", lcol="white", rcol="yellow")),
    dict(id="s18", text="Y desde el primer segundo quedó claro a dónde volvíamos: a Vice City, en el estado de Leonida, la versión de Rockstar de Florida.",
         visual=G(160)),
    dict(id="s19", text="Veinticuatro años después, la ciudad vuelve.",
         visual=dict(type="stamp", text="GTA 6\nVICE CITY · LEONIDA", stamp="CONFIRMADO", col="green")),
    dict(id="s20", text="Pero, ¿cuánto de lo que estás viendo sobrevive?",
         visual=G(176, "24 AÑOS DESPUÉS")),

    # --- 03 LEAF LINKS ---
    dict(id="s21", text="Tercera parada: Leaf Links.",
         visual=dict(type="title", num="03", text="LEAF LINKS", name="Leaf Links")),
    dict(id="s22", text="Leaf Links es una isla entera dedicada a un club de golf, en el medio de la bahía. Para GTA seis, Rockstar todavía no la mencionó.",
         visual=G(232, "LEAF LINKS")),
    dict(id="s23", text="Desde este puente se ve el centro. Y es un buen momento para aclarar algo: la nueva Vice City no es un mapa suelto. Es una parte de un estado entero.",
         visual=G(242, "RUMBO AL CENTRO")),
    dict(id="s24", text="Rockstar ya mostró seis regiones de Leonida: Vice City, los cayos de Leonida, Grassrivers, Port Gellhorn, Ambrosia y Mount Kalaga.",
         visual=dict(type="quote", text="VICE CITY\nLEONIDA KEYS\nGRASSRIVERS\nPORT GELLHORN\nAMBROSIA\nMOUNT KALAGA")),
    dict(id="s25", text="En dos mil dos, en cambio, todo el mapa era la ciudad: dos islas grandes y un puñado de islitas en el medio.",
         visual=G(254)),
    dict(id="s25b", text="Y la última vez que la saga pisó Vice City fue en dos mil seis, con Vice City Stories. Veinte años sin volver.",
         visual=dict(type="year", year="2006", sub="VICE CITY STORIES: LA ÚLTIMA VISITA")),

    # --- 04 LITTLE HAITI ---
    dict(id="s26", text="Cuarta parada: Little Haiti.",
         visual=dict(type="title", num="04", text="LITTLE HAITI", name="Little Haiti")),
    dict(id="s27", text="Little Haiti es uno de los barrios más pobres del mapa, y territorio de la pandilla haitiana. En la Miami real existe un barrio con el mismo nombre.",
         visual=G(263, "LITTLE HAITI")),
    dict(id="s28", text="¿Y en GTA seis? Por ahora, Rockstar no nombró ningún Little Haiti. Puede estar, pero no está confirmado.",
         visual=dict(type="stamp", text="LITTLE HAITI\nEN GTA 6", stamp="SIN NOMBRE OFICIAL", size=150)),
    dict(id="s29", text="Y acá empieza lo interesante. Porque el barrio de al lado sí aparece en GTA seis. Pero con otro nombre.",
         visual=G(276, "EL BARRIO DE AL LADO")),

    # --- 05 LITTLE HAVANA ---
    dict(id="s30", text="Quinta parada: Little Havana.",
         visual=dict(type="title", num="05", text="LITTLE HAVANA", name="Little Havana")),
    dict(id="s31", text="Little Havana es el barrio cubano: cafés, música, y la pandilla de los cubanos peleándose con los haitianos por cada esquina.",
         visual=G(299, "LITTLE HAVANA")),
    dict(id="s32", text="En GTA seis, Rockstar lo rebautizó: ahora se llama Little Cuba. Y en su web lo presenta por sus panaderías llenas de gente.",
         visual=dict(type="versus", title="EL MISMO BARRIO, OTRO NOMBRE", left=["LITTLE HAVANA", "VICE CITY · 2002"],
                     right=["LITTLE CUBA", "GTA 6 · 2026"], mid="→", lcol="white", rcol="red")),
    dict(id="s33", text="En la Miami real se llama Little Havana, y es el corazón de la comunidad cubana. Rockstar cambió el nombre, pero no la idea.",
         visual=G(334, "MIAMI REAL: LITTLE HAVANA")),

    # --- 06 VICEPORT ---
    dict(id="s34", text="Sexta parada: el puerto.",
         visual=dict(type="title", num="06", text="VICEPORT", name="Viceport")),
    dict(id="s35", text="Viceport: contenedores, camiones y depósitos. En el juego original, por acá pasaba buena parte de la mercadería que nunca vio una aduana.",
         visual=G(354, "VICEPORT")),
    dict(id="s36", text="Y este sí vuelve, casi igual: en la web de GTA seis aparece como V C Port. Casi. Porque no es el mismo nombre exacto.",
         visual=dict(type="versus", title="EL PUERTO", left=["VICEPORT", "2002"], right=["VC PORT", "GTA 6"], mid="→", lcol="white", rcol="yellow")),
    dict(id="s37", text="En la misma lista, Rockstar nombró un lugar que en dos mil dos no existía: el Tisha Woka, un mercado de pulgas donde, según su descripción, se venden marcas truchas.",
         visual=G(394, "TISHA-WOCKA: NUEVO EN GTA 6")),
    dict(id="s38", text="Por eso la nueva Vice City no es una copia de la vieja: hay lugares que vuelven, otros que cambian de nombre, y otros que nacen de cero.",
         visual=G(408)),
    dict(id="s39", text="Y hay uno que todos queremos saber si vuelve. Está ahí adelante, cruzando el puente.",
         visual=G(424, "PRÓXIMA PARADA…")),

    # --- 07 STARFISH ISLAND ---
    dict(id="s40", text="Séptima parada: Starfish Island.",
         visual=dict(type="title", num="07", text="STARFISH ISLAND", name="Starfish Island")),
    dict(id="s41", text="Starfish Island, la isla de las mansiones. Durante el desarrollo se iba a llamar Star Island, como la isla real de Miami donde viven millonarios y famosos.",
         visual=G(474, "STARFISH ISLAND")),
    dict(id="s42", text="Y acá está la mansión más famosa de la saga. Tommy se queda con ella, y la última misión del juego es un homenaje evidente al final de Scarface: un tiroteo dentro de la casa.",
         visual=G(486, "LA MANSIÓN VERCETTI")),
    dict(id="s43", text="¿Vuelve en GTA seis? Rockstar todavía no lo confirmó. Si la querés ver, vas a tener que esperar al diecinueve.",
         visual=dict(type="stamp", text="STARFISH ISLAND\nEN GTA 6", stamp="SIN CONFIRMAR")),
    dict(id="s44", text="Y mientras salimos de la isla, el cielo empieza a cambiar.",
         visual=G(500, "CASI AMANECE")),

    # --- 08 DE VUELTA A LA PLAYA ---
    dict(id="s45", text="Octava parada: de vuelta a la playa.",
         visual=dict(type="title", num="08", text="DE VUELTA A LA PLAYA", name="De vuelta a la playa")),
    dict(id="s46", text="Cruzamos otra vez a Washington Beach. Y antes del final, repasemos lo que ya sabemos de GTA seis.",
         visual=G(533, "WASHINGTON BEACH")),
    dict(id="s47", text="Sale el diecinueve de noviembre, en PlayStation cinco y Xbox Series. De PC, por ahora, no hay nada anunciado.",
         visual=dict(type="year", year="19 NOV 2026", sub="GTA 6 · PS5 Y XBOX SERIES X|S")),
    dict(id="s48", text="Y esta vez no hay un Tommy solo: hay dos protagonistas, Jason y Lucía, una pareja al estilo Bonnie y Clyde.",
         visual=G(543, "JASON Y LUCÍA")),
    dict(id="s49", text="Así describe Rockstar su nueva Vice City: el glamour, el ajetreo y la codicia de Estados Unidos, en una sola ciudad.",
         visual=dict(type="quote", text="EL GLAMOUR,\nEL AJETREO\nY LA CODICIA\nEN UNA SOLA CIUDAD")),
    dict(id="s50", text="Que es, si lo pensás, exactamente lo que era la de dos mil dos. Solo que con veinticuatro años más de tecnología.",
         visual=G(555, "2002 → 2026")),
    dict(id="s51", text="Y ahora sí. Sale el sol, y llegamos al último barrio del recorrido.",
         visual=G(590)),

    # --- 09 OCEAN BEACH (el giro) ---
    dict(id="s52", text="Novena y última parada: Ocean Beach.",
         visual=dict(type="title", num="09", text="OCEAN BEACH", name="Ocean Beach")),
    dict(id="s53", text="Ocean Beach. Acá empezó todo: en dos mil dos, Tommy llega a Vice City y su primer escondite es un hotel frente a esta playa, el Ocean View.",
         visual=G(600, "OCEAN BEACH")),
    dict(id="s54", text="Hoteles art déco pintados de colores pastel, palmeras y una avenida frente al mar, igual que el Ocean Drive de Miami.",
         visual=G(612)),
    dict(id="s55", text="Y este es el lugar. De todos los barrios que Rockstar nombró en la web oficial de GTA seis, Ocean Beach es el único que vuelve con el mismo nombre exacto.",
         visual=dict(type="stamp", text="OCEAN BEACH\nEN GTA 6", stamp="CONFIRMADO", col="green")),
    dict(id="s56", text="Rockstar lo describe con hoteles art déco en tonos pastel y arena blanca y brillante. O sea: esto mismo que estás viendo, veinticuatro años después.",
         visual=G(621.2, "«HOTELES ART DÉCO Y ARENA BLANCA»")),
    dict(id="s57", text="Little Havana ahora es Little Cuba. Viceport ahora es V C Port. Starfish Island y Little Haiti, sin confirmar. Pero Ocean Beach sigue acá.",
         visual=G(667.6)),
    dict(id="s58", text="El diecinueve de noviembre volvemos a esta misma playa, y te lo voy a mostrar acá, en setenta veces siete.",
         visual=G(681.0, "19 DE NOVIEMBRE")),
    dict(id="s59", text="Suscribite, y contame en los comentarios cuál es el primer lugar de Vice City que vas a ir a buscar.",
         visual=G(711)),
]
for _s in SCENES:  # cada escena de gameplay tiene su propio clip
    if _s["visual"]["type"] == "img" and not _s["visual"].get("key"):
        _s["visual"]["key"] = "g_" + _s["id"]

# Pronunciación para la voz (solo TTS; subtítulos y SRT usan el texto normal). tts.py aplica esto antes de generar.
PRONUNCIA = {
    "Vice City Stories": "Vais Síti Stóris", "Vice City": "Vais Síti", "Vice Point": "Vais Póint", "Viceport": "Vaisport",
    "V C Port": "ve ce port", "Washington Beach": "Uáshington Bich", "Starfish Island": "Stárfish Áiland",
    "Star Island": "Star Áiland", "Leaf Links": "Lif Links", "Little Havana": "Lítel Jabána", "Little Haiti": "Lítel Jáiti",
    "Little Cuba": "Lítel Cuba", "Ocean Beach": "Óushen Bich", "Ocean View": "Óushen Viu", "Ocean Drive": "Óushen Dráiv",
    "Rockstar": "Rokstar", "GTA seis": "ge te a seis", "GTA tres": "ge te a tres", "Tommy Vercetti": "Tomi Verchéti",
    "Tommy": "Tomi", "Ray Liotta": "Rei Lióta", "Take Two": "Teik Tu", "Tisha Woka": "Tisha Uóka", "Scarface": "Scárfeis",
    "Jason": "Yéison", "Bonnie y Clyde": "Bóni y Cláid", "Grassrivers": "Grasríverz", "Port Gellhorn": "Port Guélhorn",
    "Mount Kalaga": "Maunt Kalága", "PlayStation": "Pléisteishon", "Xbox Series": "Équis Box Síris", "YouTube": "Iutiub",
    "Guinness": "Guínes", "shopping": "shóping", "PC": "pe ce",
}

SHORTS = {
    "a": {"bar": "VICE CITY → GTA 6", "scenes": [
        dict(id="a01", text="Después de veinticuatro años, Rockstar le cambió el nombre a este barrio de Vice City.", key="g_a01", at=340),
        dict(id="a02", text="En dos mil dos era Little Havana, el barrio cubano. En GTA seis se llama Little Cuba, y Rockstar lo presenta por sus panaderías.", key="g_a02", at=301),
        dict(id="a03", text="Y no es el único cambio. El recorrido completo, en el canal.", key="g_a03", at=345),
    ]},
    "b": {"bar": "LA MANSIÓN DE TOMMY", "scenes": [
        dict(id="b01", text="Esta isla de Vice City esconde un homenaje a Scarface.", key="g_b01", at=478),
        dict(id="b02", text="Es Starfish Island, donde está la mansión de Tommy Vercetti. Y la última misión del juego es un tiroteo dentro de la casa, como el final de la película.", key="g_b02", at=486),
        dict(id="b03", text="¿Vuelve en GTA seis? Rockstar todavía no lo confirmó.", key="g_b03", at=499),
    ]},
    "c": {"bar": "SOLO UNO VUELVE", "scenes": [
        dict(id="c01", text="De los barrios que Rockstar nombró para GTA seis, solo uno vuelve con el mismo nombre que en dos mil dos.", key="g_c01", at=679),
        dict(id="c02", text="Little Havana ahora es Little Cuba. Viceport ahora es V C Port. Pero Ocean Beach, la playa donde empezó Tommy, se sigue llamando igual.", key="g_c02", at=612),
        dict(id="c03", text="GTA seis sale el diecinueve de noviembre. Suscribite para verlo acá.", key="g_c03", at=689),
    ]},
}

THUMBS = [  # fondos: fotogramas de los clips (img/<clave>.png)
    dict(img="g_s04", zoom=1.08, cx=0.5, cy=0.45, shade=["left", 210, 0.62], items=[
        ["text", 45, 60, "SOLO 1", 220, "yellow", "la"], ["text", 45, 330, "VUELVE", 150, "white", "la"], ["text", 45, 520, "EN GTA 6", 120, "pink", "la"]]),
    dict(img="g_s02", zoom=1.12, cx=0.55, cy=0.4, shade=["left", 200, 0.6], items=[
        ["text", 45, 70, "TODA", 150, "white", "la"], ["text", 45, 250, "VICE CITY", 150, "pink", "la"], ["text", 45, 430, "DE PUNTA A PUNTA", 110, "white", "la"],
        ["badge", 820, 560, 1240, 680, "ANTES DE GTA 6", 70]]),
    dict(img="g_s56", zoom=1.05, cx=0.5, cy=0.45, shade=["left", 200, 0.6], items=[
        ["text", 45, 80, "2002", 200, "white", "la"], ["text", 45, 330, "→ 2026", 200, "yellow", "la"], ["badge", 45, 590, 520, 690, "¿QUÉ VUELVE?", 70]]),
    dict(img="g_s31", zoom=1.1, cx=0.5, cy=0.45, shade=["left", 220, 0.6], items=[
        ["text", 45, 70, "LE CAMBIARON", 120, "white", "la"], ["text", 45, 230, "EL NOMBRE", 150, "pink", "la"], ["stamp", "GTA 6", 950, 520, -10, 120]]),
    dict(img="g_s41", zoom=1.1, cx=0.5, cy=0.45, shade=["left", 220, 0.6], items=[
        ["text", 45, 70, "¿VUELVE", 190, "white", "la"], ["text", 45, 320, "EN GTA 6?", 170, "yellow", "la"]]),
    dict(img="g_s57", zoom=1.0, cx=0.5, cy=0.5, shade=["left", 190, 0.55], items=[
        ["text", 45, 70, "VICE CITY", 170, "pink", "la"], ["text", 45, 300, "DE NOCHE", 120, "white", "la"], ["text", 45, 460, "AL AMANECER", 120, "yellow", "la"]]),
]
THUMBS.append(dict(img="g_s57", zoom=1.0, cx=0.6, cy=0.5, bright=0.95, shade=["left", 235, 0.62], items=[
    ["text", 45, 50, "SOLO 1", 230, "white", "la"], ["text", 45, 330, "VUELVE", 150, "pink", "la"], ["badge", 45, 560, 560, 680, "EN GTA 6", 90]]))
THUMBS.append(dict(img="g_s02", zoom=1.15, cx=0.6, cy=0.35, bright=1.15, shade=["left", 215, 0.6], items=[
    ["text", 45, 60, "VICE CITY", 175, "pink", "la"], ["text", 45, 290, "ANTES DE", 130, "white", "la"], ["text", 45, 450, "GTA 6", 170, "yellow", "la"]]))
THUMBS_TOP = [7, 1, 8]

META = {
    "code": "70x7_001",
    "name": "Toda Vice City antes de GTA 6",
    "titles": [
        "TODA Vice City antes de GTA 6… y solo UN lugar vuelve igual",
        "Vuelta completa a Vice City antes de GTA 6: esto es lo que sobrevive",
        "Vice City de noche al amanecer: qué vuelve en GTA 6 (y qué no)",
    ],
    "intro_chapter": "Volver a Vice City",
    "description": "Antes de que GTA 6 nos devuelva a Vice City, recorremos la Vice City original de punta a punta, de noche hasta el amanecer: Washington Beach, Vice Point, Leaf Links, Little Haiti, Little Havana, el puerto, Starfish Island y Ocean Beach. Barrio por barrio: qué ya confirmó Rockstar para GTA 6, qué cambió de nombre y qué todavía es un misterio.\n\n🦁 70x7: GTA 6 todas las veces que haga falta. Suscribite, el 19/11 arranca el gameplay.",
    "sources": [
        "Game Informer (6-may-2025): Rockstar muestra seis zonas de Vice City (web oficial de GTA VI)",
        "GamesRadar / Tom's Guide: fecha de salida 19-nov-2026, plataformas",
        "TechRadar / TweakTown: 475 M de vistas del tráiler 2 en 24 h (Rockstar); Guinness: 90,4 M del tráiler 1 en YouTube",
        "Take-Two (2008): ventas de GTA Vice City",
        "GTA Wiki / Grand Theft Wiki: Starfish Island, Vercetti Estate, Ocean View Hotel",
    ],
    "disclosure": "Gameplay: «Night Drive Around Vice City in a Stinger Convertible» de The Gaming Motorist (https://www.youtube.com/watch?v=7PdCFHkEkHo), sin la radio del juego. Música original generada con IA. Narración con mi voz clonada con IA. Canal no afiliado a Rockstar Games ni a Take-Two.",
    "hashtags": "#GTA6 #ViceCity #GTAVI #70x7",
    "category": "Videojuegos",
    "altered": "No (la narración es la voz del propio creador, clonada; no imita a otra persona)",
    "playlist": "GTA 6: todo lo que sabemos",
    "tags": ["GTA 6", "GTA VI", "Vice City", "GTA Vice City", "GTA 6 Vice City", "GTA 6 mapa", "GTA 6 Leonida", "Ocean Beach",
             "Little Cuba", "Little Havana", "Starfish Island", "GTA 6 español", "GTA 6 noticias", "GTA Vice City 2002",
             "Tommy Vercetti", "GTA 6 19 de noviembre", "GTA 6 Latinoamérica", "70x7"],
    "pinned": "¿Cuál es el primer lugar de Vice City que vas a ir a buscar en GTA 6? 👇 El 19/11 arranca el gameplay en el canal 🦁",
    "shorts": {
        "a": {"title": "Rockstar le cambió el nombre a este barrio 😳 #GTA6 #shorts",
              "description": "Little Havana (Vice City, 2002) ahora es Little Cuba en GTA 6. El recorrido completo por Vice City, en el canal.\n\n#GTA6 #ViceCity #shorts",
              "tags": ["GTA 6", "Little Cuba", "Little Havana", "Vice City", "GTA 6 mapa", "70x7"]},
        "b": {"title": "Esta isla de Vice City esconde un homenaje a Scarface 🏝️ #shorts",
              "description": "Starfish Island y la mansión de Tommy Vercetti. ¿Vuelve en GTA 6? Rockstar todavía no lo confirmó.\n\n#GTA6 #ViceCity #shorts",
              "tags": ["GTA 6", "Starfish Island", "Vice City", "Scarface", "Tommy Vercetti", "70x7"]},
        "c": {"title": "Solo UN barrio de Vice City vuelve igual en GTA 6 🌅 #shorts",
              "description": "Little Havana ahora es Little Cuba, Viceport ahora es VC Port… y Ocean Beach se sigue llamando igual. GTA 6 sale el 19/11.\n\n#GTA6 #ViceCity #shorts",
              "tags": ["GTA 6", "Ocean Beach", "Vice City", "GTA 6 mapa", "GTA 6 Leonida", "70x7"]},
    },
}
