import whisper

try:
    model = whisper.load_model("tiny")
    result = model.transcribe("out.wav")
    print(result["text"])
except:
    print("ERR: Invalid results")