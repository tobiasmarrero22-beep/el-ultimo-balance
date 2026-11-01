# Vídeo 002 — Forever 21: de 4.400 millones a cerrar todas sus tiendas en EE. UU.
VOICE = "fishaudio_a48e73d4fb124c689357e88b04c9db30"
SPEED = 1.0
# Hechos verificados (2026-11-01): Wikipedia, Business Insider, Forbes vía BI, NPR/WISH (venta 81 M$, feb-2020),
# Retail Dive (expediente de quiebra 2019: exceso de metros y alquileres), CNBC (cadena de suministro),
# Wharton (cambio de actitud ante la moda rápida), Axios/NBC (2ª quiebra mar-2025, 354 tiendas),
# Reuters/Retail Gazette (Shein ~1/3 de SPARC, ago-2023), The Fashion Law/TFR (+50 demandas), QMUL (Ariana Grande 10 M$).

IMAGES = {
    "store_closed": "A closed clothing store inside a shopping mall at night, metal security gate pulled down, empty racks visible behind the gate, blank paper signs on the glass, cold fluorescent light, cinematic documentary still, muted teal and orange color grade, no readable text, no logos",
    "immigrant_jobs": "A man seen from behind mopping the floor of an empty office building at night in 1980s Los Angeles, warm tungsten light, film grain, cinematic documentary still, no readable text, no logos",
    "la_1984": "A small colorful clothing boutique on a Los Angeles street in 1984, racks of bright fashionable clothes, warm vintage film photo, cinematic, no readable text, no logos",
    "mall_crowd": "A crowded American shopping mall in the late 2000s, teenagers walking with bright yellow shopping bags, warm light, cinematic wide shot, no readable text, no logos",
    "times_square": "A huge four-story fashion megastore glowing at night on a busy Manhattan square full of billboards and crowds, cinematic wide shot, no readable text, no logos",
    "design_copy": "Two nearly identical dresses on mannequins side by side in a dark studio, one under a golden spotlight and one under a cheap cold light, dramatic contrast, cinematic still, no text, no logos",
    "empty_mall": "An empty abandoned shopping mall corridor with closed stores and dusty skylights, eerie silence, cinematic documentary still, muted colors, no readable text, no logos",
    "phone_shopping": "Close-up of hands holding a smartphone in a dark bedroom, the glowing screen shows an endless grid of cheap colorful clothing thumbnails, cinematic, no readable text, no logos",
    "shipping_packages": "A pile of small grey plastic shipping parcels from overseas stacked at an apartment door at night, cinematic still, moody light, no readable text, no logos",
    "clearance_sale": "A clothing store during liquidation, bare racks, hangers scattered on the floor, a few garments left, harsh fluorescent light, cinematic documentary still, no readable text, no logos",
}

