import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables del archivo .env
load_dotenv()

# Crear cliente Groq usando la variable de entorno y la base de OpenAI
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# PUNTO 3: Inicializar el historial con el System Prompt para definir el rol de ventas
historial_mensajes = [
    {"role": "system", "content": "Eres un asistente de ventas cordial, profesional y conciso. Responde siempre en español."}
]

def ejecutar_chat():
    print("====================================================")
    print(" PROVEEDOR: Groq Cloud (API OpenAI SDK Compatibility)")
    print(" MODELO LLM: openai/gpt-oss-120b")
    print(" Escribe 'salir' o 'chau' para terminar la simulación.")
    print("====================================================\n")

    while True:
        try:
            # PUNTO 4: Entrada identificada del Usuario en la UI
            user_input = input(">> [USUARIO]: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['salir', 'chau', 'exit', 'quit']:
                print("\n<< [ASISTENTE]: ¡Gracias por comunicarte con nosotros! Que tengas un excelente día.\n")
                break
            
            # 1. Guardamos la nueva pregunta en el historial para mantener la memoria
            historial_mensajes.append({"role": "user", "content": user_input})
            
            # 2. Llamada asincrónica pasándole todo el hilo acumulado de la charla
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=historial_mensajes,
                temperature=0.6,    # Ajuste de creatividad (Punto 2)
                max_tokens=500      # Control del largo de respuestas (Punto 2)
            )
            
            # 3. Extraemos el contenido de la respuesta del modelo
            respuesta_asistente = response.choices[0].message.content
            
            # PUNTO 4: Salida identificada y separada del Asistente en la UI
            print(f"\n<< [ASISTENTE]: {respuesta_asistente}")
            print("-" * 60 + "\n")
            
            # 4. Guardamos la respuesta del bot para que la recuerde en la próxima pregunta
            historial_mensajes.append({"role": "assistant", "content": respuesta_asistente})
            
        except Exception as e:
            print(f"\n[!] Error en la comunicación con la API de Groq: {e}\n")

if __name__ == "__main__":
    ejecutar_chat()
