# Vídeo 012 — Crocs: del «peor invento» y una acción de 1 dólar a facturar 4.000 millones (guion del 18-nov-2026)
# Tema elegido por el usuario entre 4 opciones con datos (ideas.md, tanda del 13-nov): EN 1,9 M (may-2026); en español un solo
# largo de 115 k. Auge tras caída (para alternar después de Stellantis). Ángulo latino: la fábrica de México y Bad Bunny.
#
# Hechos verificados (WebSearch, 18-nov-2026):
# - Fundadores: Scott Seamans, Lyndon «Duke» Hanson y George Boedecker Jr. (Boulder, Colorado). Zueco de espuma de la canadiense
#   Foam Creations (material Croslite, resina de celda cerrada). Debut: Fort Lauderdale Boat Show, nov-2002 (unos 200 pares, agotados).
#   Crocs compra Foam Creations en jun-2004 para quedarse con el material.
# - Ingresos (comunicados de Crocs): 2004 13,5 M$; 2005 108,6 M$; 2006 354,7 M$; 2007 847,4 M$.
# - Salida a bolsa (Nasdaq) el 8-feb-2006 a 21 $ por acción: 208 M$. Jibbitz (adornos para los agujeros, creados por Sheri Schmelzer,
#   una madre de Boulder) comprada en 2006 por 10 M$ (+10 M$ si cumplía objetivos).
# - La acción pasó de 75 $ a fines de 2007; en nov-2008 llegó a valer alrededor de 1 $ (mínimo de 0,79 $ según Reuters).
#   2008: pérdida neta de 183,6 M$ (2007: beneficio de 168,2 M$); ingresos −15 %, a 721 M$; inventario rebajado tras depreciaciones.
#   Plantilla: de 5.300 a 3.700 personas (NBC; Time: −32 % de empleos desde 2007); cierre de fábricas en Brasil y Canadá.
#   Informe anual 2008 (17-mar-2009): Deloitte expresa «dudas sustanciales» sobre su capacidad de seguir en funcionamiento.
# - Time, may-2010: Crocs en la lista de los «50 peores inventos» (con el amianto y el Segway).
# - Blackstone invierte 200 M$ en ene-2014 (acciones preferentes). Andrew Rees: presidente desde 2014, CEO desde el 1-jun-2017;
#   en 2017 anuncian el cierre de unas 160 tiendas. Balenciaga presenta Crocs con plataforma en París (oct-2017); preventa en
#   Barneys el 1-feb-2018 a 850 $: agotadas en horas. Ago-2018: Crocs ya había cerrado su fábrica de México y cerraba la última,
#   en Italia (toda la producción pasa a terceros).
# - 2020: «A Free Pair for Healthcare»: hasta 10.000 pares al día; más de 860.000 pares donados en 2020. Bad Bunny x Crocs
#   (29-sep-2020, 60 $, que brillan en la oscuridad): agotados en unos 16 minutos (NYT).
# - Dic-2021: compra de HEYDUDE por unos 2.500 M$. 2024: ingresos de 4.102 M$ y beneficio neto de 950,1 M$.
# - 2.º trim. 2025: depreciación de HEYDUDE de 737 M$; el 7-ago-2025 la acción cae ~27-30 % en un día. Año 2025: ingresos de
#   4.041 M$ (marca Crocs +1,5 %, HEYDUDE −13,3 %) y pérdida neta de 81,2 M$ por la depreciación.
# - 3.er trim. 2026: ingresos de algo más de 1.000 M$ (+5 %), marca Crocs 873 M$ (+4 %), HEYDUDE +6 %; tercera mejora del pronóstico anual.
VOICE = "i4Kar2uamCWyas8TAu31"  # Adán
SPEED = 1.0

