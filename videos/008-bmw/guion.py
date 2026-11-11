# El Último Balance · Vídeo 008 — BMW: la noche de 1959 en que casi se la queda Mercedes (11-nov-2026)
# Tema por datos (API de YouTube, 11-nov): EN "INSANE Rise of BMW: The Blind Billionaire's Bet That Beat Mercedes" 2,08M
# (Think School, ago-2026); en español no hay ningún vídeo de la historia de la empresa (máx. 11k). Marca conocida en Argentina.
# 15 min, sin Shorts (pedido del usuario). Visual: tomas reales de Pexels (vía vidIQ) + 7 imágenes IA históricas + gráficos.
#
# Hechos verificados (WebSearch, 11-nov-2026):
# - Fundación oficial: Bayerische Flugzeugwerke, 7-mar-1916; Rapp Motorenwerke pasa a llamarse BMW en 1917; primer producto, un
#   motor de avión; Max Friz diseña el BMW IIIa (1917), más potente en altura que sus rivales (BMW Group, Wikipedia).
# - Logo: deriva del de Rapp; colores de Baviera; la lectura de "hélice" aparece a fines de los años 20 (mito) (Wikipedia, BMW).
# - R32 (1923), primera moto BMW. 1928: compra la fábrica de Eisenach, que hacía el Dixi (Austin Seven bajo licencia);
#   primer coche BMW: 3/15 (Dixi rebautizado).
# - Guerra: BMW reconoce en su web que la dirección "no tuvo reparos" en usar trabajo forzado y prisioneros de campos de
#   concentración; subcampo de Allach (Dachau) creado para BMW en 1943; jornadas de hasta 12 h; BMW negó su responsabilidad
#   durante mucho tiempo; desde jun-2020 el Museo BMW tiene un espacio sobre el trabajo forzado (bmwgroup.com).
# - Posguerra: naves de Múnich destruidas o desmontadas; ollas y cacerolas; motos de nuevo en 1948; Eisenach queda en zona
#   soviética → EMW. BMW 501 (1951). Isetta: licencia tras verla en el Salón de Turín de 1954, producción desde 1955.
# - 9-dic-1959: junta de accionistas en Múnich; la venta a Daimler-Benz parecía decidida (BMW); Hans Feith, del Deutsche Bank;
#   el accionista Erich Nold y el abogado Friedrich Mathern consiguen aplazar la votación; se citan 25.000 pedidos del BMW 700;
#   plan de rescate en nov-1960; Herbert Quandt aumenta su participación (cifras dispares; "cerca de la mitad"). Algunas fuentes
#   dicen que Quandt al principio apoyaba la venta (Auto Bild, autoevolution, BMW Blog, BMW Group).
# - BMW 700 con Giovanni Michelotti; BMW 1500 "Neue Klasse" en el Salón de Fráncfort de 1961, colas de media hora; Quandt
#   pidió recuperar la doble parrilla (BMW press); producción 1962–1977.
# - "The Ultimate Driving Machine": Martin Puris (Ammirati & Puris), 1974; ventas en EE. UU. 15.007 (1974) → 26.040 (1976).
# - Quandt: estudio de Joachim Scholtyseck (2011, encargado por la familia tras el documental "El silencio de los Quandt",
#   2007): unos 50.000 trabajadores forzados en las fábricas de Günther Quandt; arianización de empresas judías; Günther y
#   Herbert responsables de "numerosas injusticias"; Stefan Quandt: Herbert era "parte del sistema". BMW no fue implicada:
#   la familia compró acciones después de la guerra. Magda, exmujer de Günther (divorcio 1929), se casó con Goebbels; su hijo
#   Harald Quandt fue el único de sus hijos que sobrevivió. Hoy Stefan Quandt y Susanne Klatten tienen ~46 % de BMW.
# - Rover: comprada a British Aerospace en 1994 (~800 M£); 2000: Land Rover a Ford, Rover a Phoenix por 10 £ simbólicas
#   + préstamo sin intereses de 550 M£; BMW se queda con MINI. Rolls-Royce (1998): VW compra Rolls-Royce Motor Cars (Crewe,
#   ~430–479 M£) pero el nombre y el logo eran de Rolls-Royce plc, que se los cede a BMW por 40 M£; desde 2003, BMW.
# - 2025: grupo 2,46 M de vehículos; marca BMW 2.169.761 vs Mercedes-Benz 2,16 M; beneficio neto ~7.500 M€ (Mercedes 5.300 M€);
#   ingresos −6,3 % (133.000 M€); 442.072 eléctricos; previsión negativa para 2026 (China, aranceles). Milan Nedeljković
#   sustituye a Oliver Zipse el 14-may-2026; nueva generación eléctrica "Neue Klasse" (iX3).
VOICE = "i4Kar2uamCWyas8TAu31"  # Adán (como el 007)
SPEED = 1.0

def I(key, cap=None, pop=None, **kw):
    d = dict(type="img", key=key)
    if cap: d["cap"] = cap
    if pop: d["pop"] = pop
    d.update(kw); return d

# Imágenes IA (vidIQ generate_thumbnail): solo para momentos históricos sin vídeo. El resto son tomas reales (clips/, broll.json).
IMAGES = {
    "engine_1917": "1917 aircraft engine workshop, mechanics assembling an inline six-cylinder aero engine, sepia archival photo, no text, no logos",
    "moto_1923": "1920s motorcycle workshop, vintage motorcycle with boxer engine, two mechanics, sepia archival photo, no text, no logos",
    "factory_ruins": "bombed-out factory hall in 1945, collapsed roof, rubble, workers clearing debris, black and white, no text, no logos",
    "pots_1946": "1946 post-war workshop making aluminium pots and pans by hand, black and white archival photo, no text, no logos",
    "meeting_1959": "crowded shareholders meeting in a hall in December 1959, men in suits arguing, smoke, black and white, no text, no logos",
    "bubble_1955": "1955 European street, tiny round bubble car with front-opening door, young couple, faded color slide, no text, no logos",
    "war_factory": "1940s aircraft engine factory hall, rows of radial engines, somber, empty, black and white, no text, no logos",
}

