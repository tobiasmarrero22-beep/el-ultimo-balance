#!/bin/bash
# uso: getclip.sh <clave> <url>  → clips/<clave>.mp4 (solo vídeo, 1080p, sin audio) + img/<clave>.png (fotograma central)
set -e
k="$1"; u="$2"; mkdir -p clips img
curl -sSf -m 180 -o "clips/$k.src.mp4" "$u"
ffmpeg -v error -y -i "clips/$k.src.mp4" -an -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30" -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p "clips/$k.mp4"
rm -f "clips/$k.src.mp4"
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "clips/$k.mp4")
ffmpeg -v error -y -ss $(python3 -c "print(float('$d')/2)") -i "clips/$k.mp4" -frames:v 1 "img/$k.png"
echo "$k OK ${d}s"
