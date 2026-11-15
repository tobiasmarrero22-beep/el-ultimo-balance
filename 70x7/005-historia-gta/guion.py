# 70x7 · Vídeo 005 — De 1997 a GTA 6: toda la historia de Grand Theft Auto (guion del 15-nov-2026)
# Tema por datos (API de YouTube, 15-nov): "GTA Recap - The Complete Timeline (Watch Before GTA 6!)" 1,81 M (IGN, oct-2026, EN).
# Elegido por el usuario. Voz Adán, voseo. Sin Shorts. Visual: línea de tiempo y gráficos propios, fotos reales de consolas y
# ciudades (Wikimedia Commons, dominio público / CC BY) e imágenes IA de vídeos anteriores del canal. Nada de imágenes de los juegos.
#
# Hechos verificados (WebSearch y conocimiento contrastado, 15-nov-2026):
# - GTA (1997): DMA Design, estudio de Dundee (Escocia), vista desde arriba, con Liberty City, San Andreas y Vice City. El proyecto
#   empezó como «Race'n'Chase»; según contaron sus creadores, un fallo que volvía muy agresivos a los policías resultó divertido.
# - 1999: GTA London 1969 y GTA 2. Rockstar Games se funda en Nueva York en 1998 (Sam y Dan Houser, entre otros); DMA pasa a ser
#   Rockstar North (2002).
# - GTA III: 22-oct-2001, PS2, primer GTA en 3D; desarrollo entre DMA (Edimburgo) y Rockstar (Nueva York). Tras el 11-S cambiaron
#   la portada y los colores de los patrulleros (parecidos a los del NYPD); Rockstar dijo que el juego quedó «un 1 % diferente».
# - Vice City (oct-2002, 1986, Tommy Vercetti). San Andreas (oct-2004, CJ, Los Santos, San Fierro y Las Venturas), el juego más
#   vendido de PS2. Liberty City Stories (2005) y Vice City Stories (2006).
# - GTA IV (29-abr-2008, Niko Bellic): unos 500 M$ en su primera semana (Take-Two).
# - GTA V (17-sep-2013, tres protagonistas): 1.000 M$ en 3 días (Guinness); más de 230 M de copias (Take-Two, jun-2026), en tres
#   generaciones de consolas; la saga, cerca de 475 M. GTA Online: 1-oct-2013.
# - GTA 6: filtración de sep-2022 (70x7-002); tráiler 1 en dic-2023, 90 M de vistas en 24 h (Guinness); tráiler 2 el 6-may-2025;
#   retrasos: 2025 → 26-may-2026 → 19-nov-2026. Trece años entre GTA V y GTA VI.
VOICE = "i4Kar2uamCWyas8TAu31"  # Adán
SPEED = 1.0
THEME = {"RED": (255, 56, 150), "YEL": (80, 230, 235)}

def I(key, cap=None, pop=None, **kw):
    d = dict(type="img", key=key)
    if cap: d["cap"] = cap
    if pop: d["pop"] = pop
    d.update(kw); return d

def T(num, text):
    return dict(type="title", num=num, text=text.upper(), name=text)

TL = [["1997", "GTA"], ["2001", "GTA III"], ["2002", "Vice City"], ["2004", "San Andreas"], ["2008", "GTA IV"], ["2013", "GTA V"], ["2026", "GTA 6"]]

