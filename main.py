import os
from stt import transcribe
from agent import get_response
from tts import speak

def play_audio(path):
    os.startfile(path)

def choose_language():
    print("\n" + "=" * 40)
    print("Choose your language / భాష ఎంచుకోండి / भाषा चुनें")
    print("=" * 40)
    print("1. English")
    print("2. Hindi - हिंदी")
    print("3. Telugu - తెలుగు")
    print("=" * 40)
    
    choice = input("Enter 1, 2 or 3: ")
    
    if choice == "1":
        return "en"
    elif choice == "2":
        return "hi"
    elif choice == "3":
        return "te"
    else:
        print("Invalid choice, defaulting to English")
        return "en"

def run():
    print("=" * 40)
    print("🌍 Multilingual Voice Support Agent")
    print("Speak in English, Hindi or Telugu!")
    print("Press Ctrl+C to stop")
    print("=" * 40)

    lang = choose_language()

    if lang == "te":
        print("✅ Telugu selected! మీరు తెలుగులో మాట్లాడవచ్చు!")
    elif lang == "hi":
        print("✅ Hindi selected! आप हिंदी में बात कर सकते हैं!")
    else:
        print("✅ English selected! You can speak in English!")

    while True:
        try:
            text = transcribe()

            if text == "":
                print("⚠️ Could not hear you. Try again!")
                continue

            print(f"📝 You said: {text}")
            response = get_response(text, lang)
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