SCENES = [
    # --- GANCHO ---
    dict(id="s01", text="En dos mil quince, Forever 21 vendía cuatro mil cuatrocientos millones de dólares al año. Y sus fundadores tenían una fortuna de cinco mil novecientos millones.",
         visual=dict(type="img", key="mall_crowd", cap="FOREVER 21 · 2015")),
    dict(id="s02", text="Cinco años después, la empresa entera se vendió por ochenta y un millones. Y en dos mil veinticinco cerró todas sus tiendas en Estados Unidos.",
         visual=dict(type="bars", title="MILLONES DE DÓLARES", data=[["VENTAS 2015", 4400], ["SE VENDIÓ POR (2020)", 81]], reveal=2)),
    dict(id="s03", text="Esta es la historia de cómo un inmigrante que limpiaba oficinas construyó un imperio de la moda rápida, y de cómo ese imperio se hundió dos veces.",
         visual=dict(type="img", key="store_closed")),
    dict(id="s04", text="Y el final tiene un giro que casi nadie conoce: Forever 21 terminó aliada con la empresa que le estaba quitando a sus clientes.",
         visual=dict(type="quote", text="EL FINAL:\nSE ALIÓ CON\nSU PEOR RIVAL")),

    # --- CAPÍTULO 1 ---
    dict(id="s05", text="Capítulo uno. El sueño americano.",
         visual=dict(type="title", num="01", text="EL SUEÑO AMERICANO", name="El sueño americano")),
    dict(id="s06", text="Mil novecientos ochenta y uno. Do Won Chang y Jin Sook Chang llegan a Los Ángeles desde Corea del Sur. Llegan con muy poco.",
         visual=dict(type="year", year="1981", sub="DE COREA DEL SUR A LOS ÁNGELES")),
    dict(id="s07", text="Él trabaja en lo que sale: limpiando oficinas, en una gasolinera, en una cafetería. Y se fija en algo: los que conducían los mejores coches del barrio trabajaban en el negocio de la ropa.",
         visual=dict(type="img", key="immigrant_jobs", cap="TRES TRABAJOS A LA VEZ")),
    dict(id="s08", text="En mil novecientos ochenta y cuatro abren su primera tienda en Highland Park, un barrio de Los Ángeles. Se llama Fashion 21, y mide unos ochenta metros cuadrados.",
         visual=dict(type="year", year="1984", sub="NACE FASHION 21 · 80 m²")),
    dict(id="s09", text="El primer año venden setecientos mil dólares. La fórmula era sencilla: ropa a la moda, muy barata, y siempre algo nuevo en las perchas.",
         visual=dict(type="num", start=0, end=700000, prefix="$", suffix="", label="VENTAS DEL PRIMER AÑO")),
    dict(id="s10", text="Cambian el nombre a Forever 21 y empiezan a abrir tiendas en centros comerciales. Una tras otra. Durante dos décadas, la receta funciona.",
         visual=dict(type="img", key="la_1984", cap="FASHION 21 → FOREVER 21")),
    dict(id="s11", text="Su cliente era la chica que quería vestir como su cantante favorita, pero por diez dólares.",
         visual=dict(type="quote", text="VESTIR COMO\nTU ÍDOLO\nPOR 10 DÓLARES")),
    dict(id="s11b", text="El truco era casi psicológico: si veías algo que te gustaba, tenías que comprarlo en ese momento, porque la semana siguiente ya no estaría. Y volvías a la tienda, una y otra vez.",
         visual=dict(type="quote", text="SI TE GUSTA,\nCÓMPRALO YA.\nMAÑANA NO ESTARÁ.")),

    # --- CAPÍTULO 2 ---
    dict(id="s12", text="Capítulo dos. El imperio amarillo.",
         visual=dict(type="title", num="02", text="EL IMPERIO AMARILLO", name="El imperio amarillo")),
    dict(id="s13", text="A finales de los dos mil, las bolsas amarillas de Forever 21 están en todos los centros comerciales de Estados Unidos. Y la empresa empieza a pensar en grande. Muy en grande.",
         visual=dict(type="img", key="mall_crowd", motion="out", cap="LA BOLSA AMARILLA")),
    dict(id="s14", text="En dos mil diez abre en Times Square, en Nueva York, una tienda de cuatro plantas y más de ocho mil metros cuadrados. Una de las tiendas de ropa más grandes de Manhattan.",
         visual=dict(type="img", key="times_square", cap="2010 · TIMES SQUARE · 8.000 m²")),
    dict(id="s15", text="Sale a Asia, a Europa, a América Latina. Llega a unos cuarenta países.",
         visual=dict(type="num", start=0, end=40, prefix="", suffix="", label="PAÍSES")),
    dict(id="s16", text="Y en dos mil quince toca techo: cuatro mil cuatrocientos millones de dólares en ventas. Según Forbes, la fortuna de la familia Chang llega a cinco mil novecientos millones.",
         visual=dict(type="num", start=0, end=5900, prefix="$", suffix=" M", label="FORTUNA DE LOS CHANG · 2015")),
    dict(id="s16b", text="Y sigue siendo un negocio de familia. Sus hijas, Linda y Esther, se suman a la empresa: una se encarga del marketing y la otra de la imagen de las tiendas. Las grandes decisiones se quedan en casa.",
         visual=dict(type="quote", text="UN IMPERIO\nDE 4.400 MILLONES…\nDIRIGIDO EN FAMILIA")),
    dict(id="s17", text="Pero el imperio tenía un lado oscuro. Para ser tan rápida y tan barata, la ropa de Forever 21 se parecía demasiado a la que diseñaban otros.",
         visual=dict(type="img", key="design_copy")),
    dict(id="s18", text="Diseñadores independientes y grandes marcas la llevaron a los tribunales más de cincuenta veces, acusándola de copiar sus diseños. Varias demandas terminaron en acuerdos fuera de los juzgados.",
         visual=dict(type="num", start=0, end=50, prefix="+", suffix="", label="DEMANDAS POR COPIAR DISEÑOS")),
    dict(id="s19", text="Y mientras abría tiendas gigantes por todo el mundo, había firmado algo que la iba a perseguir durante años: alquileres larguísimos, y carísimos.",
         visual=dict(type="quote", text="ERROR Nº 1:\nTIENDAS GIGANTES\nCON ALQUILERES ETERNOS")),
    dict(id="s19b", text="Recuerda esta idea, porque es la clave de todo lo que viene: cuando vendes mucho, una tienda enorme parece una gran idea. Cuando vendes menos, se convierte en una cadena atada al pie.",
         visual=dict(type="img", key="times_square", motion="out")),

    # --- CAPÍTULO 3 ---
    dict(id="s20", text="Capítulo tres. La trampa de los centros comerciales.",
         visual=dict(type="title", num="03", text="LA TRAMPA DE LOS CENTROS COMERCIALES", name="La trampa de los centros comerciales")),
    dict(id="s21", text="En la década de dos mil diez, algo cambia. La gente deja de pasar la tarde en el centro comercial. Ahora compra desde el móvil.",
         visual=dict(type="img", key="store_closed", motion="out")),
    dict(id="s22", text="Y Forever 21 estaba atrapada. Su propio expediente de quiebra lo reconocería después: tenía demasiados metros cuadrados, con alquileres firmados hacía casi una década, en mercados que ya no daban dinero.",
         visual=dict(type="quote", text="DEMASIADOS METROS.\nALQUILERES DE HACE\nUNA DÉCADA.")),
    dict(id="s22b", text="Imagina pagar cada mes el alquiler de una tienda de ocho mil metros cuadrados en Times Square, mientras tus clientes compran desde el sofá.",
         visual=dict(type="img", key="times_square", cap="EL ALQUILER NO BAJA")),
    dict(id="s23", text="Mientras tanto, en internet, tiendas como ASOS, Boohoo o Fashion Nova se le adelantan. Venden online, sin pagar tiendas gigantes.",
         visual=dict(type="img", key="phone_shopping", cap="ASOS · BOOHOO · FASHION NOVA")),
    dict(id="s24", text="Y la propia Forever 21 se había vuelto lenta. Estaba tan ocupada abriendo tiendas que no invirtió lo suficiente en su cadena de suministro. Su ropa nueva tardaba más en llegar que la de sus rivales.",
         visual=dict(type="quote", text="ERROR Nº 2:\nLA MÁS RÁPIDA\nSE VOLVIÓ LENTA")),
    dict(id="s25", text="Y había un problema más. Muchos jóvenes empezaban a mirar mal la moda rápida: la ropa de usar y tirar, y su impacto en el planeta.",
         visual=dict(type="quote", text="LA MODA RÁPIDA\nDEJA DE ESTAR\nDE MODA")),

    # --- CAPÍTULO 4 ---
    dict(id="s26", text="Capítulo cuatro. La primera quiebra.",
         visual=dict(type="title", num="04", text="LA PRIMERA QUIEBRA", name="La primera quiebra")),
    dict(id="s27", text="Septiembre de dos mil diecinueve. Forever 21 se declara en quiebra en Estados Unidos. Anuncia que puede cerrar hasta ciento setenta y ocho tiendas en el país, y hasta trescientas cincuenta en todo el mundo.",
         visual=dict(type="year", year="SEPT. 2019", sub="PRIMERA QUIEBRA · HASTA 350 CIERRES")),
    dict(id="s27b", text="Se retira de la mayoría de sus mercados en Asia y Europa. Pero mantiene sus tiendas en México y en América Latina, donde la marca todavía funcionaba.",
         visual=dict(type="quote", text="ADIÓS ASIA Y EUROPA.\nMÉXICO Y LATAM\nSE QUEDAN.")),
    dict(id="s28", text="Para entonces, según Forbes, los Chang ya habían dejado de ser multimillonarios.",
         visual=dict(type="quote", text="LOS CHANG\nYA NO ERAN\nMULTIMILLONARIOS")),
    dict(id="s29", text="Y ese mismo mes llega otro golpe: la cantante Ariana Grande la demanda por diez millones de dólares, acusándola de usar su imagen sin permiso, con una modelo que se le parecía demasiado.",
         visual=dict(type="img", key="clearance_sale", cap="DEMANDA DE 10 MILLONES $")),
    dict(id="s30", text="En febrero de dos mil veinte, la empresa que había vendido cuatro mil cuatrocientos millones en un año se vende por unos ochenta y un millones de dólares.",
         visual=dict(type="num", start=4400, end=81, prefix="$", suffix=" M", label="PRECIO DE VENTA · FEBRERO 2020")),
    dict(id="s31", text="¿Quién la compra? Authentic Brands, una empresa especializada en comprar marcas en apuros, y dos gigantes de los centros comerciales: Simon Property y Brookfield. Sus mayores caseros. Si Forever 21 cerraba, ellos se quedaban con cientos de locales vacíos.",
         visual=dict(type="quote", text="LA COMPRARON\nSUS PROPIOS\nCASEROS")),

    # --- CAPÍTULO 5 ---
    dict(id="s32", text="Capítulo cinco. El enemigo en casa.",
         visual=dict(type="title", num="05", text="EL ENEMIGO EN CASA", name="El enemigo en casa")),
    dict(id="s33", text="Pero el mundo había cambiado otra vez. Llegan Shein y Temu: millones de productos, precios todavía más bajos, y envíos directos desde China hasta tu puerta.",
         visual=dict(type="img", key="shipping_packages", cap="SHEIN · TEMU")),
    dict(id="s34", text="Si Forever 21 había sido rápida, Shein era otra cosa: subía miles de diseños nuevos cada día.",
         visual=dict(type="img", key="phone_shopping", motion="out")),
    dict(id="s34b", text="Para un comprador joven, ir hasta el centro comercial ya no tenía sentido, si en el móvil tenía mil opciones más baratas y se las traían a casa.",
         visual=dict(type="img", key="shipping_packages", motion="out")),
    dict(id="s35", text="Y entonces, en agosto de dos mil veintitrés, llega el giro. La empresa que operaba Forever 21 se asocia con Shein. Shein se queda con cerca de un tercio de esa empresa, y la ropa de Forever 21 empieza a venderse dentro de Shein.",
         visual=dict(type="year", year="AGOSTO 2023", sub="FOREVER 21 + SHEIN")),
    dict(id="s36", text="La marca a la que habían acusado de copiar a todos acababa vendiéndose en la tienda de su rival más peligroso.",
         visual=dict(type="quote", text="SU RIVAL MÁS PELIGROSO\nAHORA ERA\nSU SOCIO")),
    dict(id="s37", text="No funcionó.",
         visual=dict(type="quote", text="NO FUNCIONÓ.")),

    # --- CAPÍTULO 6 ---
    dict(id="s38", text="Capítulo seis. Para siempre, no.",
         visual=dict(type="title", num="06", text="PARA SIEMPRE, NO", name="Para siempre, no")),
    dict(id="s39", text="Marzo de dos mil veinticinco. Forever 21 se declara en quiebra por segunda vez en menos de seis años.",
         visual=dict(type="year", year="MARZO 2025", sub="SEGUNDA QUIEBRA")),
    dict(id="s40", text="Esta vez no hay rescate. Cierra sus trescientas cincuenta y cuatro tiendas en Estados Unidos.",
         visual=dict(type="num", start=354, end=0, prefix="", suffix="", label="TIENDAS EN ESTADOS UNIDOS")),
    dict(id="s41", text="La empresa culpó al aumento de costes, a los problemas económicos de sus clientes y a la competencia extranjera. Es decir: a los que vendían todavía más barato que ella.",
         visual=dict(type="img", key="store_closed", motion="out", cap="CIERRE TOTAL EN EE. UU.")),
    dict(id="s42", text="Fuera de Estados Unidos, la marca sigue viva en algunos países, como México, porque sus tiendas las operan otras empresas con licencia. Pero el imperio que fundaron los Chang ya no existe.",
         visual=dict(type="quote", text="LA MARCA SIGUE.\nEL IMPERIO,\nNO.")),

    # --- CIERRE ---
    dict(id="s43", text="Entonces, ¿qué mató a Forever 21?",
         visual=dict(type="quote", text="¿QUÉ MATÓ A\nFOREVER 21?")),
    dict(id="s44", text="No fue un solo error. Fue crecer con tiendas gigantes y alquileres eternos. Fue llegar tarde a internet. Fue dejar de ser la más rápida. Y fue encontrarse con alguien que hacía lo mismo que ella, pero más rápido y más barato.",
         visual=dict(type="quote", text="1. TIENDAS GIGANTES\n2. ALQUILERES ETERNOS\n3. TARDE A INTERNET\n4. ALGUIEN MÁS RÁPIDO")),
    dict(id="s45", text="La marca que nació para ganar en velocidad perdió porque llegó alguien más veloz. Exactamente lo que ella les había hecho a las tiendas de antes.",
         visual=dict(type="img", key="la_1984", motion="out")),
    dict(id="s45b", text="Y la lección sirve para cualquier negocio, grande o pequeño: lo que te hace ganar hoy, puede ser exactamente lo que te hunda mañana, si el mundo cambia y tú no.",
         visual=dict(type="quote", text="LO QUE TE HACE GANAR HOY\nPUEDE HUNDIRTE\nMAÑANA")),
    dict(id="s46", text="Si quieres que analicemos otra marca que está en problemas, dímelo en los comentarios. Y suscríbete, porque la próxima historia ya está en camino.",
         visual=dict(type="quote", text="¿QUÉ MARCA\nANALIZAMOS AHORA?")),
]