SCENES = [
    # --- GANCHO ---
    dict(id="s01", text="El diecinueve sale GTA seis, trece años después de GTA cinco. Pero toda esta locura empezó en mil novecientos noventa y siete, en una ciudad de Escocia, con un error de programación.",
         visual=I("dundee", pop=["1997 · ESCOCIA"])),
    dict(id="s02", text="Un error que convirtió un juego de autos cualquiera en la saga que vendió casi quinientos millones de copias.",
         visual=dict(type="num", start=0, end=475, suffix=" M", label="COPIAS VENDIDAS DE LA SAGA GTA (TAKE-TWO, 2026)"), abre="P1: ¿Qué error hizo nacer GTA?"),
    dict(id="s03", text="Te cuento toda la historia, de punta a punta: del juego que se veía desde arriba al más esperado del planeta. Ideal si el diecinueve vas a jugar tu primer GTA.",
         visual=dict(type="timeline", title="DE 1997 A GTA 6", points=TL, hl=0)),
    dict(id="s04", text="Y al final, la pregunta que todos se hacen: por qué tardaron trece años en hacer el sexto.",
         visual=I("controller", pop=["¿POR QUÉ 13 AÑOS?"]), abre="P2: ¿Por qué GTA 6 tardó trece años?"),

    # --- 01 ESCOCIA ---
    dict(id="s05", text="Capítulo uno: un juego hecho en Escocia.", bloque="desarrollo", visual=T("01", "Un juego hecho en Escocia")),
    dict(id="s06", text="La historia arranca en Dundee, Escocia, en un estudio llamado DMA Design, el mismo que había creado Lemmings.",
         visual=I("dundee", cap="DUNDEE, ESCOCIA")),
    dict(id="s06b", text="DMA lo había fundado a fines de los ochenta David Jones, un programador escocés. Nadie se imaginaba que de ese estudio chico saldría una de las sagas más grandes de la historia.",
         visual=dict(type="quote", text="DMA DESIGN\nFUNDADA POR DAVID JONES")),
    dict(id="s07", text="Estaban haciendo un juego de persecuciones que se llamaba Race and Chase. Vos eras el policía y perseguías a los malos.",
         visual=dict(type="quote", text="«RACE'N'CHASE»\nEL PROYECTO ORIGINAL")),
    dict(id="s08", text="Pero según contaron sus creadores, un fallo hizo que la policía del juego se volviera muy agresiva y persiguiera al jugador sin piedad. Y probarlo era mucho más divertido que el juego original.",
         visual=dict(type="terminal", title="dma design · 1995", lines=["> probando IA de la policía...", "!> ERROR: la policía persigue al jugador", "> ...esto es más divertido"]), cierra="P1"),
    dict(id="s09", text="Así que cambiaron la idea: ahora vos eras el delincuente. En mil novecientos noventa y siete sale Grand Theft Auto, visto desde arriba, para PC y PlayStation.",
         visual=I("ps1", cap="PLAYSTATION (1994)")),
    dict(id="s09b", text="El juego armó un escándalo en la prensa británica: había políticos que pedían prohibirlo. Y esa polémica, paradójicamente, lo hizo todavía más famoso.",
         visual=dict(type="headline", kicker="1997", text="Políticos británicos piden prohibir un videojuego de robar autos", mark="prohibir", source="Fuente: prensa británica de la época (resumen)")),
    dict(id="s10", text="Ya tenía tres ciudades con nombres que vas a reconocer: Liberty City, San Andreas y Vice City.",
         visual=dict(type="quote", text="LIBERTY CITY · SAN ANDREAS · VICE CITY\nYA ESTABAN EN 1997")),
    dict(id="s11", text="Después vinieron una expansión en el Londres de mil novecientos sesenta y nueve y GTA dos. Y en Nueva York, unos hermanos británicos fundaban Rockstar Games: Sam y Dan Houser.",
         visual=I("london_1969", cap="LONDRES, AÑOS 60")),
    dict(id="s12", text="Pero el salto que cambió todo todavía no había llegado. Y llegó en el peor momento posible.",
         visual=dict(type="stamp", text="GTA III", stamp="2001", col="yellow"), abre="P3: ¿Qué pasó con GTA III justo antes de salir?"),

    # --- 02 EL SALTO A 3D ---
    dict(id="s13", text="Capítulo dos: el salto a 3D.", visual=T("02", "El salto a 3D")),
    dict(id="s14", text="Octubre de dos mil uno. Sale GTA tres para PlayStation dos. Por primera vez podías caminar y manejar por una ciudad entera en tres dimensiones.",
         visual=I("ps2", cap="PLAYSTATION 2")),
    dict(id="s14b", text="El protagonista ni siquiera hablaba. Pero la ciudad, con sus radios, sus peatones y su policía, era la verdadera protagonista.",
         visual=I("store_night", pop=["LA CIUDAD ERA LA PROTAGONISTA"])),
    dict(id="s15", text="La ciudad era Liberty City, inspirada en Nueva York. Y salió apenas unas semanas después de los atentados del once de septiembre.",
         visual=I("nyc_skyline", cap="NUEVA YORK")),
    dict(id="s16", text="Rockstar cambió la portada y el color de los patrulleros, que se parecían mucho a los de la policía de Nueva York. Según la empresa, el juego quedó un uno por ciento distinto.",
         visual=dict(type="stamp", text="«UN 1 %\nDISTINTO»", stamp="2001", col="yellow"), cierra="P3"),
    dict(id="s16b", text="Aun así, GTA tres terminó siendo uno de los juegos más vendidos de dos mil uno y convirtió a la PlayStation dos en la consola de GTA.",
         visual=I("ps2", pop=["UNO DE LOS MÁS VENDIDOS DE 2001"])),
    dict(id="s17", text="GTA tres fue un éxito enorme y creó un género. Desde ese día, cada juego de mundo abierto se comparó con él.",
         visual=I("game_store", pop=["NACE UN GÉNERO"])),
    dict(id="s18", text="Y Rockstar no esperó: en apenas tres años sacó los dos juegos que muchos consideran la época dorada de la saga.",
         visual=dict(type="timeline", title="TRES JUEGOS EN TRES AÑOS", points=[["2001", "GTA III"], ["2002", "Vice City"], ["2004", "San Andreas"]], hl=1),
         abre="P4: ¿Cuál fue el GTA más vendido de la PlayStation 2?"),

    # --- 03 LA ÉPOCA DORADA ---
    dict(id="s19", text="Capítulo tres: la época dorada.", visual=T("03", "La época dorada")),
    dict(id="s20", text="Dos mil dos: Vice City. Una ciudad inspirada en Miami, en mil novecientos ochenta y seis, con Tommy Vercetti y mucho de Scarface y Miami Vice.",
         visual=I("neon_city", cap="VICE CITY = MIAMI, 1986")),
    dict(id="s21", text="Dos mil cuatro: San Andreas. Ya no era una ciudad, era un estado entero con tres: Los Santos, San Fierro y Las Venturas.",
         visual=I("las_vegas", cap="LAS VENTURAS = LAS VEGAS")),
    dict(id="s22", text="Con CJ volviendo a su barrio, gimnasio, comida y hasta aviones. San Andreas terminó siendo el juego más vendido de toda la PlayStation dos.",
         visual=I("los_angeles", pop=["EL MÁS VENDIDO DE PS2"]), cierra="P4"),
    dict(id="s22b", text="Aunque también trajo la mayor polémica de su época: en dos mil cinco apareció un contenido oculto que obligó a cambiar su clasificación de edad y a reeditar el juego.",
         visual=dict(type="stamp", text="POLÉMICA", stamp="2005", col="red")),
    dict(id="s23", text="Después llegaron dos versiones para la consola portátil de Sony: Liberty City Stories y Vice City Stories.",
         visual=dict(type="timeline", title="LAS VERSIONES PORTÁTILES", points=[["2005", "Liberty City Stories"], ["2006", "Vice City Stories"]], hl=1)),
    dict(id="s24", text="Y esa fue la última vez que la saga pisó Vice City. Hasta ahora.",
         visual=I("highway_neon", pop=["HASTA 2026"])),
    dict(id="s25", text="Pero para dar el siguiente paso, Rockstar hizo algo que nadie esperaba: volvió a Liberty City, y con un protagonista totalmente distinto.",
         visual=I("nyc_skyline2"), abre="P5: ¿Cuánto recaudó GTA IV en su primera semana?"),

    # --- 04 GTA IV ---
    dict(id="s26", text="Capítulo cuatro: Niko y Liberty City.", visual=T("04", "Niko y Liberty City")),
    dict(id="s27", text="Abril de dos mil ocho. GTA cuatro, en PlayStation tres y Xbox trescientos sesenta. Más realista, más oscuro y con un protagonista que venía de Europa del Este: Niko Bellic.",
         visual=I("xbox360", cap="XBOX 360")),
    dict(id="s28", text="Según Take-Two, recaudó unos quinientos millones de dólares en su primera semana. Una cifra de película.",
         visual=dict(type="num", start=0, end=500, suffix=" M$", label="GTA IV EN SU PRIMERA SEMANA (TAKE-TWO)"), cierra="P5"),
    dict(id="s28b", text="Al año siguiente sumó dos expansiones con historias nuevas en la misma ciudad, contadas desde otros personajes.",
         visual=dict(type="timeline", title="GTA IV SE AMPLÍA", points=[["2008", "GTA IV"], ["2009", "Dos expansiones"]], hl=1)),
    dict(id="s29", text="Liberty City se veía como nunca: una Nueva York con lluvia, tráfico y vida en cada esquina.",
         visual=I("nyc_skyline", pop=["NUEVA YORK COMO NUNCA"])),
    dict(id="s30", text="Pero lo que vino después hizo que todo eso pareciera chico. Cinco años más tarde, Rockstar lanzó el juego que iba a romper todos los récords.",
         visual=I("los_angeles"), abre="P6: ¿Qué récord rompió GTA V en sus primeros días?"),

    # --- 05 EL MONSTRUO ---
    dict(id="s31", text="Capítulo cinco: el monstruo.", visual=T("05", "El monstruo")),
    dict(id="s32", text="Diecisiete de septiembre de dos mil trece. Sale GTA cinco, con una novedad: tres protagonistas. Michael, Franklin y Trevor, y podías cambiar entre ellos en cualquier momento.",
         visual=dict(type="quote", text="MICHAEL · FRANKLIN · TREVOR")),
    dict(id="s33", text="En solo tres días facturó mil millones de dólares. Guinness lo registró como el producto de entretenimiento que más rápido llegó a esa cifra.",
         visual=dict(type="num", start=0, end=1000, suffix=" M$", label="GTA V EN 3 DÍAS (GUINNESS)"), cierra="P6"),
    dict(id="s34", text="Ese mismo año arrancó GTA Online, el modo en línea que mantuvo vivo al juego durante más de una década.",
         visual=I("friends_midnight", pop=["GTA ONLINE · 2013"])),
    dict(id="s34b", text="En dos mil quince llegaron los atracos cooperativos, los famosos golpes con amigos, y GTA Online se convirtió en un juego dentro del juego, con actualizaciones durante años.",
         visual=I("friends_midnight", pop=["GOLPES CON AMIGOS · 2015"])),
    dict(id="s35", text="GTA cinco salió en tres generaciones de consolas: PlayStation tres, cuatro y cinco, y lo mismo en Xbox. Y también en PC.",
         visual=I("ps4", cap="PLAYSTATION 4")),
    dict(id="s35b", text="En la nueva generación incluso agregaron la vista en primera persona: podías jugar todo GTA cinco como si fueras el personaje.",
         visual=I("controller", pop=["PRIMERA PERSONA"])),
    dict(id="s36", text="¿El resultado? Más de doscientos treinta millones de copias vendidas, según Take-Two a mediados de dos mil veintiséis. Uno de los juegos más vendidos de la historia.",
         visual=dict(type="bars", title="COPIAS VENDIDAS (MILLONES, TAKE-TWO)", data=[["GTA V", 230], ["RESTO DE LA SAGA", 245]])),
    dict(id="s37", text="Y justamente por eso GTA seis tardó tanto. Pero no fue la única razón.",
         visual=I("controller")),

    # --- 06 EL CAMINO A GTA 6 ---
    dict(id="s38", text="Capítulo seis: el camino a GTA seis.", visual=T("06", "El camino a GTA 6")),
    dict(id="s39", text="Primero, porque GTA cinco y GTA Online seguían vendiendo y dando ganancias año tras año. No había apuro.",
         visual=dict(type="bars", title="GTA V SIGUE VENDIENDO (MILLONES DE COPIAS)", data=[["2013", 0], ["2026", 230]])),
    dict(id="s39b", text="Rockstar recién confirmó que estaba haciendo el próximo GTA en febrero de dos mil veintidós, casi nueve años después de GTA cinco.",
         visual=dict(type="year", year="2022", sub="ROCKSTAR CONFIRMA EL NUEVO GTA")),
    dict(id="s40", text="Segundo, por el tamaño: Leonida, el estado de GTA seis, es el mundo más grande y detallado que hizo Rockstar.",
         visual=dict(type="leonida", all=True, sub="LEONIDA")),
    dict(id="s41", text="En septiembre de dos mil veintidós hubo una filtración enorme de videos del desarrollo. De eso tenemos un video entero en el canal.",
         visual=dict(type="stamp", text="FILTRACIÓN", stamp="2022", col="red")),
    dict(id="s42", text="En diciembre de dos mil veintitrés llegó el primer tráiler: noventa millones de vistas en veinticuatro horas, un récord Guinness.",
         visual=dict(type="num", start=0, end=90, suffix=" M", label="VISTAS DEL TRÁILER 1 EN 24 HORAS (GUINNESS)")),
    dict(id="s42b", text="El tráiler confirmó la vuelta a Vice City y presentó a los protagonistas: Jason y Lucía, una pareja metida en el crimen.",
         visual=dict(type="versus", title="GTA 6", left=["JASON", "PROTAGONISTA"], right=["LUCÍA", "PROTAGONISTA"], mid="&", lcol="yellow", rcol="red")),
    dict(id="s42c", text="Y el segundo tráiler, en mayo de dos mil veinticinco, sumó según Rockstar cuatrocientos setenta y cinco millones de vistas en veinticuatro horas, contando todas las plataformas.",
         visual=dict(type="num", start=0, end=475, suffix=" M", label="VISTAS DEL TRÁILER 2 EN 24 H (ROCKSTAR)")),
    dict(id="s43", text="Después, dos retrasos: de dos mil veinticinco pasó a mayo de dos mil veintiséis, y de mayo, al diecinueve de noviembre.",
         visual=dict(type="timeline", title="LOS RETRASOS", points=[["2025", "Fecha original"], ["MAYO 2026", "Primer retraso"], ["19 NOV 2026", "Fecha final"]], hl=2), cierra="P2", abre="P7: ¿Qué tiene GTA 6 que no tuvo ningún GTA moderno?"),
    dict(id="s44", text="Así que, entre un juego y otro, pasaron trece años. Nunca la saga había esperado tanto.",
         visual=dict(type="num", start=0, end=13, label="AÑOS ENTRE GTA V Y GTA 6")),

    # --- CIERRE ---
    dict(id="s44b", text="Y llega con algo que ningún GTA de la era moderna tuvo: una protagonista mujer, Lucía, compartiendo la historia con Jason.",
         visual=dict(type="stamp", text="LUCÍA", stamp="PRIMERA VEZ", col="red"), cierra="P7", bloque="cierre"),
    dict(id="s45", text="Repasemos: un error en Escocia, el salto a 3D, Vice City y San Andreas, Niko, los tres protagonistas de GTA cinco… y ahora, Leonida.",
         visual=dict(type="timeline", title="TODA LA SAGA", points=TL, hl=6)),
    dict(id="s46", text="Casi treinta años después de aquel juego visto desde arriba, el diecinueve volvemos a Vice City.",
         visual=I("highway_neon", pop=["19 DE NOVIEMBRE"])),
    dict(id="s47", text="Y vos, ¿cuál fue tu primer GTA? Contalo en los comentarios, que quiero ver quién arrancó con el de mil novecientos noventa y siete.",
         visual=I("controller", pop=["¿CUÁL FUE TU PRIMER GTA?"])),
    dict(id="s48", text="Suscribite, que el diecinueve arranca el gameplay en el canal. Todas las veces que haga falta.",
         visual=I("neon_city", pop=["EL 19 ARRANCA EL GAMEPLAY"])),
]