# Fotos reales (Wikimedia Commons, solo dominio público / CC0 / CC BY, con crédito). Las que no aparezcan van como escenas de código.
IMAGES = {
    "crocs_clog": "Photorealistic product photo of a single bright lime-green foam clog shoe with round ventilation holes on top and a heel strap, resting on a weathered wooden boat deck, soft morning light, shallow depth of field, cinematic 16:9, no text, no logos",
    "crocs_many": "Photorealistic wide shot of a store wall filled with rows of colorful foam clog shoes with round ventilation holes, every color of the rainbow, bright retail lighting, cinematic 16:9, no text, no logos",
    "crocs_store": "Tienda de Crocs (foto real)", "crocs_feet": "Pies con Crocs (foto real)",
    "boat_show": "Salón náutico / velero (foto real)", "boulder": "Boulder, Colorado (foto real)",
    "nasdaq": "Nasdaq MarketSite (foto real)", "jibbitz": "Photorealistic close-up of a child's colorful foam clog shoe decorated with small playful charms plugged into its round holes (flowers, stars, smiley faces), on a kitchen table, warm light, cinematic 16:9, no text, no logos", "nurses": "Photorealistic hospital corridor, tired doctors and nurses in blue scrubs wearing colorful foam clog shoes, face masks, 2020 pandemic atmosphere, cinematic documentary still, 16:9, no text, no logos",
    "runway": "Photorealistic high-fashion runway show in Paris, model walking toward camera wearing oversized chunky platform foam clogs, audience with phones on both sides, dramatic lighting, cinematic 16:9, no text, no logos", "warehouse": "Photorealistic huge warehouse with endless shelves stacked to the ceiling with unsold shoe boxes, dim lighting, forklift, sense of excess inventory, cinematic 16:9, no text, no logos", "wall_street": "Photorealistic 2008 financial crisis scene, stressed stock trader holding his head in front of screens full of red falling charts, cinematic documentary still, 16:9, no text, no logos",
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
    dict(id="s01", text="En dos mil diez, la revista Time lo puso en su lista de los cincuenta peores inventos de la historia. En la misma lista que el amianto.",
         visual=dict(type="headline", kicker="TIME · 2010", text="Los 50 peores inventos de la historia", mark="peores", source="Paráfrasis de la lista de Time (mayo de 2010)")),
    dict(id="s02", text="Poco antes, su acción se había desplomado de setenta y cinco dólares a uno solo, y sus auditores dudaban de que la empresa sobreviviera.",
         visual=dict(type="lines", title="ACCIÓN DE CROCS (DÓLARES)", x=["FEB 2006", "OCT 2007", "NOV 2008"], series=[["US$", [21, 75, 1], "red"]])),
    dict(id="s03", text="Hoy, ese zapato de plástico con agujeros vende más de cuatro mil millones de dólares al año. Se llama Crocs.",
         visual=I("crocs_many", pop=["+4.000 M$ AL AÑO"])),
    dict(id="s04", text="¿Cómo pasó el peor invento del mundo a ser una máquina de hacer dinero? Y lo más curioso: el empujón definitivo llegó de una pasarela de París… y de un reguetonero de Puerto Rico.",
         visual=I("crocs_clog", pop=["¿EL PEOR INVENTO?"]), abre="P1: ¿Cómo pasó Crocs del «peor invento» a facturar 4.000 millones?"),

    # --- 01 UN ZAPATO PARA BARCOS ---
    dict(id="s05", text="Capítulo uno: un zapato para barcos.", bloque="desarrollo", visual=T("01", "Un zapato para barcos")),
    dict(id="s06", text="Dos mil dos. Tres amigos de Boulder, en Colorado, se van a navegar por el Caribe. Uno de ellos lleva puesto un zueco raro, hecho de espuma.",
         visual=I("boulder", cap="BOULDER, COLORADO")),
    dict(id="s07", text="Lo fabrica una pequeña empresa de Canadá con un material propio: liviano, que no absorbe el agua y no resbala en la cubierta mojada.",
         visual=dict(type="quote", text="LIVIANO · NO ABSORBE EL AGUA\nNO RESBALA")),
    dict(id="s08", text="Ven el negocio enseguida: el calzado perfecto para la gente de los barcos. Le ponen un nombre de animal que se mueve igual de bien en el agua que en tierra: el cocodrilo. Crocs.",
         visual=I("boat_show", pop=["CROCS"])),
    dict(id="s09", text="En noviembre de dos mil dos lo presentan en el salón náutico de Fort Lauderdale, en Florida. Llevan unos doscientos pares. Los venden todos.",
         visual=dict(type="num", start=0, end=200, label="PARES VENDIDOS EN SU PRIMERA FERIA (2002)")),
    dict(id="s09b", text="El secreto estaba en el material, que luego bautizarían Croslite: según la empresa, se ablanda con el calor del cuerpo y toma la forma del pie. Por eso es tan cómodo… y tan difícil de copiar.",
         visual=dict(type="quote", text="CROSLITE\nSE AMOLDA AL PIE")),
    dict(id="s10", text="Al principio lo compran sobre todo marineros y gente que pasa el día de pie. Pero en dos mil cuatro hacen la jugada clave: compran la empresa canadiense para quedarse con su material en exclusiva.",
         visual=dict(type="year", year="2004", sub="CROCS COMPRA EL MATERIAL EN EXCLUSIVA")),
    dict(id="s11", text="Ese año facturan trece millones de dólares. Nada mal para un zapato que todo el mundo llamaba feo. Pero lo que viene después no lo esperaba nadie.",
         visual=dict(type="num", start=0, end=13.5, dec=1, prefix="", suffix=" M$", label="INGRESOS DE CROCS EN 2004"),
         abre="P2: ¿Por qué un zapato de barco se volvió la locura de 2007?"),

    # --- 02 LA FIEBRE ---
    dict(id="s12", text="Capítulo dos: la fiebre.", visual=T("02", "La fiebre")),
    dict(id="s13", text="Resulta que los Crocs eran cómodos de verdad. Médicos, enfermeras, cocineros y niños empiezan a usarlos todo el día. Y el boca a boca hace el resto.",
         visual=I("crocs_feet", pop=["CÓMODOS DE VERDAD"])),
    dict(id="s14", text="Las ventas explotan: de trece millones en dos mil cuatro a ciento ocho millones en dos mil cinco. Y a trescientos cincuenta y cinco millones en dos mil seis.",
         visual=dict(type="bars", title="INGRESOS DE CROCS (MILLONES DE DÓLARES)", data=[["2004", 13.5], ["2005", 108.6], ["2006", 354.7]], dec=1)),
    dict(id="s15", text="En febrero de dos mil seis salen a la bolsa Nasdaq a veintiún dólares por acción y recaudan doscientos ocho millones.",
         visual=I("nasdaq", pop=["208 M$"])),
    dict(id="s16", text="Y aparece otra idea genial: una madre de Boulder había empezado a decorar los Crocs de sus hijos metiendo adornos en los agujeros.",
         visual=I("jibbitz", pop=["UNA IDEA DE CASA"])),
    dict(id="s17", text="Su pequeña empresa se llama Jibbitz. Crocs se la compra por diez millones de dólares. Ahora cada par se podía personalizar… y vender adornos sin parar.",
         visual=dict(type="stamp", text="JIBBITZ", stamp="10 M$", col="yellow")),
    dict(id="s18", text="En dos mil siete, Crocs factura ochocientos cuarenta y siete millones de dólares. Y su acción llega a los setenta y cinco dólares.",
         visual=dict(type="bars", title="INGRESOS DE CROCS (MILLONES DE DÓLARES)", data=[["2004", 13.5], ["2005", 108.6], ["2006", 354.7], ["2007", 847.4]], dec=1),
         cierra="P2"),
    dict(id="s19", text="Para no quedarse sin stock, la empresa abre fábricas, multiplica modelos y produce como si la moda fuera a durar para siempre. Ese fue el error que casi la mata.",
         visual=I("warehouse", pop=["PRODUCIR SIN FRENO"]), abre="P3: ¿Qué error casi mata a Crocs?"),

    # --- 03 EL DERRUMBE ---
    dict(id="s20", text="Capítulo tres: el derrumbe.", visual=T("03", "El derrumbe")),
    dict(id="s21", text="En dos mil ocho, la fiebre se apaga. El que quería unos Crocs ya los tenía, y los que los odiaban los seguían odiando.",
         visual=dict(type="quote", text="EL QUE LOS QUERÍA… YA LOS TENÍA")),
    dict(id="s22", text="Y encima llega la crisis financiera. Las tiendas dejan de pedir, y Crocs se queda con almacenes llenos de zapatos que nadie quiere.",
         visual=I("wall_street", pop=["CRISIS DE 2008"])),
    dict(id="s23", text="Ese año pasa de ganar ciento sesenta y ocho millones a perder ciento ochenta y cuatro. Cierra sus fábricas de Brasil y Canadá y recorta casi un tercio de la plantilla.",
         visual=dict(type="bars", title="RESULTADO NETO DE CROCS (MILLONES DE DÓLARES)", data=[["2007", 168.2], ["2008", -183.6]], dec=1)),
    dict(id="s24", text="La acción se hunde. En noviembre de dos mil ocho llega a valer alrededor de un dólar. Había valido setenta y cinco.",
         visual=dict(type="lines", title="ACCIÓN DE CROCS (DÓLARES)", x=["FEB 2006", "OCT 2007", "NOV 2008"], series=[["US$", [21, 75, 1], "red"]]),
         cierra="P3"),
    dict(id="s25", text="Y en marzo de dos mil nueve, sus propios auditores escriben en el informe anual que tienen dudas sustanciales de que la empresa pueda seguir funcionando.",
         visual=dict(type="headline", kicker="INFORME ANUAL 2008", text="Los auditores dudan de que Crocs pueda seguir funcionando", mark="dudan", source="Paráfrasis del informe anual de Crocs (marzo de 2009)")),
    dict(id="s26", text="Sobrevive, pero queda tocada durante años. Y en dos mil diez llega la humillación de la revista Time: uno de los peores inventos de la historia.",
         visual=dict(type="stamp", text="EL PEOR INVENTO", stamp="2010", col="red")),
    dict(id="s27", text="Para salir de ese pozo hacía falta algo más que dinero. Y la ayuda llegó del lugar menos pensado.",
         visual=I("crocs_clog"), abre="P4: ¿Quién rescató a Crocs?"),

    # --- 04 EL RESCATE ---
    dict(id="s28", text="Capítulo cuatro: el rescate.", visual=T("04", "El rescate")),
    dict(id="s29", text="Primero, el dinero: en enero de dos mil catorce, el fondo Blackstone mete doscientos millones de dólares en la empresa.",
         visual=dict(type="num", start=0, end=200, suffix=" M$", label="INVERSIÓN DE BLACKSTONE (ENERO DE 2014)")),
    dict(id="s29b", text="A cambio se queda con acciones preferentes y dos asientos en el consejo. Ahora alguien vigilaba cada dólar.",
         visual=dict(type="stamp", text="BLACKSTONE", stamp="2014", col="yellow")),
    dict(id="s30", text="Ese año llega Andrew Rees, que en dos mil diecisiete se convierte en director general. Su receta es casi lo contrario de la de dos mil siete.",
         visual=dict(type="timeline", title="ANDREW REES", points=[["2014", "Llega como presidente"], ["2017", "Director general"], ["2018", "Cierra las fábricas propias"]], hl=1)),
    dict(id="s31", text="Cierra unas ciento sesenta tiendas, recorta modelos y vuelve a lo esencial: el zueco clásico de siempre, el mismo que todos llamaban feo.",
         visual=dict(type="stamp", text="VOLVER AL ZUECO", stamp="2017", col="yellow")),
    dict(id="s32", text="En dos mil dieciocho cierra su fábrica de México y después la última que le quedaba, en Italia. Desde entonces, todos sus Crocs los fabrican otras empresas.",
         visual=dict(type="versus", title="2018: ADIÓS A LAS FÁBRICAS PROPIAS", left=["MÉXICO", "CERRADA"], right=["ITALIA", "CERRADA"], mid="+", lcol="red", rcol="red")),
    dict(id="s33", text="Y entonces ocurre lo impensado. En octubre de dos mil diecisiete, la casa de lujo Balenciaga saca a su pasarela de París… unos Crocs con plataforma.",
         visual=I("runway", cap="PARÍS, OCTUBRE DE 2017")),
    dict(id="s34", text="Cuestan ochocientos cincuenta dólares. Y cuando salen a la venta, se agotan en horas. El zapato feo se había vuelto moda.",
         visual=dict(type="num", start=0, end=850, suffix=" $", label="CROCS DE BALENCIAGA (PREVENTA, FEBRERO DE 2018)"), cierra="P4"),
    dict(id="s35", text="Después llegan las colaboraciones con artistas, como el rapero Post Malone, que se agotan casi al instante. Pero el empujón definitivo todavía estaba por llegar.",
         visual=I("crocs_store", pop=["AGOTADOS"]), abre="P5: ¿Qué terminó de convertir a Crocs en un fenómeno?"),

    # --- 05 LO FEO SE VUELVE COOL ---
    dict(id="s36", text="Capítulo cinco: lo feo se vuelve cool.", visual=T("05", "Lo feo se vuelve cool")),
    dict(id="s37", text="Dos mil veinte. La pandemia encierra a medio mundo en casa, y la gente quiere comodidad. Ya nadie se fija en si un zapato es lindo.",
         visual=dict(type="year", year="2020", sub="LA PANDEMIA LO CAMBIA TODO")),
    dict(id="s38", text="Crocs regala pares a médicos y enfermeras: más de ochocientos sesenta mil solo en dos mil veinte. Una campaña que nadie podía criticar.",
         visual=I("nurses", pop=["+860.000 PARES REGALADOS"])),
    dict(id="s39", text="Y en septiembre de ese año, Bad Bunny lanza sus propios Crocs, que brillan en la oscuridad. Cuestan sesenta dólares y se agotan en unos dieciséis minutos.",
         visual=dict(type="num", start=0, end=16, label="MINUTOS QUE TARDARON EN AGOTARSE LOS CROCS DE BAD BUNNY")),
    dict(id="s40", text="El reguetonero de Puerto Rico, el más escuchado del planeta, con el zapato que Time llamaba el peor invento. Ya no había vuelta atrás.",
         visual=dict(type="quote", text="BAD BUNNY × CROCS\nSEPTIEMBRE DE 2020"), cierra="P5"),
    dict(id="s40b", text="Detrás vendrían Justin Bieber y hasta KFC, con unos Crocs que imitaban el balde de pollo frito. Lo que antes daba vergüenza ahora era una declaración de estilo.",
         visual=I("crocs_feet", pop=["DE VERGÜENZA A ESTILO"])),
    dict(id="s40c", text="En dos mil veintiuno, sus ventas suben un sesenta y siete por ciento, hasta dos mil trescientos millones de dólares. Récord. Y no iba a ser el último.",
         visual=dict(type="bars", title="INGRESOS DE CROCS (MILLONES DE DÓLARES)", data=[["2007", 847.4], ["2021", 2313.0]], dec=0)),
    dict(id="s41", text="En dos mil veinticuatro, Crocs factura más de cuatro mil cien millones de dólares y gana novecientos cincuenta millones. Récord absoluto.",
         visual=dict(type="bars", title="INGRESOS DE CROCS (MILLONES DE DÓLARES)", data=[["2007", 847.4], ["2024", 4102.1]], dec=0),
         cierra="P1", abre="P6: ¿Repitió Crocs el error de 2008?"),
    dict(id="s42", text="Pero con tanto dinero en la caja, Crocs hizo una apuesta enorme. Y por un momento pareció que iba a repetir la historia de dos mil ocho.",
         visual=I("warehouse")),

    # --- 06 ¿Y AHORA? ---
    dict(id="s43", text="Capítulo seis: ¿y ahora?", visual=T("06", "¿Y ahora?")),
    dict(id="s44", text="A fines de dos mil veintiuno, Crocs anuncia la compra de otra marca de calzado cómodo, HEYDUDE, por unos dos mil quinientos millones de dólares.",
         visual=dict(type="num", start=0, end=2500, suffix=" M$", label="COMPRA DE HEYDUDE (DICIEMBRE DE 2021)")),
    dict(id="s45", text="Pero HEYDUDE se frena. En dos mil veinticinco, Crocs reconoce que la marca vale mucho menos de lo que pagó y anota una pérdida de setecientos treinta y siete millones.",
         visual=dict(type="num", start=0, end=-737, suffix=" M$", label="DEPRECIACIÓN DE HEYDUDE (2025)")),
    dict(id="s46", text="El día que lo anuncia, en agosto, su acción cae casi un treinta por ciento. Y por esa pérdida, Crocs termina dos mil veinticinco en rojo.",
         visual=dict(type="headline", kicker="AGOSTO DE 2025", text="La acción de Crocs se desploma tras el golpe de HEYDUDE", mark="desploma", source="Paráfrasis de la prensa financiera (7 de agosto de 2025)")),
    dict(id="s47", text="La diferencia con dos mil ocho es que el zueco seguía vendiendo. La marca Crocs creció ese año, sobre todo fuera de Estados Unidos.",
         visual=dict(type="versus", title="2025", left=["CROCS", "+1,5 %"], right=["HEYDUDE", "−13,3 %"], mid="VS", lcol="yellow", rcol="red"), cierra="P6", abre="P7: ¿Durará esta vez la moda de Crocs?"),
    dict(id="s48", text="Y en dos mil veintiséis, la empresa vuelve a crecer: en el tercer trimestre supera los mil millones de dólares y mejora su pronóstico por tercera vez en el año.",
         visual=dict(type="num", start=0, end=1000, prefix="+", suffix=" M$", label="INGRESOS DEL 3.ER TRIMESTRE DE 2026")),
    dict(id="s48b", text="En ese trimestre, la marca Crocs vende ochocientos setenta y tres millones de dólares. Y HEYDUDE, la que casi la hunde, vuelve a crecer: un seis por ciento.",
         visual=dict(type="versus", title="3.ER TRIMESTRE DE 2026", left=["CROCS", "873 M$"], right=["HEYDUDE", "+6 %"], mid="+", lcol="yellow", rcol="yellow")),
    dict(id="s49", text="¿Durará? Nadie lo sabe. La moda de lo feo ya se apagó una vez. Pero esta vez Crocs aprendió algo: no fabricar como si la fiesta no fuera a terminar nunca.",
         visual=I("crocs_many", pop=["¿DURARÁ?"])),

    # --- CIERRE ---
    dict(id="s50", text="Así que la próxima vez que veas unos Crocs, acuérdate: es el zapato que pasó de valer un dólar en bolsa y ser el peor invento del mundo a facturar más de cuatro mil millones.", bloque="cierre", cierra="P7",
         visual=I("crocs_clog")),
    dict(id="s51", text="¿Tú tienes unos Crocs, o jamás te los pondrías? Cuéntamelo en los comentarios.",
         visual=dict(type="quote", text="¿TIENES CROCS…\nO JAMÁS TE LOS PONDRÍAS?")),
    dict(id="s52", text="Y si te gustan estas historias de empresas que suben y caen, suscríbete: cada semana, un nuevo balance.",
         visual=I("crocs_store")),
]