SCENES = [
    # --- GANCHO ---
    dict(id="s01", text="Nueve de diciembre de mil novecientos cincuenta y nueve. En una sala de Múnich, cientos de accionistas están a punto de votar el final de BMW.",
         visual=I("meeting_1959", pop=["9 DE DICIEMBRE DE 1959"])),
    dict(id="s02", text="La propuesta es vendérsela a su gran rival: Mercedes-Benz. El banco que controla la deuda de BMW ya lo da por hecho.",
         visual=I("merc_emblem", pop=["VENDIDA A MERCEDES"], pop_col="red")),
    dict(id="s03", text="Pero esa noche pasa algo que nadie esperaba. Y sesenta y seis años después, BMW vende más autos de su marca que Mercedes y gana miles de millones más.",
         visual=dict(type="versus", title="2025", left=["BMW", "2.169.761 AUTOS"], right=["MERCEDES", "2.160.000 AUTOS"], mid="VS", lcol="yellow", rcol="red")),
    dict(id="s04", text="¿Cómo pasó de estar a punto de desaparecer a ser una de las marcas más deseadas del planeta?",
         visual=I("bmw_hq_1")),
    dict(id="s05", text="Esta historia tiene motores de avión, motos, ollas de cocina, un auto con forma de huevo y la peor compra de su historia.",
         visual=I("engine_1917", pop=["AVIONES", "OLLAS", "UN HUEVO CON RUEDAS"])),
    dict(id="s06", text="Y también tiene una parte oscura. La de la familia que salvó a BMW, y un pasado que tardó más de sesenta años en contar.",
         visual=I("war_factory", shake=True)),
    dict(id="s07", text="Esta es la historia completa de BMW. Del cielo, a casi la quiebra, a la cima.",
         visual=I("bmw_forest")),

    # --- 01 MOTORES PARA EL CIELO ---
    dict(id="s08", text="Capítulo uno. Motores para el cielo.",
         visual=dict(type="title", num="01", text="MOTORES PARA EL CIELO", name="Motores para el cielo")),
    dict(id="s09", text="Múnich, plena Primera Guerra Mundial. Alemania necesita aviones, y los aviones necesitan motores.",
         visual=I("munich_aerial", cap="MÚNICH, 1916")),
    dict(id="s10", text="BMW cuenta como fecha de nacimiento el siete de marzo de mil novecientos dieciséis, cuando se funda una fábrica de aviones en Múnich.",
         visual=dict(type="year", year="1916", sub="NACE LA EMPRESA QUE SERÁ BMW")),
    dict(id="s11", text="Muy cerca, otra empresa, Rapp Motorenwerke, fabrica motores de avión. En mil novecientos diecisiete cambia de nombre: Bayerische Motoren Werke. Fábrica bávara de motores. BMW.",
         visual=dict(type="quote", text="BAYERISCHE\nMOTOREN\nWERKE")),
    dict(id="s12", text="Su primer gran producto lo diseña un ingeniero llamado Max Friz: un motor de avión, el BMW tres A.",
         visual=I("engine_1917", pop=["MAX FRIZ"])),
    dict(id="s13", text="Su ventaja era enorme para la época: en altura, donde el aire es más fino, rendía más que los motores rivales.",
         visual=I("ww2_plane", pop=["MÁS POTENCIA EN ALTURA"])),
    dict(id="s14", text="Y de esos años viene el logo. Durante décadas se dijo que era una hélice girando contra el cielo azul.",
         visual=I("bmw_hq_2", pop=["¿UNA HÉLICE?"])),
    dict(id="s15", text="Pero no. El círculo viene del logo de Rapp, y el azul y el blanco son los colores de Baviera. Lo de la hélice apareció recién a fines de los años veinte, en publicidad.",
         visual=dict(type="stamp", text="EL LOGO DE LA HÉLICE", stamp="MITO", col="yellow")),
    dict(id="s16", text="Entonces la guerra termina, y Alemania pierde. El Tratado de Versalles le prohíbe a Alemania tener aviación militar.",
         visual=dict(type="headline", kicker="28 de junio de 1919", text="El Tratado de Versalles prohíbe a Alemania la aviación militar", mark="prohíbe", source="Fuente: Tratado de Versalles")),
    dict(id="s17", text="Para una empresa que vivía de hacer motores de avión, eso es una sentencia. BMW tiene que inventarse otro negocio.",
         visual=I("factory_ruins", pop=["SIN NEGOCIO"], pop_col="red")),

    # --- 02 DOS RUEDAS, CUATRO RUEDAS ---
    dict(id="s18", text="Capítulo dos. Dos ruedas, cuatro ruedas.",
         visual=dict(type="title", num="02", text="DOS RUEDAS, CUATRO RUEDAS", name="Dos ruedas, cuatro ruedas")),
    dict(id="s19", text="En mil novecientos veintitrés, BMW presenta su primera moto: la R treinta y dos.",
         visual=I("moto_1923", pop=["R32 · 1923"])),
    dict(id="s20", text="Tenía un motor bóxer: dos cilindros acostados, que sobresalen a cada lado. Se enfrían con el aire y bajan el centro de gravedad.",
         visual=I("moto_1923", pop=["MOTOR BÓXER"])),
    dict(id="s21", text="Cien años después, BMW sigue fabricando motos con esa misma idea. Es una de sus señas de identidad.",
         visual=I("moto_gs", pop=["100 AÑOS DESPUÉS"])),
    dict(id="s22", text="Pero las motos no alcanzan. BMW quiere autos. Y en mil novecientos veintiocho encuentra un atajo.",
         visual=I("moto_country")),
    dict(id="s23", text="Compra una fábrica en Eisenach, en el centro de Alemania, que hacía un auto pequeño llamado Dixi.",
         visual=dict(type="route", title="LA PRIMERA FÁBRICA DE AUTOS", points={"Múnich": [0.56, 0.80], "Eisenach": [0.47, 0.38]}, routes=[["Múnich", "Eisenach"]])),
    dict(id="s24", text="El detalle curioso: el Dixi no era un diseño alemán. Era una copia, con licencia, del Austin Seven británico.",
         visual=dict(type="versus", title="EL PRIMER BMW", left=["DIXI", "HECHO EN ALEMANIA"], right=["AUSTIN SEVEN", "DISEÑO BRITÁNICO"], mid="=", lcol="yellow", rcol="red")),
    dict(id="s25", text="Así que el primer auto con el nombre BMW, el tres quince, era en realidad un auto inglés con otro escudo.",
         visual=I("classic_interior", pop=["UN AUTO INGLÉS"])),
    dict(id="s26", text="Durante los años treinta, BMW aprende rápido. Sus autos ganan fama de deportivos, ligeros y bien hechos.",
         visual=I("classic_wheel")),
    dict(id="s27", text="Y entonces llega otra guerra. Y con ella, la parte de la historia que BMW tardó décadas en contar.",
         visual=I("ww2_plane", shake=True)),

    # --- 03 LA PARTE QUE BMW CALLÓ ---
    dict(id="s28", text="Capítulo tres. La parte que BMW calló.",
         visual=dict(type="title", num="03", text="LA PARTE QUE BMW CALLÓ", name="La parte que BMW calló")),
    dict(id="s29", text="Durante la Segunda Guerra Mundial, BMW vuelve a lo que mejor sabe hacer: motores de avión. Esta vez, para el ejército de Hitler.",
         visual=I("war_factory", pop=["MOTORES PARA LA LUFTWAFFE"])),
    dict(id="s30", text="Para cumplir con la producción, faltan trabajadores. Y la empresa recurre al trabajo forzado.",
         visual=I("war_factory", shake=True)),
    dict(id="s31", text="No lo decimos nosotros. Lo dice hoy la propia BMW en su web: su dirección no tuvo reparos en usar trabajadores forzados y prisioneros de campos de concentración.",
         visual=dict(type="headline", kicker="BMW Group, historia oficial", text="La dirección no tuvo reparos en usar trabajo forzado y prisioneros de campos de concentración", mark="trabajo forzado", source="Fuente: bmwgroup.com (parafraseado)")),
    dict(id="s32", text="En mil novecientos cuarenta y tres se crea, junto a una de sus fábricas, el campo de Allach, dependiente del campo de concentración de Dachau. Los prisioneros trabajaban hasta doce horas por día.",
         visual=dict(type="stamp", text="ALLACH, 1943\nHASTA 12 HORAS POR DÍA", stamp="TRABAJO FORZADO")),
    dict(id="s33", text="Como casi todas las empresas alemanas, BMW negó durante mucho tiempo su responsabilidad. Desde dos mil veinte, su museo en Múnich tiene un espacio dedicado a este capítulo.",
         visual=I("bmw_hq_1", pop=["DESDE 2020, EN SU MUSEO"])),
    dict(id="s34", text="Y cuando la guerra termina, en mil novecientos cuarenta y cinco, BMW está destruida.",
         visual=I("factory_ruins", pop=["1945"], pop_col="red")),

    # --- 04 OLLAS, MOTOS Y UN HUEVO CON RUEDAS ---
    dict(id="s35", text="Capítulo cuatro. Ollas, motos y un huevo con ruedas.",
         visual=dict(type="title", num="04", text="OLLAS, MOTOS Y UN HUEVO", name="Ollas, motos y un huevo con ruedas")),
    dict(id="s36", text="Las naves de Múnich están bombardeadas o desmontadas. Y la fábrica de autos de Eisenach queda del otro lado: en la zona soviética.",
         visual=dict(type="route", title="ALEMANIA PARTIDA EN DOS", points={"Múnich (BMW)": [0.56, 0.80], "Eisenach (zona soviética)": [0.47, 0.38]}, routes=[["Múnich (BMW)", "Eisenach (zona soviética)"]], red=True)),
    dict(id="s37", text="Allí los soviéticos se quedan con la fábrica, y durante años hacen autos con diseños de BMW bajo otro nombre: EMW.",
         visual=I("dealership_bw", pop=["EMW"], pop_col="red")),
    dict(id="s38", text="BMW se queda sin fábrica de autos. ¿Y qué hace para no cerrar? Ollas. Cacerolas. Utensilios de cocina.",
         visual=I("pots_1946", pop=["OLLAS Y CACEROLAS"])),
    dict(id="s39", text="La idea era simple: mantener ocupados a sus obreros especializados hasta que se pudiera volver a fabricar algo de verdad.",
         visual=I("pots_1946", shake=True)),
    dict(id="s40", text="En mil novecientos cuarenta y ocho vuelven las motos. Y en mil novecientos cincuenta y uno, el primer auto de posguerra: el BMW quinientos uno.",
         visual=dict(type="timeline", title="VOLVER A FABRICAR", points=[["1945", "Fábricas destruidas"], ["1946", "Ollas y cacerolas"], ["1948", "Vuelven las motos"], ["1951", "BMW 501"]], hl=3)),
    dict(id="s41", text="Era un sedán grande, lujoso y caro. El problema es que la Alemania de los cincuenta estaba en ruinas, y casi nadie podía pagarlo.",
         visual=I("showroom", pop=["DEMASIADO CARO"], pop_col="red")),
    dict(id="s42", text="Entonces, en el Salón de Turín de mil novecientos cincuenta y cuatro, alguien de BMW ve algo raro: un auto diminuto, redondo, con la puerta adelante.",
         visual=dict(type="route", title="UNA IDEA ITALIANA", points={"Turín": [0.36, 0.86], "Múnich": [0.56, 0.62]}, routes=[["Turín", "Múnich"]])),
    dict(id="s43", text="Se llamaba Isetta, lo fabricaba una empresa italiana llamada Iso, y para entrar había que abrir todo el frente del auto.",
         visual=I("bubble_1955", pop=["ISETTA"])),
    dict(id="s44", text="BMW compra la licencia y desde mil novecientos cincuenta y cinco fabrica su propia Isetta. La gente la llama el auto burbuja.",
         visual=I("bubble_1955", pop=["EL AUTO BURBUJA"])),
    dict(id="s45", text="Es barata, gasta muy poco, y salva miles de empleos en Múnich. Los obreros que hacían motos pasan a fabricar Isettas.",
         visual=I("antique_show")),
    dict(id="s46", text="Pero BMW tiene un problema de fondo. Los autos de lujo pierden dinero, y los baratos no dejan suficiente.",
         visual=dict(type="versus", title="EL PROBLEMA DE BMW", left=["LUJO", "NADIE LOS COMPRA"], right=["ISETTA", "DEJA POCO"], mid="+", lcol="red", rcol="red")),
    dict(id="s47", text="Las deudas crecen. Y a finales de los años cincuenta, BMW está al borde de la quiebra.",
         visual=dict(type="stamp", text="FINALES DE LOS AÑOS 50", stamp="AL BORDE DE LA QUIEBRA")),

    # --- 05 LA NOCHE DEL 9 DE DICIEMBRE ---
    dict(id="s48", text="Capítulo cinco. La noche del nueve de diciembre.",
         visual=dict(type="title", num="05", text="LA NOCHE DEL 9 DE DICIEMBRE", name="La noche del 9 de diciembre")),
    dict(id="s49", text="Mil novecientos cincuenta y nueve. BMW le debe muchísimo dinero al Deutsche Bank, el banco más poderoso de Alemania.",
         visual=I("meeting_1959", pop=["DEUTSCHE BANK"])),
    dict(id="s50", text="Y el hombre del banco en el consejo de BMW, Hans Feith, tiene un plan: que Daimler-Benz, la dueña de Mercedes, se quede con BMW.",
         visual=I("merc_gt", pop=["DAIMLER-BENZ"], pop_col="red")),
    dict(id="s51", text="Según la propia BMW, la venta parecía cosa decidida. BMW iba a ser, como mucho, una fábrica más de Mercedes.",
         visual=dict(type="headline", kicker="BMW Group, sobre 1959", text="La venta de BMW a Daimler-Benz parecía cosa decidida", mark="decidida", source="Fuente: BMW Group (parafraseado)")),
    dict(id="s52", text="El nueve de diciembre se convoca la junta de accionistas en Múnich. La opción que les ponen delante es brutal: o Mercedes, o la quiebra.",
         visual=dict(type="versus", title="9 DE DICIEMBRE DE 1959", left=["OPCIÓN 1", "VENDER A MERCEDES"], right=["OPCIÓN 2", "LA QUIEBRA"], mid="O", lcol="yellow", rcol="red")),
    dict(id="s53", text="Pero en la sala hay gente que no está dispuesta a rendirse. Pequeños accionistas, concesionarios, trabajadores.",
         visual=I("meeting_1959", shake=True)),
    dict(id="s54", text="Uno de ellos es Erich Nold, un pequeño accionista que empieza a alargar la reunión con preguntas y objeciones.",
         visual=I("meeting_1959", pop=["ERICH NOLD"])),
    dict(id="s55", text="Otro es Friedrich Mathern, un abogado que representa a concesionarios y que llega con argumentos legales contra las cuentas que presenta la dirección.",
         visual=I("meeting_1959", pop=["FRIEDRICH MATHERN"])),
    dict(id="s56", text="Y en la sala se menciona un dato que lo cambia todo: el nuevo modelo pequeño de BMW, el setecientos, ya tiene veinticinco mil pedidos.",
         visual=dict(type="num", start=0, end=25000, label="PEDIDOS DEL BMW 700 CITADOS EN LA JUNTA")),
    dict(id="s57", text="Después de horas de discusión, los opositores reúnen las acciones suficientes para frenar la votación. La venta a Mercedes no se aprueba.",
         visual=dict(type="stamp", text="LA VENTA A DAIMLER-BENZ", stamp="FRENADA", col="green")),
    dict(id="s58", text="BMW sigue viva. Pero solo por ahora: sin dinero, ese aplazamiento no sirve de nada.",
         visual=I("munich_aerial")),
    dict(id="s59", text="Y ahí aparece el personaje clave de esta historia: Herbert Quandt, un industrial que ya tenía una parte importante de BMW.",
         visual=dict(type="quote", text="HERBERT\nQUANDT")),
    dict(id="s60", text="Las versiones no coinciden. Algunas dicen que al principio Quandt apoyaba la venta a Daimler. Pero al final cambia de idea y apuesta por BMW.",
         visual=I("dealership_bw", pop=["CAMBIA DE IDEA"])),
    dict(id="s61", text="En mil novecientos sesenta respalda un plan de rescate con una ampliación de capital, y su familia termina quedándose con cerca de la mitad de la empresa.",
         visual=dict(type="timeline", title="EL RESCATE", points=[["9 DIC 1959", "Se frena la venta"], ["NOV 1960", "Plan de rescate"], ["1960", "Los Quandt, cerca de la mitad"]], hl=0)),

    # --- 06 LA NUEVA CLASE ---
    dict(id="s62", text="Capítulo seis. La Nueva Clase.",
         visual=dict(type="title", num="06", text="LA NUEVA CLASE", name="La Nueva Clase")),
    dict(id="s63", text="El setecientos, diseñado con el italiano Giovanni Michelotti, se vende bien y le da a BMW el aire que necesitaba.",
         visual=I("bmw_320i", pop=["BMW 700"])),
    dict(id="s64", text="Pero la verdadera apuesta se presenta en el Salón de Fráncfort de mil novecientos sesenta y uno: el BMW mil quinientos. La Nueva Clase.",
         visual=dict(type="year", year="1961", sub="LA NUEVA CLASE, EN FRÁNCFORT")),
    dict(id="s65", text="La gente hacía cola durante media hora para verlo. Era un sedán mediano, moderno, que se manejaba como un deportivo.",
         visual=I("showroom", pop=["MEDIA HORA DE COLA"])),
    dict(id="s66", text="Y un detalle: cuando Quandt vio el diseño terminado, pidió que volviera la doble parrilla con forma de riñones. La misma que BMW sigue usando hoy.",
         visual=I("classic_front", pop=["LOS DOS RIÑONES"])),
    dict(id="s67", text="Con la Nueva Clase, BMW encuentra por fin su lugar: autos para gente que disfruta manejar. Ni el lujo pesado de Mercedes, ni el auto barato de todos.",
         visual=dict(type="versus", title="EL LUGAR DE BMW", left=["MERCEDES", "LUJO Y CONFORT"], right=["BMW", "PLACER DE MANEJAR"], mid="≠", lcol="red", rcol="yellow")),
    dict(id="s68", text="En mil novecientos setenta y dos nace su división deportiva, BMW M. Y al año siguiente estrena su sede en Múnich: una torre con forma de cuatro cilindros.",
         visual=I("bmw_hq_1", pop=["LA TORRE DE CUATRO CILINDROS"])),
    dict(id="s69", text="En mil novecientos setenta y cinco llega la Serie tres, que con los años se convierte en su auto más importante.",
         visual=I("bmw_drift", pop=["SERIE 3"])),
    dict(id="s70", text="Y en Estados Unidos, una agencia pequeña le inventa un eslogan que todavía usa: The Ultimate Driving Machine. La máquina definitiva para manejar.",
         visual=dict(type="quote", text="«THE ULTIMATE\nDRIVING MACHINE»")),
    dict(id="s71", text="Funcionó. En mil novecientos setenta y cuatro, BMW vendía unos quince mil autos en Estados Unidos. Dos años después, más de veintiséis mil.",
         visual=dict(type="bars", title="BMW EN EE. UU.", data=[["1974", 15007], ["1976", 26040]])),
    dict(id="s72", text="La empresa que en mil novecientos cincuenta y nueve casi termina como una fábrica de Mercedes ahora competía de igual a igual con Mercedes.",
         visual=I("autobahn")),

    # --- 07 EL SILENCIO DE LOS QUANDT ---
    dict(id="s73", text="Capítulo siete. El silencio de los Quandt.",
         visual=dict(type="title", num="07", text="EL SILENCIO DE LOS QUANDT", name="El silencio de los Quandt")),
    dict(id="s74", text="Herbert Quandt murió en mil novecientos ochenta y dos como el hombre que salvó a BMW. Pero su familia guardaba una historia que no contaba.",
         visual=I("classic_interior", shake=True)),
    dict(id="s75", text="En dos mil siete, una televisión alemana emitió un documental con un título directo: El silencio de los Quandt.",
         visual=dict(type="headline", kicker="2007, televisión alemana", text="El silencio de los Quandt", mark="silencio", source="Documental (título traducido)")),
    dict(id="s76", text="Ante la presión, la familia encargó un estudio independiente al historiador Joachim Scholtyseck. Se publicó en dos mil once, y tenía unas mil doscientas páginas.",
         visual=dict(type="num", start=0, end=1200, label="PÁGINAS DEL ESTUDIO SOBRE LOS QUANDT (2011)")),
    dict(id="s77", text="Las conclusiones fueron durísimas. En las fábricas del padre de Herbert, Günther Quandt, trabajaron unos cincuenta mil trabajadores forzados durante el nazismo.",
         visual=dict(type="num", start=0, end=50000, label="TRABAJADORES FORZADOS EN LAS FÁBRICAS DE GÜNTHER QUANDT")),
    dict(id="s78", text="Esas fábricas hacían baterías y armas para el régimen. Y la familia se había quedado con empresas que les quitaron a sus dueños judíos.",
         visual=I("war_factory", pop=["EMPRESAS QUITADAS A DUEÑOS JUDÍOS"], pop_col="red")),
    dict(id="s79", text="El estudio concluyó que Günther y también Herbert fueron responsables de numerosas injusticias. Su hijo, Stefan Quandt, lo resumió así: su padre era parte del sistema.",
         visual=dict(type="quote", text="«ERA PARTE\nDEL SISTEMA»")),
    dict(id="s80", text="Una aclaración importante: el estudio no implica a BMW. La familia compró sus acciones de BMW después de la guerra.",
         visual=dict(type="stamp", text="EL ESTUDIO DE 2011\nNO IMPLICA A BMW", stamp="ACLARACIÓN", col="white")),
    dict(id="s81", text="Y hay un dato todavía más inquietante. La segunda esposa de Günther Quandt se llamaba Magda. Se divorciaron en mil novecientos veintinueve.",
         visual=dict(type="year", year="1929", sub="GÜNTHER QUANDT Y MAGDA SE DIVORCIAN")),
    dict(id="s82", text="Dos años después, Magda se casó con Joseph Goebbels, el ministro de propaganda de Hitler. Su hijo con Günther, Harald Quandt, fue el único de sus hijos que sobrevivió a la guerra.",
         visual=I("factory_ruins", pop=["MAGDA GOEBBELS"], pop_col="red")),
    dict(id="s83", text="Hoy, los hijos de Herbert, Stefan Quandt y Susanne Klatten, tienen casi la mitad de BMW. Son una de las familias más ricas de Alemania.",
         visual=dict(type="bars", title="QUIÉN CONTROLA BMW (% APROX.)", data=[["FAMILIA QUANDT", 46], ["RESTO", 54]])),

    # --- 08 DIEZ LIBRAS Y UN ROLLS-ROYCE ---
    dict(id="s84", text="Capítulo ocho. Diez libras y un Rolls-Royce.",
         visual=dict(type="title", num="08", text="DIEZ LIBRAS Y UN ROLLS-ROYCE", name="Diez libras y un Rolls-Royce")),
    dict(id="s85", text="Volvamos a los autos. En mil novecientos noventa y cuatro, BMW quiere crecer rápido, y compra el grupo británico Rover por unos ochocientos millones de libras.",
         visual=dict(type="route", title="1994: BMW COMPRA ROVER", points={"Múnich": [0.72, 0.78], "Longbridge (Rover)": [0.30, 0.36]}, routes=[["Múnich", "Longbridge (Rover)"]])),
    dict(id="s86", text="Venía con marcas legendarias: Rover, Land Rover, MG, Mini. Parecía el golpe perfecto.",
         visual=I("mini_suv", pop=["ROVER · LAND ROVER · MG · MINI"])),
    dict(id="s87", text="Fue un desastre. Rover perdía dinero año tras año, y las pérdidas empezaron a arrastrar a todo el grupo.",
         visual=I("factory_pedestal", pop=["PÉRDIDAS"], pop_col="red", shake=True)),
    dict(id="s88", text="En el año dos mil, BMW se rinde. Le vende Land Rover a Ford. ¿Y Rover? Se la vende a un grupo de empresarios por un precio simbólico: diez libras.",
         visual=dict(type="num", start=800000000, end=10, prefix="£", label="LO QUE PAGÓ BMW EN 1994 → LO QUE COBRÓ EN 2000")),
    dict(id="s89", text="Y encima les presta quinientos cincuenta millones de libras sin intereses. Comprar Rover fue la peor decisión de su historia moderna.",
         visual=dict(type="stamp", text="ROVER, 2000\n10 LIBRAS", stamp="VENDIDA")),
    dict(id="s90", text="De todo ese desastre, BMW se queda con una sola cosa: la marca Mini. Y en dos mil uno lanza un Mini nuevo que se convierte en un éxito mundial.",
         visual=I("mini_suv", pop=["SE QUEDA CON MINI"])),
    dict(id="s91", text="Y mientras tanto, gana una de las jugadas más astutas de la industria. En mil novecientos noventa y ocho se vende Rolls-Royce Motor Cars.",
         visual=I("rolls_sign", pop=["ROLLS-ROYCE"])),
    dict(id="s92", text="Volkswagen gana la subasta y se queda con la fábrica de Crewe, en Inglaterra. Pero había un detalle que se le escapó.",
         visual=I("luxury_pass", pop=["VOLKSWAGEN GANA LA SUBASTA"])),
    dict(id="s93", text="El nombre Rolls-Royce y su logo no eran de la empresa de autos. Eran de Rolls-Royce, la de los motores de avión. Y esa empresa se los cede a BMW por cuarenta millones de libras.",
         visual=dict(type="versus", title="ROLLS-ROYCE, 1998", left=["VOLKSWAGEN", "LA FÁBRICA"], right=["BMW", "EL NOMBRE"], mid="VS", lcol="red", rcol="yellow")),
    dict(id="s94", text="Resultado: Volkswagen se queda con Bentley, y desde dos mil tres los Rolls-Royce los hace BMW. La empresa que empezó con motores de avión le ganó el nombre a la de motores de avión.",
         visual=I("rolls_sign", pop=["DESDE 2003, BMW"])),

    # --- 09 EL REGRESO DE LA NUEVA CLASE ---
    dict(id="s95", text="Capítulo nueve. El regreso de la Nueva Clase.",
         visual=dict(type="title", num="09", text="EL REGRESO DE LA NUEVA CLASE", name="El regreso de la Nueva Clase")),
    dict(id="s96", text="Hoy el grupo BMW, con Mini y Rolls-Royce, entrega cerca de dos millones y medio de vehículos al año.",
         visual=I("factory_auto", pop=["2,46 MILLONES (2025)"])),
    dict(id="s97", text="Y en dos mil veinticinco pasó algo que en mil novecientos cincuenta y nueve habría parecido ciencia ficción.",
         visual=I("robots")),
    dict(id="s98", text="La marca BMW vendió dos millones ciento sesenta y nueve mil autos. Mercedes-Benz, unos dos millones ciento sesenta mil. BMW, por delante.",
         visual=dict(type="bars", title="AUTOS VENDIDOS EN 2025", data=[["BMW", 2169761], ["MERCEDES", 2160000]])),
    dict(id="s99", text="Y en beneficios, todavía más: BMW ganó casi siete mil quinientos millones de euros. Mercedes, unos cinco mil trescientos.",
         visual=dict(type="bars", title="BENEFICIO NETO 2025 (M€)", data=[["BMW", 7500], ["MERCEDES", 5300]])),
    dict(id="s100", text="Eso no quiere decir que todo vaya bien. Sus ingresos cayeron más de un seis por ciento, sufre en China y con los aranceles, y espera un dos mil veintiséis difícil.",
         visual=I("ev_charge", pop=["−6,3 % DE INGRESOS"], pop_col="red")),
    dict(id="s101", text="Pero llega mejor preparada que muchos a la era eléctrica. En dos mil veinticinco vendió más de cuatrocientos cuarenta mil autos totalmente eléctricos.",
         visual=dict(type="num", start=0, end=442072, label="ELÉCTRICOS ENTREGADOS EN 2025")),
    dict(id="s102", text="En mayo de dos mil veintiséis cambió de jefe: Oliver Zipse se fue después de treinta y cinco años, y llegó Milan Nedeljković, el responsable de las fábricas.",
         visual=dict(type="timeline", title="BMW HOY", points=[["2025", "Supera a Mercedes"], ["MAY 2026", "Nuevo CEO"], ["2026", "Nueva Clase eléctrica"]], hl=2)),
    dict(id="s103", text="Y su gran apuesta para el futuro tiene un nombre conocido. La nueva generación de autos eléctricos de BMW se llama Neue Klasse. La Nueva Clase.",
         visual=I("ev_charge", pop=["NEUE KLASSE"])),
    dict(id="s104", text="El mismo nombre del auto que la salvó en mil novecientos sesenta y uno. No es casualidad: es la forma que tiene BMW de decir que vuelve a jugarse todo.",
         visual=I("bmw_drive", pop=["1961 → 2026"])),

    # --- CIERRE ---
    dict(id="s105", text="Si hay que sacar algo de esta historia, son tres cosas.",
         visual=I("steering")),
    dict(id="s106", text="Primera: una empresa puede reinventarse más de una vez. Motores de avión, motos, ollas, autos burbuja, sedanes deportivos.",
         visual=dict(type="timeline", title="LAS VIDAS DE BMW", points=[["1916", "Aviones"], ["1923", "Motos"], ["1946", "Ollas"], ["1955", "Isetta"], ["1961", "Nueva Clase"]], hl=4)),
    dict(id="s107", text="Segunda: a veces todo depende de una noche, y de unas pocas personas que se niegan a firmar.",
         visual=I("meeting_1959", pop=["UNA NOCHE"])),
    dict(id="s108", text="Y tercera: el éxito no borra el pasado. BMW y los Quandt tardaron décadas en contar el suyo.",
         visual=I("war_factory")),
    dict(id="s109", text="Ahora te pregunto a ti. ¿BMW o Mercedes? ¿Y qué empresa quieres que contemos en el próximo video? Te leo en los comentarios.",
         visual=dict(type="versus", title="¿Y TÚ?", left=["BMW", "PLACER DE MANEJAR"], right=["MERCEDES", "LUJO Y CONFORT"], mid="¿?", lcol="yellow", rcol="red")),
    dict(id="s110", text="Si te gustó, suscríbete y activa la campanita. Gracias por llegar hasta el final. Nos vemos en el próximo balance.",
         visual=I("bmw_forest")),
]