FALLBACK = {
    "s01": dict(type="year", year="1997", sub="DUNDEE, ESCOCIA"), "s06": dict(type="quote", text="DMA DESIGN\nDUNDEE, ESCOCIA"),
    "s09": dict(type="year", year="1997", sub="GRAND THEFT AUTO"), "s11": dict(type="timeline", title="1998-1999", points=[["1998", "Nace Rockstar Games"], ["1999", "GTA London 1969 y GTA 2"]], hl=0),
    "s12": dict(type="stamp", text="GTA III", stamp="2001", col="yellow"), "s14": dict(type="year", year="2001", sub="GTA III · PRIMER GTA EN 3D"),
    "s15": dict(type="quote", text="LIBERTY CITY\n= NUEVA YORK"), "s17": dict(type="quote", text="NACE UN GÉNERO\nMUNDO ABIERTO"),
    "s21": dict(type="quote", text="LOS SANTOS · SAN FIERRO\nLAS VENTURAS"), "s22": dict(type="stamp", text="EL MÁS VENDIDO\nDE PS2", stamp="2004", col="yellow"),
    "s25": dict(type="year", year="2008", sub="VUELTA A LIBERTY CITY"), "s27": dict(type="year", year="2008", sub="GTA IV · NIKO BELLIC"),
    "s29": dict(type="quote", text="LIBERTY CITY\nCOMO NUNCA"), "s30": dict(type="year", year="2013", sub="GTA V"),
    "s35": dict(type="quote", text="PS3 · PS4 · PS5\nXBOX 360 · ONE · SERIES · PC"),
}

