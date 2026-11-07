# Vídeo 007 — Spirit Airlines: un juez le prohibió venderse… y dos años después cerró de un día para otro (15 min)
# Tema con datos (API de YouTube, 7-nov-2026): EN "Spirit Airlines shuts down" (CNN) 1,02 M, GBH 832k, "120 abandoned Spirit
# airplanes" 816k (mayo-2026); ES: Relatos Aéreos 383k, Moris Dieck 369k (más genéricos) → hay demanda en español.
# Formato nuevo (pedido del usuario): vuelve a imágenes IA (nano-banana-2-lite) + más animación: tablero de salidas, mapa
# con rutas, titulares, palabras que saltan (pop), barridos entre imágenes, destello/glitch en capítulos, temblor, grano,
# cambios de plano cada ~3,3 s. Lecciones: gancho en plena acción, giro adelantado, mini-cliffhangers cada 60–90 s.
# Hechos verificados (6/7-nov-2026):
# - Origen: Ned Homfeld funda Charter One (1983; algunas fuentes 1980) cerca de Detroit, viajes chárter a Atlantic City/Las
#   Vegas; mayo-1992 jets propios y nombre Spirit Airlines; 1-jun-1992 primera ruta regular Detroit–Atlantic City (Wikipedia).
# - 2007: Ben Baldanza, modelo de ultra bajo coste inspirado en parte en Ryanair. Abril-2010: primera aerolínea de EE. UU. en
#   cobrar el equipaje de mano (desde 1-ago-2010: 30 $ por adelantado, 45 $ en la puerta) (ABC/AP/Star Tribune).
# - 5-feb-2022 acuerdo con Frontier; 27-jul-2022 Spirit lo rompe; JetBlue: 33,50 $/acción en efectivo (~3.800 M$) (ch-aviation).
# - 16-ene-2024: el juez William Young (Boston) bloquea la compra en un fallo de 113 páginas: los clientes que dependen del
#   modelo de Spirit saldrían perjudicados; las acciones caen ~47 % (KSL/WBUR/TMJ4).
# - Motores GTF de Pratt & Whitney: ~40 aviones parados a finales de 2024; compensación posterior (AirlineGeeks/FlightGlobal).
# - Más de 2.500 M$ perdidos desde 2020; 18-nov-2024 primera quiebra; ofertas de Frontier rechazadas (ene/feb-2025);
#   12-mar-2025 sale (deuda por acciones); abr-2025 dimite el CEO; ago-2025 "dudas sustanciales"; el procesador de tarjetas
#   (Elavon) retiene hasta 3 M$/día; 29-ago-2025 segunda quiebra, 5 meses después (Financier Worldwide/AltexSoft/GMA).
# - 2026: el combustible de avión casi se duplica desde febrero por la guerra con Irán (NBC); el plan de marzo fracasa;
#   rescate federal de 500 M$ negociado con el Gobierno (con participación en la empresa, según una información) sin acuerdo
#   con los bonistas (CNBC/ABC/Travel Market Report); 2-may-2026 cierre inmediato, 277 vuelos cancelados ese día, 17.000
#   empleos directos e indirectos según la empresa; flota de ~131 aviones (dic-2025) en tierra para liquidarla.
VOICE = "i4Kar2uamCWyas8TAu31"  # ElevenLabs "Adán - Narration"
SPEED = 1.0
IMAGE_MODEL = "nano-banana-2-lite"

