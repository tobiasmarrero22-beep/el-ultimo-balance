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
