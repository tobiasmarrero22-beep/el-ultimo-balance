# Vídeo 011 — Stellantis: el gigante de Fiat, Peugeot, Citroën y Jeep que perdió 22.000 millones (guion del 15-nov-2026)
# Tema por datos (API de YouTube, 13 y 15-nov): EN "Stellantis Is Losing Everything" 3,31 M (Nimbus, oct-2026), 249 k; en español
# ningún vídeo largo (solo polaco, alemán, francés, portugués y noticias). Marcas muy conocidas en LatAm (criterio del 15-nov).
#
# Hechos verificados (WebSearch, 15-nov-2026):
# - Stellantis nace el 16-ene-2021 de la fusión de PSA (Peugeot, Citroën, Opel…) y FCA (Fiat, Chrysler, Jeep…): 14 marcas.
#   CEO Carlos Tavares, que antes había sacado a flote PSA y Opel.
# - 2023: beneficio neto récord de unos 18.600 M€. 2024: aviso de beneficios, ventas en caída en EE. UU.; beneficio neto 5.500 M€.
# - Tavares dimite el 1-dic-2024 por «diferentes puntos de vista» con el consejo (Stellantis); según Reuters, al consejo le preocupaba
#   que sus recortes de costes estuvieran afectando a la calidad y a los nuevos modelos.
# - 6-feb-2026: anuncia 22.200 M€ en cargos; la acción cae hasta un 25 % en Milán. 26-feb-2026: pérdida neta de 2025 de unos
#   22.300 M€, la primera pérdida anual de su historia; sin dividendo. Antonio Filosa (CEO desde 2025): sobrestimaron el ritmo de la
#   transición eléctrica y hubo problemas de calidad ligados a los recortes de la etapa anterior.
# - Jeep cortó en el 4.º trimestre de 2025 una racha de seis años de ventas en caída en EE. UU. (+4 %). Aranceles: 1.600 M€ en 2026.
# - Sudamérica 2025 (informe anual 20-F): 22,6 % del mercado; 29,3 % en Brasil y 30,5 % en Argentina; Fiat, marca líder.
#   Argentina: planta de Ferreyra (Córdoba: Fiat Cronos, Fiat Titano, Ram Dakota) y El Palomar (Buenos Aires: Peugeot 208 y 2008,
#   primeros autos electrificados de exportación del país). Filosa fue presidente de Stellantis para Sudamérica.
VOICE = "i4Kar2uamCWyas8TAu31"  # Adán
SPEED = 1.0