PRONUNCIA = {
    "Bayerische Motoren Werke": "Báierishe Motóren Verke", "Rapp Motorenwerke": "Rap Motórenverke", "BMW": "be eme doble ve",
    "Mercedes-Benz": "Mercedes Benz", "Daimler-Benz": "Dáimler Benz", "Daimler": "Dáimler", "Deutsche Bank": "Dóiche Bank",
    "Herbert Quandt": "Hérbert Kvant", "Günther Quandt": "Gúnter Kvant", "Harald Quandt": "Hárald Kvant", "Stefan Quandt": "Stéfan Kvant",
    "Quandt": "Kvant", "Günther": "Gúnter", "Susanne Klatten": "Susane Kláten", "Joachim Scholtyseck": "Yóajim Sholtísek",
    "Erich Nold": "Érij Nold", "Friedrich Mathern": "Frídrij Mátern", "Hans Feith": "Hans Fait", "Max Friz": "Max Frits",
    "Eisenach": "Áisenaj", "Allach": "Álaj", "Dachau": "Dájau", "Joseph Goebbels": "Yósef Guébels", "Austin Seven": "Óstin Séven",
    "Isetta": "Iseta", "Giovanni Michelotti": "Yovani Mikelóti", "Neue Klasse": "Nóie Klase", "Rolls-Royce Motor Cars": "Rols Rois Mótor Cars",
    "Rolls-Royce": "Rols Rois", "Land Rover": "Land Róver", "Rover": "Róver", "Crewe": "Kru", "Bentley": "Bentli",
    "The Ultimate Driving Machine": "Di Áltimet Dráiving Mashín", "Oliver Zipse": "Óliver Tsípse", "Milan Nedeljković": "Mílan Nedélkovich",
    "Volkswagen": "Volksvaguen", "Múnich": "Múnij", "Fráncfort": "Fráncfort", "Mini": "Mini", "MG": "eme ge",
}

