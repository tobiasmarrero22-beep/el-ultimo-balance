# Vídeo 010 — Cómo nació la NASA… y cómo 50 años después salvó a SpaceX (17 min, sin Shorts)
# Pedido del usuario (13-nov-2026): "cómo nació la NASA y lo de 50 años después" (idea: la Navidad de 2008 de Musk).
# Datos (API de YouTube, 13-nov): la historia general de Musk está saturada en español, pero "2008, casi lo pierde todo" solo tiene
# Shorts en inglés (9,9 M y 1,3 M) y largos en español de ≤1.128 vistas.
# Hechos verificados (WebSearch, 13-nov-2026):
# - Sputnik 1: 4-oct-1957; esfera de 58 cm, 4 antenas, ~83 kg (183 lb); órbita de ~96 min; emitió 21 días; reentró el 4-ene-1958.
#   Sputnik 2 con Laika: 3-nov-1957. Audiencias en el Congreso → creación de la NASA (NASA History).
# - Vanguard TV3: 6-dic-1957, sube ~1,2 m, cae y explota en directo por televisión; NYT: "golpe al prestigio de EE. UU."; Lyndon
#   Johnson: "humillante". Apodos de la prensa: Flopnik/Kaputnik. Explorer 1: 31-ene-1958 (Ejército, equipo de von Braun; satélite
#   del JPL) → cinturones de Van Allen. Vanguard 1: 17-mar-1958, primer satélite solar; sigue en órbita (el objeto humano más antiguo).
# - NASA: ley firmada por Eisenhower el 29-jul-1958; funciona desde el 1-oct-1958; absorbe el NACA (1915): ~8.000 empleados,
#   ~100 M$/año, laboratorios. Primer administrador T. Keith Glennan (Case Institute, Cleveland) con Hugh Dryden de número dos.
#   Mercury 7: abril de 1959 (incluye a Gordon Cooper). Gagarin 12-abr-1961; Shepard 5-may-1961 (15 min, suborbital); Kennedy,
#   25-may-1961. NASA = 4,41 % del presupuesto federal en 1966; ~400.000 personas en Apolo. Apolo 11: 20-jul-1969.
# - Transbordador: 1981-2011; Challenger (1986) y Columbia (2003), 14 muertos. COTS: 18-ago-2006, SpaceX 278 M$ y Rocketplane
#   Kistler (no reunió financiación; fuera, sustituida por Orbital en 2008). Soyuz: la NASA pagó de 21 a 86 M$ por asiento (OIG).
# - Musk: viajes a Moscú en oct-2001 y feb-2002 para comprar ICBM reconvertidos (Dnepr); Mars Oasis (invernadero en Marte);
#   SpaceX en 2002. Falcon 1 desde Omelek (atolón de Kwajalein). Fallos: 24-mar-2006, 21-mar-2007, 2/3-ago-2008 (error de
#   sincronización, choque entre etapas; llevaba Trailblazer, dos cubesats de la NASA y cenizas de ~208 personas, entre ellas James
#   Doohan y Gordon Cooper). 28-sep-2008: órbita con RatSat (165 kg), primer cohete de combustible líquido de desarrollo privado.
# - 23-dic-2008: contratos CRS de la NASA: SpaceX 12 vuelos ≈1.600 M$; Orbital 8 vuelos ≈1.900 M$. 24-dic-2008: Tesla cierra una
#   ronda de ~40 M$ a las 18:00, "la última hora del último día posible" (Musk); si no, las nóminas rebotaban 2 días después de Navidad.
# - Dragon: dic-2010 primera nave privada recuperada de la órbita; may-2012 primera nave comercial en la ISS. Aterrizaje de primera
#   etapa: dic-2015. Commercial Crew (16-sep-2014): Boeing 4.200 M$, SpaceX 2.600 M$. Demo-2: 30-may-2020, primer lanzamiento tripulado
#   desde EE. UU. desde 2011. Starliner: vuelve vacía (sep-2024); Wilmore y Williams vuelven en una Dragon el 18-mar-2025 (286 días).
#   HLS Starship: abr-2021, 2.890 M$. Artemis II: abril de 2026, 4 astronautas rodean la Luna (primeros desde 1972).
#   SpaceX (fusionada con xAI en feb-2026) sale a bolsa el 12-jun-2026 a 135 $/acción: ~1,77 billones de dólares (CNBC/Reuters).
VOICE = "i4Kar2uamCWyas8TAu31"  # ElevenLabs "Adán - Narration"
SPEED = 1.0
IMAGE_MODEL = "nano-banana-2-lite"

N = ", photorealistic, cinematic lighting, 16:9, no text, no logos, no flags with readable symbols"
V = ", vintage 1950s film photograph look, film grain, faded colors"
IMAGES = {
    "empty_office_night": "Silhouette of a man seen from behind sitting alone at a desk in a dark industrial office at night, rocket parts visible through a glass wall, lonely and tense" + N,
    "stock_crash_2008": "Trading floor in 2008 with screens glowing red and falling charts, traders with hands on heads seen from behind, no readable text" + N,
    "rocket_fail": "Small two-stage rocket breaking apart in the sky above the ocean, smoke trail spiraling, debris, dramatic" + N,
    "radio_1957": "1950s American family gathered around a large wooden radio in a living room at night, listening with worried faces" + V + N,
    "saturn_launch": "Giant white moon rocket lifting off at dawn with a massive column of fire and smoke, 1969 film look" + N,
    "sputnik_orbit": "Polished metal sphere satellite with four long thin antennas orbiting above the Earth, black space, sunlight glinting" + N,
    "night_sky_1957": "People on a 1950s American small-town street at night looking up at the starry sky, pointing, cars from the 1950s" + V + N,
    "dog_capsule": "Small mixed-breed dog sitting calmly inside a cramped vintage spacecraft capsule with dials and harness, soft light" + N,
    "congress_hearing": "1950s congressional hearing room, men in suits seated at a long wooden table with microphones, seen from behind, tense" + V + N,
    "tv_1957": "1950s family watching a small black-and-white television in a living room, glow on their faces, rocket on the screen" + V + N,
    "vanguard_pad": "Slender white 1950s rocket standing on a launch pad at Cape Canaveral, service tower beside it, morning light" + V + N,
    "vanguard_explosion": "1950s rocket exploding in a huge fireball on its launch pad, black smoke, black and white film look" + N,
    "explorer_launch": "1958 night rocket launch at Cape Canaveral, bright flame lighting the pad and the smoke, vintage film photograph" + N,
    "signing_desk": "Close-up of hands in a suit signing an official document with a fountain pen on a wooden desk in 1958, flags blurred behind, no faces" + V + N,
    "naca_meeting": "Final meeting of the NACA in 1958 (archive photo, NASA)",
    "hangar_naca": "1950s aeronautics laboratory with a large wind tunnel and engineers in white shirts and ties seen from behind, chalkboards" + V + N,
    "astronauts_silver": "Seven astronauts in silver pressure suits walking side by side seen from behind on an airfield in 1959" + V + N,
    "rocket_factory_60s": "Huge 1960s rocket factory with giant cylindrical rocket stages, workers on scaffolding seen from behind" + V + N,
    "moon_footprint": "Close-up of an astronaut boot print in grey lunar dust, harsh sunlight, black sky" + N,
    "shuttle_launch": "Space shuttle lifting off from its launch pad with a huge white smoke plume and bright flames, blue sky" + N,
    "shuttle_hangar": "Retired space shuttle orbiter displayed inside a huge dim museum hangar, quiet atmosphere" + N,
    "soyuz_steppe": "Russian rocket on a launch pad in the snowy Kazakh steppe at night, floodlights, steam, cold atmosphere" + N,
    "moscow_winter": "Moscow street in winter in the early 2000s at dusk, snow falling, old cars, grey buildings, no readable signs" + N,
    "greenhouse_mars": "Small transparent greenhouse with green plants growing inside, standing on the red rocky surface of Mars under a dusty sky" + N,
    "rocket_factory": "Modern rocket factory with a long white rocket stage on stands, engineers in polo shirts working, bright industrial light" + N,
    "pacific_island": "Tiny tropical island in the middle of the Pacific Ocean with a small rocket on a launch pad, palm trees, turquoise water, aerial view" + N,
    "control_room": "Small rocket launch control room in the 2000s with engineers watching screens, tense faces seen from behind, no readable text" + N,
    "roadster_2008": "Sleek red two-seat electric sports roadster in a small car workshop in 2008, unbranded, mechanics blurred behind" + N,
    "rocket_orbit": "Rocket upper stage engine glowing in space with the curve of the Earth below, blue atmosphere line" + N,
    "christmas_city": "Rainy American city street at night at Christmas with festive lights reflecting on wet asphalt, few people, 2008" + N,
    "capsule_ocean": "Space capsule floating in the ocean after splashdown with orange and white parachutes on the water, recovery boat" + N,
    "iss_capsule": "Unbranded cargo space capsule approaching the International Space Station above the blue Earth, sunlight" + N,
    "booster_landing": "Rocket first stage landing vertically on a concrete pad at night with a bright engine flame and landing legs extended" + N,
    "crew_launch": "Crowd watching a rocket launch at dusk from a Florida beach, rocket rising with a bright flame, silhouettes" + N,
    "moon_flyby": "Spacecraft flying past the far side of the Moon with the small blue Earth in the distance, crisp sunlight" + N,
}

