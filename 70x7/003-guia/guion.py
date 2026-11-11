# 70x7 · Vídeo 003 — GTA 6 en 8 días: todo lo que tenés que saber antes del 19 (11-nov-2026)
# Tema por datos (API de YouTube, 11-nov): en inglés "Everything You Need To Know Before You Play GTA 6" 2,55M (GrandGecko),
# 484k (COLETHEMAN), "15 PS5 Tips" 544k; predescarga del 9-10 nov con 0,5–0,8M por vídeo. En español: LeaPRO 44k, Doublelag 7k,
# Grand Mosquer 3k. Búsqueda práctica ("a qué hora sale GTA 6 en Argentina") con mucho tráfico esta semana.
# Voz: Adán (como el 002). Sin Shorts. Visual: imágenes IA (DubVoice nano-banana-2-lite) + del 002 + tomas de Pexels + gráficos.
#
# Hechos verificados (WebSearch, 11-nov-2026):
# - Sale el 19-nov-2026 en PS5 y Xbox Series X|S (sin PC anunciado).
# - Horario: medianoche local del 19 en cada país según las tiendas (Rockstar no publicó un horario propio). Argentina: jueves 19
#   a las 00:00 (El Destape, Aire de Santa Fe, MDZ, 3DJuegos). España: 23:00 UTC del 18 (00:00 CET). México: 06:00 UTC (00:00 CST).
#   Nueva Zelanda primero: 08:00 del 18 en hora argentina (Aire de Santa Fe; MP1st "19 horas antes que México").
# - Predescarga: desde el 10-nov; en PS5 a medianoche local, en Xbox una sola vez a las 00:00 GMT (21:00 del 9 en Argentina);
#   solo para reservas digitales; hasta 212 GB según Rockstar; los códigos de las cajas se canjean desde el 12-nov (VGC, Dot Esports).
# - La edición en caja no trae disco: trae un código de descarga (Rockstar, vía VGC / Push Square / TechRadar). Un disco más
#   adelante: sin confirmar. Un código canjeado no se puede volver a usar (no se presta ni se revende como un disco).
# - Precio: estándar 79,99 USD, Ultimate 99,99 USD (TechRadar, TechSpot); reservas desde el 25-jun-2026; las reservas antes del
#   20-nov incluyen el "Vintage Vice City Pack". Argentina (Infobae, 25-jun): ~118.140 $ la estándar y ~147.700 $ la Ultimate en
#   PS Store; Sony pasó la tienda latinoamericana a moneda local desde el 20-ago (Notebookcheck) → el precio puede haber cambiado.
# - Del 70x7-001: seis zonas (Game Informer, 6-may-2025); tráiler 1 (dic-2023) 90.421.491 vistas en 24 h (Guinness); tráiler 2
#   (6-may-2025) 475 M en 24 h en todas las plataformas según Rockstar (TechRadar). Jason y Lucía, protagonistas (tráileres).
# - 30 FPS: Rob Nelson (Rockstar) dijo que las versiones de consola actuales van a 30 fps y que tenía que consultar al equipo técnico
#   por un modo de 60 (TechRadar, TweakTown); la ficha de PS Store muestra "PS5 Pro Enhanced". Tráiler de lanzamiento: 15-oct-2026,
#   grabado en PS5.
VOICE = "i4Kar2uamCWyas8TAu31"  # Adán (como el 70x7-002)
SPEED = 1.0
IMAGE_MODEL = "nano-banana-2-lite"
THEME = {"RED": (255, 56, 150), "YEL": (80, 230, 235)}  # rosa y celeste Vice City

def I(key, cap=None, pop=None, **kw):
    d = dict(type="img", key=key)
    if cap: d["cap"] = cap
    if pop: d["pop"] = pop
    d.update(kw); return d