# Fotos reales (Wikimedia Commons, solo dominio público / CC0 / CC BY, con crédito)
IMAGES = {
    "fiat_strada": "Fiat Strada (foto real, Wikimedia Commons)", "jeep_wrangler": "Jeep Wrangler (foto real)",
    "peugeot_208": "Peugeot 208 (foto real)", "citroen_c3": "Citroën C3 (foto real)", "fiat_500": "Fiat 500 (foto real)",
    "car_factory": "Línea de montaje de autos (foto real)", "car_lot": "Playa de autos sin vender (foto real)",
    "tavares": "Carlos Tavares (foto real)", "ram_truck": "Ram 1500 (foto real)", "turin_lingotto": "Lingotto, Turín (foto real)",
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
    dict(id="s01", text="En Argentina, casi uno de cada tres autos nuevos que se venden es de la misma empresa. En Brasil, también.",
         visual=dict(type="num", start=0, end=30.5, dec=1, suffix=" %", label="AUTOS NUEVOS EN ARGENTINA DE UNA SOLA EMPRESA (2025)")),
    dict(id="s02", text="Esa empresa se llama Stellantis. Fiat, Peugeot, Citroën, Jeep, Ram… catorce marcas bajo el mismo techo.",
         visual=I("fiat_strada", pop=["14 MARCAS"])),
    dict(id="s03", text="Y en dos mil veinticinco perdió más de veintidós mil millones de euros. La primera pérdida anual de toda su historia.",
         visual=dict(type="num", start=0, end=-22300, prefix="", suffix=" M€", label="RESULTADO NETO DE STELLANTIS EN 2025")),
    dict(id="s04", text="¿Cómo pasa una empresa de batir récords a perder todo eso en solo dos años? Y lo más raro: mientras se hundía en medio mundo, en Sudamérica seguía siendo la reina.",
         visual=I("car_lot", pop=["DEL RÉCORD AL AGUJERO"]), abre="P1: ¿Cómo pasó Stellantis de los récords a la mayor pérdida de su historia?"),

    # --- 01 LA BODA ---
    dict(id="s05", text="Capítulo uno: la boda del siglo.", bloque="desarrollo", visual=T("01", "La boda del siglo")),
    dict(id="s06", text="Enero de dos mil veintiuno. Dos grupos gigantes se unen: el francés PSA, el de Peugeot y Citroën, y el ítalo-estadounidense FCA, el de Fiat, Chrysler y Jeep.",
         visual=dict(type="versus", title="16 DE ENERO DE 2021", left=["PSA", "PEUGEOT · CITROËN · OPEL"], right=["FCA", "FIAT · CHRYSLER · JEEP"], mid="+", lcol="yellow", rcol="yellow")),
    dict(id="s06b", text="FCA, a su vez, venía de otra historia increíble: Fiat se había quedado con Chrysler después de su quiebra en dos mil nueve.",
         visual=dict(type="year", year="2009", sub="FIAT SE QUEDA CON CHRYSLER")),
    dict(id="s06c", text="La fusión se hizo mitad y mitad: ninguno de los dos se comía al otro. Al menos sobre el papel.",
         visual=dict(type="versus", title="LA FUSIÓN", left=["PSA", "50 %"], right=["FCA", "50 %"], mid="=", lcol="yellow", rcol="yellow")),
    dict(id="s07", text="Nace Stellantis, uno de los mayores fabricantes de autos del mundo. Catorce marcas, de Fiat y Peugeot a Maserati y Alfa Romeo.",
         visual=dict(type="quote", text="ABARTH · ALFA ROMEO · CHRYSLER · CITROËN · DODGE\nDS · FIAT · JEEP · LANCIA · MASERATI\nOPEL · PEUGEOT · RAM · VAUXHALL")),
    dict(id="s07b", text="El nombre viene del latín: «stello», que significa iluminar con estrellas. La idea era que juntas, todas esas marcas brillaran más.",
         visual=dict(type="quote", text="STELLO\n«ILUMINAR CON ESTRELLAS»")),
    dict(id="s08", text="Al frente ponen a Carlos Tavares, un ejecutivo portugués con fama de mago de los números: antes había rescatado a Peugeot y a Opel cuando perdían dinero.",
         visual=I("tavares", cap="CARLOS TAVARES")),
    dict(id="s08b", text="En dos mil catorce, Peugeot estaba tan mal que el Estado francés y la china Dongfeng tuvieron que entrar en su capital. Tavares llegó ese año y la devolvió a las ganancias.",
         visual=dict(type="timeline", title="CARLOS TAVARES", points=[["2014", "Rescata a PSA (Peugeot)"], ["2017", "Compra Opel a GM"], ["2021", "Dirige Stellantis"]], hl=0)),
    dict(id="s08c", text="Después compró Opel, que llevaba casi veinte años perdiendo dinero con General Motors. Al año siguiente, Opel ya ganaba.",
         visual=dict(type="stamp", text="OPEL VUELVE\nA GANAR", stamp="2018", col="yellow")),
    dict(id="s09", text="Su receta era simple: recortar costes en todo lo que se pudiera y subir los márgenes. Y al principio funcionó de maravilla.",
         visual=I("car_factory", pop=["RECORTAR · RECORTAR · RECORTAR"])),

    # --- 02 LA MÁQUINA DE HACER DINERO ---
    dict(id="s10", text="Capítulo dos: la máquina de hacer dinero.", visual=T("02", "La máquina de hacer dinero")),
    dict(id="s11", text="En dos mil veintitrés, Stellantis gana unos dieciocho mil seiscientos millones de euros. Un récord.",
         visual=dict(type="bars", title="BENEFICIO NETO DE STELLANTIS (MILES DE MILLONES DE €)", data=[["2023", 18.6]], dec=1)),
    dict(id="s12", text="Buena parte venía de Estados Unidos: camionetas Ram y Jeep vendidas a precios cada vez más altos.",
         visual=I("ram_truck", pop=["PRECIOS CADA VEZ MÁS ALTOS"])),
    dict(id="s12b", text="Y Jeep tiene una marca con más de ochenta años de historia: nació como el todoterreno del ejército estadounidense en la Segunda Guerra Mundial.",
         visual=I("jeep_wrangler", cap="JEEP WRANGLER")),
    dict(id="s13", text="Los accionistas estaban felices. Pero dentro de la empresa, y en los concesionarios, algo empezaba a crujir.",
         visual=I("jeep_wrangler"), abre="P2: ¿Qué se estaba rompiendo detrás de los récords?"),
    dict(id="s14", text="Porque cuando subes tanto los precios y recortas tanto por dentro, tarde o temprano alguien deja de comprar.",
         visual=I("car_lot")),

    # --- 03 LAS GRIETAS ---
    dict(id="s15", text="Capítulo tres: las grietas.", visual=T("03", "Las grietas")),
    dict(id="s16", text="En dos mil veinticuatro, las ventas en Estados Unidos caen. Los concesionarios se llenan de autos sin vender y la empresa tiene que avisar a los inversores de que ganará mucho menos.",
         visual=I("car_lot", pop=["AUTOS SIN VENDER"])),
    dict(id="s16c", text="En septiembre de dos mil veinticuatro, los propios concesionarios de Estados Unidos le escribieron una carta abierta a la empresa criticando a Tavares por cómo iba el negocio.",
         visual=dict(type="headline", kicker="Septiembre de 2024", text="Los concesionarios de Stellantis en EE. UU. critican a Tavares en una carta abierta", mark="carta abierta", source="Fuente: prensa automotriz de EE. UU.")),
    dict(id="s16b", text="En Italia, la cuna de Fiat, la producción de Stellantis en dos mil veinticuatro cayó a su nivel más bajo desde mil novecientos cincuenta y seis, según el sindicato FIM-CISL.",
         visual=I("turin_lingotto", pop=["LO MÁS BAJO DESDE 1956"])),
    dict(id="s17", text="El beneficio de ese año se queda en unos cinco mil quinientos millones. Un setenta por ciento menos que el año anterior.",
         visual=dict(type="bars", title="BENEFICIO NETO (MILES DE MILLONES DE €)", data=[["2023", 18.6], ["2024", 5.5]], dec=1)),
    dict(id="s18", text="Y el uno de diciembre de dos mil veinticuatro, Carlos Tavares deja la empresa. Stellantis habló de «puntos de vista diferentes» con el consejo.",
         visual=dict(type="headline", kicker="1 de diciembre de 2024", text="Carlos Tavares deja Stellantis por diferencias con el consejo", mark="deja", source="Fuente: Stellantis / Reuters")),
    dict(id="s19", text="Según Reuters, al consejo le preocupaba que tantos recortes estuvieran afectando a la calidad de los autos y a la llegada de modelos nuevos.",
         visual=I("car_factory", pop=["¿DEMASIADOS RECORTES?"]), cierra="P2"),
    dict(id="s20", text="Pero la verdadera factura de esos años todavía no había llegado. Y cuando llegó, fue la más grande de su historia.",
         visual=I("turin_lingotto"), abre="P3: ¿De cuánto fue la factura que faltaba?"),

    # --- 04 EL AGUJERO ---
    dict(id="s21", text="Capítulo cuatro: el agujero.", visual=T("04", "El agujero")),
    dict(id="s22", text="Seis de febrero de dos mil veintiséis. Stellantis anuncia cargos por veintidós mil doscientos millones de euros. Ese día, su acción llega a caer un veinticinco por ciento en la bolsa de Milán.",
         visual=dict(type="headline", kicker="6 de febrero de 2026", text="Stellantis anuncia cargos por 22.200 millones y se desploma en bolsa", mark="se desploma", source="Fuente: Bloomberg / Reuters")),
    dict(id="s22b", text="¿De dónde salía semejante cifra? Sobre todo de planes de autos eléctricos que ya no iban a dar lo que se esperaba.",
         visual=I("peugeot_208", pop=["PLANES ELÉCTRICOS"])),
    dict(id="s23", text="A fin de mes llegan las cuentas: una pérdida neta de unos veintidós mil trescientos millones de euros en dos mil veinticinco. La primera pérdida anual desde que existe la empresa.",
         visual=dict(type="bars", title="RESULTADO NETO (MILES DE MILLONES DE €)", data=[["2023", 18.6], ["2024", 5.5], ["2025", -22.3]], dec=1), cierra="P3"),
    dict(id="s24", text="Y ese año, ni un euro de dividendo para los accionistas.",
         visual=dict(type="stamp", text="SIN DIVIDENDO", stamp="2025", col="red"), abre="P4: ¿Por qué en Sudamérica seguía ganando?"),
    dict(id="s25", text="¿La explicación oficial? El nuevo jefe, Antonio Filosa, dijo que habían sobrestimado lo rápido que la gente iba a pasarse al auto eléctrico.",
         visual=I("peugeot_208", pop=["SOBRESTIMARON EL ELÉCTRICO"]), cierra="P1"),
    dict(id="s25b", text="Mientras tanto, desde abril de dos mil veinticinco, Estados Unidos cobraba aranceles del veinticinco por ciento a los autos importados. Otro golpe para una empresa que fabrica en medio mundo.",
         visual=dict(type="num", start=0, end=25, suffix=" %", label="ARANCEL DE EE. UU. A LOS AUTOS IMPORTADOS (2025)")),
    dict(id="s26", text="Y reconoció problemas de calidad que vinculó a los recortes de la etapa anterior. O sea: la receta que había hecho ganar récords también explicaba parte del agujero.",
         visual=dict(type="versus", title="LA RECETA", left=["RECORTES", "RÉCORDS EN 2023"], right=["RECORTES", "PROBLEMAS DE CALIDAD"], mid="→", lcol="yellow", rcol="red")),
    dict(id="s27", text="Ahora, la parte que casi nadie cuenta: mientras todo eso pasaba en Europa y Estados Unidos, en Sudamérica la empresa seguía arrasando.",
         visual=I("fiat_strada")),

    # --- 05 LA EXCEPCIÓN SUDAMERICANA ---
    dict(id="s28", text="Capítulo cinco: la excepción sudamericana.", visual=T("05", "La excepción sudamericana")),
    dict(id="s29", text="En dos mil veinticinco, Stellantis vendió casi uno de cada cuatro autos nuevos de Sudamérica. En Brasil, el veintinueve por ciento. En Argentina, el treinta y medio.",
         visual=dict(type="bars", title="CUOTA DE MERCADO DE STELLANTIS EN 2025 (%)", data=[["SUDAMÉRICA", 22.6], ["BRASIL", 29.3], ["ARGENTINA", 30.5]], dec=1)),
    dict(id="s30", text="Fiat es la marca líder de la región. En Brasil, camionetas como la Strada, la Toro y la Titano dominan el mercado de las pick-ups.",
         visual=I("fiat_strada", cap="FIAT STRADA")),
    dict(id="s30b", text="La Strada, una pick-up chica fabricada en Brasil, fue durante varios años seguidos el vehículo más vendido de ese país.",
         visual=I("fiat_strada", pop=["LA MÁS VENDIDA DE BRASIL"])),
    dict(id="s31", text="Y en Argentina tiene dos fábricas: en Ferreyra, Córdoba, salen el Fiat Cronos, la Titano y la Ram Dakota. En El Palomar, Buenos Aires, los Peugeot 208 y 2008.",
         visual=dict(type="route", title="STELLANTIS EN ARGENTINA", points={"FERREYRA (CÓRDOBA)": [0.36, 0.42], "EL PALOMAR (BS. AS.)": [0.62, 0.62]}, routes=[["FERREYRA (CÓRDOBA)", "EL PALOMAR (BS. AS.)"]])),
    dict(id="s31b", text="Solo en dos mil veinticinco, la planta de Córdoba sumó unos mil ochocientos trabajadores y se convirtió en un centro de pick-ups para toda la región.",
         visual=dict(type="num", start=0, end=1800, prefix="+", label="TRABAJADORES NUEVOS EN FERREYRA (2025)")),
    dict(id="s32", text="De El Palomar salieron incluso los primeros autos electrificados que Argentina fabricó para exportar: los Peugeot 208 y 2008 híbridos.",
         visual=I("peugeot_208", cap="PEUGEOT 208")),
    dict(id="s32b", text="Según la propia empresa, en dos mil veinticinco superó el millón de vehículos vendidos en Sudamérica.",
         visual=dict(type="num", start=0, end=1000000, prefix="+", label="VEHÍCULOS VENDIDOS EN SUDAMÉRICA (2025)")),
    dict(id="s33", text="¿Por qué allá sí? Una pista: en la región vende autos accesibles y populares, justo lo que el mercado pide. Y otra pista, todavía más curiosa: quién es el nuevo jefe.",
         visual=I("fiat_500", pop=["AUTOS ACCESIBLES"]), cierra="P4", abre="P5: ¿Quién es el nuevo jefe y por qué importa?"),

    # --- 06 ¿Y AHORA? ---
    dict(id="s34", text="Capítulo seis: ¿y ahora?", visual=T("06", "¿Y ahora?")),
    dict(id="s35", text="Antonio Filosa, el italiano que tomó el mando en dos mil veinticinco, fue presidente de Stellantis para Sudamérica antes de dirigir Jeep.",
         visual=dict(type="timeline", title="ANTONIO FILOSA", points=[["SUDAMÉRICA", "Presidente de la región"], ["JEEP", "CEO de la marca"], ["2025", "CEO de Stellantis"]], hl=2), cierra="P5", abre="P6: ¿Le alcanzará todo eso para salvarse?"),
    dict(id="s36", text="O sea: el hombre que tiene que salvar al gigante viene justo de la única región donde nunca dejó de ganar.",
         visual=I("fiat_strada", pop=["DE SUDAMÉRICA AL MANDO"])),
    dict(id="s37", text="Y hay alguna señal: a fines de dos mil veinticinco, Jeep cortó una racha de seis años seguidos de ventas en caída en Estados Unidos.",
         visual=I("jeep_wrangler", pop=["+4 % (4.º TRIMESTRE 2025)"])),
    dict(id="s37b", text="Además, en dos mil veintitrés Stellantis compró alrededor del veintiuno por ciento de Leapmotor, un fabricante chino de autos eléctricos, para vender sus modelos fuera de China.",
         visual=dict(type="versus", title="LA APUESTA CHINA", left=["STELLANTIS", "~21 %"], right=["LEAPMOTOR", "ELÉCTRICOS CHINOS"], mid="→", lcol="yellow", rcol="yellow"),
),
    dict(id="s38", text="Pero el camino es largo. Solo por los aranceles de Estados Unidos, la empresa calcula un golpe de unos mil seiscientos millones de euros en dos mil veintiséis.",
         visual=dict(type="num", start=0, end=1600, suffix=" M€", label="IMPACTO ESTIMADO DE LOS ARANCELES EN 2026")),
    dict(id="s39", text="Filosa lo resumió así: este año, el objetivo es cerrar las brechas de ejecución del pasado. En otras palabras: arreglar lo que se rompió.",
         visual=dict(type="quote", text="«CERRAR LAS BRECHAS\nDE EJECUCIÓN DEL PASADO»")),

    # --- CIERRE ---
    dict(id="s40", text="Así que la próxima vez que veas un Fiat, un Peugeot o un Jeep por la calle, acuérdate: es de una empresa que perdió veintidós mil millones en un año. ¿Se salvará? Todavía nadie lo sabe.", bloque="cierre", cierra="P6",
         visual=I("car_lot")),
    dict(id="s41", text="Y que, aun así, en Argentina y en Brasil sigue vendiendo casi uno de cada tres autos.",
         visual=dict(type="num", start=0, end=30.5, dec=1, suffix=" %", label="CUOTA EN ARGENTINA (2025)")),
    dict(id="s42", text="¿Tú tienes o tuviste un auto de alguna de sus catorce marcas? Cuéntamelo en los comentarios.",
         visual=I("fiat_500")),
    dict(id="s43", text="Y si te gustan estas historias de empresas que suben y caen, suscríbete: cada semana, un nuevo balance.",
         visual=I("turin_lingotto")),
]

