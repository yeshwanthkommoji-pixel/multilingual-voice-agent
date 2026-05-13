import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

st.title("AI Customer Support Agent")

user_input = st.text_input("Ask something:")

if user_input:
    response = client.models.generate_content(
        model="gemini-1.5-flash-001",   # 👈 FIXED HERE
        contents=user_input
    )

    st.write(response.text)