N = ", photorealistic, cinematic lighting, 16:9, no text, no logos"
IMAGES = {
    "console_download": "a modern white game console on a TV stand in a dark living room at night, the big TV shows a glowing horizontal progress bar filling up, neon pink and cyan room lights" + N,
    "ssd_install": "close-up of hands installing a small NVMe SSD into the expansion slot of a game console, dramatic side lighting, dark background" + N,
    "empty_box": "an opened video game case on a wooden table, the disc holder is empty, only a small blank paper card inside, moody light" + N,
    "obelisco_night": "the Obelisk of Buenos Aires at midnight, empty avenue with neon reflections on wet asphalt, cinematic night" + N,
    "friends_midnight": "a group of young friends on a couch at midnight holding game controllers, faces lit by the blue glow of a TV, excited" + N,
    "earth_night": "the Earth seen from space at night with glowing city lights, the sunrise line crossing the Pacific near New Zealand" + N,
    "phone_spoilers": "a young man covering his eyes with one hand while holding a smartphone full of blurred colorful video thumbnails, dark room" + N,
    "neon_racing_tv": "a large TV in a dark room showing a motion blurred sports car racing through a neon tropical city at night, reflections on the floor" + N,
    "store_night": "young people queuing outside a video game store at night, neon pink and cyan lights, anticipation" + N,
    "pesos_controller": "Argentine peso banknotes and a credit card next to a black game controller on a dark table, dramatic light" + N,
    "swamp_airboat": "a Florida style swamp at golden hour with an airboat gliding through tall grass, humid haze" + N,
    "highway_neon": "an elevated highway at night in a tropical city with palm trees and pink and cyan neon lights, light trails" + N,
}