SHORTS = {}  # sin Shorts (pedido del usuario)

THUMBS = [
    dict(img="meeting_1959", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "CASI", 210, "yellow", "la"], ["text", 45, 320, "DESAPARECE", 150, "white", "la"], ["badge", 45, 540, 520, 660, "BMW · 1959", 80]]),
    dict(img="merc_emblem", zoom=1.05, cx=0.6, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "CASI LA", 150, "white", "la"], ["text", 45, 250, "COMPRA", 150, "white", "la"], ["text", 45, 440, "MERCEDES", 160, "red", "la"]]),
    dict(img="bmw_hq_1", zoom=1.0, cx=0.5, cy=0.5, shade=["left", 200, 0.55], items=[
        ["text", 45, 60, "DE OLLAS", 170, "yellow", "la"], ["text", 45, 300, "A SUPERAR", 140, "white", "la"], ["text", 45, 480, "A MERCEDES", 140, "white", "la"]]),
    dict(img="pots_1946", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "BMW HACÍA", 150, "white", "la"], ["text", 45, 260, "OLLAS", 220, "yellow", "la"], ["stamp", "1946", 960, 540, -10, 140]]),
    dict(img="bubble_1955", zoom=1.05, cx=0.55, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "ESTE AUTO", 150, "white", "la"], ["text", 45, 260, "SALVÓ", 190, "yellow", "la"], ["text", 45, 480, "A BMW", 160, "white", "la"]]),
    dict(img="rolls_sign", zoom=1.05, cx=0.6, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "LE GANÓ", 160, "white", "la"], ["text", 45, 260, "ROLLS-ROYCE", 130, "yellow", "la"], ["text", 45, 430, "A VOLKSWAGEN", 110, "white", "la"]]),
    dict(img="war_factory", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "EL SECRETO", 160, "white", "la"], ["text", 45, 270, "DE BMW", 170, "red", "la"]]),
    dict(img="mini_suv", zoom=1.05, cx=0.6, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "PAGÓ 800 M", 150, "white", "la"], ["text", 45, 260, "VENDIÓ POR", 130, "white", "la"], ["text", 45, 430, "10 LIBRAS", 170, "red", "la"]]),
    dict(img="classic_front", zoom=1.05, cx=0.5, cy=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "CASI ES", 190, "yellow", "la"], ["text", 45, 300, "DE", 130, "white", "la"], ["text", 45, 450, "MERCEDES", 160, "red", "la"]]),
    dict(img="meeting_1959", zoom=1.15, cx=0.6, cy=0.45, shade=["left", 230, 0.62], items=[
        ["text", 45, 60, "LA NOCHE", 170, "white", "la"], ["text", 45, 280, "QUE SALVÓ", 150, "yellow", "la"], ["text", 45, 460, "A BMW", 160, "white", "la"]]),
]
THUMBS_TOP = [4, 2, 10]

