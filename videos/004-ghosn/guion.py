# Vídeo 004 — Carlos Ghosn y Nissan: salvó a Nissan… y escapó de Japón en una caja
# Fórmula ganadora (datos del canal, 3-nov): personaje + cifra enorme + conflicto. Gancho nuevo: arranque "en plena acción"
# (la huida) y giro final adelantado (hoy salva a Nissan un mexicano).
VOICE = "i4Kar2uamCWyas8TAu31"  # ElevenLabs "Adán - Narration" (latinoamericano)
SPEED = 1.0
IMAGE_MODEL = "z_image"  # Higgsfield (DubVoice sin imágenes desde el 1-nov)
# Hechos verificados (2026-11-03): InsideHook/Gulf News/Kyodo/NTV (huida 29-dic-2019: tren bala, hotel de Kansai, caja de audio
# con agujeros, Estambul → Beirut; fianza ~14 M$), NPR/Al Jazeera/UPI (condena de Michael y Peter Taylor, 19-jul-2021),
# NHK/Bloomberg/Newshub (arresto en Haneda 19-nov-2018; acusación ~10.000 M¥ en 5 años, mitad no declarada; 108 días),
# NBC (grupo de la ONU: detención arbitraria, 2020), Darden/Autotrade/Alliance (Renault 36,8 % por ~5.400 M$, 1999),
# IndustryWeek/ChiefExecutive (21.000 empleos, 14 %; beneficio de 2.700 M$ en el año fiscal 2000), Encyclopedia.com (manga 2002),
# Fortune/Autonews/MexicoBusiness/Drive (pérdidas de 671.000 y 533.000 M¥, Re:Nissan 20.000 empleos y 17 → 10 fábricas,
# CIVAC → Aguascalientes, previsión de ~20.000 M¥ de beneficio), Bloomberg Línea/exchange4media (Espinosa CEO desde 1-abr-2025,
# en Nissan México desde 2003), Nissan Mexicana/UnoTV (17 años líder en México), Bloomberg (demanda de 1.000 M$, 2023).

IMAGES = {
    "caja_avion": "A large black flight case for concert audio equipment with small drilled air holes, sitting in the cargo area of a private jet at night, dramatic low light, cinematic, no people, no logos, no readable text",
    "jet_noche": "A private business jet on a dark airport tarmac at night, light fog, runway lights, a few silhouettes loading a large black case, cinematic, no logos, no readable text",
    "fabrica_vacia": "An empty modern car factory assembly line with idle robots and half-built car bodies, most lights off, cold and abandoned mood, cinematic, no logos, no readable text",
    "tire_factory": "Rows of new black car tires stacked high in a tire factory warehouse, industrial light, 1980s documentary photo style, no logos, no readable text",
    "fabrica_90s": "A Japanese car factory in the late 1990s, workers in white uniforms and caps on an assembly line with compact sedans, documentary photo, film grain, no logos, no readable text",
    "manga": "A stack of colorful Japanese manga comic books on a wooden table in a Tokyo bookstore, shallow depth of field, covers without readable text, no logos",
    "tokyo_hq": "A modern glass corporate headquarters tower in Yokohama, Japan at dusk, city lights, cinematic wide shot, no logos, no readable text",
    "haneda": "A private jet parked at a Tokyo airport at night, surrounded by dark sedans and men in dark suits, flashing lights reflecting on the wet tarmac, tense mood, cinematic, no logos, no readable text",
    "carcel": "A narrow corridor in a Japanese detention center with closed grey doors and cold fluorescent light, empty, oppressive mood, cinematic, no people, no readable text",
    "casa_tokyo": "A quiet upscale residential street in Tokyo at night with a security camera mounted above a house gate, cinematic, no people, no logos, no readable text",
    "shinkansen": "A Japanese bullet train speeding through a station at night, motion blur, platform lights, cinematic, no logos, no readable text",
    "beirut": "Beirut city skyline at dusk seen from the hills, Mediterranean sea in the background, warm light, cinematic, no logos, no readable text",
    "mexico_planta": "A car assembly plant in Mexico with workers in safety vests next to a line of compact cars, bright daylight through high windows, wide shot, cinematic, no logos, no readable text",
}
THUMB_IMAGES = {
    "thumb_caja": "A large black road case with drilled air holes standing alone on a dark airport tarmac at night under a single spotlight, a private jet with open door behind it, dramatic, cinematic, no people, no logos, no text",
    "thumb_split": "A dramatic split image: left side a bright Japanese car factory celebration with confetti and new cars, right side a dark empty airport hangar at night with a single black case, cinematic, no people, no logos, no text",
}

