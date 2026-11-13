# El Último Balance — instrucciones para Claude

Canal de YouTube en español: historias de empresas (auge y caída). Vídeos largos de 8–10 min + 2–3 Shorts por vídeo.
El usuario **sube los vídeos y contesta comentarios**; Claude **investiga, escribe, produce y entrega el paquete de subida**.
Idioma de trabajo con el usuario: español. Público: hispanohablante (LatAm + España), español neutro, "tú".

## Reglas fijas de guion (pedido del usuario, 13-nov-2026, para TODOS los canales: El Último Balance, 70x7 y Anacron)
1. **Gancho fuerte en los primeros segundos:** qué va a ver el espectador, por qué le importa y por qué quedarse.
2. **Estructura fija por bloques:** GANCHO → DESARROLLO → CIERRE (en guion.py: `bloque="desarrollo"` y `bloque="cierre"`
   en la primera escena de cada bloque; el desarrollo va por capítulos `type="title"`).
3. **Preguntas abiertas:** dudas que no se resuelven en el momento, sino más adelante (`abre="P1: ¿...?"` / `cierra="P1"`).
4. **Regla de oro:** cuando se cierra una pregunta, se abre otra; el espectador nunca piensa «ya me puedo ir».
5. **Sin saludos ni relleno:** nada de «hola», «bienvenidos», «en este vídeo»; el gancho arranca en el segundo 0 contando
   la historia. Suscribirse, solo en el cierre.
6. **Primero el guion, después el vídeo:** `python3 pipeline/guion_md.py videos/NNN` → `guion_revision.md` (bloques, minuto de
   cada escena, preguntas abiertas y comprobación automática). Corregir los ⚠️, enviarlo al usuario y **esperar su OK** antes de
   la voz y las imágenes (pasos 4 en adelante).

## Reglas anti-desmonetización (pedido del usuario, 13-nov-2026, para TODOS los canales)
YouTube no castiga usar IA: castiga el contenido «no auténtico» (hecho en serie, con plantilla, casi igual entre vídeos) y el
«reutilizado» (material ajeno sin aportar nada). La sanción es para el canal entero. Por eso, siempre:
1. **Guion original e investigado** en cada vídeo, con datos verificados y **fuentes citadas** en la descripción
   (`META["sources"]` / `youtube.sources`). Nada de texto genérico.
2. **Variedad obligatoria:** cada vídeo distinto de los anteriores en enfoque, tipo de gancho, estructura y recursos visuales.
   No repetir la misma plantilla en vídeos seguidos ni crear canales casi iguales.
3. **Nada de material ajeno sin transformación:** tráilers, gameplays, clips o fotos de otros solo como apoyo breve y siempre con
   análisis o comentario propio encima (la regla aplica aunque haya permiso). Preferir material propio, dominio público o
   licencias libres con crédito.
4. **Aviso de IA:** «Contenido alterado o sintético: Sí» cuando haya imágenes o voz realistas que puedan confundirse con personas,
   lugares o hechos reales, y el aviso en la descripción (`META["disclosure"]`).
5. **Calidad antes que cantidad:** ritmo de subida razonable; nada de ráfagas ni de muchos Shorts iguales al día.
6. **Nunca** un personaje o voz de IA presentado como experto humano en salud, finanzas, temas legales o política.
7. **Rastro del trabajo humano:** guion revisado con el usuario (regla de guion 6) y guion, fuentes e historial en el repo. Si
   llega una desmonetización, hay 21 días para apelar y esto es la prueba.

## Flujo de un vídeo (carpeta `videos/NNN-slug/`)
1. **Tema**: elegir con datos (`pipeline/ytlib.py`, API de YouTube con la clave inyectada por el proxy;
   100 búsquedas/día, se renueva a medianoche hora del Pacífico). Criterio: mucho público en inglés en los
   últimos meses + poco o nada en español. Backlog en `datos/ideas.md`.
2. **Hechos**: verificar con WebSearch (cuentas anuales, comunicados, prensa). No afirmar nada no verificado.
   Evitar acusaciones no probadas a empresas o personas.
