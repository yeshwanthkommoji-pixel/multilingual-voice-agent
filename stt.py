import speech_recognition as sr

def transcribe() -> str:
    r = sr.Recognizer()
    print("\n🎤 Listening... Speak now!")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 300
        audio = r.listen(source, timeout=15, phrase_time_limit=10)
    print("✅ Got your voice!")

    try:
        # Use English India as default - works for English, Hindi and Telugu
        text = r.recognize_google(audio, language="en-IN")
        print(f"📝 You said: {text}")
        return text
    except:
        try:
            # Try Hindi
            text = r.recognize_google(audio, language="hi-IN")
            print(f"📝 You said: {text}")
            return text
        except:
            try:
                # Try Telugu
                text = r.recognize_google(audio, language="te-IN")
                print(f"📝 You said: {text}")
                return text
            except Exception as e:
                print(f"Could not understand audio: {e}")
                return ""