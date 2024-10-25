#!/bin/bash

#export LD_LIBRARY_PATH="/home/pi/bmos/gv/opt"
#export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/bmos/credentials.json"

# python3 /home/pi/bmos/gv/transcribe.py

ffmpeg -y -i ./rec.wav -ar 16000 -ac 1 -c:a pcm_s16le ./out16.wav > /dev/null 2>&1
python3 whisper_trascribe.py out116.wav

rm out.wav
rm out16.wav
rm speech.txt