SHORTS = {
    "a": {"bar": "FOREVER 21", "scenes": [
        dict(id="a01", text="Este hombre limpiaba oficinas en Los Ángeles. Treinta años después tenía una fortuna de miles de millones.", key="immigrant_jobs"),
        dict(id="a02", text="En mil novecientos ochenta y cuatro abrió una pequeña tienda de ropa con su mujer: Forever 21.", key="la_1984"),
        dict(id="a03", text="Ropa de moda, muy barata y siempre nueva. En dos mil quince vendía cuatro mil cuatrocientos millones al año.", key="mall_crowd"),
        dict(id="a04", text="Pero firmó alquileres carísimos, llegó tarde a internet, y aparecieron Shein y Temu.", key="phone_shopping"),
        dict(id="a05", text="Quebró dos veces, y en dos mil veinticinco cerró todas sus tiendas en Estados Unidos.", key="store_closed"),
        dict(id="a06", text="La historia completa, en el vídeo de mi canal.", key="times_square"),
    ]},
    "b": {"bar": "DEMANDADA +50 VECES", "scenes": [
        dict(id="b01", text="Esta tienda fue llevada a juicio más de cincuenta veces por copiar diseños.", key="design_copy"),
        dict(id="b02", text="Forever 21 vendía ropa que se parecía muchísimo a la de las pasarelas, por una fracción del precio.", key="mall_crowd"),
        dict(id="b03", text="Diseñadores independientes y grandes marcas la denunciaron una y otra vez. Y en dos mil diecinueve, Ariana Grande le pidió diez millones de dólares por usar su imagen.", key="clearance_sale"),
        dict(id="b04", text="Ese mismo año se declaró en quiebra. Cómo terminó todo, te lo cuento en el canal.", key="store_closed"),
    ]},
    "c": {"bar": "FOREVER 21 × SHEIN", "scenes": [
        dict(id="c01", text="Forever 21 se alió con la empresa que le estaba quitando a sus clientes.", key="phone_shopping"),
        dict(id="c02", text="En dos mil veintitrés, Shein se quedó con cerca de un tercio de la empresa que operaba Forever 21, y empezó a vender su ropa.", key="shipping_packages"),
        dict(id="c03", text="Año y medio después, Forever 21 quebró por segunda vez y cerró todas sus tiendas en Estados Unidos.", key="store_closed"),
        dict(id="c04", text="La historia completa de cómo se hundió, en mi canal.", key="clearance_sale"),
    ]},
}

