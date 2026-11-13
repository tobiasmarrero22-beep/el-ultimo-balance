# Dato de Tribuna — canal de Shorts de fútbol (tercer canal del usuario, 13-nov-2026)

Se pensó como «Fútbol Sin Relato» (sin voz, con música) y el mismo 13-nov el usuario lo cambió: **sin música y con relato de IA**
(relator emocionado, acento argentino con voseo). Nombre nuevo **Dato de Tribuna**, handle `@datodetribuna`.

- Solo Shorts con **relato de IA** (DubVoice/ElevenLabs, voz argentina; `VOICE`, `SPEED`, `PRONUNCIA` y `say` en guion.py), texto que se
  teclea al ritmo de la voz, efectos (silbato, hinchada, golpes) y **sin música** (`MUSIC = None`). Voseo. 30–40 s por Short.
- Identidad en `canal/` (avatar, banner con `banner.py`, descripción).
- Motor: `python3 pipeline/sinvoz.py futbol/NNN-slug` (`--frames` para la hoja de revisión) → `entrega/NNN.mp4` + `entrega/SUBIR.md`.
  Guion en `guion.py`: `CARDS` (texto con `*amarillo*` y `^rojo^`, `hero` del tipo score, counter (style="tag"), quiz, place, redcard,
  big, items, player, badges, clock, tactic, stamp, final), `crowd`, `cut` (silencio), `sfx`; `META`; `MUSIC` y `MUSIC_START`.
- `futbol/music/*.mp3` (DubVoice, 5.000 cr) quedó sin uso desde que el usuario pidió sin música.
- **Reglas** (además de las fijas de guion y anti-desmonetización de todos los canales):
  - Guion primero, con datos verificados y fuentes; esperar el OK del usuario.
  - Turnar formatos: historia en tarjetas, precio que sube, adivina en 3 segundos, cifra y silencio (nunca dos iguales seguidos).
  - Nada de jugadas, transmisiones, escudos ni canciones. Fotos solo de dominio público o licencia libre, con crédito.
  - Un Short al día como máximo. Cada Short termina con una pregunta para los comentarios.

| Nº | Short | Formato | Duración | Estado |
|---|---|---|---|---|
| 001 | 149 a 0 | historia en tarjetas | 30 s | entregado 13-nov |
| 002 | Cascarino, fichado por ropa de entrenamiento | precio que sube | 30 s | entregado 13-nov |
| 003 | El gol más rápido de un Mundial | quiz | 26 s | entregado 13-nov |
| 004 | Maracanazo, 173.850 | cifra y silencio | 27 s | entregado 13-nov |