3. **Guion** `guion.py` (copiar la estructura de `videos/001-roomba/guion.py`):
   - Gancho en los primeros 3 s con la cifra más fuerte; adelantar el giro final ("el último llegó desde…").
   - Capítulos (`type="title"`, con `name` en minúsculas correctas), un cambio visual cada 5–10 s.
   - Números escritos en palabras en el texto narrado (TTS). ~6.500–7.500 caracteres ≈ 8–9 min.
   - `IMAGES` (prompts, terminar con "no text, no logos"), `SHORTS` (2–3, ~45 s, gancho distinto cada uno),
     `THUMBS` (10 variantes) + `THUMBS_TOP`, `META` (títulos, descripción, fuentes, etiquetas, comentario fijado).
   - **Duración mínima 8:00** (anuncios a mitad de vídeo).
3b. **Revisión del guion con el usuario** (regla 6): `python3 pipeline/guion_md.py videos/NNN`, enviar `guion_revision.md` y
   esperar el OK (o aplicar los cambios que pida) antes de seguir.
4. `python3 pipeline/tts.py videos/NNN` → voz (DubVoice, 1 crédito/carácter). Revisar duraciones: si una escena
   dura mucho más de lo esperado (<10 caracteres/s), regenerarla (Fish Audio a veces añade audio de más).
5. `python3 pipeline/img.py videos/NNN` → imágenes (nano-banana-2-lite, 500 cr). **No reintentar a ciegas**:
   los 502 "upstream request failed" de DubVoice se cobran igual. Si fallan, sustituir por escenas de código
   (quote/num/year/bars) o reutilizar imágenes.
5b. (Opcional, vídeos "premium") `python3 pipeline/vid.py videos/NNN` → clips de vídeo IA desde las imágenes
   (`CLIPS` en guion.py; Meta AI 2.000 cr/clip, DubVoice devuelve los créditos si falla). Si existe `clips/<clave>.mp4`,
   el render usa el clip en lugar de la foto con zoom (también en los Shorts).
5c. (Opcional) Música IA: `POST /api/music-generate` (5.000 cr, 2 pistas) → `music/*.mp3`; si existe, sustituye al fondo sintético.
   Si faltan imágenes, `FALLBACK = {id_escena: visual}` en guion.py las sustituye por escenas de código
   (también `versus` y `stamp`); thumbs.py usa un fondo sintético.
6. `python3 pipeline/render.py videos/NNN long` y `... short a|b|c|d|e` → `build/` (no se sube a git).
   El render añade transición de entrada en cada escena, whoosh/golpes de sonido y la gráfica `type="lines"`.
   Desde el 004 (análisis de YouTube: "la imagen apenas cambia"): las fotos cortan a otro encuadre cada ~4 s y los gráficos
   llevan detrás la foto anterior desenfocada en movimiento + un acercamiento lento (`BG_BROLL = False` en guion.py lo apaga).
   Fotogramas casi iguales al anterior (1 por segundo): 46 % → 3 %. Ojo: la caché de escenas (`.sig`) no detecta cambios
   de código: borrar `build/sNN.mp4` al cambiar el render. `CRF=27 MAXRATE=3000k` en el render deja el largo < 90 MB.
   Títulos: dejar algo por descubrir (no revelar el detalle clave; que lo enseñe la miniatura). Publicar los lunes.
7. `python3 pipeline/thumbs.py videos/NNN` → 10 miniaturas + TOP1-3. Revisar la hoja a tamaño móvil.
8. `python3 pipeline/meta.py videos/NNN` → `entrega/SUBIR.md`, SRT y copia de los mp4 a `entrega/`.
9. Enviar al usuario: mp4 (largo + Shorts), TOP1-3, SUBIR.md, SRT. Commit sin mp4/wav. Anotar en `produccion.md`.

## Servicios y costes
- DubVoice (`www.dubvoice.ai`, clave inyectada por el proxy): voz Fish Audio `fishaudio_a48e73d4fb124c689357e88b04c9db30`
  ("Narrador Cálido Español", velocidad 1.05). ElevenLabs falló el 2026-11-01. Coste típico por vídeo:
  ~8.000 (voz) + ~5.000 (10 imágenes) + ~2.000 (Shorts) ≈ 15.000 créditos. Saldo: `GET /api/v1/me`.