N = ", photorealistic, cinematic lighting, 16:9, no text, no logos"
IMAGES = {
    "terminal_night": "Empty airport terminal at night before dawn, rows of empty seats, dim blue lights, closed departure gates, quiet and tense" + N,
    "stranded": "Stranded travelers sitting on the floor of an airport terminal with suitcases at dawn, tired atmosphere, seen from behind" + N,
    "tarmac_sunset": "Bright yellow passenger jet on an airport tarmac at sunset, dramatic sky" + N,
    "courtroom": "Empty American federal courtroom with wooden judge bench and gavel, dramatic window light, no people" + N,
    "yellow_parked": "Aerial view of many bright yellow passenger jets parked in rows at an airport, overcast sky" + N,
    "charter_80s": "1980s film photo style, small vintage passenger jet on a snowy Michigan airport apron, tourists boarding with luggage, film grain, faded colors" + N,
    "vintage_jet": "Early 1990s passenger jet taking off at dusk, vintage film look, warm tones" + N,
    "casino_night": "Seaside casino boardwalk lights at night in the early 1990s, film photo look, no readable signs" + N,
    "florida_airport": "Florida airport with palm trees and a bright yellow passenger jet taxiing on a sunny day" + N,
    "cramped_seats": "Interior of a crowded low-cost airplane cabin, narrow seats with yellow headrests, passengers seen from behind" + N,
    "bag_sizer": "Traveler at an airport gate pushing a carry-on suitcase into a metal bag sizer frame, gate counter blurred behind" + N,
    "frustrated": "Frustrated traveler at an airline check-in counter with hand on forehead, seen from the side, airport blurred behind" + N,
    "full_cabin": "Airplane cabin packed with passengers, every seat occupied, view down the aisle" + N,
    "yellow_flying": "Bright yellow passenger jet flying above white clouds in a blue sky" + N,
    "boardroom": "Corporate boardroom with executives around a long table seen from behind, city skyline at night through windows" + N,
    "two_planes": "Two passenger jets, one painted green and one painted dark blue, parked nose to nose on an airport apron at dusk, rivalry mood" + N,
    "courthouse": "Exterior of a modern federal courthouse on a cold grey winter day by the harbor" + N,
    "trading_red": "Stock trading screens glowing red with falling charts in a dark office, no readable numbers" + N,
    "engine_hangar": "Close-up of a large jet engine with its cowling open in a maintenance hangar, mechanic inspecting with a flashlight" + N,
    "grounded_hangar": "Several passenger jets parked inside a huge hangar with engines removed and covered intakes" + N,
    "legal_docs": "Stack of legal documents and a fountain pen on a dark desk under a lamp, serious mood, no readable text" + N,
    "card_terminal": "Close-up of a hand tapping a credit card on a payment terminal at an airport counter, shallow depth of field, no readable text" + N,
    "refinery_night": "Oil refinery at night with flare stacks burning, dramatic orange light" + N,
    "tanker_sea": "Oil tanker ship sailing through a narrow strait at sunset, hazy, tense atmosphere" + N,
    "fuel_truck": "Fuel truck refueling a passenger jet at night on the apron, glowing lights" + N,
    "capitol_dusk": "United States Capitol building at dusk with dramatic clouds" + N,
    "empty_counters": "Row of empty yellow airline check-in counters with lights turned off in an airport terminal, lonely atmosphere" + N,
    "boneyard": "Many passenger jets stored in a desert aircraft boneyard under harsh sun, engines covered, aerial view" + N,
    "last_takeoff": "Silhouette of a passenger jet taking off into a deep red sunset" + N,
    "family_travel": "Family with children and suitcases walking through a busy airport terminal toward the gates, seen from behind" + N,
    "metal_powder": "Macro shot of grey metallic powder and a jet engine turbine disk on a laboratory bench under bright light" + N,
    "ops_center": "Airline operations control center at night with many glowing screens and staff seen from behind, no readable text" + N,
    "goodbye_hug": "Two airline employees in uniform hugging goodbye in an empty dark airport terminal, seen from behind, emotional" + N,
    "crew_leaving": "Flight attendants walking away down an empty airport corridor pulling their suitcases, seen from behind, melancholic" + N,
}

BOARD = dict(type="board", title="SALIDAS · SÁBADO 2 DE MAYO DE 2026", rows=[
    ["06:05", "Fort Lauderdale → Cancún", "SPIRIT", "A TIEMPO"], ["06:40", "Detroit → Las Vegas", "SPIRIT", "A TIEMPO"],
    ["07:15", "Orlando → Bogotá", "SPIRIT", "EMBARCANDO"], ["07:50", "Newark → Fort Myers", "SPIRIT", "A TIEMPO"],
    ["08:20", "Houston → San Salvador", "SPIRIT", "A TIEMPO"], ["09:00", "Atlantic City → Miami", "SPIRIT", "A TIEMPO"]])

def I(key, cap=None, pop=None, **kw):
    d = dict(type="img", key=key)
    if cap: d["cap"] = cap
    if pop: d["pop"] = pop
    d.update(kw); return d