SCENES = [
    # --- GANCHO ---
    dict(id="s01", text="Faltan ocho días para GTA seis. Y hay cosas que tenés que saber ya, porque te pueden arruinar el diecinueve.",
         visual=I("neon_city", pop=["FALTAN 8 DÍAS"])),
    dict(id="s02", text="En Nueva Zelanda lo van a estar jugando dieciséis horas antes que nosotros en Argentina. La caja que compres en una tienda no trae disco. Y el juego pesa más de doscientos gigas.",
         visual=dict(type="stamp", text="16 HORAS ANTES\nSIN DISCO · 212 GB", stamp="OJO", col="yellow")),
    dict(id="s03", text="Así que en este video te cuento todo lo que necesitás para llegar listo: a qué hora sale, cómo predescargarlo, cuánto cuesta y por qué va a treinta cuadros por segundo.",
         visual=dict(type="timeline", title="LO QUE VAS A SABER", points=[["HORA", "A qué hora sale"], ["212 GB", "La predescarga"], ["CAJA", "Sin disco"], ["PRECIO", "Cuánto cuesta"], ["30 FPS", "El rendimiento"]], hl=0)),
    dict(id="s04", text="Quedate hasta el final, que te dejo una lista para tener todo preparado antes de la medianoche. Arrancamos.",
         visual=I("controller")),

    # --- 01 A QUÉ HORA SALE ---
    dict(id="s05", text="Capítulo uno. A qué hora sale.",
         visual=dict(type="title", num="01", text="A QUÉ HORA SALE", name="A qué hora sale")),
    dict(id="s06", text="GTA seis sale el jueves diecinueve de noviembre, en PlayStation cinco y en Xbox Series. De PC, por ahora, nada.",
         visual=dict(type="versus", title="19 DE NOVIEMBRE", left=["PS5", "SÍ"], right=["PC", "POR AHORA NO"], mid="·", lcol="yellow", rcol="red")),
    dict(id="s07", text="Rockstar no publicó un horario propio. Lo que manda son las tiendas digitales, y en las tiendas el juego se habilita a la medianoche de cada país.",
         visual=I("obelisco_night", pop=["MEDIANOCHE LOCAL"])),
    dict(id="s08", text="En Argentina, eso significa el jueves diecinueve a las doce de la noche en punto. Es decir, apenas termina el miércoles dieciocho.",
         visual=dict(type="year", year="00:00", sub="JUEVES 19 · HORA ARGENTINA")),
    dict(id="s09", text="Y en Chile y Uruguay, a la misma hora que en Argentina, porque en noviembre comparten huso horario.",
         visual=I("obelisco_night", cap="ARGENTINA · CHILE · URUGUAY")),
    dict(id="s10", text="Ahora, mirá lo que pasa en el resto del mundo, todo en hora argentina.",
         visual=I("earth_night")),
    dict(id="s11", text="Nueva Zelanda es el primero: lo habilita el miércoles dieciocho a las ocho de la mañana. España, ese mismo miércoles a las ocho de la noche. Nosotros, a la medianoche. Y México, a las tres de la mañana del jueves.",
         visual=dict(type="board", title="GTA 6 · HORA ARGENTINA", rows=[
             ["08:00 · MIÉ 18", "Nueva Zelanda", "PS5 · XBOX", "PRÓXIMAMENTE"],
             ["20:00 · MIÉ 18", "España", "PS5 · XBOX", "PRÓXIMAMENTE"],
             ["00:00 · JUE 19", "Argentina", "PS5 · XBOX", "PRÓXIMAMENTE"],
             ["00:00 · JUE 19", "Chile · Uruguay", "PS5 · XBOX", "PRÓXIMAMENTE"],
             ["02:00 · JUE 19", "Colombia · Perú", "PS5 · XBOX", "PRÓXIMAMENTE"],
             ["03:00 · JUE 19", "México", "PS5 · XBOX", "PRÓXIMAMENTE"]], final="DISPONIBLE", step=0.55, cols=[0, 330, 880, 1170])),
    dict(id="s12", text="Eso quiere decir que mientras vos estás en el trabajo o en el colegio el miércoles, en la otra punta del mundo ya hay gente jugando. Y subiendo todo a internet.",
         visual=I("phone_spoilers", pop=["16 HORAS DE SPOILERS"], pop_col="red")),
    dict(id="s13", text="Así que el consejo es simple: el miércoles, silenciá en tus redes palabras como GTA seis, Jason, Lucía o Vice City. Y no entres a YouTube sin cuidado.",
         visual=dict(type="chat", title="# configuración · palabras silenciadas", kicker="consejo para el miércoles 18", msgs=[
             ["70x7", "Silenciá: GTA 6, GTA VI, Jason, Lucía, Vice City", "alert"],
             ["70x7", "Y ojo con las miniaturas de YouTube ese día"]])),
    dict(id="s14", text="Y una aclaración: en Xbox, las tiendas muestran los mismos horarios que en PlayStation, país por país.",
         visual=I("friends_midnight")),

    # --- 02 LA PREDESCARGA ---
    dict(id="s15", text="Capítulo dos. La predescarga.",
         visual=dict(type="title", num="02", text="LA PREDESCARGA", name="La predescarga")),
    dict(id="s16", text="La buena noticia: si ya lo reservaste en digital, no tenés que esperar al diecinueve para bajarlo. La predescarga ya empezó.",
         visual=I("console_download", pop=["YA EMPEZÓ"])),
    dict(id="s17", text="Arrancó el martes diez de noviembre. En PlayStation se habilitó a la medianoche de cada país. En Xbox, a la misma hora en todo el mundo: en Argentina, el lunes nueve a las nueve de la noche.",
         visual=dict(type="versus", title="PREDESCARGA", left=["PS5", "MAR 10 · 00:00"], right=["XBOX", "LUN 9 · 21:00 (AR)"], mid="·", lcol="yellow", rcol="red")),
    dict(id="s18", text="Y ahora, el número que asusta. Según Rockstar, el juego ocupa hasta doscientos doce gigas.",
         visual=dict(type="num", start=0, end=212, suffix=" GB", label="LO QUE OCUPA GTA 6 (SEGÚN ROCKSTAR)")),
    dict(id="s19", text="Para que te des una idea, es como tener varios juegos grandes instalados al mismo tiempo. Si tenés la consola llena, el diecinueve no vas a poder jugar.",
         visual=I("ssd_install", pop=["LIBERÁ ESPACIO"])),
    dict(id="s20", text="El tamaño exacto depende de tu consola: la tienda te lo muestra antes de bajarlo. Así que hoy, no el diecinueve, revisá cuánto espacio libre te queda.",
         visual=dict(type="terminal", title="almacenamiento", lines=["> espacio libre: revisar hoy", "> gta6 predescarga: hasta 212 GB", "> internet: dejar bajando de noche", "!> no esperar al 19"])),
    dict(id="s20b", text="Y si tu internet no es rápida, hacé la cuenta: bajar doscientos doce gigas puede llevar muchas horas. Dejalo descargando de noche, durante varios días si hace falta.",
         visual=I("console_download", pop=["DEJALO BAJANDO DE NOCHE"])),
    dict(id="s21", text="Un detalle importante: la predescarga es solo para quienes reservaron la versión digital. ¿Y los que compraron la caja? Ahí viene la sorpresa.",
         visual=I("store_night")),

    # --- 03 LA CAJA SIN DISCO ---
    dict(id="s22", text="Capítulo tres. La caja sin disco.",
         visual=dict(type="title", num="03", text="LA CAJA SIN DISCO", name="La caja sin disco")),
    dict(id="s23", text="Rockstar lo confirmó: la edición física de lanzamiento no trae disco. Abrís la caja y adentro hay un código para descargar el juego.",
         visual=I("empty_box", pop=["SIN DISCO"], pop_col="red")),
    dict(id="s24", text="Sí, el juego más esperado de la historia, y la caja es básicamente un papelito con un código.",
         visual=dict(type="headline", kicker="Rockstar", text="La edición física de GTA 6 trae un código de descarga dentro de la caja, no un disco", mark="código", source="Fuente: VGC / Push Square / TechRadar")),
    dict(id="s25", text="Esos códigos se pueden canjear desde el doce de noviembre. Así que si compraste la caja, canjealo apenas puedas, y vas a poder bajarlo antes del lanzamiento.",
         visual=dict(type="timeline", title="SI COMPRASTE LA CAJA", points=[["10 NOV", "Predescarga digital"], ["12 NOV", "Canjeás el código"], ["19 NOV", "A jugar"]], hl=1)),
    dict(id="s26", text="Pero ojo con lo que eso implica. Un código, una vez canjeado, no se puede volver a usar. No lo vas a poder prestar ni revender como un disco.",
         visual=dict(type="versus", title="CÓDIGO VS DISCO", left=["DISCO", "SE PRESTA Y SE VENDE"], right=["CÓDIGO", "UNA SOLA CUENTA"], mid="VS", lcol="yellow", rcol="red")),
    dict(id="s27", text="Y vas a necesitar internet y los mismos doscientos gigas libres, igual que en digital.",
         visual=I("console_download", pop=["INTERNET + 212 GB"])),
    dict(id="s28", text="¿Va a salir un disco más adelante? Hay rumores que dicen que sí, en los meses siguientes al lanzamiento. Pero no hay nada confirmado.",
         visual=dict(type="stamp", text="¿DISCO MÁS ADELANTE?", stamp="SIN CONFIRMAR", col="yellow")),

    # --- 04 CUÁNTO CUESTA ---
    dict(id="s29", text="Capítulo cuatro. Cuánto cuesta.",
         visual=dict(type="title", num="04", text="CUÁNTO CUESTA", name="Cuánto cuesta")),
    dict(id="s30", text="Rockstar fijó dos ediciones. La estándar, a setenta y nueve dólares con noventa y nueve. Y la Ultimate, a noventa y nueve con noventa y nueve.",
         visual=dict(type="bars", title="PRECIO OFICIAL (USD)", data=[["ESTÁNDAR", 79.99], ["ULTIMATE", 99.99]])),
    dict(id="s31", text="Es más caro que el precio de siempre de los juegos grandes, que era de setenta dólares. Pero menos de los cien que muchos temían para la edición base.",
         visual=I("pesos_controller", pop=["MÁS CARO QUE LOS 70 DE SIEMPRE"])),
    dict(id="s32", text="La Ultimate suma ropa, vehículos y armas exclusivas, y acceso a vendedores y lugares especiales dentro del juego.",
         visual=I("highway_neon", pop=["ULTIMATE"])),
    dict(id="s33", text="Y si lo reservás antes del veinte de noviembre, te llevás de regalo un paquete llamado Vintage Vice City.",
         visual=dict(type="stamp", text="RESERVA ANTES DEL 20 DE NOVIEMBRE", stamp="+ VINTAGE VICE CITY", col="green")),
    dict(id="s34", text="¿Y en pesos? En junio, cuando abrieron las reservas, en la PlayStation Store argentina la estándar rondaba los ciento dieciocho mil pesos, y la Ultimate, unos ciento cuarenta y ocho mil.",
         visual=dict(type="versus", title="ARGENTINA · JUNIO 2026 (PS STORE)", left=["ESTÁNDAR", "≈ $118.000"], right=["ULTIMATE", "≈ $148.000"], mid="·", lcol="yellow", rcol="red")),
    dict(id="s35", text="Pero cuidado: desde agosto, Sony pasó su tienda latinoamericana a moneda local, y el precio pudo cambiar. Antes de comprar, fijate el precio final en la tienda.",
         visual=I("pesos_controller", pop=["FIJATE EL PRECIO HOY"], pop_col="red")),
    dict(id="s36", text="Y si querés el detalle país por país en Latinoamérica, en el canal tenés un video entero sobre el precio y la consola.",
         visual=I("forum_screen")),

    # --- 05 POR QUÉ 30 FPS ---
    dict(id="s37", text="Capítulo cinco. Por qué va a treinta cuadros por segundo.",
         visual=dict(type="title", num="05", text="POR QUÉ VA A 30 FPS", name="Por qué va a 30 FPS")),
    dict(id="s38", text="Esta es la pregunta que más se repite. Y la respuesta la dio el propio Rockstar.",
         visual=I("neon_racing_tv")),
    dict(id="s39", text="Rob Nelson, uno de sus responsables, dijo que las versiones de consola actuales corren a treinta cuadros por segundo. Y que tenía que consultar con su equipo técnico si era posible un modo a sesenta.",
         visual=dict(type="headline", kicker="Rob Nelson, Rockstar", text="Las versiones de consola actuales de GTA 6 corren a 30 cuadros por segundo", mark="30 cuadros", source="Fuente: TechRadar / TweakTown (parafraseado)")),
    dict(id="s40", text="Es decir: treinta está confirmado para lo que hoy funciona. Sesenta, ni confirmado ni descartado.",
         visual=dict(type="versus", title="CUADROS POR SEGUNDO", left=["30 FPS", "LO QUE HAY HOY"], right=["60 FPS", "SIN CONFIRMAR"], mid="VS", lcol="yellow", rcol="red")),
    dict(id="s41", text="¿Por qué no sesenta? Porque cada cuadro tiene que mostrar una ciudad gigante, llena de gente, autos, luces y reflejos. A treinta, la consola tiene el doble de tiempo para dibujar cada imagen.",
         visual=I("highway_neon", pop=["EL DOBLE DE TIEMPO POR CUADRO"])),
    dict(id="s42", text="¿Y la PS cinco Pro? En la ficha de la PlayStation Store ya aparece la etiqueta de mejorado para PS cinco Pro. Qué mejora exactamente, todavía no se sabe.",
         visual=dict(type="stamp", text="PS5 PRO ENHANCED", stamp="¿QUÉ MEJORA?", col="yellow")),
    dict(id="s43", text="Lo que sí sabemos es que el tráiler de lanzamiento, el que salió el quince de octubre, se grabó entero en una PS cinco normal. Lo que viste ahí es lo que vas a tener.",
         visual=I("neon_city", pop=["GRABADO EN UNA PS5"])),

    # --- 06 POR SI LLEGASTE TARDE ---
    dict(id="s43b", text="Capítulo seis. Por si llegaste tarde.",
         visual=dict(type="title", num="06", text="POR SI LLEGASTE TARDE", name="Por si llegaste tarde")),
    dict(id="s43c", text="Si no seguiste nada de GTA seis hasta ahora, en un minuto te pongo al día.",
         visual=I("swamp_airboat")),
    dict(id="s43d", text="El juego transcurre en Leonida, un estado inventado inspirado en Florida. Y la ciudad principal es una vieja conocida: Vice City, la versión de Rockstar de Miami.",
         visual=I("neon_city", pop=["LEONIDA", "VICE CITY"])),
    dict(id="s43e", text="Rockstar ya mostró seis zonas: Vice City, los cayos de Leonida, Grassrivers, Port Gellhorn, Ambrosia y Mount Kalaga.",
         visual=dict(type="route", title="LEONIDA: LAS 6 ZONAS", points={"Mount Kalaga": [0.30, 0.22], "Ambrosia": [0.50, 0.30], "Port Gellhorn": [0.24, 0.42], "Grassrivers": [0.52, 0.58], "Vice City": [0.70, 0.66], "Leonida Keys": [0.48, 0.86]},
                     routes=[["Vice City", "Grassrivers"], ["Grassrivers", "Ambrosia"], ["Vice City", "Leonida Keys"]])),
    dict(id="s43f", text="Los protagonistas son dos: Jason y Lucía, una pareja que se mete en el mundo del crimen. Como en GTA cinco, vamos a manejar a más de un personaje.",
         visual=I("highway_neon", pop=["JASON", "LUCÍA"])),
    dict(id="s43g", text="Y la expectativa es histórica. El primer tráiler, en diciembre de dos mil veintitrés, hizo más de noventa millones de vistas en YouTube en veinticuatro horas: récord Guinness.",
         visual=dict(type="num", start=0, end=90421491, label="VISTAS DEL TRÁILER 1 EN 24 HORAS (YOUTUBE)")),
    dict(id="s43h", text="Y el segundo, en mayo de dos mil veinticinco, según Rockstar sumó cuatrocientos setenta y cinco millones de vistas en un día, contando todas las plataformas.",
         visual=dict(type="num", start=0, end=475000000, label="VISTAS DEL TRÁILER 2 EN 24 H (TODAS LAS PLATAFORMAS)")),

    # --- 07 LA LISTA PARA EL 19 ---
    dict(id="s44", text="Capítulo siete. La lista para el diecinueve.",
         visual=dict(type="title", num="07", text="LA LISTA PARA EL 19", name="La lista para el 19")),
    dict(id="s45", text="Te dejo todo resumido, para que no se te pase nada.",
         visual=I("friends_midnight")),
    dict(id="s46", text="Uno: liberá espacio. Hasta doscientos doce gigas. Hacelo hoy.",
         visual=dict(type="terminal", title="lista para el 19", lines=["> 1. liberar hasta 212 GB"])),
    dict(id="s47", text="Dos: si es digital, dejalo predescargando. Si es la caja, canjeá el código desde el doce.",
         visual=dict(type="terminal", title="lista para el 19", lines=["> 1. liberar hasta 212 GB", "> 2. predescargar / canjear código (12/11)"])),
    dict(id="s48", text="Tres: el miércoles, silenciá las palabras clave en tus redes para esquivar los spoilers de Nueva Zelanda.",
         visual=dict(type="terminal", title="lista para el 19", lines=["> 1. liberar hasta 212 GB", "> 2. predescargar / canjear código (12/11)", "> 3. silenciar spoilers el miércoles"])),
    dict(id="s49", text="Cuatro: si todavía no lo reservaste, hacelo antes del veinte para llevarte el paquete de regalo. Y fijate el precio final en pesos.",
         visual=dict(type="terminal", title="lista para el 19", lines=["> 1. liberar hasta 212 GB", "> 2. predescargar / canjear código (12/11)", "> 3. silenciar spoilers el miércoles", "> 4. reservar antes del 20 (precio en pesos)"])),
    dict(id="s50", text="Y cinco: poné la alarma. Jueves diecinueve, a las doce de la noche en punto.",
         visual=dict(type="terminal", title="lista para el 19", lines=["> 1. liberar hasta 212 GB", "> 2. predescargar / canjear código (12/11)", "> 3. silenciar spoilers el miércoles", "> 4. reservar antes del 20 (precio en pesos)", "!> 5. alarma: jueves 19, 00:00"])),
    dict(id="s50b", text="Y si te toca trabajar el jueves, tranquilo: el juego no se va a ningún lado. Lo importante es que el diecinueve no te encuentre sin espacio o con el código sin canjear.",
         visual=I("friends_midnight", pop=["SIN APURO, PERO LISTO"])),
    dict(id="s51", text="Trece años después de GTA cinco, y después de dos retrasos, ahora sí: falta una semana.",
         visual=I("swamp_airboat", pop=["FALTA UNA SEMANA"])),
    dict(id="s52", text="Y ahora te pregunto a vos: ¿a qué hora lo vas a empezar? ¿A la medianoche, o lo dejás para el fin de semana? Te leo en los comentarios.",
         visual=dict(type="versus", title="¿Y VOS?", left=["00:00", "APENAS SALE"], right=["FINDE", "CON CALMA"], mid="¿?", lcol="yellow", rcol="red")),
    dict(id="s53", text="Suscribite, porque el diecinueve arranca el gameplay de GTA seis acá en el canal. Todas las veces que haga falta.",
         visual=I("controller")),
]