FALLBACK = {
    "s02": dict(type="quote", text="FIAT · PEUGEOT · CITROËN\nJEEP · RAM · 14 MARCAS"),
    "s04": dict(type="stamp", text="DEL RÉCORD\nAL AGUJERO", stamp="STELLANTIS", col="red"),
    "s08": dict(type="quote", text="CARLOS TAVARES\nRESCATÓ A PEUGEOT Y A OPEL"),
    "s09": dict(type="quote", text="RECORTAR COSTES\nSUBIR MÁRGENES"),
    "s12": dict(type="quote", text="RAM · JEEP\nPRECIOS CADA VEZ MÁS ALTOS"),
    "s13": dict(type="stamp", text="ALGO CRUJE", stamp="2023", col="yellow"),
    "s14": dict(type="quote", text="PRECIOS ↑\nCALIDAD ↓"),
    "s16": dict(type="stamp", text="AUTOS SIN VENDER", stamp="2024", col="red"),
    "s19": dict(type="quote", text="¿DEMASIADOS RECORTES?"),
    "s20": dict(type="stamp", text="LA FACTURA", stamp="2026", col="red"),
    "s25": dict(type="quote", text="«SOBRESTIMAMOS\nLA TRANSICIÓN ELÉCTRICA»"),
    "s27": dict(type="stamp", text="EXCEPTO EN\nSUDAMÉRICA", stamp="2025", col="yellow"),
    "s30": dict(type="quote", text="FIAT: MARCA LÍDER\nEN SUDAMÉRICA"),
    "s32": dict(type="quote", text="PEUGEOT 208 Y 2008\nHÍBRIDOS · HECHOS EN ARGENTINA"),
    "s33": dict(type="quote", text="AUTOS ACCESIBLES\nY POPULARES"),
    "s36": dict(type="quote", text="DE SUDAMÉRICA\nAL MANDO"),
    "s37": dict(type="num", start=0, end=4, prefix="+", suffix=" %", label="VENTAS DE JEEP EN EE. UU. (4.º TRIMESTRE 2025)"),
    "s40": dict(type="num", start=0, end=-22300, suffix=" M€", label="RESULTADO NETO 2025"),
    "s42": dict(type="quote", text="¿TIENES UN AUTO\nDE STELLANTIS?"),
    "s43": dict(type="quote", text="SUSCRÍBETE\nCADA SEMANA, UN NUEVO BALANCE"),
    "s12b": dict(type="year", year="1941", sub="JEEP NACE COMO VEHÍCULO MILITAR"),
    "s16b": dict(type="num", start=0, end=1956, label="PRODUCCIÓN EN ITALIA: LA MÁS BAJA DESDE"),
    "s22b": dict(type="quote", text="PLANES ELÉCTRICOS\nQUE NO IBAN A RENDIR"),
    "s30b": dict(type="quote", text="FIAT STRADA\nLA MÁS VENDIDA DE BRASIL"),
}