SCENES = [
    # --- GANCHO (en plena acción) ---
    dict(id="s01", text="Sábado, dos de mayo de dos mil veintiséis. Antes del amanecer, miles de pasajeros miran sus teléfonos en los aeropuertos de Estados Unidos. Y todos leen el mismo mensaje.",
         visual=I("terminal_night", cap="2 DE MAYO DE 2026")),
    dict(id="s02", text="Todos los vuelos de Spirit Airlines, cancelados. Los doscientos setenta y siete previstos para ese día… y todos los que vendrían después.",
         visual=BOARD),
    dict(id="s03", text="La aerolínea de los aviones amarillos y los billetes más baratos del país acababa de cerrar para siempre. Y con ella, unos diecisiete mil empleos, entre directos e indirectos.",
         visual=I("stranded", pop=["CERRADA", "17.000 EMPLEOS"])),
    dict(id="s04", text="Lo más increíble es que, solo dos años antes, otra aerolínea quiso comprarla por tres mil ochocientos millones de dólares. Y un juez lo impidió.",
         visual=I("courtroom", pop=["3.800 MILLONES"])),
    dict(id="s05", text="Lo hizo para proteger a los pasajeros que vuelan barato. Dos años después, esos pasajeros se quedaron sin Spirit.",
         visual=I("yellow_parked")),
    dict(id="s06", text="Entre medias hubo dos quiebras, motores que dejaron decenas de aviones en tierra y una guerra que disparó el precio del combustible.",
         visual=I("tarmac_sunset", shake=True)),
    dict(id="s07", text="Esta es la historia de la aerolínea que todos criticaban… y en la que todos volaban. Y de cómo se estrelló sin sufrir un solo accidente.",
         visual=I("yellow_flying")),

    # --- 01 ---
    dict(id="s08", text="Capítulo uno: un chárter de Detroit.",
         visual=dict(type="title", num="01", text="UN CHÁRTER DE DETROIT", name="Un chárter de Detroit")),
    dict(id="s09", text="La historia empieza en los años ochenta, cerca de Detroit. Un empresario llamado Ned Homfeld monta Charter One, una pequeña empresa que vende viajes organizados.",
         visual=I("charter_80s", cap="MICHIGAN · AÑOS 80")),
    dict(id="s10", text="Su negocio son los paquetes de casino: vuelo, hotel y fin de semana en sitios como Atlantic City o Las Vegas. Al principio, ni siquiera tiene aviones propios.",
         visual=I("casino_night")),
    dict(id="s11", text="En mil novecientos noventa y dos da el gran salto: incorpora sus propios jets, cambia su nombre a Spirit Airlines y empieza a vender vuelos regulares.",
         visual=dict(type="year", year="1992", sub="CHARTER ONE SE CONVIERTE EN SPIRIT AIRLINES")),
    dict(id="s12", text="Su primera ruta regular une Detroit con Atlantic City. Y poco a poco, Spirit va bajando hacia el sur.",
         visual=dict(type="route", title="LA PRIMERA RUTA REGULAR (1992)", points={"Detroit": [0.36, 0.30], "Atlantic City": [0.62, 0.52]},
                     routes=[["Detroit", "Atlantic City"]])),
    dict(id="s12b", text="Durante su primera década, Spirit vive de unir el norte frío de Estados Unidos con el sol: Detroit, Atlantic City, Florida… vuelos para escapar del invierno.",
         visual=I("vintage_jet", pop=["DEL FRÍO AL SOL"])),
    dict(id="s13", text="Con los años, traslada su sede a Florida. Y desde Fort Lauderdale empieza a volar al Caribe y a América Latina.",
         visual=dict(type="route", title="DE FLORIDA AL CARIBE Y AMÉRICA LATINA", points={"Fort Lauderdale": [0.50, 0.30], "Cancún": [0.33, 0.52],
                     "San José": [0.40, 0.80], "Bogotá": [0.62, 0.86], "Puerto Príncipe": [0.70, 0.50]},
                     routes=[["Fort Lauderdale", "Cancún"], ["Fort Lauderdale", "Puerto Príncipe"], ["Fort Lauderdale", "San José"], ["Fort Lauderdale", "Bogotá"]])),
    dict(id="s14", text="Pero durante años, Spirit es una aerolínea más. Barata, sí, pero del montón. Hasta que llega una idea copiada de Europa que lo cambia todo.",
         visual=I("vintage_jet")),

    # --- 02 ---
    dict(id="s15", text="Capítulo dos: barato… y todo lo demás se paga.",
         visual=dict(type="title", num="02", text="BARATO… Y TODO LO DEMÁS SE PAGA", name="Barato… y todo lo demás se paga")),
    dict(id="s16", text="En dos mil siete, bajo la dirección de Ben Baldanza, Spirit anuncia que se convierte en una aerolínea de ultra bajo coste. El modelo viene de la irlandesa Ryanair.",
         visual=I("cramped_seats", cap="2007 · ULTRA BAJO COSTE")),
    dict(id="s17", text="La idea es sencilla: un billete base bajísimo, y todo lo demás se cobra aparte. Elegir asiento, facturar una maleta, imprimir la tarjeta de embarque en el aeropuerto.",
         visual=dict(type="versus", title="EL MODELO SPIRIT", left=["BILLETE", "SÚPER BARATO"], right=["TODO LO DEMÁS", "SE PAGA APARTE"], mid="+", lcol="yellow", rcol="red")),
    dict(id="s17b", text="¿Y cómo se gana dinero así? Primero, metiendo en cada avión más asientos que nadie. Más asientos significa que el coste por pasajero baja.",
         visual=I("cramped_seats", pop=["MÁS ASIENTOS"])),
    dict(id="s17c", text="Segundo, haciendo que los aviones pasen el máximo tiempo posible en el aire: cuantas más horas vuela un avión cada día, más rentable es.",
         visual=I("yellow_flying", pop=["MÁS HORAS VOLANDO"])),
    dict(id="s17d", text="Y tercero, con todo lo que cobra aparte: asientos, maletas, embarque prioritario… Lo que el sector llama ingresos complementarios.",
         visual=dict(type="quote", text="ASIENTO\nMALETA\nPRIORIDAD\n= INGRESOS EXTRA")),
    dict(id="s18", text="Y en dos mil diez da un paso que nadie se había atrevido a dar: se convierte en la primera aerolínea de Estados Unidos en cobrar por el equipaje de mano que va en el compartimento de arriba.",
         visual=I("bag_sizer", pop=["EQUIPAJE DE MANO", "DE PAGO"])),
    dict(id="s19", text="Hasta cuarenta y cinco dólares, si lo pagabas en la puerta de embarque.",
         visual=dict(type="num", start=0, end=45, suffix=" $", label="POR UNA MALETA DE MANO PAGADA EN LA PUERTA (2010)")),
    dict(id="s19b", text="Su director general defendía que no era por dinero: decía que así se embarcaba más rápido, porque la gente subía menos maletas al avión. Al principio, ninguna gran aerolínea se atrevió a copiarlo.",
         visual=I("bag_sizer", pop=["¿NO ERA POR DINERO?"])),
    dict(id="s19c", text="Según se publicó entonces, esa sola tarifa podía aportarle a la aerolínea unos cincuenta millones de dólares.",
         visual=dict(type="num", start=0, end=50, suffix=" M$", label="LO QUE PODÍA APORTAR LA TARIFA DEL EQUIPAJE DE MANO")),
    dict(id="s20", text="La gente lo odiaba. Durante años, Spirit estuvo entre las aerolíneas con más quejas del país. Y los chistes sobre sus asientos que no se reclinan se volvieron casi un género propio.",
         visual=I("frustrated")),
    dict(id="s21", text="Pero había un detalle que lo cambiaba todo: los aviones iban llenos. Porque cuando buscabas el vuelo más barato, casi siempre aparecía Spirit.",
         visual=I("full_cabin", pop=["LLENOS"])),
    dict(id="s21b", text="Era la aerolínea de las familias que viajaban a ver a los suyos, de los estudiantes y de los que se iban de vacaciones con lo justo.",
         visual=I("family_travel")),
    dict(id="s22", text="Y con su amarillo chillón se convirtió en un símbolo: el avión de la gente que no podía pagar otra cosa.",
         visual=I("yellow_flying")),
    dict(id="s23", text="El modelo funcionó tan bien que, en dos mil veintidós, dos aerolíneas se pelearon por quedarse con ella.",
         visual=I("florida_airport")),

    # --- 03 ---
    dict(id="s24", text="Capítulo tres: la guerra por Spirit.",
         visual=dict(type="title", num="03", text="LA GUERRA POR SPIRIT", name="La guerra por Spirit")),
    dict(id="s25", text="En febrero de dos mil veintidós, Spirit acuerda fusionarse con Frontier, otra aerolínea de bajo coste. Juntas serían la gran potencia del vuelo barato en Estados Unidos.",
         visual=I("boardroom", cap="FEBRERO DE 2022")),
    dict(id="s26", text="Pero entonces aparece JetBlue, una aerolínea más grande y más cara, con una oferta mejor y en efectivo.",
         visual=I("two_planes", pop=["FRONTIER", "VS", "JETBLUE"])),
    dict(id="s27", text="JetBlue quiere crecer para plantar cara a las cuatro grandes: American, Delta, United y Southwest, que se reparten la mayor parte del mercado.",
         visual=dict(type="quote", text="AMERICAN\nDELTA\nUNITED\nSOUTHWEST")),
    dict(id="s28", text="Durante meses hay una guerra de ofertas. Frontier mejora su propuesta y añade una indemnización si el acuerdo fracasa. JetBlue sube la suya.",
         visual=dict(type="versus", title="LA GUERRA DE OFERTAS (2022)", left=["FRONTIER", "ACCIONES + EFECTIVO"], right=["JETBLUE", "TODO EN EFECTIVO"], mid="VS", lcol="white", rcol="yellow")),
    dict(id="s28b", text="Frontier llegó a ofrecer doscientos cincuenta millones de dólares de indemnización si la fusión no salía adelante.",
         visual=dict(type="num", start=0, end=250, suffix=" M$", label="LA INDEMNIZACIÓN QUE OFRECIÓ FRONTIER")),
    dict(id="s28c", text="JetBlue respondió prometiendo cientos de millones si los reguladores tumbaban la compra. Una apuesta muy arriesgada.",
         visual=I("boardroom", pop=["APUESTA"])),
    dict(id="s28d", text="Mientras las dos ofertas subían, la votación de los accionistas de Spirit se fue aplazando una y otra vez.",
         visual=I("boardroom", pop=["APLAZADA"])),
    dict(id="s29", text="Al final gana JetBlue: treinta y tres dólares con cincuenta por acción. En total, unos tres mil ochocientos millones de dólares.",
         visual=dict(type="num", start=0, end=3800, suffix=" M$", label="LO QUE JETBLUE IBA A PAGAR POR SPIRIT")),
    dict(id="s30", text="En julio de dos mil veintidós, Spirit rompe con Frontier y firma con JetBlue.",
         visual=dict(type="stamp", text="JULIO DE 2022\nSPIRIT ELIGE A JETBLUE", stamp="VENDIDA")),
    dict(id="s31", text="Parecía un final feliz. Pero el Departamento de Justicia de Estados Unidos no pensaba lo mismo.",
         visual=I("courthouse")),

    # --- 04 ---
    dict(id="s32", text="Capítulo cuatro: el juez.",
         visual=dict(type="title", num="04", text="EL JUEZ", name="El juez")),
    dict(id="s33", text="El Gobierno demandó para frenar la compra. Su argumento: si JetBlue se quedaba con Spirit, desaparecería el rival que obliga a todos los demás a bajar precios.",
         visual=I("courthouse", cap="DEPARTAMENTO DE JUSTICIA")),
    dict(id="s33b", text="La demanda se presentó en marzo de dos mil veintitrés, y el juicio se celebró en Boston a finales de ese mismo año.",
         visual=dict(type="year", year="2023", sub="EL GOBIERNO DEMANDA PARA FRENAR LA COMPRA")),
    dict(id="s34", text="JetBlue pensaba reconfigurar los aviones de Spirit con más espacio entre asientos. Es decir: menos asientos por avión y, según el Gobierno, billetes más caros.",
         visual=I("cramped_seats", pop=["MENOS ASIENTOS", "MÁS CAROS"])),
    dict(id="s35", text="El dieciséis de enero de dos mil veinticuatro, el juez William Young, en Boston, bloquea la operación en un fallo de ciento trece páginas.",
         visual=dict(type="headline", kicker="16 de enero de 2024", text="Un juez federal bloquea la compra de Spirit por JetBlue", mark="bloquea", source="Fuente: AP / Reuters")),
    dict(id="s36", text="Su razonamiento: los clientes que dependen de los precios bajísimos de Spirit saldrían perjudicados.",
         visual=dict(type="quote", text="«LOS CLIENTES DE SPIRIT\nSALDRÍAN\nPERJUDICADOS»")),
    dict(id="s36b", text="El juez reconoció incluso que una JetBlue más grande podría plantar cara a las grandes aerolíneas. Pero pesó más el daño a los clientes de Spirit.",
         visual=I("courtroom", pop=["PESÓ MÁS"])),
    dict(id="s36c", text="Y no era la primera derrota de JetBlue en los tribunales: unos meses antes, otro juez ya había tumbado su alianza con American Airlines en el noreste del país.",
         visual=dict(type="stamp", text="2023\nALIANZA JETBLUE–AMERICAN", stamp="TUMBADA")),
    dict(id="s37", text="Ese día, las acciones de Spirit se desploman cerca de un cuarenta y siete por ciento.",
         visual=dict(type="num", start=0, end=-47, suffix=" %", label="LAS ACCIONES DE SPIRIT, EL DÍA DEL FALLO")),
    dict(id="s37b", text="Las dos aerolíneas dijeron que no estaban de acuerdo con el fallo y que estudiaban recurrir. Pero el tiempo corría en su contra.",
         visual=I("legal_docs", pop=["¿RECURRIR?"])),
    dict(id="s38", text="Los inversores lo leen así: sin JetBlue, Spirit se queda sola… justo cuando más necesitaba a alguien.",
         visual=I("trading_red", shake=True)),
    dict(id="s39", text="Poco después, JetBlue abandona definitivamente el acuerdo. Y los problemas de Spirit empiezan a llegar todos a la vez.",
         visual=dict(type="stamp", text="MARZO DE 2024\nJETBLUE SE RETIRA", stamp="SOLA")),

    # --- 05 ---
    dict(id="s40", text="Capítulo cinco: aviones en tierra.",
         visual=dict(type="title", num="05", text="AVIONES EN TIERRA", name="Aviones en tierra")),
    dict(id="s41", text="El primero llega de donde menos lo esperaba: los motores. Muchos aviones nuevos de Spirit llevaban motores de Pratt and Whitney con un defecto de fabricación.",
         visual=I("engine_hangar", cap="MOTORES PRATT & WHITNEY")),
    dict(id="s41b", text="El problema estaba en un metal en polvo contaminado, usado para fabricar algunas piezas. RTX, la empresa dueña de Pratt and Whitney, reservó unos tres mil millones de dólares para afrontarlo.",
         visual=I("metal_powder", pop=["3.000 MILLONES"])),
    dict(id="s41c", text="No solo afectó a Spirit: aerolíneas de todo el mundo tuvieron que dejar aviones en tierra. Pero a una empresa tan endeudada le dolió muchísimo más.",
         visual=I("ops_center")),
    dict(id="s42", text="Hubo que revisarlos uno a uno, en un proceso larguísimo. Y Spirit llegó a tener unos cuarenta aviones parados, sin poder volar.",
         visual=I("grounded_hangar", pop=["≈40 AVIONES", "EN TIERRA"], pop_col="red")),
    dict(id="s43", text="Un avión parado no gana dinero, pero sigue costando: hay que pagarlo, guardarlo y mantener a sus tripulaciones.",
         visual=I("grounded_hangar")),
    dict(id="s44", text="El fabricante acabó compensando a la aerolínea. Pero el daño ya estaba hecho: menos vuelos, menos ingresos y una deuda que no paraba de crecer.",
         visual=I("legal_docs")),
    dict(id="s45", text="Desde dos mil veinte, Spirit había perdido más de dos mil quinientos millones de dólares.",
         visual=dict(type="num", start=0, end=-2500, suffix=" M$", label="PÉRDIDAS DE SPIRIT DESDE 2020")),
    dict(id="s46", text="Y además, su gran ventaja se estaba evaporando: las grandes aerolíneas habían copiado sus tarifas básicas, y muchos viajeros preferían pagar un poco más por viajar mejor.",
         visual=I("full_cabin")),
    dict(id="s47", text="Recapitulemos: Spirit había perdido su venta, tenía decenas de aviones en tierra y una montaña de deudas. El siguiente paso era casi inevitable.",
         visual=I("tarmac_sunset", pop=["SIN VENTA", "SIN AVIONES", "CON DEUDAS"])),

    # --- 06 ---
    dict(id="s48", text="Capítulo seis: dos quiebras en nueve meses.",
         visual=dict(type="title", num="06", text="DOS QUIEBRAS EN NUEVE MESES", name="Dos quiebras en nueve meses")),
    dict(id="s49", text="El dieciocho de noviembre de dos mil veinticuatro, Spirit se declara en quiebra. Es la primera gran aerolínea de Estados Unidos en hacerlo desde dos mil once.",
         visual=dict(type="year", year="18 NOV 2024", sub="SPIRIT SE DECLARA EN QUIEBRA")),
    dict(id="s49b", text="Este tipo de quiebra, el famoso capítulo once, no significa cerrar: permite seguir funcionando mientras se renegocian las deudas con los acreedores.",
         visual=dict(type="versus", title="¿QUÉ ES EL CAPÍTULO 11?", left=["SIGUE", "VOLANDO"], right=["RENEGOCIA", "SUS DEUDAS"], mid="+", lcol="yellow", rcol="white")),
    dict(id="s50", text="Pero promete seguir volando. Y mientras tanto, Frontier vuelve a la carga: intenta comprarla otra vez.",
         visual=I("two_planes")),
    dict(id="s51", text="Spirit rechaza sus ofertas. Prefiere salir de la quiebra por su cuenta, cambiando deuda por acciones.",
         visual=dict(type="stamp", text="FRONTIER\nLO VUELVE A INTENTAR", stamp="RECHAZADA")),
    dict(id="s52", text="En marzo de dos mil veinticinco sale del concurso. Y un mes después, su director general dimite.",
         visual=I("boardroom", cap="MARZO-ABRIL DE 2025")),
    dict(id="s52b", text="Y la Spirit que sale de la quiebra es más pequeña: vende aviones, recorta rutas y prescinde de parte de su plantilla.",
         visual=I("empty_counters", pop=["MÁS PEQUEÑA"])),
    dict(id="s53", text="En agosto, la propia empresa avisa a los reguladores de que hay dudas sustanciales sobre su capacidad de seguir operando.",
         visual=dict(type="headline", kicker="Agosto de 2025", text="Spirit advierte de «dudas sustanciales» sobre su futuro", mark="dudas sustanciales", source="Fuente: informe de Spirit ante la SEC", size=96)),
    dict(id="s54", text="Y su procesador de pagos con tarjeta empieza a retener hasta tres millones de dólares al día de sus ventas, como garantía.",
         visual=I("card_terminal", pop=["3 MILLONES", "AL DÍA"])),
    dict(id="s55", text="El veintinueve de agosto de dos mil veinticinco, Spirit vuelve a declararse en quiebra. Solo cinco meses después de haber salido de la primera.",
         visual=dict(type="year", year="29 AGO 2025", sub="SEGUNDA QUIEBRA EN MENOS DE UN AÑO")),
    dict(id="s55b", text="Para seguir volando durante esta segunda quiebra, consigue un préstamo de emergencia con unos cuatrocientos setenta y cinco millones de dólares de dinero nuevo.",
         visual=dict(type="num", start=0, end=475, suffix=" M$", label="DINERO NUEVO PARA SEGUIR VOLANDO (2025)")),
    dict(id="s56", text="Esta vez promete recortes agresivos: menos aviones, menos rutas y menos empleados. Encoger para sobrevivir.",
         visual=I("empty_counters")),
    dict(id="s57", text="Y durante unos meses, parece que podría funcionar. Hasta que, a miles de kilómetros, estalla una guerra.",
         visual=I("yellow_flying")),

    # --- 07 ---
    dict(id="s58", text="Capítulo siete: la guerra del combustible.",
         visual=dict(type="title", num="07", text="LA GUERRA DEL COMBUSTIBLE", name="La guerra del combustible")),
    dict(id="s59", text="A principios de dos mil veintiséis estalla la guerra con Irán, y el precio del petróleo se dispara.",
         visual=I("tanker_sea", cap="2026", shake=True)),
    dict(id="s60", text="Con él, el del combustible de avión. Desde febrero, en pocas semanas, prácticamente se duplica.",
         visual=dict(type="versus", title="COMBUSTIBLE DE AVIÓN EN 2026", left=["FEBRERO", "PRECIO NORMAL"], right=["x2", "SEMANAS DESPUÉS"], mid="→", lcol="white", rcol="red")),
    dict(id="s61", text="Para cualquier aerolínea es un golpe. Para una que vive de vender los billetes más baratos, con márgenes mínimos, es mortal.",
         visual=I("refinery_night")),
    dict(id="s61b", text="El combustible es, junto con los sueldos, uno de los mayores gastos de cualquier aerolínea. Cuando se duplica, no hay recorte que lo compense.",
         visual=I("fuel_truck", pop=["COMBUSTIBLE x2"], pop_col="red")),
    dict(id="s62", text="El plan de reestructuración que Spirit había presentado en marzo se queda sin sentido: con el combustible al doble, los números ya no cuadran.",
         visual=I("fuel_truck")),
    dict(id="s62b", text="Las grandes aerolíneas pueden subir sus tarifas para compensar. Spirit no: si sube los precios, deja de ser Spirit.",
         visual=I("full_cabin", pop=["SIN MARGEN"])),
    dict(id="s63", text="Spirit pide ayuda a Washington. Durante semanas negocia con el Gobierno un rescate de quinientos millones de dólares.",
         visual=I("capitol_dusk", cap="WASHINGTON")),
    dict(id="s63b", text="Durante días pareció que el acuerdo estaba cerca. Incluso se esperaba un anuncio desde la Casa Blanca.",
         visual=I("capitol_dusk", pop=["¿RESCATE?"])),
    dict(id="s64", text="A cambio, según una de las informaciones publicadas, el Gobierno se habría quedado con una parte de la compañía.",
         visual=dict(type="num", start=0, end=500, suffix=" M$", label="EL RESCATE QUE SE NEGOCIÓ CON EL GOBIERNO")),
    dict(id="s65", text="Pero el acuerdo necesitaba también el visto bueno de los bonistas, los acreedores que le habían prestado dinero. Y no hubo acuerdo.",
         visual=dict(type="stamp", text="RESCATE DE 500 M$\nSIN ACUERDO", stamp="FRACASA")),
    dict(id="s66", text="El viernes uno de mayo, por la noche, ya no hay marcha atrás.",
         visual=I("terminal_night", shake=True)),

    # --- 08 ---
    dict(id="s66b", text="Dos quiebras, un rescate que no llega y el combustible por las nubes. Esa noche, en la sede de Spirit en Florida, se toma la decisión.",
         visual=I("ops_center", shake=True)),
    dict(id="s67", text="Capítulo ocho: el último vuelo.",
         visual=dict(type="title", num="08", text="EL ÚLTIMO VUELO", name="El último vuelo")),
    dict(id="s68", text="Esa madrugada, Spirit cancela todos sus vuelos y anuncia el cierre ordenado de sus operaciones, con efecto inmediato.",
         visual=BOARD),
    dict(id="s69", text="Pide a los pasajeros que no vayan a los aeropuertos. Los que pagaron con tarjeta recibirán su dinero de vuelta. Los vales y los puntos, ya se verá en la quiebra.",
         visual=I("stranded")),
    dict(id="s70", text="En las terminales, los mostradores amarillos se apagan uno a uno. Los empleados se despiden entre ellos.",
         visual=I("crew_leaving")),
    dict(id="s70b", text="Según contó la cadena CNBC, en esas últimas horas los trabajadores se despedían con frases como «que te vaya bien, amigo».",
         visual=I("goodbye_hug")),
    dict(id="s71", text="Diecisiete mil empleos, entre directos e indirectos, según la propia empresa.",
         visual=dict(type="num", start=0, end=17000, suffix=" EMPLEOS", label="DIRECTOS E INDIRECTOS, SEGÚN SPIRIT")),
    dict(id="s72", text="Sus aviones, unos ciento treinta según los últimos datos, se quedan en tierra para ser vendidos.",
         visual=I("boneyard", pop=["≈130 AVIONES", "A LA VENTA"])),
    dict(id="s72b", text="La quiebra pasa a ser una liquidación ordenada, bajo la supervisión del tribunal: vender los aviones y todo lo que queda para pagar a los acreedores.",
         visual=dict(type="stamp", text="MAYO DE 2026\nLIQUIDACIÓN ORDENADA", stamp="FIN")),
    dict(id="s73", text="Treinta y cuatro años después de su primer vuelo regular, Spirit Airlines deja de existir.",
         visual=dict(type="year", year="1992 – 2026", sub="SPIRIT AIRLINES")),

    # --- 09 ---
    dict(id="s73b", text="Era el final de una aerolínea que, durante años, fue sinónimo de volar barato en Estados Unidos. Para bien… y para mal.",
         visual=I("yellow_parked")),
    dict(id="s74", text="Capítulo nueve: ¿quién mató a Spirit?",
         visual=dict(type="title", num="09", text="¿QUIÉN MATÓ A SPIRIT?", name="¿Quién mató a Spirit?")),
    dict(id="s75", text="Algunos culpan al juez que impidió la venta a JetBlue. Otros, a los motores defectuosos, a las deudas acumuladas o a la guerra que disparó el combustible.",
         visual=dict(type="quote", text="¿EL JUEZ?\n¿LOS MOTORES?\n¿LAS DEUDAS?\n¿EL COMBUSTIBLE?")),
    dict(id="s76", text="La respuesta más honesta es que fueron todos a la vez. Spirit llegó a dos mil veintiséis sin colchón, y cada golpe la encontró más débil que el anterior.",
         visual=I("legal_docs")),
    dict(id="s77", text="En un negocio de márgenes mínimos, lo que decide cuánto aguantas cuando llega la tormenta no es lo barato que vendes. Es cuánto debes.",
         visual=I("refinery_night")),
    dict(id="s77b", text="Si hay que sacar tres lecciones, serían estas: la deuda decide cuánto aguantas; cada rescate fallido te deja más débil; y la suerte también juega, porque nadie podía prever una guerra.",
         visual=dict(type="quote", text="1. LA DEUDA\n2. EL TIEMPO\n3. LA SUERTE")),
    dict(id="s78", text="Pero hay una ironía difícil de ignorar. El juez bloqueó la fusión para proteger a los pasajeros que dependían de los vuelos más baratos.",
         visual=I("courtroom")),
    dict(id="s79", text="Dos años después, esos pasajeros no tienen ni Spirit, ni una Spirit dentro de JetBlue. Tienen una opción barata menos.",
         visual=I("last_takeoff")),
    dict(id="s79b", text="Y nos deja una pregunta incómoda: ¿se protege a los clientes impidiendo que una empresa en apuros sea comprada?",
         visual=I("courtroom", pop=["¿PROTEGER?"])),
    dict(id="s80", text="Y el modelo que Spirit popularizó en Estados Unidos, el de pagar por todo, sigue muy vivo: hoy lo usan muchas de las aerolíneas que tanto lo criticaban.",
         visual=I("bag_sizer")),
    dict(id="s81", text="¿Volaste alguna vez en Spirit, o en otra aerolínea de bajo coste? Cuéntame en los comentarios tu peor… o tu mejor experiencia.",
         visual=I("cramped_seats")),
    dict(id="s82", text="Y si te gustan estas historias, suscríbete: cada semana, el último balance de una empresa. Gracias por llegar hasta el final. Nos vemos en el próximo balance.",
         visual=I("last_takeoff")),
]

