import speech_recognition as sr


def transcribe_audio(audio_file, lang_code: str = "en-IN") -> str:
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
    except Exception as e:
        print(f"Could not read audio: {e}")
        return ""
    try:
        text = recognizer.recognize_google(audio, language=lang_code)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print(f"Speech recognition service error: {e}")
        return ""


def transcribe() -> str:
    import pyaudio  # noqa: F401
    r = sr.Recognizer()
    print("Listening... Speak now!")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 300
        audio = r.listen(source, timeout=15, phrase_time_limit=10)
    print("Got your voice!")
    for lang_code in ("en-IN", "hi-IN", "te-IN"):
        try:
            text = r.recognize_google(audio, language=lang_code)
            print(f"You said: {text}")
            return text
        except Exception:
            continue
    print("Could not understand audio")
    return ""