PRONUNCIA = {"Stellantis": "Estelántis", "Citroën": "Citroén", "Jeep": "Yip", "Ram": "Ram", "Chrysler": "Cráisler", "Opel": "Ópel",
             "Maserati": "Maserati", "Tavares": "Tavares", "Filosa": "Filósa", "Reuters": "Róiters", "Strada": "Strada",
             "pick-ups": "picaps", "Titano": "Titano", "Dakota": "Dakóta", "Cronos": "Cronos", "Dongfeng": "Dongféng", "General Motors": "Yeneral Mótors", "Leapmotor": "Lipmótor", "FIM-CISL": "fim chisl", "Lingotto": "Lingotto"}

SHORTS = {
    "a": {"bar": "1 DE CADA 3 AUTOS", "scenes": [
        dict(id="a01", text="En Argentina, casi uno de cada tres autos nuevos es de la misma empresa.", key="fiat_strada"),
        dict(id="a02", text="Fiat, Peugeot, Citroën, Jeep… todas son de Stellantis.", key="peugeot_208"),
        dict(id="a03", text="Y en dos mil veinticinco perdió más de veintidós mil millones de euros.", key="car_lot"),
        dict(id="a04", text="¿Cómo? La historia completa, en el vídeo del canal.", key="car_factory"),
    ]},
    "b": {"bar": "EL MAGO DE LOS NÚMEROS", "scenes": [
        dict(id="b01", text="Este hombre rescató a Peugeot y a Opel cuando perdían dinero.", key="tavares"),
        dict(id="b02", text="Le dieron catorce marcas, y en dos mil veintitrés ganó un récord de dieciocho mil millones.", key="car_factory"),
        dict(id="b03", text="Un año después se fue. Y la empresa perdió veintidós mil millones.", key="car_lot"),
        dict(id="b04", text="Lo que pasó en el medio, en el vídeo del canal.", key="jeep_wrangler"),
    ]},
}
FALLBACK.update({
    "a01": dict(type="num", start=0, end=30.5, dec=1, suffix=" %", label="ARGENTINA"), "a02": dict(type="quote", text="FIAT · PEUGEOT\nCITROËN · JEEP"),
    "a03": dict(type="num", start=0, end=-22300, suffix=" M€", label="2025"), "a04": dict(type="quote", text="LA HISTORIA COMPLETA\nEN EL CANAL 👆"),
    "b01": dict(type="quote", text="RESCATÓ A\nPEUGEOT Y OPEL"), "b02": dict(type="num", start=0, end=18600, suffix=" M€", label="RÉCORD 2023"),
    "b03": dict(type="num", start=0, end=-22300, suffix=" M€", label="2025"), "b04": dict(type="quote", text="LA HISTORIA COMPLETA\nEN EL CANAL 👆"),
})