SHORTS = {}

THUMBS = [
    dict(img="tarmac_sunset", zoom=1.05, cx=0.6, shade=["left", 225, 0.6], items=[
        ["text", 45, 60, "CERRÓ", 200, "white", "la"], ["text", 45, 300, "DE UN DÍA", 120, "yellow", "la"], ["text", 45, 450, "PARA OTRO", 120, "yellow", "la"]]),
    dict(img="courtroom", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "UN JUEZ", 170, "white", "la"], ["text", 45, 280, "LO PROHIBIÓ", 130, "red", "la"], ["badge", 45, 520, 560, 640, "3.800 M$", 90]]),
    dict(img="terminal_night", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "277", 230, "yellow", "la"], ["text", 45, 330, "VUELOS", 130, "white", "la"], ["stamp", "CANCELADOS", 880, 560, -10, 100]]),
    dict(img="yellow_parked", zoom=1.0, cx=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "LA AEROLÍNEA", 120, "white", "la"], ["text", 45, 220, "QUE TODOS", 120, "white", "la"], ["text", 45, 380, "ODIABAN", 170, "red", "la"]]),
    dict(img="stranded", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "17.000", 200, "yellow", "la"], ["text", 45, 310, "EMPLEOS", 130, "white", "la"], ["text", 45, 460, "EN UNA NOCHE", 100, "white", "la"]]),
    dict(img="yellow_flying", zoom=1.1, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "SPIRIT", 200, "yellow", "la"], ["stamp", "QUIEBRA", 420, 470, -10, 130]]),
    dict(img="boneyard", zoom=1.05, cx=0.5, shade=["left", 220, 0.62], items=[
        ["text", 45, 60, "130 AVIONES", 140, "white", "la"], ["text", 45, 250, "A LA VENTA", 140, "yellow", "la"]]),
    dict(img="bag_sizer", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "TE COBRABA", 140, "white", "la"], ["text", 45, 250, "HASTA LA", 120, "white", "la"], ["text", 45, 400, "MALETA", 170, "yellow", "la"]]),
    dict(img="refinery_night", zoom=1.0, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "LA GUERRA", 150, "white", "la"], ["text", 45, 260, "QUE LA", 130, "white", "la"], ["text", 45, 420, "HUNDIÓ", 170, "red", "la"]]),
    dict(img="last_takeoff", zoom=1.0, cx=0.5, shade=["left", 200, 0.6], items=[
        ["text", 45, 60, "EL ÚLTIMO", 150, "white", "la"], ["text", 45, 260, "VUELO", 200, "yellow", "la"]]),
]
THUMBS_TOP = [2, 3, 1]

