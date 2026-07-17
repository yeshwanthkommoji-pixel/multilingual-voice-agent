import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

for key in ("GROQ_API_KEY",):
    if not os.getenv(key) and key in st.secrets:
        os.environ[key] = st.secrets[key]

from stt import transcribe_audio
from agent import get_response
from tts import speak

st.set_page_config(
    page_title="Multilingual Voice Agent",
    page_icon="🌍",
    layout="centered",
)

st.title("🌍 Multilingual Customer Support Voice Agent")
st.caption("Speak in English, Hindi or Telugu — get a spoken reply back")

LANGUAGES = {
    "English": ("en", "en-IN"),
    "Hindi - हिंदी": ("hi", "hi-IN"),
    "Telugu - తెలుగు": ("te", "te-IN"),
}

lang_label = st.selectbox("Choose your language", list(LANGUAGES.keys()))
tts_lang, stt_lang = LANGUAGES[lang_label]

st.divider()
audio_value = st.audio_input("🎤 Tap to record your question")

if audio_value is not None:
    with st.spinner("Transcribing your voice..."):
        user_text = transcribe_audio(audio_value, lang_code=stt_lang)

    if not user_text:
        st.warning("⚠️ Could not understand the audio. Please try again, speaking clearly.")
    else:
        st.markdown(f"**📝 You said:** {user_text}")

        with st.spinner("Thinking..."):
            reply = get_response(user_text, tts_lang)

        st.markdown(f"**🤖 Agent:** {reply}")

        with st.spinner("Generating voice reply..."):
            audio_path = speak(reply, lang=tts_lang)

        st.audio(audio_path)