THUMBS = [
    dict(img="store_closed", zoom=1.05, cx=0.6, shade=["left", 230, 0.65], items=[
        ["text", 50, 70, "DE $4.400M", 150, "white", "la"], ["text", 50, 250, "A $81M", 280, "red", "la"]]),
    dict(img="mall_crowd", zoom=1.05, cx=0.6, shade=["left", 220, 0.62], items=[
        ["text", 50, 80, "¿QUÉ LE", 160, "white", "la"], ["text", 50, 250, "PASÓ A", 160, "white", "la"], ["text", 50, 420, "FOREVER 21?", 170, "yellow", "la"]]),
    dict(img="store_closed", zoom=1.1, cx=0.5, shade=["left", 160, 0.9], items=[
        ["text", 640, 60, "FOREVER 21", 150, "white", "mt"], ["stamp", "QUEBRÓ 2 VECES", 640, 470, -8, 130]]),
    dict(img="immigrant_jobs", zoom=1.05, cx=0.6, shade=["left", 230, 0.7], items=[
        ["text", 50, 60, "DE CONSERJE", 130, "white", "la"], ["text", 50, 210, "A $5.900M", 160, "yellow", "la"], ["text", 50, 400, "…Y A LA RUINA", 130, "red", "la"]]),
    dict(img="phone_shopping", zoom=1.05, cx=0.5, shade=["right", 220, 0.6], items=[
        ["text", 1230, 90, "¿SHEIN", 190, "white", "ra"], ["text", 1230, 300, "LA MATÓ?", 190, "red", "ra"]]),
    dict(img="clearance_sale", zoom=1.05, cx=0.5, bright=0.9, items=[
        ["text", 640, 40, "EL FIN DE FOREVER 21", 125, "white", "mt"], ["stamp", "CERRADO", 640, 480, -8, 150]]),
    dict(img="clearance_sale", zoom=1.1, cx=0.5, shade=["left", 160, 1.2], items=[
        ["text", 640, 110, "$4.400.000.000", 140, "yellow", "mt"], ["arrow", 605, 290, 70, 150], ["text", 640, 460, "$81M", 200, "red", "mt"]]),
    dict(img="design_copy", zoom=1.05, cx=0.5, shade=["left", 220, 0.7], items=[
        ["text", 50, 60, "DEMANDADA", 140, "white", "la"], ["text", 50, 220, "+50", 300, "red", "la"], ["text", 50, 530, "VECES POR COPIAR", 90, "white", "la"]]),
    dict(img="store_closed", zoom=1.2, cx=0.4, shade=["right", 220, 0.65], items=[
        ["text", 1230, 70, "CERRÓ", 190, "red", "ra"], ["text", 1230, 280, "TODAS SUS", 130, "white", "ra"], ["text", 1230, 430, "TIENDAS", 150, "white", "ra"], ["badge", 60, 540, 470, 680, "EE. UU.", 110]]),
    dict(img="times_square", zoom=1.05, cx=0.5, shade=["left", 200, 0.7], items=[
        ["text", 50, 80, "EL IMPERIO", 150, "white", "la"], ["text", 50, 250, "QUE SE HUNDIÓ", 130, "yellow", "la"], ["text", 50, 420, "2 VECES", 190, "red", "la"]]),
]
THUMBS_TOP = [1, 2, 5]