SCENES = [
    # --- GANCHO (en plena acción + giro adelantado) ---
    dict(id="s01", text="Este hombre escapó de Japón escondido dentro de una caja de equipos de música.",
         visual=dict(type="img", key="caja_avion", cap="29 DIC 2019")),
    dict(id="s02", text="La caja tenía agujeros para que pudiera respirar. Dos hombres la subieron a un avión privado en Osaka.",
         visual=dict(type="img", key="jet_noche", cap="UN AVIÓN PRIVADO RUMBO A ESTAMBUL")),
    dict(id="s03", text="Veinte años antes, ese mismo hombre había salvado a Nissan de la quiebra. Japón lo trató como a un héroe. Hasta le dedicaron un cómic.",
         visual=dict(type="versus", left=["1999", "SALVA A NISSAN\nDE LA QUIEBRA"], right=["2019", "HUYE DE JAPÓN\nEN UNA CAJA"])),
    dict(id="s04", text="Se llama Carlos Ghosn. Y esta es la historia de cómo pasó de ser uno de los ejecutivos más admirados del automóvil… a fugitivo internacional.",
         visual=dict(type="quote", text="CARLOS GHOSN:\nDE HÉROE\nA FUGITIVO")),
    dict(id="s05", text="Y el giro final: hoy Nissan vuelve a perder miles de millones. Y la persona que intenta rescatarla… es un mexicano.",
         visual=dict(type="img", key="fabrica_vacia", cap="NISSAN, 2026")),

    # --- CAPÍTULO 1 ---
    dict(id="s06", text="Capítulo uno. El asesino de costes.",
         visual=dict(type="title", num="01", text="EL ASESINO DE COSTES", name="El asesino de costes")),
    dict(id="s07", text="Carlos Ghosn nace en mil novecientos cincuenta y cuatro en Brasil, en una familia de origen libanés. De niño se muda a Beirut, y después estudia ingeniería en París, en algunas de las escuelas más exigentes de Francia.",
         visual=dict(type="year", year="1954", sub="NACE EN BRASIL, CRECE EN LÍBANO")),
    dict(id="s08", text="Empieza en Michelin, el fabricante de neumáticos, y sube rapidísimo: con treinta y pocos años ya dirige sus operaciones en Sudamérica.",
         visual=dict(type="img", key="tire_factory", cap="MICHELIN")),
    dict(id="s09", text="En mil novecientos noventa y seis lo ficha Renault. Allí recorta tanto gasto que la prensa francesa le pone un apodo: le cost killer. El asesino de costes.",
         visual=dict(type="quote", text="\"LE COST KILLER\"\nEL ASESINO\nDE COSTES")),
    dict(id="s10", text="Pero su gran prueba estaba a casi diez mil kilómetros de París. En Japón.",
         visual=dict(type="img", key="tokyo_hq", cap="YOKOHAMA, JAPÓN")),

    # --- CAPÍTULO 2 ---
    dict(id="s11", text="Capítulo dos. Salvar lo imposible.",
         visual=dict(type="title", num="02", text="SALVAR LO IMPOSIBLE", name="Salvar lo imposible")),
    dict(id="s12", text="En mil novecientos noventa y nueve, Nissan está al borde de la quiebra, con una deuda de más de veinte mil millones de dólares. Daimler Chrysler, que estudiaba comprarla, se retira.",
         visual=dict(type="year", year="1999", sub="NISSAN, AL BORDE DE LA QUIEBRA")),
    dict(id="s13", text="Entonces Renault se arriesga: paga unos cinco mil cuatrocientos millones de dólares por el treinta y seis coma ocho por ciento de Nissan. Y manda a Ghosn a Tokio.",
         visual=dict(type="num", start=0, end=5400, suffix=" M$", label="LO QUE PAGA RENAULT POR EL 36,8 % DE NISSAN")),
    dict(id="s14", text="Su plan es brutal: cerrar fábricas en Japón y eliminar veintiún mil puestos de trabajo, el catorce por ciento de la plantilla.",
         visual=dict(type="img", key="fabrica_90s", cap="21.000 EMPLEOS MENOS")),
    dict(id="s14b", text="También rompe una tradición casi sagrada en Japón: vende las participaciones que Nissan tenía en muchos de sus proveedores, el famoso keiretsu, y obliga a todos a bajar precios.",
         visual=dict(type="stamp", text="ADIÓS AL KEIRETSU\nPROVEEDORES SIN PRIVILEGIOS", stamp="TABÚ ROTO")),
    dict(id="s15", text="Y hace una promesa pública: si Nissan no vuelve a ganar dinero en el plazo previsto, él y todo su equipo directivo dimitirán.",
         visual=dict(type="quote", text="\"SI NO LO\nCONSEGUIMOS,\nDIMITIMOS\"")),
    dict(id="s16", text="Lo consigue. En el año fiscal dos mil, Nissan gana unos dos mil setecientos millones de dólares. Uno de los rescates más rápidos de la historia del automóvil.",
         visual=dict(type="versus", left=["1999", "PÉRDIDAS Y\nDEUDA GIGANTE"], right=["+2.700 M$", "BENEFICIO EN EL\nAÑO FISCAL 2000"], lcol="red", rcol="yellow")),
    dict(id="s17", text="Japón se rinde ante él. En dos mil dos se publica un manga sobre su vida, donde aparece como el superhéroe que salvó a Nissan.",
         visual=dict(type="img", key="manga", cap="2002 · SU VIDA, EN MANGA")),
    dict(id="s18", text="Y su poder no deja de crecer. En dos mil cinco se convierte también en jefe de Renault. Dirige dos gigantes del automóvil al mismo tiempo.",
         visual=dict(type="quote", text="JEFE DE NISSAN\nY DE RENAULT\nA LA VEZ")),
    dict(id="s19", text="En dos mil dieciséis, Nissan toma el control de Mitsubishi Motors. Y en dos mil diecisiete, la alianza que preside Ghosn presume de ser el mayor grupo de coches del mundo por ventas.",
         visual=dict(type="img", key="tokyo_hq", motion="out", cap="RENAULT · NISSAN · MITSUBISHI")),

    # --- CAPÍTULO 3 ---
    dict(id="s20", text="Capítulo tres. La caída.",
         visual=dict(type="title", num="03", text="LA CAÍDA", name="La caída")),
    dict(id="s21", text="Diecinueve de noviembre de dos mil dieciocho. El avión privado de Ghosn aterriza en el aeropuerto de Haneda, en Tokio. Los fiscales lo están esperando. Lo arrestan allí mismo.",
         visual=dict(type="stamp", text="19 DE NOVIEMBRE DE 2018\nAEROPUERTO DE HANEDA, TOKIO", stamp="ARRESTADO")),
    dict(id="s22", text="La acusación: según la fiscalía, en cinco años cobró unos diez mil millones de yenes, unos ochenta y ocho millones de dólares, pero solo declaró la mitad.",
         visual=dict(type="img", key="haneda", cap="LA FISCALÍA DE TOKIO")),
    dict(id="s23", text="Después llegan más cargos, como haber pasado a Nissan pérdidas de sus inversiones personales. Ghosn lo niega todo, y dice que es un complot para frenar una fusión más estrecha entre Nissan y Renault.",
         visual=dict(type="quote", text="GHOSN:\n\"ES UN COMPLOT\"")),
    dict(id="s24", text="Pasa ciento ocho días en una celda. En Japón los interrogatorios se hacen sin abogado presente, y la fiscalía añade cargos nuevos que alargan su detención.",
         visual=dict(type="num", start=0, end=108, suffix=" DÍAS", label="EN PRISIÓN TRAS SU ARRESTO")),
    dict(id="s25", text="Más tarde, un grupo de trabajo de la ONU calificará esa detención de arbitraria.",
         visual=dict(type="img", key="carcel", cap="ONU: DETENCIÓN \"ARBITRARIA\"")),
    dict(id="s26", text="En dos mil diecinueve sale bajo fianza, unos catorce millones de dólares, pero con condiciones estrictas: una cámara en la puerta de su casa, internet muy limitado, y sin poder hablar con su esposa sin permiso del tribunal. Lo que hizo después, nadie en Japón lo vio venir.",
         visual=dict(type="img", key="casa_tokyo", cap="LIBERTAD BAJO FIANZA")),

    # --- CAPÍTULO 4 ---
    dict(id="s27", text="Capítulo cuatro. La caja.",
         visual=dict(type="title", num="04", text="LA CAJA", name="La caja")),
    dict(id="s28", text="Veintinueve de diciembre de dos mil diecinueve. Ghosn sale caminando de su casa en Tokio, con gorra y mascarilla. Nadie lo detiene.",
         visual=dict(type="year", year="29 DIC 2019", sub="LA HUIDA")),
    dict(id="s29", text="Se sube a un tren bala hacia Osaka, a unos quinientos kilómetros. Allí lo esperan dos hombres, en un hotel junto al aeropuerto de Kansai.",
         visual=dict(type="img", key="shinkansen", cap="TOKIO → OSAKA EN TREN BALA")),
    dict(id="s29b", text="Según The Wall Street Journal, en la huida participaron entre diez y quince personas, y prepararla llevó meses y más de veinte viajes a Japón.",
         visual=dict(type="num", start=0, end=20, prefix="+", suffix=" VIAJES", label="A JAPÓN PARA PREPARAR LA HUIDA (WSJ)")),
    dict(id="s30", text="En la habitación, Ghosn se mete en una enorme caja negra, de las que se usan para transportar equipos de música. Le han hecho agujeros para que pueda respirar.",
         visual=dict(type="img", key="caja_avion", motion="out", cap="AGUJEROS PARA RESPIRAR")),
    dict(id="s31", text="Las cámaras del hotel solo grabaron a dos hombres saliendo con dos cajas enormes. Las suben a un avión privado rumbo a Estambul. En Turquía, la pasan a otro avión. Destino: Beirut.",
         visual=dict(type="img", key="jet_noche", motion="out", cap="OSAKA → ESTAMBUL → BEIRUT")),
    dict(id="s32", text="Cuando Japón se entera, ya es tarde. Ghosn está en Líbano, el país de su familia, que no tiene tratado de extradición con Japón.",
         visual=dict(type="img", key="beirut", cap="SIN TRATADO DE EXTRADICIÓN")),
    dict(id="s33", text="Su primer mensaje fue este: no he huido de la justicia. He escapado de la injusticia y de la persecución política.",
         visual=dict(type="quote", text="\"NO HE HUIDO\nDE LA JUSTICIA.\nHE ESCAPADO DE\nLA INJUSTICIA\"")),
    dict(id="s33b", text="Días después da una rueda de prensa en Beirut ante cientos de periodistas de todo el mundo, y durante más de dos horas acusa a Nissan y a la fiscalía japonesa de haber conspirado contra él.",
         visual=dict(type="img", key="beirut", motion="out", cap="RUEDA DE PRENSA EN BEIRUT")),
    dict(id="s34", text="Los que lo ayudaron no tuvieron tanta suerte. El exboina verde estadounidense Michael Taylor y su hijo Peter fueron condenados en Japón a dos años y a veinte meses de cárcel.",
         visual=dict(type="quote", text="MICHAEL TAYLOR: 2 AÑOS\nPETER TAYLOR: 20 MESES\nDE CÁRCEL EN JAPÓN")),
    dict(id="s34b", text="En Turquía, dos pilotos y un empleado de la compañía de vuelos privados también fueron condenados. Un trabajador admitió haber falsificado la lista de pasajeros para que Ghosn no apareciera.",
         visual=dict(type="stamp", text="TURQUÍA: LISTA DE PASAJEROS\nFALSIFICADA", stamp="CONDENADOS")),
    dict(id="s35", text="Ghosn pierde su fianza y queda atrapado en Líbano, buscado por Interpol. Si sale del país, puede ser detenido. Su huida es tan increíble que ya tiene dos documentales: uno en Netflix y otro en Apple TV.",
         visual=dict(type="stamp", text="NOTIFICACIÓN ROJA\nDE INTERPOL", stamp="BUSCADO")),

    # --- CAPÍTULO 5 ---
    dict(id="s36", text="Capítulo cinco. Nissan sin Ghosn.",
         visual=dict(type="title", num="05", text="NISSAN SIN GHOSN", name="Nissan sin Ghosn")),
    dict(id="s37", text="¿Y Nissan? Desde la salida de Ghosn, la empresa va de crisis en crisis.",
         visual=dict(type="img", key="fabrica_vacia", motion="out", cap="DE CRISIS EN CRISIS")),
    dict(id="s38", text="En febrero de dos mil veinticinco se rompen las negociaciones para fusionarse con Honda, que iban a crear el tercer mayor grupo de coches del mundo por ventas.",
         visual=dict(type="stamp", text="FEBRERO DE 2025\nFUSIÓN NISSAN + HONDA", stamp="CANCELADA")),
    dict(id="s39", text="Y llegan las pérdidas: seiscientos setenta y un mil millones de yenes en el año fiscal dos mil veinticuatro. Y quinientos treinta y tres mil millones en el siguiente.",
         visual=dict(type="bars", title="PÉRDIDAS NETAS DE NISSAN (MILES DE MILLONES DE YENES)", data=[["AÑO FISCAL 2024", 671], ["AÑO FISCAL 2025", 533]], reveal=2)),
    dict(id="s39b", text="Sus ingresos también bajan: unos doce billones de yenes en su último año fiscal, un cinco por ciento menos que el anterior.",
         visual=dict(type="num", start=0, end=-5, suffix=" %", label="INGRESOS DE NISSAN · AÑO FISCAL 2025")),
    dict(id="s40", text="Nissan anuncia un recorte enorme: veinte mil empleos menos, y pasar de diecisiete fábricas a diez en todo el mundo.",
         visual=dict(type="num", start=17, end=10, suffix=" FÁBRICAS", label="PLAN RE:NISSAN · 20.000 EMPLEOS MENOS")),
    dict(id="s41", text="Una de las fábricas que cierra está en México: la planta CIVAC, en Morelos, una de las más antiguas de Nissan fuera de Japón. Su producción se muda a Aguascalientes.",
         visual=dict(type="img", key="mexico_planta", cap="CIVAC, MORELOS → AGUASCALIENTES")),
    dict(id="s42", text="Y lo curioso es que en México Nissan sigue siendo la marca que más coches vende. Lleva diecisiete años seguidos en el primer puesto.",
         visual=dict(type="quote", text="NISSAN EN MÉXICO:\nNº1 EN VENTAS\n17 AÑOS SEGUIDOS")),
    dict(id="s43", text="Por eso hay un dato que pocos conocen: desde abril de dos mil veinticinco, el jefe mundial de Nissan es un mexicano, Iván Espinosa. Entró en Nissan México en dos mil tres, como especialista de producto.",
         visual=dict(type="versus", left=["2003", "ESPECIALISTA DE\nPRODUCTO EN MÉXICO"], right=["2025", "CEO MUNDIAL\nDE NISSAN"])),
    dict(id="s44", text="Su plan promete que Nissan volverá a ganar dinero en el año fiscal dos mil veintiséis. Poco: unos veinte mil millones de yenes. Pero después de dos años de pérdidas gigantes, sería un respiro.",
         visual=dict(type="img", key="mexico_planta", motion="out", cap="OBJETIVO: VOLVER A GANAR DINERO")),

    # --- CAPÍTULO 6 / CIERRE ---
    dict(id="s45", text="Capítulo seis. ¿Héroe o fugitivo?",
         visual=dict(type="title", num="06", text="¿HÉROE O FUGITIVO?", name="¿Héroe o fugitivo?")),
    dict(id="s46", text="¿Y Ghosn? Hasta donde se sabe, sigue en Líbano. En dos mil veintitrés demandó a Nissan por mil millones de dólares, y sigue diciendo que es inocente. La justicia japonesa nunca llegó a juzgarlo.",
         visual=dict(type="img", key="beirut", motion="out", cap="BEIRUT")),
    dict(id="s47", text="Así que la pregunta es esta: ¿fue el genio que salvó a Nissan cuando nadie más podía? ¿O el jefe que llegó a creerse por encima de las reglas?",
         visual=dict(type="versus", left=["1999", "EL HOMBRE QUE\nSALVÓ A NISSAN"], right=["2019", "EL HOMBRE QUE\nHUYÓ EN UNA CAJA"], lcol="yellow", rcol="red")),
    dict(id="s48", text="Te leo en los comentarios. Y si te gustan estas historias, suscríbete: la próxima ya está en camino.",
         visual=dict(type="quote", text="¿HÉROE\nO FUGITIVO?")),
]