META = {
    "code": "008",
    "name": "BMW",
    "intro_chapter": "Intro: el 9 de diciembre de 1959",
    "titles": [
        "Estuvo a punto de ser de Mercedes… hoy le gana a Mercedes",
        "BMW: de hacer ollas a superar a Mercedes (la historia completa)",
        "La noche en que BMW casi desaparece (y el secreto de la familia que la salvó)",
    ],
    "description": "El 9 de diciembre de 1959, los accionistas de BMW se reunieron en Múnich para votar su venta a Daimler-Benz, la dueña de Mercedes. El banco lo daba por hecho. Pero esa noche un pequeño accionista, un abogado y 25.000 pedidos de un auto pequeño frenaron la venta, y Herbert Quandt terminó salvando la empresa. Esta es la historia completa de BMW: los motores de avión de 1916, el mito del logo, la primera moto, el trabajo forzado en la guerra (que la propia BMW reconoce), las ollas de posguerra, la Isetta, la Nueva Clase, el pasado nazi de la familia Quandt, el desastre de Rover vendido por 10 libras, la jugada de Rolls-Royce… y cómo en 2025 vendió más autos que Mercedes.",
    "sources": [
        "BMW Group: historia de la empresa; BMW en la época del nacionalsocialismo; \"Learning from crises\" (1959)",
        "Wikipedia / BMW Blog / Bimmerfile / Auto Bild: la junta del 9-dic-1959, Erich Nold, Friedrich Mathern, Hans Feith",
        "BMW 700 Club / BMW press (2011, 50 años de la Neue Klasse)",
        "Ammirati & Puris / BMW press: \"The Ultimate Driving Machine\" (1974)",
        "JTA / History News Network / Forward (2011): estudio de Joachim Scholtyseck sobre la familia Quandt",
        "Wikipedia (Günther, Herbert y Harald Quandt); InvestmentNews / Daily Herald: participación de la familia",
        "Wikipedia (Rover Group, Phoenix Venture Holdings) / Honest John: Rover por 10 £ (2000)",
        "Fleet News / Wikipedia (Rolls-Royce Motors): BMW compra el nombre Rolls-Royce por 40 M£ (1998)",
        "BMW Blog / cars.co.za / Yahoo Finance: ventas y beneficios 2025 de BMW y Mercedes-Benz",
        "heise / electrive / Wards Auto: Milan Nedeljković sustituye a Oliver Zipse (mayo de 2026)",
        "Tomas de vídeo: Pexels — Graphicpedia Creative, Surja Sen Das Raj, Kaboompics, Luis Quintero, K, Gaurav Kumar, LayG Traveller, Edoardo Geninatti, Engin Altundağ, Usman AbdulrasheedGambo, Fich View Studio, Abed Ismail, Ammad Rasool, Yash Rao, Harshal, Kindel Media, CALI_MEDIA, Jozef Papp, El Jundi, Amar Preciado, Altaf Shah",
    ],
    "disclosure": "Las tomas de vídeo son reales (Pexels, autores en las fuentes) y no muestran los hechos narrados. Las imágenes históricas (taller de 1917, moto de los años 20, ruinas de 1945, ollas, la junta de 1959, el auto burbuja y la fábrica de guerra) son ilustraciones generadas con IA, no fotografías reales. Narración con voz sintética.",
    "hashtags": "#BMW #Mercedes #HistoriaDeEmpresas #Negocios",
    "playlist": "Auges y gigantes",
    "tags": ["BMW", "historia de BMW", "BMW vs Mercedes", "Mercedes-Benz", "BMW historia", "familia Quandt", "Herbert Quandt",
             "BMW 1959", "BMW Isetta", "Rolls-Royce", "Mini", "Rover", "historia de empresas", "autos alemanes", "el último balance"],
    "pinned": "¿BMW o Mercedes? 🚗 Cuéntame cuál eliges y qué empresa quieres para el próximo video 👇",
    "shorts": {},
}
