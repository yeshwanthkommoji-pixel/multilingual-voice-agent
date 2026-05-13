from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a helpful multilingual customer support agent.
Always reply in the SAME language the user writes in.
Be friendly, concise, and helpful.
If you cannot solve the issue, say you will connect them to a human agent."""

def get_response(user_text: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ]
        )
        reply = response.choices[0].message.content
        print(f"💬 Agent: {reply}")
        return reply
    except Exception as e:
        print(f"Groq error: {e}")
        return "I am sorry, there was an error. Please try again."