# Shorts: 3 ganchos distintos con la fórmula ganadora (conflicto · de héroe a caída · giro mexicano)
SHORTS = {
    "a": {"bar": "ESCAPÓ EN UNA CAJA", "scenes": [
        dict(id="a01", text="Este hombre escapó de Japón escondido en una caja de equipos de música.", key="caja_avion"),
        dict(id="a02", text="Estaba en libertad bajo fianza, vigilado por cámaras, y acusado de ocultar la mitad de su sueldo. Él lo niega.", key="casa_tokyo"),
        dict(id="a03", text="Tomó un tren bala hasta Osaka, se metió en la caja, y un avión privado lo sacó del país.", key="shinkansen"),
        dict(id="a04", text="Era Carlos Ghosn, el hombre que había salvado a Nissan. La historia completa, en mi canal.", key="jet_noche"),
    ]},
    "b": {"bar": "DE HÉROE A FUGITIVO", "scenes": [
        dict(id="b01", text="En mil novecientos noventa y nueve, Nissan estaba al borde de la quiebra.", key="fabrica_90s"),
        dict(id="b02", text="Llegó un ejecutivo criado en Líbano, recortó veintiún mil empleos, y en un año la empresa volvió a ganar dinero.", key="tokyo_hq"),
        dict(id="b03", text="Japón lo convirtió en héroe de manga.", key="manga"),
        dict(id="b04", text="Diecinueve años después, lo arrestaron al bajar de su avión. La historia completa, en mi canal.", key="haneda"),
    ]},
    "c": {"bar": "UN MEXICANO AL RESCATE", "scenes": [
        dict(id="c01", text="Nissan es la marca que más coches vende en México desde hace diecisiete años.", key="mexico_planta"),
        dict(id="c02", text="Pero en el mundo pierde miles de millones. Va a quedarse con diez fábricas de diecisiete, y una de las que cierra está en Morelos.", key="fabrica_vacia"),
        dict(id="c03", text="¿Y quién intenta salvarla? Un mexicano, Iván Espinosa, que entró en Nissan México en dos mil tres.", key="tokyo_hq"),
        dict(id="c04", text="La historia completa de Nissan, en mi canal.", key="mexico_planta"),
    ]},
}