THUMBS = []  # se definen al tener las fotos
THUMBS_TOP = []

META = {
    "code": "011",
    "name": "Stellantis",
    "intro_chapter": "Uno de cada tres autos",
    "titles": [
        "Fiat, Peugeot y Jeep: el gigante que perdió 22.000 millones (y sigue reinando en Argentina)",
        "Stellantis: de ganar récords a la mayor pérdida de su historia",
        "La empresa que vende 1 de cada 3 autos en Argentina… y perdió 22.000 millones",
    ],
    "description": "Fiat, Peugeot, Citroën, Jeep y Ram son de la misma empresa: Stellantis. En 2023 ganó un récord de 18.600 millones de euros; en 2025 perdió más de 22.000 millones, la primera pérdida anual de su historia. Y mientras tanto, en Argentina y Brasil sigue vendiendo casi uno de cada tres autos. Cómo pasó todo eso, qué tuvo que ver Carlos Tavares y quién es el hombre de Sudamérica que ahora tiene que salvarla.",
    "sources": [
        "Stellantis: fusión de PSA y FCA (16-ene-2021) y resultados anuales 2023, 2024 y 2025",
        "Stellantis / Reuters / NBC News (dic-2024): dimisión de Carlos Tavares",
        "Bloomberg / The Star / RTÉ (feb-2026): cargos de 22.200 M€, caída en bolsa y pérdida neta de 2025",
        "Stellantis, informe anual 20-F 2025 (SEC): cuota de mercado en Sudamérica, Brasil y Argentina",
        "Perfil / El Cronista / iProfesional (2025-2026): plantas de Ferreyra y El Palomar",
        "Stellantis / Bloomberg Línea: biografía de Antonio Filosa",
    ],
    "disclosure": "Fotos reales de Wikimedia Commons (créditos en las fuentes). Narración con voz sintética.",
    "altered": "No",
    "hashtags": "#Stellantis #Fiat #Peugeot #Jeep",
    "tags": ["stellantis", "fiat", "peugeot", "citroën", "jeep", "ram", "carlos tavares", "stellantis argentina", "stellantis brasil",
             "industria automotriz", "historia de empresas", "negocios", "el último balance"],
    "pinned": "¿Tienes o tuviste un auto de alguna de sus 14 marcas? 🚗 Cuéntamelo 👇",
    "playlist": "Auges y caídas",
    "category": "Educación",
    "shorts": {
        "a": {"title": "1 de cada 3 autos en Argentina es de esta empresa… y perdió 22.000 millones",
              "description": "Fiat, Peugeot, Citroën y Jeep son de Stellantis. La historia completa en el canal.\nFuentes: Stellantis (20-F 2025, resultados 2025).\n#Stellantis #Fiat #Argentina #shorts",
              "tags": ["stellantis", "fiat", "peugeot", "argentina", "autos", "shorts"]},
        "b": {"title": "Rescató a Peugeot… y un año después de irse, su empresa perdió 22.000 millones",
              "description": "Carlos Tavares y Stellantis: del récord de 2023 a la pérdida de 2025. La historia completa en el canal.\nFuentes: Stellantis, Reuters.\n#Stellantis #Peugeot #Jeep #shorts",
              "tags": ["stellantis", "carlos tavares", "peugeot", "jeep", "autos", "shorts"]},
    },
}
