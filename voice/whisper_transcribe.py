import subprocess
import sys
import os

def process_audio(wav_file):

    if not os.path.exists(wav_file):
        raise FileNotFoundError(f"WAV file not found: {wav_file}")

    full_command = f"main --file {wav_file} --model /home/pi/git/whisper.cpp/models/ggml-tiny.en.bin -otxt -of speech"

    # Execute the command
    process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output and error (if any)
    output, error = process.communicate()

    if error:
        print(f"ERR: processing audio: {error.decode('utf-8')}")
        return ""

    res = ""
    # Process and return the output string
    try: 
        f = open("speech.txt", "r")
        res = f.read()
        f.close()
    except:
        res = ""

    return res


def main():
    if len(sys.argv) >= 2:
        wav_file = "out.wav"
        model_name = sys.argv[2] if len(sys.argv) == 3 else "tiny.en"
        try:
            result = process_audio(wav_file, model_name)
            print(result)
        except Exception as e:
            print(f"ERR: {e}")
    else:
        print("Usage: python whisper_processor.py <wav_file> [<model_name>]")


if __name__ == "__main__":
    main()