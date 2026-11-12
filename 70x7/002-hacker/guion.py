# 70x7 · Vídeo 002 — El chico que filtró GTA 6 desde un hotel (y vuelve a juicio 10 días antes del lanzamiento)
# Tema por datos (8-nov-2026, API de YouTube): en inglés, Shorts de 11,7 M ("The Teen Who Leaked GTA 6 From A Hotel Room"),
# 5,8 M (fire stick) y 4,3 M; largos de 487 k (SomeOrdinaryGamers). En español solo hay Shorts y reacciones: ningún largo
# con la historia completa. Gancho de actualidad: el juicio está fijado para el 9-nov-2026, diez días antes de GTA 6.
# Visual: imágenes IA (vidIQ) + escenas de código (chat, terminal, línea de tiempo, titulares). Sin metraje de Rockstar.
# Voz: Adán (la del 007), sin Shorts (pedido del usuario).
#
# Hechos verificados (WebSearch, 8-nov-2026):
# - Arion Kurtaj, de Oxford, autismo; miembro clave de Lapsus$. Jurado (Southwark, 23-ago-2023, unanimidad, juicio de ~2 meses
#   empezado en julio): cometió 12 delitos (extorsión, fraude, Computer Misuse Act). Por no estar en condiciones de ser juzgado
#   (psiquiatras), el jurado solo decidió si cometió los hechos, no culpable/inocente (Reuters, BBC vía Infosecurity, The Register).
# - Nvidia (feb-2022): ~1 TB, publicó ~80 GB y amenazó con el resto. Revolut: datos de ~5.000 clientes; Uber dos días después:
#   casi 3 M$ de daños según la fiscalía (Reuters, breakingnews.ie). Estaba en libertad bajo fianza por hackeos anteriores (Nvidia).
# - Rivales publicaron sus datos personales → la policía lo alojó en un Travelodge de Bicester por su seguridad; le quitaron
#   la computadora y tenía prohibido internet. Usó un Amazon Fire Stick en la tele del hotel + celular nuevo, teclado y mouse
#   para conectarse a servicios en la nube (BBC vía PC Gamer, NME, MobileSyrup, Notebookcheck). La policía de la City de Londres
#   entró en la habitación; el Fire Stick seguía enchufado a la tele (reporte alemán, t3n/GameStar). Detenido: 17 años, Oxfordshire.
# - Mensaje en el Slack interno de Rockstar, leído en el juicio: "I am not a Rockstar employee, I am an attacker"; amenaza:
#   "if Rockstar does not contact me on Telegram within 24 hours I will start releasing the source code" (LBC/PA, ITPro).
# - 18-sep-2022: "teapotuberhacker" publica 90 videos de GTA 6 en GTAForums (Rockstar confirmó que eran reales).
#   19-sep-2022: Rockstar confirma la intrusión ("extremely disappointed"), el desarrollo sigue según lo previsto (Variety,
#   GameSpot); Take-Two cae un 5,8 % antes de abrir (CNBC vía GameSpot). Take-Two pidió retirar los videos (DMCA).
# - Rockstar en el juicio: 5 M$ + "thousands of hours of staff time" (GamesRadar). La defensa citó el éxito del tráiler.
#   Tráiler 1 (dic-2023): 90,4 M de vistas en YouTube en 24 h, récord Guinness.
# - Sentencia (dic-2023): hospital order indefinida; el juez: sus "habilidades y deseo de cometer ciberdelitos" lo hacen de alto
#   riesgo; informe médico: seguía expresando la intención de volver al cibercrimen lo antes posible. Coacusado de 17 años:
#   orden de rehabilitación juvenil de 18 meses (TechRadar, Engadget, Bloomberg Law).
# - 2026: médicos lo consideran apto para un juicio; Joe Tidy (BBC, Bluesky, julio) informa que pasó a una cárcel común a la
#   espera del juicio (restricciones levantadas el 14-jul); no está claro por qué ahora (Tidy). Abogados (Red Lion Chambers):
#   juicio fijado para el 9-nov-2026 en Woolwich Crown Court (Notebookcheck, OpenCritic, GamingHQ). Fuente única para la fecha:
#   se dice "según sus abogados, está fijado".
# - Filtraciones de 2026: cuenta anónima "CyberLeek"; ninguna fuente pública la vincula con Kurtaj.
# - GTA 6: otoño 2025 → 26-may-2026 → 19-nov-2026 (Rockstar/Take-Two). Take-Two prevé 8.000–8.200 M$ de reservas netas en el
#   año fiscal 2027, sobre todo por GTA 6 (resultados del 21-may-2026).
VOICE = "i4Kar2uamCWyas8TAu31"  # ElevenLabs "Adán - Narration" (la del 007), por pedido del usuario
SPEED = 1.0
THEME = {"RED": (255, 56, 150), "YEL": (80, 230, 235)}  # rosa y celeste Vice City

