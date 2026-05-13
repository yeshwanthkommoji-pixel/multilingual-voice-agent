import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key found: {api_key[:10]}...")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Say hello in English")
print(f"Response: {response.text}")