PRONUNCIA = {
    "GTA seis": "ge te a seis", "GTA cinco": "ge te a cinco", "GTA": "ge te a", "Rockstar": "Rokstar", "PlayStation Store": "Pléisteishon Stor",
    "PlayStation cinco": "Pléisteishon cinco", "PlayStation": "Pléisteishon", "PS cinco Pro": "pe ese cinco Pro", "PS cinco": "pe ese cinco",
    "Xbox Series": "Équis Box Síris", "Xbox": "Équis Box", "PC": "pe ce", "YouTube": "Iutiub", "Vice City": "Vais Síti",
    "Vintage Vice City": "Víntach Vais Síti", "Ultimate": "Áltimet", "Rob Nelson": "Rob Nélson", "Leonida": "Leónida", "Grassrivers": "Grasríverz", "Port Gellhorn": "Port Guélhorn", "Mount Kalaga": "Maunt Kalága", "Guinness": "Guínes", "Jason": "Yéison", "Lucía": "Lucía",
    "Nueva Zelanda": "Nueva Zelanda",
}

SHORTS = {}  # sin Shorts (como el 002)

THUMBS = [
    dict(img="obelisco_night", zoom=1.05, cx=0.5, cy=0.5, bright=0.55, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "00:00", 230, "yellow", "la"], ["text", 45, 340, "EN ARGENTINA", 120, "white", "la"], ["badge", 45, 540, 470, 660, "GTA 6", 100]]),
    dict(img="empty_box", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 50, "SIN", 200, "pink", "la"], ["text", 45, 290, "DISCO", 190, "white", "la"], ["badge", 45, 575, 470, 690, "GTA 6", 100]]),
    dict(img="console_download", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "212 GB", 220, "yellow", "la"], ["text", 45, 330, "PREDESCARGA", 120, "white", "la"], ["badge", 45, 530, 470, 650, "GTA 6", 100]]),
    dict(img="phone_spoilers", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "16 HORAS", 190, "pink", "la"], ["text", 45, 310, "ANTES", 170, "white", "la"], ["badge", 45, 540, 620, 660, "OJO CON LOS SPOILERS", 70]]),
    dict(img="neon_racing_tv", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "30 FPS", 220, "yellow", "la"], ["text", 45, 330, "¿POR QUÉ?", 160, "white", "la"]]),
    dict(img="neon_city", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "GTA 6", 220, "pink", "la"], ["text", 45, 330, "TODO ANTES", 130, "white", "la"], ["text", 45, 480, "DEL 19", 140, "yellow", "la"]]),
    dict(img="earth_night", zoom=1.05, cx=0.6, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "A QUÉ HORA", 150, "white", "la"], ["text", 45, 250, "SALE GTA 6", 150, "yellow", "la"], ["badge", 45, 470, 600, 590, "EN CADA PAÍS", 80]]),
    dict(img="pesos_controller", zoom=1.05, cx=0.6, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "¿CUÁNTO", 170, "white", "la"], ["text", 45, 280, "CUESTA?", 170, "yellow", "la"], ["badge", 45, 520, 470, 640, "GTA 6", 100]]),
    dict(img="friends_midnight", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "FALTAN", 180, "white", "la"], ["text", 45, 290, "8 DÍAS", 210, "pink", "la"], ["badge", 45, 540, 470, 660, "GTA 6", 100]]),
    dict(img="console_download", zoom=1.12, cx=0.6, cy=0.5, shade=["left", 230, 0.62], items=[
        ["text", 45, 60, "NO ESPERES", 150, "white", "la"], ["text", 45, 250, "AL 19", 200, "yellow", "la"], ["badge", 45, 500, 600, 620, "HACÉ ESTO HOY", 80]]),
]
THUMBS_TOP = [1, 2, 7]