def I(key, cap=None, pop=None, **kw):
    d = dict(type="img", key=key)
    if cap: d["cap"] = cap
    if pop: d["pop"] = pop
    d.update(kw); return d

def T(num, text):
    return dict(type="title", num=num, text=text.upper(), name=text)

SCENES = [
    # --- GANCHO ---
    dict(id="s01", text="Veintitrés de diciembre de dos mil ocho. Elon Musk lleva meses viendo cómo se le acaba el dinero. Su empresa de cohetes, SpaceX, ha fallado tres lanzamientos seguidos.",
         visual=I("empty_office_night", cap="23 DE DICIEMBRE DE 2008")),
    dict(id="s02", text="Su fábrica de coches eléctricos, Tesla, está a punto de no poder pagar los sueldos. Y el mundo está hundido en la peor crisis financiera en décadas.",
         visual=I("stock_crash_2008", pop=["CRISIS DE 2008"])),
    dict(id="s03", text="Ese día, la NASA anuncia un contrato: unos mil seiscientos millones de dólares para que SpaceX lleve carga a la Estación Espacial Internacional.",
         visual=dict(type="num", start=0, end=1600, suffix=" M$", label="CONTRATO DE LA NASA CON SPACEX · 23-DIC-2008 · 12 VUELOS")),
    dict(id="s04", text="Al día siguiente, a las seis de la tarde de Nochebuena, Tesla cierra el dinero que la salva. Según Musk, en la última hora del último día posible.",
         visual=dict(type="stamp", text="24 DE DICIEMBRE DE 2008\n18:00", stamp="TESLA, SALVADA", col="yellow")),
    dict(id="s05", text="Pero para entender por qué una agencia del Gobierno de Estados Unidos terminó rescatando a una empresa privada con un cohete que no paraba de explotar, hay que volver cincuenta años atrás.",
         visual=I("rocket_fail", shake=True)),
    dict(id="s06", text="A un pitido. Un pitido que llegó desde el espacio en mil novecientos cincuenta y siete y que asustó a todo un país.",
         visual=I("sputnik_orbit", pop=["BIP… BIP… BIP…"])),
    dict(id="s07", text="Esta es la historia de cómo nació la NASA. Y de cómo, medio siglo después, la agencia que se creó para ganarle una carrera a los soviéticos acabó dependiendo de un cohete privado.",
         visual=I("saturn_launch")),
    dict(id="s08", text="Y al final te voy a hacer una pregunta incómoda: después de todo lo que pasó, ¿quién le debe más a quién?",
         visual=dict(type="quote", text="¿QUIÉN LE DEBE MÁS\nA QUIÉN?")),

    # --- 01 ---
    dict(id="s09", text="Capítulo uno: un pitido en el cielo.", visual=T("01", "Un pitido en el cielo")),
    dict(id="s10", text="Cuatro de octubre de mil novecientos cincuenta y siete. La Unión Soviética anuncia que ha puesto en órbita el primer satélite artificial de la historia: el Sputnik.",
         visual=I("sputnik_orbit", cap="4 DE OCTUBRE DE 1957")),
    dict(id="s11", text="Es una esfera de metal pulido de cincuenta y ocho centímetros, con cuatro antenas largas. Pesa unos ochenta y tres kilos.",
         visual=dict(type="quote", text="58 CENTÍMETROS\n83 KILOS\n4 ANTENAS")),
    dict(id="s12", text="Y casi no hace nada: solo emite un pitido de radio. Pero cualquiera con un receptor podía oírlo cuando pasaba por encima.",
         visual=I("radio_1957", motion="out")),
    dict(id="s13", text="Daba una vuelta completa a la Tierra en algo más de hora y media. Una y otra vez, de día y de noche, durante semanas.",
         visual=dict(type="num", start=0, end=96, suffix=" MIN", label="LO QUE TARDABA EL SPUTNIK EN DAR LA VUELTA A LA TIERRA")),
    dict(id="s14", text="En Estados Unidos, la noticia cae como una bomba. Si los soviéticos podían lanzar una bola de metal al espacio, también podían lanzar algo mucho peor.",
         visual=I("night_sky_1957", pop=["¿Y SI FUERA UNA BOMBA?"], pop_col="red")),
    dict(id="s15", text="En plena Guerra Fría, el miedo era fácil de entender: el mismo cohete que pone un satélite en órbita puede llevar una bomba atómica al otro lado del mundo.",
         visual=dict(type="versus", title="EL MIEDO DE 1957", left=["SATÉLITE", "EN ÓRBITA"], right=["MISIL", "CON BOMBA"], mid="=", lcol="yellow", rcol="red")),
    dict(id="s16", text="Y un mes después, los soviéticos lo vuelven a hacer. El tres de noviembre lanzan el Sputnik dos. Esta vez, con un pasajero: una perra llamada Laika.",
         visual=I("dog_capsule", cap="3 DE NOVIEMBRE DE 1957")),
    dict(id="s17", text="Laika no sobrevivió al viaje. Pero el mensaje para Estados Unidos fue clarísimo: los soviéticos iban por delante. Y mucho.",
         visual=dict(type="quote", text="LOS SOVIÉTICOS\nVAN POR DELANTE")),
    dict(id="s18", text="El Congreso abre audiencias para averiguar cómo se había quedado atrás el país más rico del mundo. En la prensa se empieza a hablar de la crisis del Sputnik.",
         visual=I("congress_hearing")),
    dict(id="s19", text="Estados Unidos tenía que responder rápido. Tenía un cohete preparado. Y decidió enseñárselo al mundo… en directo por televisión.",
         visual=I("tv_1957")),

    # --- 02 ---
    dict(id="s20", text="Capítulo dos: Flopnik.", visual=T("02", "Flopnik")),
    dict(id="s21", text="Seis de diciembre de mil novecientos cincuenta y siete. Cabo Cañaveral, Florida. El cohete Vanguard espera en la plataforma con un pequeño satélite en la punta.",
         visual=I("vanguard_pad", cap="CABO CAÑAVERAL · 6-DIC-1957")),
    dict(id="s22", text="Las cámaras de televisión lo transmiten en directo. Todo el país está mirando.",
         visual=I("tv_1957", motion="out")),
    dict(id="s23", text="Cuenta atrás. Encendido. El cohete se eleva… poco más de un metro.",
         visual=dict(type="terminal", title="cabo cañaveral · 6 de diciembre de 1957", lines=["> T-3... T-2... T-1...", "> ENCENDIDO", "> DESPEGUE", "!> ALTURA MÁXIMA: ~1,2 METROS"])),
    dict(id="s24", text="Pierde empuje, cae sobre la plataforma y estalla en una enorme bola de fuego.",
         visual=I("vanguard_explosion", shake=True, pop=["¡BOOM!"], pop_col="red")),
    dict(id="s25", text="El pequeño satélite salió despedido y, según se contó después, quedó tirado entre los arbustos… todavía emitiendo su señal.",
         visual=I("vanguard_explosion", motion="out")),
    dict(id="s26", text="La prensa no tuvo piedad. Lo bautizaron con apodos como Flopnik o Kaputnik. El New York Times habló de un golpe al prestigio del país.",
         visual=dict(type="headline", kicker="Diciembre de 1957", text="La explosión del Vanguard, un golpe al prestigio de Estados Unidos", mark="golpe al prestigio", source="Fuente: The New York Times (citado por la NASA)")),
    dict(id="s27", text="Y un senador de Texas llamado Lyndon Johnson, que años después sería presidente, lo calificó de humillante para el pueblo estadounidense.",
         visual=dict(type="quote", text="\"HUMILLANTE\"\n— LYNDON B. JOHNSON, 1957")),
    dict(id="s28", text="Pero ocho semanas después llega la revancha. El treinta y uno de enero de mil novecientos cincuenta y ocho, el Ejército lanza el Explorer uno.",
         visual=I("explorer_launch", cap="31 DE ENERO DE 1958")),
    dict(id="s29", text="El cohete lo había preparado el equipo del ingeniero alemán Wernher von Braun. Y el satélite, el Laboratorio de Propulsión a Chorro de California.",
         visual=dict(type="versus", title="EXPLORER 1", left=["COHETE", "EQUIPO DE\nVON BRAUN"], right=["SATÉLITE", "JPL\n(CALIFORNIA)"], mid="+", lcol="yellow", rcol="yellow")),
    dict(id="s30", text="Y el Explorer uno hizo algo que el Sputnik no había hecho: un descubrimiento científico. Detectó unos cinturones de radiación alrededor de la Tierra que hoy llevan el nombre del científico James Van Allen.",
         visual=I("explorer_launch", pop=["CINTURONES DE VAN ALLEN"], motion="out")),
    dict(id="s31", text="En marzo llega el Vanguard uno, el primer satélite que funcionó con energía solar. Y aquí va un dato increíble: sigue en órbita. Es el objeto fabricado por el ser humano más antiguo que sigue allá arriba.",
         visual=dict(type="year", year="1958", sub="VANGUARD 1: SIGUE EN ÓRBITA HOY")),
    dict(id="s32", text="Estados Unidos ya tenía satélites. Pero tenía un problema más grande: cada rama del Gobierno y del Ejército iba por su lado. Hacía falta una sola agencia.",
         visual=I("congress_hearing", motion="out")),

    # --- 03 ---
    dict(id="s33", text="Capítulo tres: nace la NASA.", visual=T("03", "Nace la NASA")),
    dict(id="s34", text="Veintinueve de julio de mil novecientos cincuenta y ocho. El presidente Dwight Eisenhower firma la Ley Nacional de Aeronáutica y del Espacio.",
         visual=I("signing_desk", cap="29 DE JULIO DE 1958")),
    dict(id="s35", text="Así nace la NASA: la Administración Nacional de Aeronáutica y del Espacio.",
         visual=dict(type="stamp", text="LEY NACIONAL DE AERONÁUTICA\nY DEL ESPACIO · 1958", stamp="NACE LA NASA", col="yellow")),
    dict(id="s36", text="Y nace con una decisión clave: sería una agencia civil, no militar. Al menos en público, el espacio se iba a explorar con fines pacíficos.",
         visual=dict(type="quote", text="UNA AGENCIA\nCIVIL,\nNO MILITAR")),
    dict(id="s37", text="El uno de octubre, la NASA abre sus puertas. Pero no empieza de cero: absorbe una agencia que llevaba décadas investigando aviones, el NACA, fundado en mil novecientos quince.",
         visual=I("hangar_naca", cap="NACA · TÚNEL DE VIENTO DE LANGLEY")),
    dict(id="s38", text="Con él llegan unos ocho mil empleados, varios laboratorios y un presupuesto de unos cien millones de dólares al año.",
         visual=dict(type="num", start=0, end=8000, suffix=" EMPLEADOS", label="LO QUE LA NASA HEREDÓ DEL NACA (Y UNOS 100 M$ AL AÑO)")),
    dict(id="s39", text="Su primer administrador es Keith Glennan, presidente de una universidad de Ohio. Aceptó con una condición: que el director del NACA, Hugh Dryden, fuera su número dos.",
         visual=I("naca_meeting", cap="ÚLTIMA REUNIÓN DEL NACA · 1958")),
    dict(id="s40", text="Y en abril de mil novecientos cincuenta y nueve presenta a sus primeros siete astronautas, los del programa Mercury. El país los recibió como héroes antes de que hubieran volado.",
         visual=I("astronauts_silver", cap="ABRIL DE 1959 · LOS 7 DEL MERCURY")),
    dict(id="s41", text="Uno de ellos se llamaba Gordon Cooper. Recuerda ese nombre: volverá a aparecer en esta historia cincuenta años después.",
         visual=I("astronauts_silver", pop=["GORDON COOPER"], motion="out")),
    dict(id="s42", text="Pero los soviéticos seguían ganando. El doce de abril de mil novecientos sesenta y uno, Yuri Gagarin se convierte en el primer ser humano en viajar al espacio y dar la vuelta a la Tierra.",
         visual=dict(type="year", year="1961", sub="YURI GAGARIN, PRIMER SER HUMANO EN EL ESPACIO")),
    dict(id="s43", text="Estados Unidos responde tres semanas después con Alan Shepard. Pero su vuelo dura quince minutos y no da la vuelta al planeta.",
         visual=dict(type="versus", title="ABRIL-MAYO DE 1961", left=["GAGARIN", "DA LA VUELTA\nA LA TIERRA"], right=["SHEPARD", "15 MINUTOS\nY ABAJO"], mid="VS", lcol="red", rcol="yellow")),
    dict(id="s44", text="Entonces, el presidente John F. Kennedy hace una apuesta enorme: llevar un hombre a la Luna y traerlo de vuelta antes de que terminara la década.",
         visual=dict(type="quote", text="\"ANTES DE QUE TERMINE\nESTA DÉCADA\"\n— JOHN F. KENNEDY, 1961")),
    dict(id="s45", text="Para lograrlo, la NASA crece como nunca. En mil novecientos sesenta y seis llega a gastar más del cuatro por ciento de todo el presupuesto federal.",
         visual=dict(type="num", start=0, end=4.4, dec=1, suffix=" %", label="DEL PRESUPUESTO FEDERAL DE EE. UU. PARA LA NASA (1966)")),
    dict(id="s46", text="Unas cuatrocientas mil personas trabajaron en el programa Apolo, entre empleados de la NASA y de las empresas contratistas.",
         visual=dict(type="num", start=0, end=400000, suffix=" PERSONAS", label="TRABAJARON EN EL PROGRAMA APOLO")),
    dict(id="s47", text="Y fíjate en ese detalle, porque es la semilla de todo lo que vendrá: la NASA casi nunca fabricó sola sus cohetes. Los diseñaba y los pagaba, pero los construían empresas privadas.",
         visual=I("rocket_factory_60s", pop=["LOS CONSTRUÍAN EMPRESAS"])),
    dict(id="s48", text="Y el veinte de julio de mil novecientos sesenta y nueve, Estados Unidos gana la carrera: el Apolo once se posa en la Luna.",
         visual=I("moon_footprint", cap="20 DE JULIO DE 1969")),
    dict(id="s49", text="La agencia que había nacido del miedo a un pitido soviético había llevado al ser humano a otro mundo en solo once años.",
         visual=I("saturn_launch", motion="out")),
    dict(id="s50", text="Pero ganar la carrera tenía un problema: cuando ya no hay rival, también desaparece la prisa. Y el dinero.",
         visual=dict(type="quote", text="SIN RIVAL\nNO HAY PRISA.\nNI DINERO.")),

    # --- 04 ---
    dict(id="s51", text="Capítulo cuatro: el precio de ir al espacio.", visual=T("04", "El precio de ir al espacio")),
    dict(id="s52", text="Después del Apolo, el presupuesto de la NASA se desploma. Su gran apuesta para las décadas siguientes es una nave reutilizable: el transbordador espacial.",
         visual=I("shuttle_launch")),
    dict(id="s53", text="Vuela por primera vez en mil novecientos ochenta y uno. La idea era que ir al espacio fuera casi como subirse a un avión: rápido y barato. No lo fue.",
         visual=dict(type="year", year="1981", sub="PRIMER VUELO DEL TRANSBORDADOR ESPACIAL")),
    dict(id="s54", text="Y costó vidas. En mil novecientos ochenta y seis explota el Challenger. En dos mil tres, el Columbia se desintegra al volver a la Tierra. Mueren catorce astronautas.",
         visual=dict(type="quote", text="1986 · CHALLENGER\n2003 · COLUMBIA\n14 ASTRONAUTAS")),
    dict(id="s55", text="Después del Columbia, Estados Unidos decide jubilar el transbordador. Y la NASA tiene que pensar cómo seguirá llevando carga y astronautas a la Estación Espacial Internacional.",
         visual=I("shuttle_hangar")),
    dict(id="s56", text="En dos mil seis prueba algo que en los años cincuenta habría sonado a locura: en vez de ser dueña de la nave, le pagará a empresas privadas por cumplir objetivos.",
         visual=dict(type="versus", title="UN CAMBIO DE MODELO", left=["ANTES", "LA NASA ES\nDUEÑA DE LA NAVE"], right=["DESDE 2006", "LA NASA PAGA\nPOR RESULTADOS"], mid="→", lcol="white", rcol="yellow")),
    dict(id="s57", text="El programa se llama COTS. En agosto de dos mil seis elige a dos empresas. Una de ellas recibe doscientos setenta y ocho millones de dólares. Se llama SpaceX.",
         visual=dict(type="num", start=0, end=278, suffix=" M$", label="PARA SPACEX EN EL PROGRAMA COTS DE LA NASA (AGOSTO DE 2006)")),
    dict(id="s58", text="La otra, Rocketplane Kistler, no consiguió reunir el dinero que necesitaba y acabó fuera del programa.",
         visual=dict(type="stamp", text="ROCKETPLANE KISTLER", stamp="FUERA DEL PROGRAMA", col="red")),
    dict(id="s59", text="Para entender quién estaba detrás de SpaceX, tenemos que viajar a Moscú, en el otoño de dos mil uno.",
         visual=I("moscow_winter")),

    # --- 05 ---
    dict(id="s60", text="Capítulo cinco: un millonario que quería ir a Marte.", visual=T("05", "Un millonario que quería ir a Marte")),
    dict(id="s61", text="Elon Musk tenía treinta años y se había hecho rico con PayPal, la empresa de pagos por internet que eBay compró en dos mil dos.",
         visual=dict(type="year", year="2002", sub="eBAY COMPRA PAYPAL")),
    dict(id="s62", text="Y tenía una idea extraña: mandar un pequeño invernadero a Marte para que crecieran plantas allí, y despertar otra vez el interés del público por el espacio. La llamó Mars Oasis.",
         visual=I("greenhouse_mars", pop=["MARS OASIS"])),
    dict(id="s63", text="El problema era el cohete: en Estados Unidos costaban una fortuna. Así que en octubre de dos mil uno viajó a Moscú para comprar misiles balísticos rusos reconvertidos.",
         visual=I("moscow_winter", cap="MOSCÚ · OCTUBRE DE 2001", motion="out")),
    dict(id="s64", text="Fue dos veces, en octubre de dos mil uno y en febrero de dos mil dos. Y las dos veces volvió sin cohete.",
         visual=dict(type="timeline", title="DE MOSCÚ A SPACEX", points=[["OCT 2001", "1.er viaje a Moscú"], ["FEB 2002", "2.º viaje, sin trato"], ["2002", "Funda SpaceX"]], hl=2)),
    dict(id="s65", text="Según contó después, en el viaje de vuelta hizo números y llegó a una conclusión: los materiales de un cohete costaban solo una pequeña parte de su precio. Podía fabricarlos él.",
         visual=dict(type="quote", text="LOS MATERIALES\nERAN UNA PEQUEÑA PARTE\nDEL PRECIO")),
    dict(id="s66", text="En dos mil dos funda Space Exploration Technologies: SpaceX. Su primer cohete será pequeño y barato: el Falcon uno.",
         visual=I("rocket_factory")),
    dict(id="s67", text="Para lanzarlo eligen un lugar insólito: Omelek, una isla diminuta del atolón de Kwajalein, en medio del océano Pacífico.",
         visual=dict(type="route", title="DE CALIFORNIA A UNA ISLA DEL PACÍFICO", points={"California": [0.84, 0.30], "Hawái": [0.56, 0.50], "Kwajalein": [0.20, 0.66]},
                     routes=[["California", "Kwajalein"]])),
    dict(id="s68", text="Casi todos los expertos pensaban que una empresa privada no podía llegar sola a la órbita. Y durante años, los hechos parecieron darles la razón.",
         visual=I("pacific_island")),

    # --- 06 ---
    dict(id="s69", text="Capítulo seis: tres explosiones.", visual=T("06", "Tres explosiones")),
    dict(id="s70", text="Veinticuatro de marzo de dos mil seis. Primer lanzamiento del Falcon uno. A los pocos segundos, un incendio en el motor. El cohete cae al mar.",
         visual=I("rocket_fail", cap="24 DE MARZO DE 2006")),
    dict(id="s71", text="Veintiuno de marzo de dos mil siete. Segundo intento. Esta vez llega al espacio, pero la segunda etapa empieza a oscilar y no alcanza la órbita.",
         visual=I("control_room", pop=["2.º FALLO"], pop_col="red")),
    dict(id="s72", text="Dos de agosto de dos mil ocho. Tercer intento. Y esta vez el cohete lleva carga de verdad: un satélite militar y dos pequeños experimentos de la NASA.",
         visual=I("pacific_island", motion="out")),
    dict(id="s73", text="La primera etapa funciona a la perfección. Pero al separarse, un error de sincronización hace que las dos etapas choquen. Tercer fallo.",
         visual=dict(type="board", title="FALCON 1 · LANZAMIENTOS", rows=[["24/03/2006", "Vuelo 1 · Omelek", "FALCON 1", "DESPEGUE"],
                     ["21/03/2007", "Vuelo 2 · Omelek", "FALCON 1", "DESPEGUE"], ["02/08/2008", "Vuelo 3 · Omelek", "FALCON 1", "DESPEGUE"]], final="FALLO")),
    dict(id="s74", text="A bordo iba también una cápsula con las cenizas de más de doscientas personas que habían querido descansar en el espacio.",
         visual=I("rocket_fail", shake=True, motion="out")),
    dict(id="s75", text="Entre ellas estaban las del actor que hacía de Scotty en Star Trek… y las de Gordon Cooper, uno de aquellos siete primeros astronautas de la NASA.",
         visual=dict(type="quote", text="GORDON COOPER\nASTRONAUTA DEL MERCURY\n1959")),
    dict(id="s76", text="Medio siglo después de que la NASA presentara a sus primeros astronautas, las cenizas de uno de ellos se perdían en un cohete privado que no lograba llegar a la órbita.",
         visual=I("astronauts_silver", motion="out")),
    dict(id="s77", text="Y mientras tanto, la otra empresa de Musk también se estaba hundiendo.",
         visual=I("roadster_2008", shake=True)),

    # --- 07 ---
    dict(id="s78", text="Capítulo siete: el peor año.", visual=T("07", "El peor año")),
    dict(id="s79", text="Tesla llevaba años intentando fabricar su primer coche, un deportivo eléctrico llamado Roadster. Iba con retraso y costaba mucho más de lo previsto.",
         visual=I("roadster_2008", motion="out")),
    dict(id="s80", text="En octubre de dos mil ocho, Musk pasa a dirigir Tesla. Despide a parte de la plantilla y pone su propio dinero para que la empresa no cierre.",
         visual=dict(type="stamp", text="OCTUBRE DE 2008\nMUSK, DIRECTOR DE TESLA", stamp="DESPIDOS", col="red")),
    dict(id="s81", text="Y en septiembre había quebrado el banco Lehman Brothers. Los bancos no prestaban y los inversores no querían arriesgar. Era el peor momento posible para pedir dinero.",
         visual=I("stock_crash_2008", motion="out")),
    dict(id="s82", text="Musk ha recordado muchas veces aquel año como uno de los más duros de su vida. Tenía dos empresas, y las dos podían caer a la vez.",
         visual=dict(type="versus", title="FINALES DE 2008", left=["SPACEX", "3 FALLOS\nSEGUIDOS"], right=["TESLA", "SIN DINERO\nPARA SUELDOS"], mid="+", lcol="red", rcol="red")),
    dict(id="s83", text="Según se ha contado, a SpaceX le quedaba lo justo para un último lanzamiento del Falcon uno. Si fallaba, probablemente se acababa todo.",
         visual=dict(type="quote", text="UN ÚLTIMO\nLANZAMIENTO")),
    dict(id="s84", text="Todo dependía de un cohete en una isla perdida del Pacífico.",
         visual=I("pacific_island")),

    # --- 08 ---
    dict(id="s85", text="Capítulo ocho: el cuarto intento.", visual=T("08", "El cuarto intento")),
    dict(id="s86", text="Veintiocho de septiembre de dos mil ocho. Omelek. El cuarto Falcon uno lleva una carga de prueba: un bloque de metal de unos ciento sesenta y cinco kilos, apodado RatSat.",
         visual=I("pacific_island", motion="out", pop=["4.º INTENTO"])),
    dict(id="s87", text="Despegue. La primera etapa funciona. Separación… limpia. La segunda etapa enciende su motor.",
         visual=dict(type="terminal", title="omelek · 28 de septiembre de 2008", lines=["> T+00:00 DESPEGUE", "> PRIMERA ETAPA: OK", "> SEPARACIÓN: OK", "> SEGUNDA ETAPA: ENCENDIDA"])),
    dict(id="s88", text="Y unos minutos después llega la confirmación: el Falcon uno está en órbita.",
         visual=I("control_room", pop=["EN ÓRBITA"])),
    dict(id="s89", text="Es el primer cohete de combustible líquido desarrollado por una empresa privada que llega a la órbita de la Tierra. En SpaceX, los empleados gritan y se abrazan.",
         visual=dict(type="stamp", text="28 DE SEPTIEMBRE DE 2008\nFALCON 1 · VUELO 4", stamp="EN ÓRBITA", col="green")),
    dict(id="s90", text="Y fíjate en la fecha: tres días después, el uno de octubre de dos mil ocho, la NASA cumplía exactamente cincuenta años.",
         visual=dict(type="year", year="1958 – 2008", sub="LA NASA CUMPLE 50 AÑOS · 1 DE OCTUBRE")),
    dict(id="s91", text="Pero llegar a la órbita no paga las facturas. Después del éxito, SpaceX seguía necesitando clientes. Y Tesla, dinero.",
         visual=I("empty_office_night", motion="out")),

    # --- 09 ---
    dict(id="s92", text="Capítulo nueve: la Navidad de dos mil ocho.", visual=T("09", "La Navidad de 2008")),
    dict(id="s93", text="Diciembre de dos mil ocho. Musk está repartiendo lo poco que le queda entre sus empresas. Según ha contado, llegó a pedir dinero prestado a amigos.",
         visual=I("christmas_city")),
    dict(id="s94", text="Y entonces, el veintitrés de diciembre, la NASA anuncia quién llevará la carga a la Estación Espacial Internacional cuando se jubile el transbordador.",
         visual=dict(type="headline", kicker="23 de diciembre de 2008", text="La NASA elige a SpaceX y a Orbital para abastecer la Estación Espacial Internacional", mark="SpaceX", source="Fuente: NASA / Spaceflight Now")),
    dict(id="s95", text="A SpaceX le encarga doce vuelos por unos mil seiscientos millones de dólares. A Orbital Sciences, ocho vuelos por unos mil novecientos millones.",
         visual=dict(type="bars", title="CONTRATOS DE CARGA DE LA NASA (MILES DE MILLONES DE $)", data=[["SPACEX · 12 VUELOS", 1.6], ["ORBITAL · 8 VUELOS", 1.9]], dec=1)),
    dict(id="s96", text="Para una empresa que tres meses antes estaba a un fallo de desaparecer, aquello lo cambiaba todo.",
         visual=I("rocket_factory", pop=["LO CAMBIA TODO"])),
    dict(id="s97", text="Y al día siguiente, el veinticuatro de diciembre, Tesla cierra una ronda de financiación de unos cuarenta millones de dólares.",
         visual=dict(type="num", start=0, end=40, suffix=" M$", label="RONDA DE FINANCIACIÓN DE TESLA · 24-DIC-2008")),
    dict(id="s98", text="Musk contó años después que se cerró a las seis de la tarde de Nochebuena, en la última hora posible. Si no, dos días después de Navidad no habría podido pagar los sueldos.",
         visual=dict(type="quote", text="24 DE DICIEMBRE\n18:00\nLA ÚLTIMA HORA POSIBLE")),
    dict(id="s99", text="En dos días, sus dos empresas pasaron del borde de la quiebra a tener un futuro. Y una de ellas se lo debía a la NASA.",
         visual=I("christmas_city", motion="out")),

    # --- 10 ---
    dict(id="s100", text="Capítulo diez: la deuda se devuelve.", visual=T("10", "La deuda se devuelve")),
    dict(id="s101", text="Lo que vino después cambió la industria espacial. En diciembre de dos mil diez, SpaceX se convierte en la primera empresa privada en recuperar una nave desde la órbita: la cápsula Dragon.",
         visual=I("capsule_ocean", cap="DICIEMBRE DE 2010")),
    dict(id="s102", text="En mayo de dos mil doce, una Dragon llega a la Estación Espacial Internacional. Es la primera nave comercial en hacerlo.",
         visual=I("iss_capsule", cap="MAYO DE 2012")),
    dict(id="s103", text="Y en diciembre de dos mil quince logra algo que parecía ciencia ficción: hacer aterrizar la primera etapa de un cohete orbital después del lanzamiento.",
         visual=I("booster_landing", cap="DICIEMBRE DE 2015", pop=["ATERRIZA"])),
    dict(id="s104", text="Mientras tanto, la NASA vivía una situación incómoda. Desde que se jubiló el transbordador, en dos mil once, no tenía forma propia de llevar astronautas al espacio.",
         visual=I("shuttle_hangar", motion="out")),
    dict(id="s105", text="Para subirlos a la estación, le pagaba a Rusia por asientos en las naves Soyuz. Los más caros llegaron a costar unos ochenta y seis millones de dólares por astronauta.",
         visual=dict(type="num", start=0, end=86, suffix=" M$", label="PRECIO MÁXIMO DE UN ASIENTO EN LA SOYUZ RUSA (INSPECTOR GENERAL DE LA NASA)")),
    dict(id="s106", text="La agencia que había nacido para ganarle la carrera espacial a los soviéticos tenía que comprarle los viajes a Rusia.",
         visual=I("soyuz_steppe", pop=["LA IRONÍA"])),
    dict(id="s107", text="En dos mil catorce, la NASA reparte los contratos para volver a lanzar astronautas desde casa: cuatro mil doscientos millones para Boeing, el gigante de siempre. Dos mil seiscientos millones para SpaceX.",
         visual=dict(type="bars", title="CONTRATOS PARA LLEVAR ASTRONAUTAS (2014, MILES DE MILLONES DE $)", data=[["BOEING", 4.2], ["SPACEX", 2.6]], dec=1)),
    dict(id="s108", text="Y el treinta de mayo de dos mil veinte, dos astronautas de la NASA despegan desde Florida en una Crew Dragon. Es el primer lanzamiento tripulado desde Estados Unidos en nueve años. Y el primero de una empresa privada.",
         visual=I("crew_launch", cap="30 DE MAYO DE 2020")),
    dict(id="s109", text="¿Y Boeing? Su nave, la Starliner, tuvo tantos problemas en su primer vuelo con tripulación, en dos mil veinticuatro, que volvió a la Tierra vacía.",
         visual=dict(type="stamp", text="STARLINER · 2024", stamp="VOLVIÓ VACÍA", col="red")),
    dict(id="s110", text="Sus dos astronautas regresaron en marzo de dos mil veinticinco… a bordo de una Dragon de SpaceX, después de doscientos ochenta y seis días en el espacio.",
         visual=dict(type="num", start=0, end=286, suffix=" DÍAS", label="EN EL ESPACIO · VOLVIERON EN UNA DRAGON DE SPACEX (MARZO DE 2025)")),
    dict(id="s111", text="En dos mil veintiuno, la NASA eligió la nave Starship de SpaceX para volver a posar astronautas en la Luna, con un contrato de dos mil ochocientos noventa millones de dólares.",
         visual=dict(type="num", start=0, end=2890, suffix=" M$", label="CONTRATO DE LA NASA PARA EL MÓDULO LUNAR STARSHIP (2021)")),
    dict(id="s112", text="Y en abril de dos mil veintiséis, la propia NASA volvió a la Luna con la misión Artemis dos: cuatro astronautas la rodearon por primera vez desde mil novecientos setenta y dos.",
         visual=I("moon_flyby", cap="ABRIL DE 2026 · ARTEMIS II")),
    dict(id="s113", text="Y en junio de dos mil veintiséis, SpaceX, ya fusionada con la empresa de inteligencia artificial de Musk, salió a bolsa. Quedó valorada en cerca de un billón ochocientos mil millones de dólares.",
         visual=dict(type="num", start=0, end=1.77, dec=2, suffix=" BILLONES $", label="VALOR DE SPACEX EN SU SALIDA A BOLSA (JUNIO DE 2026)")),
    dict(id="s114", text="La empresa que en dos mil ocho estaba a un fallo de desaparecer se había convertido en una de las más valiosas del mundo.",
         visual=I("booster_landing", motion="out")),

    # --- CIERRE ---
    dict(id="s115", text="Entonces, ¿quién le debe más a quién?", visual=dict(type="quote", text="¿QUIÉN LE DEBE MÁS\nA QUIÉN?")),
    dict(id="s116", text="Sin la NASA, SpaceX probablemente no habría sobrevivido a dos mil ocho. Su dinero y sus contratos le dieron una oportunidad cuando nadie más se la daba.",
         visual=dict(type="versus", title="LA NASA → SPACEX", left=["2006", "278 M$\nCOTS"], right=["2008", "1.600 M$\nCARGA"], mid="+", lcol="yellow", rcol="yellow")),
    dict(id="s117", text="Pero sin SpaceX, la NASA habría pasado muchos más años pagándole a Rusia por cada asiento. Y sus astronautas varados en dos mil veinticinco habrían tenido que esperar otra nave.",
         visual=dict(type="versus", title="SPACEX → LA NASA", left=["2020", "VUELVEN LOS\nASTRONAUTAS"], right=["2025", "RESCATA A LOS\nDE STARLINER"], mid="+", lcol="yellow", rcol="yellow")),
    dict(id="s118", text="Y todo empezó con un pitido. El miedo a una pequeña bola de metal soviética creó la agencia que llevó al ser humano a la Luna.",
         visual=I("sputnik_orbit", motion="out")),
    dict(id="s119", text="Y cincuenta años después, esa misma agencia salvó con un contrato a la empresa privada que hoy le lleva a sus astronautas al espacio.",
         visual=I("crew_launch", motion="out")),
    dict(id="s120", text="¿Tú qué opinas? ¿La NASA hizo bien en apostar por empresas privadas, o el espacio debería quedar en manos de los gobiernos? Te leo en los comentarios.",
         visual=I("moon_flyby", motion="out")),
    dict(id="s121", text="Y si te gustan estas historias, suscríbete: cada semana, el último balance de una empresa. Gracias por llegar hasta el final. Nos vemos en el próximo balance.",
         visual=I("saturn_launch")),
]