PRONUNCIA = {
    "GTA seis": "ge te a seis", "GTA cinco": "ge te a cinco", "GTA cuatro": "ge te a cuatro", "GTA tres": "ge te a tres", "GTA dos": "ge te a dos",
    "GTA Online": "ge te a Onláin", "GTA": "ge te a", "Grand Theft Auto": "Grand Zeft Óto", "Rockstar Games": "Rokstar Guéims", "Rockstar": "Rokstar",
    "Race and Chase": "Réis and Chéis", "DMA Design": "de eme a Disáin", "Lemmings": "Lémings", "Dundee": "Dandí", "Sam y Dan Houser": "Sam y Dan Jáuser",
    "Liberty City Stories": "Líberti Síti Stóris", "Vice City Stories": "Vais Síti Stóris", "Liberty City": "Líberti Síti", "Vice City": "Vais Síti",
    "San Andreas": "San Andréas", "Los Santos": "Los Santos", "San Fierro": "San Fierro", "Las Venturas": "Las Venturas", "Tommy Vercetti": "Tómi Verchéti",
    "Scarface": "Scárfeis", "Miami Vice": "Maiámi Váis", "Niko Bellic": "Níko Bélik", "Take-Two": "Téik Tu", "Guinness": "Guínes", "Michael": "Máikol",
    "Franklin": "Fránklin", "Trevor": "Trévor", "Leonida": "Leónida", "PlayStation": "Pléisteishon", "Xbox": "Équis Box", "PC": "pe ce", "CJ": "ci yei", "David Jones": "Déivid Yóuns", "Jason": "Yéison",
}