META = {
    "code": "007",
    "name": "Spirit Airlines",
    "intro_chapter": "Intro: el 2 de mayo de 2026",
    "titles": [
        "Un juez le prohibió venderse… y 2 años después cerró de un día para otro",
        "Spirit Airlines: la aerolínea que todos odiaban (y en la que todos volaban)",
        "Cómo se estrelló Spirit Airlines sin sufrir un solo accidente",
    ],
    "description": "El 2 de mayo de 2026, Spirit Airlines canceló todos sus vuelos y cerró para siempre: 277 vuelos ese día y unos 17.000 empleos. Solo dos años antes, JetBlue había querido comprarla por 3.800 millones de dólares, pero un juez federal bloqueó la operación para proteger a los pasajeros de vuelos baratos. Entre medias: el modelo de cobrar por todo (fue la primera aerolínea de EE. UU. en cobrar el equipaje de mano), los motores de Pratt & Whitney que dejaron decenas de aviones en tierra, dos quiebras en nueve meses, la guerra que duplicó el precio del combustible y un rescate de 500 millones que nunca llegó.",
    "sources": [
        "Wikipedia / AeroXplorer: historia de Charter One y Spirit Airlines (1983–1992), modelo de ultra bajo coste (2007)",
        "ABC News / AP / Star Tribune (2010): Spirit, primera aerolínea de EE. UU. en cobrar el equipaje de mano",
        "ch-aviation / Boston Globe (2022): Frontier, JetBlue y la oferta de 33,50 dólares por acción",
        "AP / WBUR / KSL (16-ene-2024): el juez William Young bloquea la compra de Spirit por JetBlue",
        "AirlineGeeks / FlightGlobal: motores GTF de Pratt & Whitney y aviones de Spirit en tierra",
        "Financier Worldwide / AltexSoft / Good Morning America (2024–2025): las dos quiebras de Spirit",
        "NBC News / CNBC / ABC News / Travel Market Report (mayo de 2026): combustible, rescate federal y cierre de Spirit",
    ],
    "disclosure": "Las imágenes de este vídeo son ilustraciones generadas con IA y no muestran a personas, aviones ni lugares reales. El tablero de salidas es una recreación: ese día se cancelaron todos los vuelos de Spirit. La narración está hecha con voz sintética.",
    "hashtags": "#SpiritAirlines #Aerolíneas #Quiebra #Negocios",
    "tags": ["spirit airlines", "spirit airlines quiebra", "spirit airlines cierra", "jetblue", "frontier", "aerolíneas low cost",
             "aerolínea de bajo coste", "quiebra", "historia de empresas", "aviación", "negocios", "el último balance"],
    "pinned": "¿Volaste alguna vez en Spirit? ✈️ Cuéntame tu peor (o mejor) experiencia 👇 Y dime qué empresa quieres para el próximo vídeo.",
    "playlist": "Quiebras y caídas",
    "shorts": {},
}
