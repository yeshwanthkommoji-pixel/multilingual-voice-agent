from gtts import gTTS


def speak(text: str, lang: str = "en", output_path: str = "response.mp3") -> str:
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        print("Audio response ready!")
        return output_path
    except Exception as e:
        print(f"TTS error: {e}")
        return output_path