def I(key, cap=None, pop=None, **kw):
    d = dict(type="img", key=key)
    if cap: d["cap"] = cap
    if pop: d["pop"] = pop
    d.update(kw); return d

# Imágenes: vidIQ generate_thumbnail (fotograma realista, sin texto). Nunca personas reales reconocibles ni logos.
Q = "Photorealistic cinematic documentary still, NOT a thumbnail: {}. Absolutely no text, no words, no letters, no logos, no watermarks. Wide 16:9 movie frame, moody cinematic lighting."
IMAGES = {
    "hotel_tv": "a cheap budget hotel room at night, the only light comes from a large wall TV glowing blue, a small phone, a compact keyboard and a mouse lie on the unmade bed, curtains closed, no people",
    "firestick": "extreme close-up macro of a small black streaming media stick plugged into the HDMI port on the back of a television, tiny LED glowing, shallow depth of field, dark room lit by the screen",
    "hoodie_back": "a teenage boy in a dark hoodie seen strictly from behind, sitting on a hotel bed facing a big glowing TV screen full of abstract blue light, his face not visible, phone in hand, keyboard on his lap",
    "oxford_street": "a rainy English town street at dusk, old brick terraced houses, wet pavement reflecting warm street lights, quiet and gloomy",
    "hackers_room": "a dark bedroom lit only by several laptop screens and RGB lights, energy drink cans, two silhouetted teenagers seen from behind typing, faces not visible",
    "data_center": "a corridor of server racks in a data center with blinking lights, red emergency lighting, ominous atmosphere",
    "hotel_exterior": "exterior of a plain roadside budget hotel in the English countryside at night, wet car park, a single lit window, overcast sky",
    "studio_office": "a dark modern video game studio office at night, rows of empty desks with large monitors showing colorful abstract 3D city environments, neon pink and cyan glow",
    "forum_screen": "close-up of a laptop screen in a dark room showing a blurry grid of small video thumbnails with tropical neon city scenes, a person's silhouette reflected, unreadable interface",
    "neon_city": "a neon-lit Miami-style beach boulevard at night, palm trees, pastel art deco hotels glowing pink and cyan, a vintage convertible driving by, humid air",
    "stock_red": "a trading screen with a steep red falling stock chart in a dark office, a blurred silhouette of a worried man holding his head in the foreground",
    "police_hotel": "British police officers in high-visibility vests seen from behind walking down a narrow budget hotel corridor at night toward an open room door, tense",
    "court_exterior": "exterior of a modern British crown court building on an overcast grey day, concrete and glass facade, a few people walking, no signs",
    "courtroom": "interior of an English courtroom with light wood panelling, an empty glass-walled dock, empty judge bench and benches, cold daylight",
    "hospital": "a long corridor of a secure psychiatric hospital, locked heavy doors with small windows, cold fluorescent light, empty and silent",
    "prison": "a British prison wing interior, two levels of metal cell doors and railings, dim evening light, empty",
    "controller": "a game controller resting on a coffee table in a dark living room at night, a big TV glowing pink and cyan in the background, cozy anticipation",
}