FALLBACK = {
    "s03": dict(type="num", start=0, end=4000, prefix="+", suffix=" M$", label="INGRESOS ANUALES DE CROCS"),
    "s04": dict(type="quote", text="¿EL PEOR INVENTO…\nO UNA MÁQUINA DE HACER DINERO?"),
    "s06": dict(type="year", year="2002", sub="TRES AMIGOS DE BOULDER, COLORADO"),
    "s08": dict(type="quote", text="COCODRILO = AGUA Y TIERRA\nCROCS"),
    "s13": dict(type="quote", text="MÉDICOS · ENFERMERAS\nCOCINEROS · NIÑOS"),
    "s15": dict(type="num", start=0, end=208, suffix=" M$", label="SALIDA A BOLSA (FEBRERO DE 2006)"),
    "s16": dict(type="quote", text="ADORNOS EN LOS AGUJEROS\nUNA IDEA DE CASA"),
    "s19": dict(type="stamp", text="PRODUCIR\nSIN FRENO", stamp="2007", col="red"),
    "s22": dict(type="stamp", text="ALMACENES LLENOS", stamp="2008", col="red"),
    "s27": dict(type="quote", text="¿QUIÉN PODÍA\nSALVAR A CROCS?"),
    "s33": dict(type="stamp", text="BALENCIAGA", stamp="PARÍS 2017", col="yellow"),
    "s35": dict(type="stamp", text="AGOTADOS", stamp="EN MINUTOS", col="yellow"),
    "s38": dict(type="num", start=0, end=860000, prefix="+", label="PARES REGALADOS AL PERSONAL SANITARIO (2020)"),
    "s42": dict(type="quote", text="¿REPETIRÍA\nEL ERROR DE 2008?"),
    "s49": dict(type="quote", text="¿DURARÁ?"),
    "s40b": dict(type="quote", text="JUSTIN BIEBER · KFC\nDE VERGÜENZA A ESTILO"),
    "s50": dict(type="quote", text="DE 1 $ EN BOLSA\nA +4.000 M$ AL AÑO"),
    "s52": dict(type="quote", text="SUSCRÍBETE\nCADA SEMANA, UN NUEVO BALANCE"),
}

