# 🌍 Multilingual Customer Support Voice Agent

A browser-based AI voice agent that transcribes your speech, replies using an LLM, and speaks the answer back — in English, Hindi, or Telugu.

## Features

- 🎤 Voice input via browser microphone
- 🤖 AI-powered replies using Groq (Llama 3.1 8B Instant)
- 🔊 Spoken audio responses via text-to-speech
- 💬 Supports English, Hindi, and Telugu

## Live Demo

https://multilingual-voice-agent-app.streamlit.app

## Run Locally

1. Clone this repo
2. Run: pip install -r requirements.txt
3. Add your GROQ_API_KEY in a .env file
4. Run: streamlit run app.py

## Project Structure

- app.py — the deployed web app
- main.py — original CLI version (local microphone only)
- agent.py — LLM response logic
- stt.py — speech-to-text
- tts.py — text-to-speech