SCENES = [
    # --- GANCHO ---
    dict(id="s01", text="Septiembre de dos mil veintidós. Un chico de diecisiete años está encerrado en la habitación de un hotel, controlado por la policía y sin computadora.",
         visual=I("hotel_tv", pop=["SIN COMPUTADORA"])),
    dict(id="s02", text="Y aun así, con un Fire Stick enchufado a la tele del hotel, un celular y un teclado, logró meterse en Rockstar.",
         visual=I("firestick", pop=["UN FIRE STICK"])),
    dict(id="s03", text="Lo que sacó de ahí terminó siendo una de las filtraciones más grandes de la historia de los videojuegos.",
         visual=dict(type="terminal", title="habitación de hotel · 2022", lines=["> conectando desde la tele del hotel...", "> fire_stick: ok", "> acceso: chat interno de la empresa", "!> descargando videos de GTA VI..."])),
    dict(id="s04", text="Noventa videos de GTA seis, el juego más esperado del mundo, subidos a un foro un domingo cualquiera.",
         visual=dict(type="num", start=0, end=90, label="VIDEOS DE GTA 6 PUBLICADOS EN UN FORO")),
    dict(id="s05", text="Según Rockstar, arreglar el desastre le costó cinco millones de dólares y miles de horas de trabajo.",
         visual=dict(type="num", start=0, end=5000000, suffix=" $", label="LO QUE LE COSTÓ A ROCKSTAR (SEGÚN LA EMPRESA)")),
    dict(id="s06", text="Al chico no lo mandaron a la cárcel. Lo mandaron a un hospital de alta seguridad. Sin fecha de salida.",
         visual=I("hospital", pop=["SIN FECHA DE SALIDA"])),
    dict(id="s07", text="Pero la historia no terminó ahí. Diez días antes de que salga GTA seis, ese chico vuelve a sentarse frente a un juez. Y esta vez, de verdad.",
         visual=dict(type="versus", title="NOVIEMBRE DE 2026", left=["9 NOV", "EMPIEZA EL JUICIO"], right=["19 NOV", "SALE GTA 6"], mid="→", lcol="red", rcol="yellow")),
    dict(id="s08", text="Esta es la historia completa del hacker que filtró GTA seis. Subite, que arrancamos.",
         visual=I("neon_city")),

    # --- 01 UN CHICO DE OXFORD ---
    dict(id="s09", text="Capítulo uno. Un chico de Oxford.",
         visual=dict(type="title", num="01", text="UN CHICO DE OXFORD", name="Un chico de Oxford")),
    dict(id="s10", text="Se llama Arion Kurtaj, es de Oxford, en Inglaterra, y tiene autismo. Cuando empieza esta historia, todavía es menor de edad.",
         visual=I("oxford_street", cap="OXFORD, INGLATERRA")),
    dict(id="s11", text="Y no es un hacker cualquiera. Es una de las piezas clave de Lapsus, un grupo de hackers con varios adolescentes que en dos mil veintidós se volvió famoso en todo el mundo.",
         visual=I("hackers_room", pop=["LAPSUS$"])),
    dict(id="s12", text="El grupo se atribuyó ataques contra gigantes como Microsoft, Samsung y Nvidia. Y no pedían rescates discretos: lo anunciaban en público, como si fuera un show.",
         visual=dict(type="quote", text="MICROSOFT\nSAMSUNG\nNVIDIA")),
    dict(id="s13", text="En febrero de dos mil veintidós, según el jurado que lo juzgó después, Kurtaj entró en Nvidia, la empresa de las placas de video, y se llevó cerca de un terabyte de información.",
         visual=dict(type="num", start=0, end=1, suffix=" TB", label="DATOS ROBADOS A NVIDIA · FEBRERO DE 2022")),
    dict(id="s14", text="Publicó unos ochenta gigas y amenazó con soltar el resto si no le hacían caso.",
         visual=I("data_center", pop=["80 GB PUBLICADOS"])),
    dict(id="s15", text="La policía ya lo tenía en la mira. Lo detienen por los primeros hackeos y queda libre bajo fianza, a la espera del juicio.",
         visual=dict(type="stamp", text="2022\nDETENIDO POR LOS PRIMEROS HACKEOS", stamp="BAJO FIANZA", col="yellow")),
    dict(id="s16", text="Y entonces pasa algo que lo cambia todo: otros hackers, rivales suyos, publican en internet sus datos personales.",
         visual=I("hackers_room", pop=["SUS DATOS, EN INTERNET"], pop_col="red")),
    dict(id="s16b", text="De golpe, el chico que exponía a las empresas queda expuesto él. Y la policía decide sacarlo de su casa.",
         visual=I("oxford_street", shake=True)),

    # --- 02 ENCERRADO EN UN HOTEL ---
    dict(id="s17", text="Capítulo dos. Encerrado en un hotel.",
         visual=dict(type="title", num="02", text="ENCERRADO EN UN HOTEL", name="Encerrado en un hotel")),
    dict(id="s18", text="Para protegerlo, lo llevan a un hotel barato de la cadena Travelodge en Bicester, un pueblo cerca de Oxford.",
         visual=I("hotel_exterior", cap="BICESTER, INGLATERRA")),
    dict(id="s19", text="Las condiciones son claras: le quitan la computadora y tiene prohibido usar internet. Sobre el papel, está completamente desconectado.",
         visual=dict(type="stamp", text="SIN COMPUTADORA\nSIN INTERNET", stamp="PROHIBIDO")),
    dict(id="s20", text="Pero en la habitación hay una tele.",
         visual=I("hotel_tv", pop=["UNA TELE"])),
    dict(id="s21", text="Y él consigue un Fire Stick de Amazon. Sí, ese aparatito que se enchufa a la tele para ver series y películas.",
         visual=I("firestick", pop=["FIRE STICK"])),
    dict(id="s22", text="Le suma un celular nuevo, un teclado y un mouse. Con eso arma su centro de operaciones, en una habitación de hotel.",
         visual=I("hoodie_back", pop=["CELULAR", "TECLADO", "MOUSE"])),
    dict(id="s23", text="Según se contó en el juicio, desde la tele se conectaba a servicios en la nube. Y desde la nube, a todo lo demás.",
         visual=dict(type="quote", text="UN FIRE STICK\n+ LA TELE DEL HOTEL\n= ROCKSTAR")),
    dict(id="s23b", text="Nadie se imaginaba que un aparato de unos cuarenta dólares, en una tele de hotel, iba a poner en jaque a uno de los estudios más grandes del mundo.",
         visual=I("hoodie_back", shake=True)),

    # --- 03 NOVENTA VIDEOS ---
    dict(id="s24", text="Capítulo tres. Noventa videos.",
         visual=dict(type="title", num="03", text="NOVENTA VIDEOS", name="Noventa videos")),
    dict(id="s25", text="Septiembre de dos mil veintidós. Desde esa habitación, según el jurado, Kurtaj ataca primero a Revolut, un banco digital, y se lleva datos de unos cinco mil clientes.",
         visual=dict(type="num", start=0, end=5000, label="CLIENTES DE REVOLUT EXPUESTOS")),
    dict(id="s26", text="Dos días después entra en Uber. La fiscalía calculó los daños en casi tres millones de dólares.",
         visual=I("data_center", pop=["UBER", "≈3 MILLONES $"])),
    dict(id="s27", text="Y entonces va por el premio mayor: Rockstar Games, el estudio de GTA.",
         visual=I("studio_office", pop=["ROCKSTAR"])),
    dict(id="s28", text="Entra en el chat interno de la empresa y les escribe a los empleados. Según se leyó en el juicio, el mensaje decía: no soy un empleado de Rockstar, soy un atacante.",
         visual=dict(type="chat", title="# chat-interno", kicker="mensajes leídos en el juicio (traducidos)", msgs=[
             ["atacante", "No soy un empleado de Rockstar. Soy un atacante.", "alert"],
             ["atacante", "Si no me contactan por Telegram en 24 horas, empiezo a publicar el código fuente.", "alert"]])),
    dict(id="s29", text="Y amenaza: si no lo contactan por Telegram en veinticuatro horas, empieza a publicar el código fuente del juego.",
         visual=I("studio_office", pop=["24 HORAS"], pop_col="red", shake=True)),
    dict(id="s30", text="El domingo dieciocho de septiembre, un usuario llamado teapotuberhacker sube noventa videos de GTA seis a GTAForums, un foro de fans.",
         visual=dict(type="year", year="18/09/2022", sub="90 VIDEOS DE GTA 6 APARECEN EN UN FORO")),
    dict(id="s31", text="El nombre ya era una pista: Uber hacker. El mismo usuario decía estar detrás del ataque a Uber de esa semana.",
         visual=I("forum_screen", pop=["TEAPOT·UBER·HACKER"])),
    dict(id="s32", text="Los videos eran de una versión muy temprana del juego: gráficos sin terminar, menús de prueba, textos de desarrollo.",
         visual=I("forum_screen", pop=["VERSIÓN TEMPRANA"])),
    dict(id="s33", text="Pero lo que mostraban era oro para los fans: la vuelta a Vice City y una protagonista mujer.",
         visual=I("neon_city", pop=["VICE CITY"])),
    dict(id="s34", text="En pocas horas los videos estaban en todas las redes. Take Two pedía que los borraran, y volvían a aparecer en otro lado.",
         visual=I("forum_screen", shake=True)),
    dict(id="s35", text="Al día siguiente, Rockstar lo confirma: alguien entró en sus sistemas y se llevó material del juego. La empresa dice que está muy decepcionada, pero que el desarrollo sigue según lo previsto.",
         visual=dict(type="headline", kicker="19 de septiembre de 2022", text="Rockstar confirma el hackeo y asegura que GTA 6 sigue según lo previsto", mark="hackeo", source="Fuente: Rockstar Games vía Variety / GameSpot")),
    dict(id="s36", text="Ese lunes, las acciones de Take Two, la dueña de Rockstar, llegaron a caer casi un seis por ciento antes de abrir la bolsa.",
         visual=dict(type="num", start=0, end=5.8, prefix="-", suffix=" %", label="TAKE-TWO ANTES DE ABRIR LA BOLSA (19/09/2022)")),
    dict(id="s37", text="Y la policía se mueve rápido. Entra en la habitación del hotel y, según se contó después, encuentra el Fire Stick todavía enchufado a la tele.",
         visual=I("police_hotel", pop=["TODAVÍA ENCHUFADO"])),
    dict(id="s38", text="Pocos días después, la policía de Londres anuncia que detuvo a un chico de diecisiete años en Oxfordshire. El hotel se había terminado.",
         visual=dict(type="stamp", text="SEPTIEMBRE DE 2022\nUN CHICO DE 17 AÑOS", stamp="DETENIDO")),

    # --- 04 UN JUICIO SIN CULPABLE ---
    dict(id="s39", text="Capítulo cuatro. Un juicio sin culpable.",
         visual=dict(type="title", num="04", text="UN JUICIO SIN CULPABLE", name="Un juicio sin culpable")),
    dict(id="s40", text="El juicio empieza en julio de dos mil veintitrés, en Londres, y dura casi dos meses.",
         visual=I("court_exterior", cap="LONDRES · JULIO DE 2023")),
    dict(id="s41", text="Pero tiene algo muy raro. Los psiquiatras dicen que Kurtaj, por su autismo severo, no está en condiciones de ser juzgado.",
         visual=I("courtroom", pop=["NO APTO PARA JUICIO"])),
    dict(id="s42", text="Entonces el jurado no puede declararlo culpable ni inocente. Solo puede decidir una cosa: si cometió los hechos o no.",
         visual=dict(type="versus", title="LO QUE DECIDE EL JURADO", left=["¿LO HIZO?", "SÍ SE DECIDE"], right=["¿CULPABLE?", "NO SE DECIDE"], mid="≠", lcol="yellow", rcol="red")),
    dict(id="s43", text="Y el veintitrés de agosto, por unanimidad, el jurado decide que sí: cometió doce delitos, entre ellos extorsión, fraude y ataques informáticos.",
         visual=dict(type="stamp", text="23 DE AGOSTO DE 2023\n12 DELITOS", stamp="LOS COMETIÓ")),
    dict(id="s44", text="El otro acusado, un chico de diecisiete años del mismo grupo, es declarado culpable de tres delitos.",
         visual=I("hackers_room")),
    dict(id="s45", text="En el juicio, Rockstar cuenta cuánto le costó todo: cinco millones de dólares y miles de horas de trabajo de su gente.",
         visual=dict(type="quote", text="5 MILLONES DE DÓLARES\n+ MILES DE HORAS")),
    dict(id="s46", text="La defensa contesta con otro dato. El primer tráiler de GTA seis hizo noventa millones de vistas en YouTube en un solo día, un récord Guinness. ¿Dónde está el daño grave?",
         visual=I("controller", pop=["90 MILLONES EN 24 H"])),
    dict(id="s47", text="En diciembre llega la decisión. Y sorprende a todos.",
         visual=I("courtroom", shake=True)),
    dict(id="s48", text="No es la cárcel: es una internación en un hospital de alta seguridad, por tiempo indefinido.",
         visual=dict(type="headline", kicker="diciembre de 2023", text="El hacker de GTA 6, internado en un hospital de seguridad por tiempo indefinido", mark="indefinido", source="Fuente: BBC / Reuters / Bloomberg Law")),
    dict(id="s49", text="El juez explica por qué: sus habilidades y sus ganas de cometer delitos informáticos lo convierten en un peligro para la gente.",
         visual=dict(type="quote", text="«SUS HABILIDADES\nY SUS GANAS DE\nCOMETER CIBERDELITOS»")),
    dict(id="s50", text="Y un informe médico agrega un dato inquietante: él seguía diciendo que quería volver al cibercrimen lo antes posible.",
         visual=I("hospital", pop=["VOLVER AL CIBERCRIMEN"], pop_col="red")),
    dict(id="s51", text="En la práctica, podía quedarse ahí toda la vida. Solo iba a salir el día que los médicos dijeran que ya no era un peligro.",
         visual=dict(type="stamp", text="SOLO SALE SI LOS MÉDICOS\nDICEN QUE NO ES UN PELIGRO", stamp="SIN FECHA")),

    # --- 05 DIEZ DÍAS ANTES DE GTA 6 ---
    dict(id="s52", text="Capítulo cinco. Diez días antes de GTA seis.",
         visual=dict(type="title", num="05", text="DIEZ DÍAS ANTES DE GTA 6", name="Diez días antes de GTA 6")),
    dict(id="s53", text="Durante más de dos años, Kurtaj está internado. Y mientras tanto, GTA seis se retrasa una y otra vez.",
         visual=I("hospital")),
    dict(id="s54", text="Primero iba a salir en dos mil veinticinco. Después, el veintiséis de mayo de dos mil veintiséis. Y al final, el diecinueve de noviembre.",
         visual=dict(type="timeline", title="GTA 6: LAS FECHAS", points=[["2025", "Primera fecha"], ["26 MAY 2026", "Segunda fecha"], ["19 NOV 2026", "Fecha final"]], hl=2)),
    dict(id="s55", text="Y en dos mil veintiséis, los médicos cambian de opinión: deciden que Kurtaj ya está en condiciones de enfrentar un juicio normal.",
         visual=I("prison", pop=["APTO PARA JUICIO"])),
    dict(id="s56", text="En julio, el periodista de la BBC Joe Tidy cuenta que lo sacaron del hospital y lo pasaron a una cárcel común, a la espera del juicio.",
         visual=dict(type="headline", kicker="julio de 2026", text="El hacker de GTA 6 deja el hospital y pasa a una cárcel común a la espera de un juicio", mark="cárcel común", source="Fuente: Joe Tidy (BBC) / PC Gamer")),
    dict(id="s57", text="Ni siquiera está claro por qué cambiaron de opinión ahora. Pero el resultado es enorme: esta vez lo pueden juzgar como a cualquier otro acusado.",
         visual=I("prison", shake=True)),
    dict(id="s58", text="En dos mil veintitrés solo se decidió si había cometido los hechos. Ahora se decide si es culpable. Y, si lo es, qué condena le corresponde.",
         visual=dict(type="versus", title="DOS JUICIOS", left=["2023", "¿LO HIZO?"], right=["2026", "¿ES CULPABLE?"], mid="→", lcol="yellow", rcol="red")),
    dict(id="s59", text="Según sus abogados, el juicio está fijado para el nueve de noviembre, en un tribunal de Londres. Mientras ves este video, puede que ya haya empezado.",
         visual=I("court_exterior", pop=["9 DE NOVIEMBRE"])),
    dict(id="s60", text="Mirá las fechas. El chico que filtró GTA seis desde un hotel vuelve al banquillo diez días antes de que el juego salga a la venta. Ni Rockstar lo hubiera escrito mejor.",
         visual=dict(type="timeline", title="DEL HOTEL AL JUICIO", points=[["SEP 2022", "Hackeo desde el hotel"], ["AGO 2023", "El jurado: fue él"], ["DIC 2023", "Hospital sin fecha de salida"], ["JUL 2026", "Pasa a una cárcel"], ["9 NOV", "Empieza el juicio"], ["19 NOV", "Sale GTA 6"]], hl=4)),
    dict(id="s61", text="Y ojo con lo que circula en redes. Este año aparecieron nuevas filtraciones de GTA seis desde una cuenta anónima llamada CyberLeek. Pero no hay ninguna fuente seria que la conecte con Kurtaj.",
         visual=I("forum_screen", pop=["¿CYBERLEEK?"])),
    dict(id="s62", text="¿Y a GTA seis qué le hizo todo esto? Al final, casi nada. Take Two espera facturar más de ocho mil millones de dólares este año fiscal, sobre todo gracias al juego.",
         visual=dict(type="num", start=0, end=8000, suffix=" M$", label="LO QUE TAKE-TWO ESPERA FACTURAR ESTE AÑO FISCAL")),
    dict(id="s63", text="Lo que sí queda es la historia de un chico que, con un aparato para ver series, puso en jaque a uno de los estudios más grandes del mundo. Y que ahora, por fin, va a escuchar un veredicto.",
         visual=I("hoodie_back")),
    dict(id="s64", text="Y ahora te pregunto a vos. Si lo declaran culpable, ¿tiene que ir preso? ¿O ya pagó con todo el tiempo que estuvo internado? Te leo en los comentarios.",
         visual=dict(type="quote", text="¿CÁRCEL?\n¿O YA PAGÓ\nCON EL HOSPITAL?")),
    dict(id="s65", text="Y suscribite, porque el diecinueve de noviembre arranca el gameplay de GTA seis acá en el canal. Todas las veces que haga falta.",
         visual=I("controller")),
]

