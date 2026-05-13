import speech_recognition as sr

def transcribe() -> str:
    r = sr.Recognizer()
    print("\n🎤 Listening... Speak now!")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 300
        audio = r.listen(source, timeout=15, phrase_time_limit=10)
    print("✅ Got your voice!")
    text = r.recognize_google(audio)
    print(f"📝 You said: {text}")
    return text