PRONUNCIA = {"Crocs": "Crocs", "Boulder": "Bóulder", "Fort Lauderdale": "Fort Lóderdeil", "Nasdaq": "Násdak", "Jibbitz": "Yíbits",
             "Blackstone": "Bláckston", "Andrew Rees": "Ándru Ris", "Balenciaga": "Balenciaga", "Bad Bunny": "Bad Bani",
             "HEYDUDE": "Jei Dud", "Time": "Taim"}

# Shorts (pautas del 15-nov): cifra o conflicto en el primer segundo, 20–25 s, ángulo latino, bucle y cierre hacia el largo.
SHORTS = {
    "a": {"bar": "BAD BUNNY Y LOS CROCS", "scenes": [
        dict(id="a01", text="Dieciséis minutos. Eso tardaron en agotarse los Crocs de Bad Bunny en dos mil veinte.", key="crocs_many"),
        dict(id="a02", text="Doce años antes, la acción de Crocs valía un dólar y sus auditores dudaban de que la empresa sobreviviera.", key="wall_street"),
        dict(id="a03", text="Hoy vende más de cuatro mil millones de dólares al año, y el reguetonero de Puerto Rico tuvo mucho que ver.", key="crocs_store"),
        dict(id="a04", text="La historia completa, en el vídeo del canal.", key="crocs_clog"),
    ]},
    "b": {"bar": "EL PEOR INVENTO", "scenes": [
        dict(id="b01", text="La revista Time lo puso entre los cincuenta peores inventos de la historia, junto al amianto.", key="crocs_clog"),
        dict(id="b02", text="Siete años después, Balenciaga lo subió a una pasarela de París y lo vendió a ochocientos cincuenta dólares.", key="runway"),
        dict(id="b03", text="Se agotó en horas. Hoy ese zapato de plástico factura más de cuatro mil millones al año.", key="crocs_many"),
        dict(id="b04", text="La historia completa, en el vídeo del canal.", key="crocs_store"),
    ]},
}
FALLBACK.update({
    "a01": dict(type="num", start=0, end=16, label="MINUTOS"), "a02": dict(type="num", start=75, end=1, prefix="", suffix=" $", label="ACCIÓN DE CROCS (2008)"),
    "a03": dict(type="num", start=0, end=4000, prefix="+", suffix=" M$", label="AL AÑO"), "a04": dict(type="quote", text="LA HISTORIA COMPLETA\nEN EL CANAL 👆"),
    "b01": dict(type="quote", text="«LOS 50 PEORES\nINVENTOS»"), "b02": dict(type="num", start=0, end=850, suffix=" $", label="BALENCIAGA × CROCS"),
    "b03": dict(type="num", start=0, end=4000, prefix="+", suffix=" M$", label="AL AÑO"), "b04": dict(type="quote", text="LA HISTORIA COMPLETA\nEN EL CANAL 👆"),
})