SHORTS = {}

THUMBS = [
    dict(img="ps1", zoom=1.0, cx=0.6, items=[
        ["text", 45, 40, "1997", 200, "pink", "la"], ["text", 45, 290, "→ GTA 6", 170, "cyan", "la"]]),
    dict(img="controller", zoom=1.05, cx=0.55, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "TODA LA", 150, "white", "la"], ["text", 45, 250, "HISTORIA", 190, "pink", "la"], ["badge", 45, 520, 470, 640, "GTA", 110]]),
    dict(img="neon_city", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "UN ERROR", 170, "pink", "la"], ["text", 45, 280, "CREÓ GTA", 170, "white", "la"]]),
    dict(img="nyc_skyline", zoom=1.1, cx=0.6, shade=["left", 200, 0.55], items=[
        ["text", 45, 60, "EL JUEGO QUE", 130, "white", "la"], ["text", 45, 230, "CAMBIÓ TODO", 150, "cyan", "la"], ["badge", 45, 470, 470, 590, "2001", 100]]),
    dict(img="highway_neon", zoom=1.05, cx=0.55, shade=["left", 200, 0.6], items=[
        ["text", 45, 60, "13 AÑOS", 200, "pink", "la"], ["text", 45, 320, "ESPERANDO", 150, "white", "la"]]),
    dict(img="friends_midnight", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "¿CUÁL FUE", 150, "white", "la"], ["text", 45, 250, "TU PRIMER", 150, "white", "la"], ["text", 45, 440, "GTA?", 190, "pink", "la"]]),
]
THUMBS_TOP = [3, 1, 2]