# Pronunciación para la voz (solo TTS; subtítulos y SRT usan el texto normal).
PRONUNCIA = {
    "teapotuberhacker": "tí pot úber jáker", "Uber hacker": "Úber jáker", "Fire Stick": "Fáier Stik", "Rockstar Games": "Rokstar Guéims",
    "Rockstar": "Rokstar", "GTAForums": "ge te a fórums", "GTA seis": "ge te a seis", "GTA": "ge te a", "Take Two": "Teik Tu",
    "Travelodge": "Trávelodch", "Bicester": "Bíster", "Oxfordshire": "Óxfordshir", "Oxford": "Óxford", "Arion Kurtaj": "Árion Kurtái",
    "Kurtaj": "Kurtái", "Lapsus": "Lápsus", "Nvidia": "Envidia", "Revolut": "Révolut", "Uber": "Úber", "Telegram": "Télegram",
    "Joe Tidy": "Yóu Táidi", "BBC": "bi bi si", "CyberLeek": "Sáiber Lik", "Vice City": "Vais Síti", "Guinness": "Guínes",
    "YouTube": "Iutiub", "Microsoft": "Máicrosoft", "Samsung": "Sámsung", "Amazon": "Ámazon",
}

SHORTS = {}  # sin Shorts (pedido del usuario)