META = {
    "code": "70x7_003",
    "name": "GTA 6: todo antes del 19",
    "intro_chapter": "Faltan 8 días",
    "titles": [
        "GTA 6: a qué hora sale en Argentina (y 4 cosas que tenés que hacer ANTES del 19)",
        "GTA 6 en 8 días: hora, predescarga de 212 GB, la caja sin disco y los 30 FPS",
        "No esperes al 19: lo que tenés que saber de GTA 6 antes de jugar",
    ],
    "description": "GTA 6 sale el jueves 19 de noviembre a las 00:00 en Argentina (medianoche local en cada país, según las tiendas). Nueva Zelanda lo habilita 16 horas antes, la edición física no trae disco (es un código), la predescarga ya empezó y ocupa hasta 212 GB, y Rockstar dice que en consola va a 30 FPS. Horarios país por país en hora argentina, cómo predescargarlo, cuánto cuesta en dólares y en pesos, por qué 30 FPS y la lista de lo que tenés que hacer antes de la medianoche.\n\n🦁 70x7: GTA 6 todas las veces que haga falta. Suscribite, el 19/11 arranca el gameplay.",
    "sources": [
        "El Destape / Aire de Santa Fe / MDZ / 3DJuegos (nov-2026): horario de lanzamiento en Argentina y por país",
        "MP1st / GamerFuzion (nov-2026): horarios de desbloqueo por región",
        "VGC / Dot Esports / KeenGamer (nov-2026): predescarga desde el 10 de noviembre, hasta 212 GB",
        "VGC / Push Square / TechRadar (2026): la edición física trae un código, no un disco",
        "TechRadar / TechSpot / Esquire India (jun-2026): precios oficiales y bonificación por reserva",
        "Infobae (25-jun-2026) y Notebookcheck: precios en Argentina y cambio a moneda local en PS Store",
        "TechRadar / TweakTown (2026): Rob Nelson sobre los 30 FPS; ficha de PS Store \"PS5 Pro Enhanced\"",
        "Tomas de vídeo: Pexels — Franco Molinari, SHVETS production, MART PRODUCTION, Pixabay, Joshua Malic, Foster, Ege Tutuncu, MIA Alaska TV, Media Hopper Studio, Kaboompics, Ron Lach, Kuiyibo Campos",
    ],
    "disclosure": "Las tomas de vídeo son de Pexels (autores en las fuentes) y algunas imágenes son ilustraciones generadas con IA: nada de eso muestra el juego. Los horarios son los que muestran las tiendas digitales; confirmalos en tu consola cerca de la fecha. Narración con voz sintética. Canal no afiliado a Rockstar Games ni a Take-Two.",
    "hashtags": "#GTA6 #GTAVI #Rockstar #70x7",
    "category": "Videojuegos",
    "playlist": "GTA 6: todo lo que sabemos",
    "tags": ["GTA 6", "GTA VI", "a qué hora sale GTA 6", "GTA 6 Argentina", "GTA 6 hora Argentina", "GTA 6 predescarga", "GTA 6 212 GB",
             "GTA 6 sin disco", "GTA 6 precio", "GTA 6 precio Argentina", "GTA 6 30 fps", "GTA 6 PS5", "GTA 6 19 de noviembre",
             "GTA 6 México", "GTA 6 España", "GTA 6 español", "70x7"],
    "pinned": "¿A qué hora lo vas a empezar: a las 00:00 del jueves o el finde? 👇 El 19/11 arranca el gameplay en el canal 🦁",
    "shorts": {},
}
