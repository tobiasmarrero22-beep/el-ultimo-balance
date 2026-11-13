# 70x7 — canal de GTA 6 (segundo canal del usuario)

- YouTube: @70veces7Oficial (`UCaqDxc05VhkesL19MNtXaug`), país AR. Lema: "todas las veces que haga falta. 🦁"
- Contenido: noticias, teorías, guías y gameplay de GTA 6 en español. **Voseo** ("suscribite", "fijate").
- Pie de descripción: `🦁 70x7: GTA 6 todas las veces que haga falta. Suscribite, el 19/11 arranca el gameplay.` +
  "Canal no afiliado a Rockstar Games ni a Take-Two."
- Voz: ElevenLabs "Adán - Narration" (`i4Kar2uamCWyas8TAu31`, latinoamericana) vía DubVoice.
- Paleta Vice City en el render: `THEME = {"RED": (255, 56, 150), "YEL": (80, 230, 235)}` (rosa y celeste).

## Vídeos con grabaciones del usuario
El usuario no puede mandar archivos de más de 30 MB: sube la grabación a YouTube como **oculta** y pasa el enlace.
1. `vidiq_video_upload` con el enlace de YouTube (gratis, trabajo asíncrono → `vidiq_job_poll`) → URL de
   storage.googleapis.com que sí se descarga aquí. Guardar en el scratchpad y anotar `SRC`/`SRC_URL` en guion.py.
2. **Antes de nada, comprobar que el metraje es del usuario.** El 001 resultó ser una grabación de pantalla del iPhone
   mientras se reproducía un vídeo ajeno de YouTube ("Night Drive Around Vice City in a Stinger Convertible", canal
   The Gaming Motorist, `7PdCFHkEkHo`). Señales: franjas gris oscuro (~#101010, el fondo del reproductor de YouTube),
   relación 19,5:9 (1920x886), el Centro de control con "Reproduciendo: …" en los primeros segundos, título del vídeo
   fuente en pantalla. Buscar el título en YouTube (`ytlib.get("search", ...)`). Metraje ajeno = reclamo/strike de
   copyright y contenido reutilizado → no se publica sin permiso del autor.
3. Revisar la grabación: hoja de fotogramas cada 6 s, nombres de zona que muestra el juego, franjas negras (`CROP`),
   **notificaciones del celular** y tramos con el auto parado → `BAN` (detección por bordes de texto arriba a la izquierda
   y por diferencia entre fotogramas).
4. Guion con `visual=dict(type="img", at=SEGUNDO, cap=...)` (y `at` en las escenas de los Shorts).
5. `tts.py` → `python3 pipeline/gameplay.py <carpeta>` (corta un clip por escena, se salta los BAN y avisa si se repite
   metraje) → `render.py` (con `MUSIC_VOL=0.15`) → `thumbs.py` → `meta.py`.
- **Nunca usar la radio del juego**: canciones con licencia → reclamos de Content ID. Se quita el audio original y se pone
  música generada con `vidiq_generate_music` (25 créditos/pista, WAV en S3 descargable) en `music/`.
- `img/` y `clips/` no se suben a git (se regeneran con gameplay.py a partir de la grabación).
- Revisar también el arranque y el final: el Centro de control (botón de grabar) y los controles del reproductor ("-10") aparecen al empezar/terminar la grabación. Detector usado en el 001: texto blanco desaturado y bordes horizontales largos arriba (notificaciones), píxeles blancos en los laterales (iconos del reproductor) y oscurecimiento brusco de todo el cuadro.

## Voz clonada del usuario (desde el 6-nov)
- Clon creado en la web de DubVoice ("tobias", `voice_id` **2719189**). `GET /api/voice-clone` lista los clones de la cuenta.
- Se genera con `POST /api/minimax-tts` `{"text", "voice_id": "2719189", "language": "es"}` → MP3 directo (1 crédito/carácter).
  `/api/voice-clone/tts` pide sesión web (401) y `/api/v1/tts` no acepta ids numéricos. `tts.py` usa minimax-tts si `VOICE` es numérico.
- `PRONUNCIA` en guion.py: escritura fonética de nombres en inglés (Vais Síti, Rokstar, ge te a seis…), solo para la voz.

## Vídeos sin grabación (desde el 002, 8-nov)
- Historias narradas con imágenes IA de vidIQ (`vidiq_generate_thumbnail`, 22 créditos; pedir "plain realistic photograph… no graphic
  overlays, no tier list" si sale un panel tipo ranking, como pasó con hospital y tribunal) + escenas de código.
- Escenas nuevas en render.py: `chat` (ventana de chat genérica, mensajes que aparecen con "escribiendo…"; `alert` en rojo),
  `terminal` (texto que se teclea solo, con sonido de teclas; líneas con "!" en rojo) y `timeline` (línea de tiempo; `hl` resalta un punto).
- Voz: Adán (`i4Kar2uamCWyas8TAu31`) por pedido del usuario en el 002 (no la clonada). Sin Shorts.
- Música: se reutilizan las pistas del 001 (`music/`). `img/` y `audio/` del 002 sí van a git (excepción en .gitignore).

## Reglas fijas de guion (13-nov-2026)
Las mismas que en `CLAUDE.md` para todos los canales: gancho en el segundo 0 (qué vas a ver, por qué te importa, por qué
quedarte), GANCHO → DESARROLLO → CIERRE, preguntas abiertas que se resuelven más adelante, al cerrar una se abre otra, y nada de
saludos («¿qué onda, gente?») ni relleno. Antes de producir: `python3 pipeline/guion_md.py 70x7/NNN-slug` y esperar el OK del usuario.

## Reglas anti-desmonetización (13-nov-2026)
Las de `CLAUDE.md` para todos los canales y, en 70x7 en particular (es el canal con más riesgo de «contenido reutilizado»):
- Gameplay **grabado por el usuario** como material principal; nunca vídeos de otros canales (el 001 usó uno de The Gaming
  Motorist: no repetirlo).
- Tráilers y material de Rockstar solo en fragmentos cortos y siempre con análisis o comentario encima, nunca un tráiler entero.
- Cada vídeo con un ángulo propio (guía, análisis, teoría, noticia comentada), no la misma plantilla repetida.
