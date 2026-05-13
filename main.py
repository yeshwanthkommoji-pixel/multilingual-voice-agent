import os
from stt import transcribe
from lang_detect import detect_language
from agent import get_response
from tts import speak

def play_audio(path):
    os.startfile(path)

def run():
    print("=" * 40)
    print("🌍 Multilingual Voice Support Agent")
    print("Speak in any language - I will reply!")
    print("Press Ctrl+C to stop")
    print("=" * 40)

    while True:
        try:
            text = transcribe()
            lang = detect_language(text)
            response = get_response(text)
            audio_out = speak(response)
            play_audio(audio_out)
            print("\n✅ Done! Ready for next question...\n")

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")
            print("Try again...\n")

if __name__ == "__main__":
    run()