THUMBS = [
    dict(img="firestick", zoom=1.0, cx=0.5, cy=0.5, shade=["left", 230, 0.5], items=[
        ["text", 40, 70, "CON ESTO", 135, "white", "la"], ["text", 40, 250, "HACKEÓ", 135, "pink", "la"], ["text", 40, 430, "ROCKSTAR", 135, "yellow", "la"]]),
    dict(img="hotel_tv", zoom=1.05, cx=0.6, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "HACKEÓ", 180, "white", "la"], ["text", 45, 290, "ROCKSTAR", 160, "pink", "la"], ["badge", 45, 540, 640, 660, "DESDE UN HOTEL", 80]]),
    dict(img="court_exterior", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "10 DÍAS", 200, "yellow", "la"], ["text", 45, 310, "ANTES DE GTA 6", 110, "white", "la"], ["stamp", "JUICIO", 960, 540, -10, 130]]),
    dict(img="hospital", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "SIN FECHA", 170, "white", "la"], ["text", 45, 280, "DE SALIDA", 170, "pink", "la"], ["badge", 45, 540, 560, 660, "HACKER DE GTA 6", 70]]),
    dict(img="hoodie_back", zoom=1.08, cx=0.6, cy=0.45, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "17 AÑOS", 200, "yellow", "la"], ["text", 45, 320, "FILTRÓ GTA 6", 130, "white", "la"]]),
    dict(img="forum_screen", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "90 VIDEOS", 180, "pink", "la"], ["text", 45, 290, "FILTRADOS", 150, "white", "la"], ["badge", 45, 520, 470, 640, "GTA 6", 90]]),
    dict(img="prison", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "DEL HOSPITAL", 130, "white", "la"], ["text", 45, 230, "A LA CÁRCEL", 150, "pink", "la"], ["stamp", "GTA 6", 960, 540, -10, 120]]),
    dict(img="studio_office", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "\"NO SOY", 160, "white", "la"], ["text", 45, 260, "EMPLEADO\"", 160, "pink", "la"], ["badge", 45, 520, 620, 640, "SOY UN ATACANTE", 70]]),
    dict(img="hotel_tv", zoom=1.1, cx=0.65, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "5 MILLONES", 160, "yellow", "la"], ["text", 45, 270, "DESDE", 120, "white", "la"], ["text", 45, 410, "UN HOTEL", 150, "pink", "la"]]),
    dict(img="firestick", zoom=1.15, cx=0.6, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "UN APARATO", 140, "white", "la"], ["text", 45, 240, "DE 40 $", 170, "yellow", "la"], ["badge", 45, 500, 620, 620, "VS ROCKSTAR", 80]]),
]
THUMBS_TOP = [1, 3, 2]