# Escenas de reserva (solo si falta img/<clave>.png: la generación de imágenes de DubVoice falla a veces)
FALLBACK = {
    "s01": dict(type="year", year="23/12/2008", sub="SPACEX: 3 FALLOS · TESLA: SIN DINERO"),
    "s02": dict(type="stamp", text="2008", stamp="CRISIS FINANCIERA", col="red"),
    "s05": dict(type="quote", text="UN COHETE\nQUE NO PARABA\nDE EXPLOTAR"),
    "s06": dict(type="year", year="1957", sub="UN PITIDO DESDE EL ESPACIO"),
    "s07": dict(type="versus", title="1958 → 2008", left=["1958", "NACE\nLA NASA"], right=["2008", "LA NASA\nSALVA A SPACEX"], mid="→", lcol="yellow", rcol="yellow"),
    "s10": dict(type="year", year="4/10/1957", sub="SPUTNIK, EL PRIMER SATÉLITE ARTIFICIAL"),
    "s12": dict(type="quote", text="BIP… BIP… BIP…"),
    "s14": dict(type="quote", text="¿Y SI FUERA\nUNA BOMBA?"),
    "s16": dict(type="year", year="3/11/1957", sub="SPUTNIK 2 · A BORDO, LA PERRA LAIKA"),
    "s18": dict(type="stamp", text="EE. UU. · 1957", stamp="LA CRISIS DEL SPUTNIK", col="red"),
    "s19": dict(type="quote", text="EN DIRECTO\nPOR TELEVISIÓN"),
    "s21": dict(type="year", year="6/12/1957", sub="CABO CAÑAVERAL · COHETE VANGUARD"),
    "s22": dict(type="quote", text="TODO EL PAÍS\nESTÁ MIRANDO"),
    "s24": dict(type="stamp", text="VANGUARD · 6-DIC-1957", stamp="EXPLOTA", col="red"),
    "s25": dict(type="quote", text="EL SATÉLITE,\nENTRE LOS ARBUSTOS"),
    "s28": dict(type="year", year="31/1/1958", sub="EXPLORER 1, EL PRIMER SATÉLITE DE EE. UU."),
    "s30": dict(type="quote", text="CINTURONES\nDE VAN ALLEN"),
    "s32": dict(type="quote", text="HACÍA FALTA\nUNA SOLA AGENCIA"),
    "s34": dict(type="year", year="29/7/1958", sub="EISENHOWER FIRMA LA LEY DEL ESPACIO"),
    "s37": dict(type="year", year="1/10/1958", sub="LA NASA EMPIEZA A FUNCIONAR"),
    "s39": dict(type="versus", title="LOS PRIMEROS JEFES DE LA NASA", left=["ADMINISTRADOR", "KEITH\nGLENNAN"], right=["NÚMERO DOS", "HUGH\nDRYDEN"], mid="+", lcol="yellow", rcol="white"),
    "s40": dict(type="year", year="1959", sub="LOS 7 ASTRONAUTAS DEL PROGRAMA MERCURY"),
    "s41": dict(type="quote", text="RECUERDA ESTE NOMBRE:\nGORDON COOPER"),
    "s47": dict(type="quote", text="LA NASA LOS PAGABA.\nLOS CONSTRUÍAN\nEMPRESAS."),
    "s48": dict(type="year", year="20/7/1969", sub="EL APOLO 11 SE POSA EN LA LUNA"),
    "s49": dict(type="versus", title="DE UN PITIDO A LA LUNA", left=["1957", "SPUTNIK"], right=["1969", "APOLO 11"], mid="→", lcol="red", rcol="yellow"),
    "s52": dict(type="stamp", text="DESPUÉS DEL APOLO", stamp="TRANSBORDADOR", col="yellow"),
    "s55": dict(type="stamp", text="2003 → 2011", stamp="ADIÓS AL TRANSBORDADOR", col="red"),
    "s59": dict(type="year", year="2001", sub="MOSCÚ"),
    "s62": dict(type="quote", text="MARS OASIS:\nPLANTAS EN MARTE"),
    "s63": dict(type="stamp", text="MOSCÚ · OCTUBRE DE 2001", stamp="COMPRAR MISILES", col="red"),
    "s66": dict(type="year", year="2002", sub="NACE SPACEX · COHETE FALCON 1"),
    "s68": dict(type="quote", text="\"UNA EMPRESA PRIVADA\nNO PUEDE LLEGAR\nA LA ÓRBITA\""),
    "s70": dict(type="year", year="24/3/2006", sub="FALCON 1 · VUELO 1: FALLO"),
    "s71": dict(type="year", year="21/3/2007", sub="FALCON 1 · VUELO 2: FALLO"),
    "s72": dict(type="year", year="2/8/2008", sub="FALCON 1 · VUELO 3"),
    "s74": dict(type="quote", text="CENIZAS DE\nMÁS DE 200 PERSONAS"),
    "s76": dict(type="quote", text="50 AÑOS DESPUÉS"),
    "s77": dict(type="stamp", text="MIENTRAS TANTO…", stamp="TESLA SE HUNDE", col="red"),
    "s79": dict(type="stamp", text="TESLA ROADSTER", stamp="RETRASOS", col="red"),
    "s81": dict(type="year", year="15/9/2008", sub="QUIEBRA LEHMAN BROTHERS"),
    "s84": dict(type="quote", text="TODO DEPENDÍA\nDE UN COHETE"),
    "s86": dict(type="year", year="28/9/2008", sub="FALCON 1 · VUELO 4 · RATSAT"),
    "s88": dict(type="stamp", text="FALCON 1", stamp="EN ÓRBITA", col="green"),
    "s91": dict(type="quote", text="LA ÓRBITA\nNO PAGA LAS FACTURAS"),
    "s93": dict(type="year", year="12/2008", sub="MUSK REPARTE LO QUE LE QUEDA"),
    "s96": dict(type="quote", text="LO CAMBIA TODO"),
    "s99": dict(type="versus", title="NAVIDAD DE 2008", left=["SPACEX", "CONTRATO\nDE LA NASA"], right=["TESLA", "40 M$\nEN NOCHEBUENA"], mid="+", lcol="yellow", rcol="yellow"),
    "s101": dict(type="year", year="12/2010", sub="DRAGON, PRIMERA NAVE PRIVADA RECUPERADA DE LA ÓRBITA"),
    "s102": dict(type="year", year="5/2012", sub="DRAGON LLEGA A LA ESTACIÓN ESPACIAL"),
    "s103": dict(type="year", year="12/2015", sub="ATERRIZA LA PRIMERA ETAPA DE UN COHETE ORBITAL"),
    "s104": dict(type="stamp", text="NASA · 2011-2020", stamp="SIN NAVE PROPIA", col="red"),
    "s106": dict(type="quote", text="LA NASA\nLE COMPRABA LOS VIAJES\nA RUSIA"),
    "s108": dict(type="year", year="30/5/2020", sub="CREW DRAGON · VUELVEN LOS LANZAMIENTOS DESDE EE. UU."),
    "s112": dict(type="year", year="4/2026", sub="ARTEMIS II RODEA LA LUNA"),
    "s114": dict(type="quote", text="DE CASI QUEBRAR\nA UNA DE LAS MÁS\nVALIOSAS DEL MUNDO"),
    "s118": dict(type="quote", text="TODO EMPEZÓ\nCON UN PITIDO"),
    "s119": dict(type="versus", title="50 AÑOS DESPUÉS", left=["1958", "NACE\nLA NASA"], right=["2008", "LA NASA\nSALVA A SPACEX"], mid="→", lcol="yellow", rcol="yellow"),
    "s120": dict(type="quote", text="¿NASA O EMPRESAS\nPRIVADAS?"),
    "s121": dict(type="stamp", text="EL ÚLTIMO BALANCE", stamp="SUSCRÍBETE", col="yellow"),
}

