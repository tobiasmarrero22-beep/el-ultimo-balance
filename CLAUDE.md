# El Último Balance — instrucciones para Claude

Canal de YouTube en español: historias de empresas (auge y caída). Vídeos largos de 8–10 min + 2–3 Shorts por vídeo.
El usuario **sube los vídeos y contesta comentarios**; Claude **investiga, escribe, produce y entrega el paquete de subida**.
Idioma de trabajo con el usuario: español. Público: hispanohablante (LatAm + España), español neutro, "tú".

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
  → `pipeline/getclip.sh <clave> <videoUrl>` deja `clips/<clave>.mp4` (1080p, sin audio) e `img/<clave>.png`. Las escenas
  `img` usan el clip; cada escena arranca en un tramo distinto. Guardar elecciones y créditos en `videos/NNN/broll.json` y
  acreditar a los autores en las fuentes. `META["disclosure"]` cambia el aviso (no son imágenes de IA).
- La API de YouTube con clave **no** sube vídeos ni da analíticas privadas: la retención la manda el usuario
  como captura de YouTube Studio.
- Fuentes tipográficas en `assets/fonts` (Anton, Bebas Neue, Inter Display — OFL).

## Estilo visual
Fondo #0b0f17 con rejilla, amarillo #ffd166, rojo #e63946, blanco. Títulos en Anton, etiquetas en Inter Display Black.
Identidad del canal en `canal/` (logo A = barras que caen, banner, marca de agua). Regenerar con `pipeline/brand.py`.