META = {
    "code": "70x7_005",
    "name": "Toda la historia de GTA",
    "intro_chapter": "De 1997 a GTA 6",
    "titles": [
        "De 1997 a GTA 6: toda la historia de GTA (antes del 19)",
        "GTA empezó con un error de programación: toda la saga antes de GTA 6",
        "Toda la saga GTA en 8 minutos: del juego visto desde arriba a GTA 6",
    ],
    "description": "Antes de que salga GTA 6 el 19 de noviembre, te cuento toda la historia de Grand Theft Auto: del primer juego hecho en Escocia en 1997 (y el error que lo hizo nacer) al salto a 3D con GTA III, Vice City, San Andreas, Niko Bellic, los tres protagonistas de GTA V y los 13 años de espera hasta Leonida.",
    "sources": [
        "Take-Two Interactive (resultados del trimestre a jun-2026): más de 230 millones de copias de GTA V y cerca de 475 millones de la saga",
        "TechRadar / Kotaku / MCV (2001-2011): GTA III, los cambios tras el 11-S y la declaración de Rockstar",
        "Take-Two (mayo de 2008): ventas de GTA IV en su primera semana",
        "Guinness World Records: GTA V, 1.000 millones de dólares en 3 días; tráiler 1 de GTA 6, 90 millones de vistas en 24 h",
        "Rockstar Games: fechas de lanzamiento y retrasos de GTA 6 (19-nov-2026)",
        "Fotos vía Wikimedia Commons (dominio público / CC0): consolas PlayStation, PlayStation 2, PlayStation 4 y Xbox 360, de Evan-Amos; «Reflection of the Flamingo Hotel in front of the Bellagio», de Julian Lupyan; «Los Angeles Skyline; August 30, 2022», de ItzAPotato2009",
        "Fotos con licencia CC BY 4.0: «Lower Manhattan night skyline 20261003 – 1» y «– 3», de VynedJ; «1960s tube carriage, London Transport Museum 2025-11-16», de Matt From London",
    ],
    "disclosure": "Las fotos son de lugares y consolas reales (Wikimedia Commons) y algunas imágenes son ilustraciones generadas con IA de videos anteriores del canal: nada de eso muestra el juego. Narración con voz sintética. Canal no afiliado a Rockstar Games ni a Take-Two.\n\n🦁 70x7: GTA 6 todas las veces que haga falta. Suscribite, el 19/11 arranca el gameplay.",
    "hashtags": "#GTA6 #GTA #Rockstar #70x7",
    "category": "Videojuegos",
    "playlist": "GTA 6: todo lo que sabemos",
    "altered": "Sí",
    "tags": ["GTA 6", "historia de GTA", "toda la saga GTA", "GTA III", "GTA Vice City", "GTA San Andreas", "GTA IV", "GTA V",
             "Rockstar Games", "DMA Design", "GTA resumen", "GTA 6 19 de noviembre", "GTA en español", "70x7"],
    "pinned": "¿Cuál fue tu primer GTA? 👇 El 19/11 arranca el gameplay en el canal 🦁",
    "shorts": {},
}