THUMBS = [
    dict(img="crocs_clog", zoom=1.05, cx=0.35, shade=["right", 225, 0.6], items=[
        ["text", 1240, 50, "EL PEOR", 170, "white", "ra"], ["text", 1240, 250, "INVENTO", 170, "red", "ra"],
        ["badge", 760, 490, 1240, 620, "4.000 M$", 100]]),
    dict(img="crocs_many", zoom=1.05, cx=0.5, shade=["left", 230, 0.62], items=[
        ["text", 45, 60, "1 $", 200, "red", "la"], ["text", 45, 300, "→ 4.000 M$", 150, "yellow", "la"]]),
    dict(img="wall_street", zoom=1.1, cx=0.62, shade=["left", 220, 0.55], items=[
        ["text", 45, 60, "VALÍA", 170, "white", "la"], ["text", 45, 270, "1 DÓLAR", 180, "red", "la"], ["crash", 60, 520, 560, 690]]),
    dict(img="warehouse", zoom=1.05, cx=0.6, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "EL ERROR", 170, "white", "la"], ["text", 45, 270, "QUE CASI", 140, "white", "la"], ["text", 45, 440, "LOS MATA", 170, "red", "la"]]),
    dict(img="runway", zoom=1.1, cx=0.62, shade=["left", 220, 0.55], items=[
        ["text", 45, 60, "850 $", 210, "yellow", "la"], ["text", 45, 320, "POR UNOS", 130, "white", "la"], ["text", 45, 480, "CROCS", 150, "white", "la"]]),
    dict(img="crocs_many", zoom=1.05, cx=0.5, shade=["left", 230, 0.62], items=[
        ["text", 45, 60, "DE FEO", 170, "white", "la"], ["text", 45, 270, "A MINA", 170, "yellow", "la"], ["text", 45, 470, "DE ORO", 170, "yellow", "la"]]),
    dict(img="crocs_clog", zoom=1.05, cx=0.35, shade=["right", 200, 0.55], items=[
        ["stamp", "PEOR INVENTO", 900, 250, -10, 120], ["badge", 760, 470, 1240, 600, "+4.000 M$", 100]]),
    dict(img="jibbitz", zoom=1.05, cx=0.7, shade=["left", 220, 0.6], items=[
        ["text", 45, 60, "10 M$", 210, "yellow", "la"], ["text", 45, 320, "POR ESTO", 160, "white", "la"]]),
    dict(img="nurses", zoom=1.05, cx=0.4, shade=["right", 220, 0.55], items=[
        ["text", 1240, 60, "860.000", 170, "yellow", "ra"], ["text", 1240, 270, "GRATIS", 180, "white", "ra"]]),
    dict(img="wall_street", zoom=1.1, cx=0.62, shade=["left", 220, 0.55], items=[
        ["text", 45, 60, "DE 75 $", 170, "white", "la"], ["text", 45, 270, "A 1 $", 210, "red", "la"]]),
]
THUMBS_TOP = [1, 7, 2]