- vidIQ (MCP): 5 créditos por consulta; plan gratis 150/mes. Usar solo para lo que no da la API de YouTube.
- Fallos de DubVoice (2026-11-01): imágenes nano-banana devuelven 502 y se cobran (a veces se reembolsan más tarde);
  google-pics, grok-image, vídeo y música devuelven 500 y **sí** reembolsan → para reintentar, usar esos modelos.
  ElevenLabs: la voz "Adán - Narration" (`i4Kar2uamCWyas8TAu31`, latinoamericana) funciona; "Abel" falló.
- Higgsfield (MCP): imágenes `z_image` a 0,15 créditos (16:9, 2048×1152). Su CDN (`d8j0ntlcm91z4.cloudfront.net`) está
  bloqueado en este entorno. Ruta que funciona (003): generar con `generate_image_batch`, y en `sandbox_exec` (size xl,
  4 CPU) clonar el repo público, bajar las imágenes a `img/`, correr render/thumbs/meta y subir los resultados con
  `media_upload` + `curl -X PUT -H "If-None-Match: *"` + `media_confirm` → enlaces `d2ol7oe51mr4n9.cloudfront.net` para el
  usuario. Límite de subida ~90 MB por archivo (98 MB da 400): recodificar el largo con crf 24 / maxrate 3500k (~87 MB).
  Las llamadas al sandbox cortan a los 60 s: usar background y sondear con sleep ≤ 55. Si el largo pasa de ~90 MB con crf 24,
  usar crf 27 / maxrate 3000k (004: 67 MB). Guardar las URL de las imágenes en `videos/NNN/img_urls.txt`.
- Fórmula ganadora de Shorts (datos 3-nov, `datos/rendimiento.md`): personaje + cifra enorme + conflicto
  ("Empezó haciendo baterías de móvil… hoy supera a Tesla", "Musk se rió…"). El largo abre "en plena acción" y adelanta el giro.
- **Tomas de vídeo reales con vidIQ (005, la vía preferida):** `vidiq_generate_broll` (1 crédito, Pexels; elegir MP4 hd 1280/1920)
  → `vidiq_video_upload` con esa URL (gratis; devuelve un `videoUrl` en storage.googleapis.com, que SÍ se descarga aquí)
  (008: para tener HD/4K, pasar a `vidiq_video_upload` la URL `https://www.pexels.com/download/video/<id>/` en vez del MP4 de 640×360)
  → `pipeline/getclip.sh <clave> <videoUrl>` deja `clips/<clave>.mp4` (1080p, sin audio) e `img/<clave>.png`. Las escenas
  `img` usan el clip; cada escena arranca en un tramo distinto. Guardar elecciones y créditos en `videos/NNN/broll.json` y
  acreditar a los autores en las fuentes. `META["disclosure"]` cambia el aviso (no son imágenes de IA).
- **Imágenes con vidIQ (007, la vía preferida desde el 7-nov):** `vidiq_generate_thumbnail` con `userQuery` "Photorealistic cinematic
  documentary still, NOT a thumbnail: … Absolutely no text, no words… Wide 16:9 movie frame" → 1280×720 realista y sin texto,
  22 créditos de vidIQ (se reembolsan si falla). Máximo ~10 trabajos a la vez; `vidiq_job_poll` → `imageUrl` en
  ai-thumbnails.s3.amazonaws.com (se descarga aquí); reescalar a 1920×1080 y guardar en `img/`; URLs en `img_urls.txt`.
  DubVoice nano-banana-2-lite volvió el 7-nov pero falla ~45 % con 502 y **cobra** los fallos (2.500 cr perdidos en el 007).
  **11-nov: NO probar otros modelos de imagen de DubVoice.** google-pics y gpt-image-2 dieron 502 y cobraron 1.000 y **15.000** cr;
  grok-image y meta dieron 500 (reembolsan) pero no generan. Sin precio confirmado, no se llama a ningún modelo.
- **13-nov (009):** nano-banana-2-lite funcionó en 14 de 16 imágenes (+1 prueba fallida); siguen cobrando los 502. Script con
  freno tras 3 fallos seguidos: generar de una en una y dejar FALLBACK para cada escena `img`. `num` y `bars` aceptan `dec` (decimales con
  coma). Wikimedia Commons está permitido en la red del entorno, pero la descarga la bloqueó el sistema de permisos: preguntar al usuario.
  Imágenes IA realistas (lugares o hechos reales) → `META["altered"] = "Sí"`.
