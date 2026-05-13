from gtts import gTTS
from lang_detect import detect_language

def speak(text: str, output_path="response.mp3") -> str:
    lang = detect_language(text)
    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)
    print("🔊 Audio response ready!")
    return output_path