THUMBS = [
    dict(img="thumb_caja", zoom=1.05, cx=0.5, items=[
        ["text", 50, 60, "ESCAPÓ", 200, "white", "la"], ["text", 50, 290, "EN UNA", 150, "white", "la"], ["text", 50, 460, "CAJA", 200, "red", "la"]]),
    dict(img="thumb_split", zoom=1.05, cx=0.5, items=[
        ["text", 320, 40, "HÉROE", 170, "yellow", "mt"], ["text", 960, 40, "FUGITIVO", 150, "red", "mt"], ["text", 640, 520, "NISSAN", 120, "white", "mt"]]),
    dict(img="thumb_caja", zoom=1.1, cx=0.6, shade=["left", 230, 0.6], items=[
        ["text", 50, 70, "SALVÓ NISSAN", 130, "white", "la"], ["text", 50, 240, "Y HUYÓ", 170, "yellow", "la"], ["text", 50, 450, "EN UNA CAJA", 130, "red", "la"]]),
    dict(img="jet_noche", zoom=1.05, cx=0.5, shade=["left", 220, 0.6], items=[
        ["text", 50, 80, "LA HUIDA", 190, "white", "la"], ["text", 50, 320, "MÁS LOCA", 160, "yellow", "la"], ["text", 50, 500, "DE UN CEO", 120, "red", "la"]]),
    dict(img="thumb_split", zoom=1.1, cx=0.5, items=[
        ["text", 640, 40, "¿HÉROE", 190, "white", "mt"], ["text", 640, 280, "O FUGITIVO?", 170, "red", "mt"]]),
    dict(img="fabrica_vacia", zoom=1.05, cx=0.5, shade=["left", 220, 0.65], items=[
        ["text", 50, 70, "NISSAN", 200, "white", "la"], ["text", 50, 300, "EN CRISIS", 170, "red", "la"], ["badge", 50, 520, 560, 650, "-533.000 M¥", 90]]),
    dict(img="thumb_caja", zoom=1.0, cx=0.5, bright=0.9, items=[
        ["text", 640, 30, "EL CEO QUE HUYÓ", 130, "yellow", "mt"], ["stamp", "BUSCADO", 640, 470, -8, 170]]),
    dict(img="mexico_planta", zoom=1.05, cx=0.5, shade=["left", 230, 0.65], items=[
        ["text", 50, 70, "UN MEXICANO", 150, "white", "la"], ["text", 50, 250, "AL RESCATE", 150, "yellow", "la"], ["text", 50, 430, "DE NISSAN", 150, "red", "la"]]),
    dict(img="haneda", zoom=1.05, cx=0.5, shade=["right", 220, 0.6], items=[
        ["text", 1230, 80, "ARRESTADO", 160, "red", "ra"], ["text", 1230, 280, "AL BAJAR", 140, "white", "ra"], ["text", 1230, 440, "DEL AVIÓN", 140, "white", "ra"]]),
    dict(img="thumb_caja", zoom=1.1, cx=0.6, shade=["left", 230, 0.6], items=[
        ["text", 50, 90, "14 M$", 260, "red", "la"], ["text", 50, 400, "DE FIANZA… Y SE FUE", 85, "white", "la"], ["badge", 50, 540, 420, 670, "NISSAN", 110]]),
]
# Miniaturas con "algo por descubrir" (acompañan al título "…dentro de ESTO" sin decir "caja")
THUMBS += [
    dict(img="thumb_caja", zoom=1.2, cx=0.75, cy=0.5, shade=["left", 235, 0.62], items=[
        ["text", 45, 70, "LA HUIDA", 150, "white", "la"], ["text", 45, 250, "IMPOSIBLE", 125, "red", "la"],
        ["text", 45, 420, "DE JAPÓN", 115, "yellow", "la"], ["arrow", 610, 40, 75, 170]]),
    dict(img="caja_avion", zoom=1.1, cx=0.5, cy=0.5, shade=["left", 230, 0.6], items=[
        ["text", 45, 70, "SALVÓ NISSAN…", 120, "white", "la"], ["text", 45, 240, "Y SE FUE", 150, "yellow", "la"],
        ["text", 45, 430, "ASÍ", 190, "red", "la"], ["arrow", 700, 60, 75, 170]]),
]
THUMBS_TOP = [11, 5, 1]