SHORTS = {}

THUMBS = [
    dict(img="sputnik_orbit", zoom=1.05, cx=0.6, shade=["left", 225, 0.62], items=[
        ["text", 45, 60, "UN PITIDO", 160, "white", "la"], ["text", 45, 260, "CREÓ", 150, "white", "la"], ["text", 45, 430, "LA NASA", 180, "yellow", "la"]]),
    dict(img="pacific_island", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "3 FALLOS", 190, "red", "la"], ["text", 45, 300, "Y CASI", 140, "white", "la"], ["text", 45, 460, "QUIEBRA", 160, "white", "la"]]),
    dict(img="roadster_2008", zoom=1.05, cx=0.6, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "SALVADO", 180, "yellow", "la"], ["text", 45, 290, "EN", 120, "white", "la"], ["text", 45, 420, "NOCHEBUENA", 150, "white", "la"]]),
    dict(img="vanguard_explosion", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "FLOPNIK", 200, "red", "la"], ["text", 45, 320, "EN DIRECTO", 120, "white", "la"]]),
    dict(img="explorer_launch", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "EL ÚLTIMO", 150, "white", "la"], ["text", 45, 260, "COHETE", 200, "yellow", "la"]]),
    dict(img="empty_office_night", zoom=1.05, cx=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "LA NASA", 170, "white", "la"], ["text", 45, 280, "LO SALVÓ", 170, "yellow", "la"], ["badge", 45, 540, 560, 640, "1.600 M$", 90]]),
    dict(img="moon_footprint", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "1958", 200, "yellow", "la"], ["text", 45, 300, "→ 2008", 170, "white", "la"]]),
    dict(img="soyuz_steppe", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "86 M$", 210, "red", "la"], ["text", 45, 320, "POR ASIENTO", 120, "white", "la"]]),
    dict(img="booster_landing", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "¿QUIÉN", 170, "white", "la"], ["text", 45, 270, "LE DEBE", 170, "white", "la"], ["text", 45, 480, "A QUIÉN?", 170, "yellow", "la"]]),
    dict(img="saturn_launch", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "CÓMO NACIÓ", 150, "white", "la"], ["text", 45, 260, "LA NASA", 200, "yellow", "la"]]),
]
THUMBS_TOP = [6, 1, 2]