META = {
    "code": "002",
    "name": "Forever 21",
    "intro_chapter": "Intro: de 4.400 millones a 81",
    "titles": [
        "Forever 21: de vender 4.400 MILLONES a venderse por 81",
        "¿Qué le pasó a FOREVER 21? La historia de sus dos quiebras",
        "Cómo Forever 21 pasó de 5.900 millones a la RUINA",
    ],
    "description": "En 2015, Forever 21 vendía 4.400 millones de dólares al año y sus fundadores tenían una fortuna de 5.900 millones. Cinco años después, la empresa entera se vendió por 81 millones, y en 2025 cerró todas sus tiendas en Estados Unidos. Esta es la historia del inmigrante que limpiaba oficinas y construyó un imperio de la moda rápida… y de cómo ese imperio se hundió dos veces.",
    "sources": [
        "Forbes (vía Business Insider): ventas de 4.400 M$ en 2015 y fortuna de 5.900 M$ de los Chang",
        "Expediente de quiebra de 2019 (vía Retail Dive) y NPR: cierres de tiendas y venta por ~81 M$ (feb-2020)",
        "CNBC y Knowledge at Wharton: por qué quebró Forever 21",
        "Reuters / Retail Gazette: acuerdo entre Shein y SPARC Group (agosto 2023)",
        "Axios / NBC News: segunda quiebra y cierre de 354 tiendas en EE. UU. (marzo 2025)",
        "The Fashion Law: historial de demandas por copia de diseños",
    ],
    "hashtags": "#Forever21 #Shein #ModaRápida #Negocios #Empresas",
    "tags": ["forever 21", "qué le pasó a forever 21", "forever 21 quiebra", "la caída de forever 21", "forever 21 shein",
             "moda rápida", "fast fashion", "shein", "temu", "historia de empresas", "empresas que quebraron", "auge y caída",
             "negocios", "el último balance"],
    "pinned": "¿Alguna vez compraste en Forever 21? 👇 Y dime qué marca quieres que analicemos en el próximo vídeo.",
    "playlist": "Quiebras y caídas",
    "shorts": {
        "a": {"title": "De limpiar oficinas a 5.900 millones… y a la ruina: Forever 21",
              "description": "La historia completa de Forever 21 está en el canal. #Forever21 #negocios #historia #shorts",
              "tags": ["forever 21", "negocios", "historia de empresas", "emprendimiento", "shorts"]},
        "b": {"title": "La tienda demandada más de 50 veces por copiar",
              "description": "Cómo terminó Forever 21: vídeo completo en el canal. #Forever21 #moda #shorts",
              "tags": ["forever 21", "moda rápida", "copias", "ariana grande", "shorts"]},
        "c": {"title": "Forever 21 se alió con Shein… y quebró",
              "description": "La historia completa en el canal. #Forever21 #Shein #negocios #shorts",
              "tags": ["forever 21", "shein", "temu", "moda rápida", "shorts"]},
    },
}