META = {
    "code": "012",
    "name": "Crocs",
    "intro_chapter": "El peor invento del mundo",
    "titles": [
        "El zapato que Time llamó «el peor invento»… y hoy factura 4.000 millones",
        "Crocs: de valer 1 dólar en bolsa a facturar 4.000 millones",
        "El zapato más feo del mundo casi quiebra… y hoy es una mina de oro",
    ],
    "description": "En 2010, la revista Time puso a Crocs entre los 50 peores inventos de la historia. Poco antes, su acción había pasado de 75 dólares a casi 1 y sus auditores dudaban de que sobreviviera. Hoy vende más de 4.000 millones de dólares al año. Cómo un zapato para barcos se volvió la locura de 2007, el error que casi lo mata, el rescate, la pasarela de Balenciaga, los Crocs de Bad Bunny y la apuesta de 2.500 millones que casi repite la historia.",
    "sources": [
        "Crocs: comunicados de resultados anuales 2005-2008 y salida a bolsa (febrero de 2006)",
        "Crocs, informe anual 2008 (marzo de 2009): advertencia de los auditores; Reuters, NBC News y Time (2008-2009): caída de la acción y recortes",
        "Time (mayo de 2010): «The 50 Worst Inventions»",
        "Blackstone y Crocs (enero de 2014): inversión de 200 M$; Crocs (marzo de 2017): Andrew Rees, director general",
        "CNBC / CBS News (agosto de 2018): cierre de las fábricas de México e Italia",
        "Refinery29 / Dazed (2017-2018): Crocs de Balenciaga en París y preventa a 850 $",
        "Crocs (2020): programa «A Free Pair for Healthcare»; The New York Times / Fox Business (septiembre de 2020): Bad Bunny × Crocs",
        "Crocs, formularios 10-K de 2024 y 2025 y comunicado del 3.er trimestre de 2026 (SEC): ingresos, HEYDUDE y depreciación",
        "Fotos vía Wikimedia Commons con licencia CC BY: «Crocs store in Toronto», de bargainmoose (CC BY 2.0); «Example of wear and tear on Crocs», de Baron Maddock (CC BY 4.0); «Caribbean Sunset», de Woody Hibbard (CC BY 2.0)",
    ],
    "disclosure": "Las escenas de zuecos, almacén, pasarela, hospital y bolsa son ilustraciones generadas con IA: no muestran productos, personas ni lugares reales. Las fotos de tiendas y lugares son reales (Wikimedia Commons, créditos en las fuentes). Narración con voz sintética.",
    "altered": "Sí",
    "hashtags": "#Crocs #BadBunny #Negocios",
    "tags": ["crocs", "historia de crocs", "crocs bad bunny", "crocs balenciaga", "heydude", "zapatos crocs", "peores inventos",
             "historia de empresas", "auge y caída", "negocios", "marcas", "el último balance"],
    "pinned": "¿Tienes unos Crocs, o jamás te los pondrías? 👟 Cuéntamelo 👇",
    "playlist": "Auges y caídas",
    "category": "Educación",
    "shorts": {
        "a": {"title": "16 minutos: eso tardaron en agotarse los Crocs de Bad Bunny",
              "description": "Doce años antes, la acción de Crocs valía 1 dólar. La historia completa en el canal.\nFuentes: The New York Times (2020), Reuters (2008), Crocs.\n#Crocs #BadBunny #shorts",
              "tags": ["crocs", "bad bunny", "crocs bad bunny", "zapatos", "negocios", "shorts"]},
        "b": {"title": "Time lo llamó uno de los peores inventos… y Balenciaga lo vendió a 850 dólares",
              "description": "Crocs: del «peor invento» de 2010 a la pasarela de París. La historia completa en el canal.\nFuentes: Time (2010), Refinery29 (2017), Crocs.\n#Crocs #Balenciaga #shorts",
              "tags": ["crocs", "balenciaga", "peores inventos", "moda", "negocios", "shorts"]},
    },
}