META = {
    "code": "010",
    "name": "La NASA y SpaceX",
    "intro_chapter": "Intro: la Navidad de 2008",
    "titles": [
        "Cómo nació la NASA… y por qué 50 años después salvó a Elon Musk",
        "Un pitido creó la NASA. 50 años después, la NASA salvó a SpaceX",
        "La Navidad en que Elon Musk casi lo pierde todo (y quién lo salvó)",
    ],
    "description": "El 23 de diciembre de 2008, con SpaceX después de tres lanzamientos fallidos y Tesla a días de no poder pagar los sueldos, la NASA le dio a SpaceX un contrato de unos 1.600 millones de dólares. Para entender por qué, volvemos a 1957: el pitido del Sputnik, la explosión en directo del Vanguard («Flopnik»), el nacimiento de la NASA en 1958 y la carrera hasta la Luna. Después, el transbordador, la dependencia de las naves rusas Soyuz y el programa que cambió la forma de ir al espacio. Y la historia de SpaceX: los viajes de Musk a Moscú, las tres explosiones del Falcon 1 (en una iban las cenizas de un astronauta del Mercury), el cuarto intento, la Nochebuena de 2008 y lo que pasó después: Crew Dragon, Starliner, Artemis II y la salida a bolsa de SpaceX en 2026.",
    "sources": [
        "NASA History: Sputnik y el nacimiento de la era espacial; respuesta de EE. UU. al Sputnik; el Vanguard TV3 (6-dic-1957)",
        "NASA / Eisenhower Presidential Library: Ley Nacional de Aeronáutica y del Espacio (29-jul-1958) y la NASA desde el 1-oct-1958",
        "Astronomy / Discover: Vanguard 1, el objeto humano más antiguo en órbita",
        "CBS News / Wikipedia (Budget of NASA): 4,41 % del presupuesto federal en 1966; unas 400.000 personas en el programa Apolo",
        "The Register / SpaceNews (ago-2006): programa COTS (278 M$ para SpaceX); TASS / Inspector General de la NASA: precios de la Soyuz",
        "History of SpaceX (Wikipedia): viajes de Musk a Moscú (2001-2002) y Mars Oasis",
        "Space.com / Spaceflight Now / TechCrunch (2008): fallos del Falcon 1 y el vuelo 4 en órbita (28-sep-2008)",
        "NASA / Spaceflight Now (23-dic-2008): contratos CRS para SpaceX y Orbital",
        "Tesla North / Business Today: la ronda de Tesla del 24-dic-2008",
        "AmericaSpace (16-sep-2014): contratos Commercial Crew; CBS News / NASASpaceflight (mar-2025): regreso de Wilmore y Williams",
        "NASA / NPR (abr-2026): Artemis II; CNBC / Reuters (jun-2026): salida a bolsa de SpaceX",
    ],
    "disclosure": "Fotos de archivo vía Wikimedia Commons: NASA, Ejército y Marina de EE. UU. (dominio público), SpaceX (CC0) y otros autores con licencia CC BY (créditos arriba). Dos imágenes (una oficina de noche y una sala de bolsa) son ilustraciones generadas con IA. Los mapas y gráficos son recreaciones. La narración está hecha con voz sintética.",
    "hashtags": "#NASA #SpaceX #ElonMusk #Historia",
    "tags": ["nasa", "historia de la nasa", "cómo nació la nasa", "spacex", "elon musk", "sputnik", "carrera espacial", "falcon 1",
             "elon musk 2008", "tesla 2008", "crew dragon", "artemis ii", "historia de empresas", "negocios", "el último balance"],
    "pinned": "¿La NASA hizo bien en apostar por empresas privadas? 🚀 Te leo 👇 Y dime qué historia quieres para el próximo vídeo.",
    "playlist": "Auges y remontadas",
    "category": "Educación",
    "altered": "Sí",
    "shorts": {},
}
