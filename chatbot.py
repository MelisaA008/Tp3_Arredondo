from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Crear cliente Groq usando la variable de entorno
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
    
)

def chat_with_bot(user_message):
    response = client.chat.completions.create(
         model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Eres un asistente de ventas cordial y profesional."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

print("Usuario: Hola, ¿qué productos tienes disponibles?")
print("Asistente:", chat_with_bot("Hola, ¿qué productos tienes disponibles?"))