META = {
    "code": "70x7_002",
    "name": "El hacker que filtró GTA 6",
    "intro_chapter": "Un hotel, una tele y un Fire Stick",
    "titles": [
        "Filtró GTA 6 desde un hotel… y ahora lo juzgan 10 días antes del lanzamiento",
        "El chico que hackeó Rockstar con un Fire Stick (y lo juzgan 10 días antes de GTA 6)",
        "La filtración de GTA 6: el hacker de 17 años que puso en jaque a Rockstar",
    ],
    "description": "En septiembre de 2022, un chico de 17 años encerrado en un hotel, sin computadora y vigilado por la policía, se metió en Rockstar con un Fire Stick enchufado a la tele y filtró 90 videos de GTA 6. Lo mandaron a un hospital de alta seguridad sin fecha de salida… y ahora, según sus abogados, su juicio estaba fijado para el 9 de noviembre, diez días antes del lanzamiento de GTA 6. La historia completa de Arion Kurtaj y Lapsus$: Nvidia, Uber, el chat interno de Rockstar, el juicio sin culpable y lo que puede pasar ahora.\n\n🦁 70x7: GTA 6 todas las veces que haga falta. Suscribite, el 19/11 arranca el gameplay.",
    "sources": [
        "Reuters / The Register / Infosecurity Magazine (agosto de 2023): el jurado de Southwark y los 12 delitos (Nvidia, Revolut, Uber, Rockstar)",
        "PC Gamer / NME / MobileSyrup (agosto de 2023, según la BBC): el hotel Travelodge de Bicester y el Amazon Fire Stick",
        "LBC / PA / ITPro (2023): los mensajes en el chat interno de Rockstar y la amenaza por Telegram",
        "Variety / GameSpot (19-sep-2022): Rockstar confirma la intrusión; caída de Take-Two antes de abrir",
        "GamesRadar (2023): Rockstar cifra el daño en 5 millones de dólares y miles de horas de trabajo",
        "TechRadar / Engadget / Bloomberg Law (diciembre de 2023): orden de internación indefinida",
        "Joe Tidy (BBC) vía PC Gamer / TechSpot (julio de 2026): traslado a una cárcel común",
        "Notebookcheck / OpenCritic / GamingHQ (octubre de 2026): juicio fijado para el 9 de noviembre en Woolwich Crown Court",
        "TechRadar / Take-Two (mayo de 2026): GTA 6 sale el 19 de noviembre de 2026; previsión de 8.000–8.200 M$",
        "Guinness World Records: 90,4 millones de vistas del tráiler 1 en 24 horas",
    ],
    "disclosure": "Las imágenes son ilustraciones generadas con IA: no muestran a las personas, lugares ni objetos reales del caso. Los mensajes del chat y la terminal son recreaciones; los textos del chat son una traducción de lo que se leyó en el juicio. Los titulares están parafraseados (se cita la fuente). Narración con voz sintética. Canal no afiliado a Rockstar Games ni a Take-Two.",
    "hashtags": "#GTA6 #Rockstar #GTAVI #70x7",
    "category": "Videojuegos",
    "playlist": "GTA 6: todo lo que sabemos",
    "tags": ["GTA 6", "GTA VI", "hacker GTA 6", "filtración GTA 6", "leak GTA 6", "Arion Kurtaj", "Lapsus", "Rockstar hackeo",
             "GTA 6 Fire Stick", "GTA 6 juicio", "GTA 6 noticias", "GTA 6 español", "GTA 6 19 de noviembre", "teapotuberhacker",
             "GTA 6 filtrado", "Rockstar Games", "70x7"],
    "pinned": "Si lo declaran culpable, ¿tiene que ir preso o ya pagó con el hospital? 👇 Y el 19/11 arranca el gameplay de GTA 6 en el canal 🦁",
    "shorts": {},
}