META = {
    "code": "004",
    "name": "Carlos Ghosn y Nissan",
    "intro_chapter": "Intro: escapó en una caja",
    "titles": [
        "Salvó a Nissan… y luego escapó de Japón dentro de ESTO",
        "El hombre que salvó a Nissan… y su huida imposible de Japón",
        "Salvó a Nissan de la quiebra. 20 años después, huyó de Japón",
    ],
    "description": "En 1999 Nissan estaba al borde de la quiebra. Carlos Ghosn la salvó en un año y Japón lo convirtió en héroe de manga. En 2018 lo arrestaron en Tokio, acusado de ocultar parte de su sueldo (él lo niega), y en 2019 escapó del país escondido en una caja de equipos de música. Hoy Nissan vuelve a perder miles de millones… y quien intenta salvarla es un mexicano.",
    "sources": [
        "InsideHook / Gulf News / Kyodo / NTV: la huida del 29 de diciembre de 2019 (tren bala, hotel de Kansai, caja, Estambul y Beirut)",
        "NPR / Al Jazeera / UPI: condena de Michael y Peter Taylor en Japón (julio de 2021)",
        "NHK / Bloomberg / Newshub: arresto en Haneda (19-nov-2018), acusaciones y 108 días de detención",
        "NBC News: grupo de trabajo de la ONU sobre detención arbitraria (2020)",
        "Darden / Autotrade / Alliance Renault-Nissan: compra del 36,8 % de Nissan por Renault (1999)",
        "IndustryWeek / Chief Executive: plan de rescate de Nissan, 21.000 empleos y beneficio del año fiscal 2000",
        "Encyclopedia.com: manga sobre Carlos Ghosn (2002)",
        "Fortune / Automotive News / Mexico Business News / Drive: pérdidas de Nissan, plan Re:Nissan y cierre de CIVAC",
        "Bloomberg Línea / exchange4media: nombramiento de Iván Espinosa como CEO (abril de 2025)",
        "Nissan Mexicana / UnoTV: Nissan, marca más vendida en México en 2025",
        "Bloomberg: demanda de Ghosn contra Nissan por 1.000 millones de dólares (2023)",
    ],
    "hashtags": "#Nissan #CarlosGhosn #Japón #Negocios #México",
    "tags": ["carlos ghosn", "nissan", "ghosn fuga", "ghosn caja", "nissan crisis", "nissan méxico", "iván espinosa",
             "renault nissan", "historia de empresas", "japón", "fugitivo", "el último balance"],
    "pinned": "¿Héroe que salvó a Nissan o jefe que se creyó por encima de las reglas? 👇 Te leo. Y dime qué empresa quieres para el próximo vídeo.",
    "playlist": "Auges y caídas",
    "shorts": {
        "a": {"title": "Escapó de Japón escondido en una caja de altavoces",
              "description": "La huida de Carlos Ghosn. Historia completa en el canal. #CarlosGhosn #Nissan #shorts",
              "tags": ["carlos ghosn", "nissan", "fuga", "japón", "shorts"]},
        "b": {"title": "Salvó a Nissan en un año… y acabó arrestado",
              "description": "De héroe de manga a fugitivo. Vídeo completo en el canal. #Nissan #CarlosGhosn #shorts",
              "tags": ["nissan", "carlos ghosn", "historia de empresas", "japón", "shorts"]},
        "c": {"title": "La marca nº1 de México está en crisis… y la salva un mexicano",
              "description": "Nissan e Iván Espinosa. Historia completa en el canal. #Nissan #México #shorts",
              "tags": ["nissan", "nissan méxico", "iván espinosa", "morelos", "shorts"]},
    },
}