- **Fotos reales de Wikimedia Commons (010, 13-nov, con permiso del usuario):** `pipeline/commons_fetch.py <vídeo> <consultas.json> <dir>`
  (consultas por clave; solo dominio público, CC0 y CC BY; guarda candidatas + licencia/autor) → revisar la hoja → `pipeline/commons_install.py
  img clave=archivo …` (1920×1080; las verticales van sobre fondo desenfocado) → `pipeline/commons_credits.py <json> "File:…"` para los créditos.
  Wikimedia limita mucho las peticiones: pausas de 3 s y esperas largas (el script ya lo hace). Ideal para temas históricos (NASA, Ejército de
  EE. UU.: dominio público). Créditos en `videos/NNN/fotos_creditos.json` y en `META["sources"]` (las CC BY con autor y licencia). No poner
  fechas en `cap` si la foto no es de ese día. `num` ajusta su etiqueta al ancho (antes se cortaba si pasaba de ~60 caracteres).
- **Animación nueva en render.py (007):** escenas `board` (tablero de salidas que gira a CANCELADO), `route` (mapa con rutas
  y avión), `headline` (titular de prensa con palabra subrayada; parafrasear y citar fuente); en escenas `img`: `pop=[...]`
  (palabras clave que saltan, con clic de sonido), `shake=True`, `pop_col="red"`; barrido con desenfoque entre imágenes
  (WHIP=1), destello + glitch RGB en capítulos, grano de película, planos cada 3,3 s (SEG). Vídeos sin Shorts: `SHORTS = {}`.
  Desde el 70x7-002: `chat` (mensajes con "escribiendo…", `alert` en rojo), `terminal` (tecleo con sonido) y `timeline` (`hl`).
- **Otros idiomas (008, 11-nov):** `pipeline/dub.py <vídeo> en|pt` → pistas de audio para YouTube "varios idiomas" + SRT, sobre el mismo
  vídeo. Traducciones en `<vídeo>/i18n.py` (VOICES, EN, PT, META_I18N). Voces DubVoice: inglés Aaron `LFd0JubQRIlhAUIf9mOH`, portugués Nassif
  `acdKA5HckGxoxxvy40dA` (velocidad 1,06; rehacer a 1,18 las escenas que necesiten >x1,15). Lista de voces: `GET /api/v1/voices?language=pt`.
  Coste: ~1 cr/carácter por idioma (≈12.000 para 15 min). Entrega en `entrega/idiomas/` con `IDIOMAS.md`.
  Escenas que salen aceleradas >x1,13: `python3 pipeline/redub.py <vídeo> <idioma> <velocidad> sNN …` (EN 1,12; PT 1,18) y volver a
  correr dub.py (solo mezcla). Si aún no entra, acortar ese texto en i18n.py. 010: EN máx. x1,13, PT máx. x1,14.
- La API de YouTube con clave **no** sube vídeos ni da analíticas privadas: la retención la manda el usuario
  como captura de YouTube Studio.
- Fuentes tipográficas en `assets/fonts` (Anton, Bebas Neue, Inter Display — OFL).

## Segundo canal: 70x7 (GTA 6, voseo)
Carpeta `70x7/NNN-slug/` con el mismo flujo; detalles en `70x7/README.md`. Grabaciones del usuario (enlace oculto de
YouTube → `vidiq_video_upload`) cortadas por escena con `pipeline/gameplay.py` (`SRC`, `CROP`, `BAN`, `at`).
`THEME` en guion.py cambia la paleta del render; `MUSIC_VOL` (env) el volumen de la música; sellos con `col="green"`.
`META["category"]` y `META["altered"]` cambian esos ajustes en SUBIR.md. Nada de radio del juego (Content ID).

## Tercer canal: Fútbol Sin Relato (Shorts sin voz)
Carpeta `futbol/NNN-slug/`; detalles y reglas en `futbol/README.md`. Motor propio `pipeline/sinvoz.py` (texto tecleado, marcador con
reloj de partido como barra de progreso, efectos sintetizados, música de `futbol/music/`). No gasta créditos de voz.

## Estilo visual
Fondo #0b0f17 con rejilla, amarillo #ffd166, rojo #e63946, blanco. Títulos en Anton, etiquetas en Inter Display Black.
Identidad del canal en `canal/` (logo A = barras que caen, banner, marca de agua). Regenerar con `pipeline/brand.py`.
