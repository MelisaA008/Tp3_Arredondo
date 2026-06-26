# TP Chatbot con Inteligencia Artificial - Programación III

Este es mi trabajo práctico de un chatbot por consola hecho en Python. 
Se conecta a internet para hablar con una Inteligencia Artificial y simula ser un vendedor.

---

## Datos del Modelo (Puntos 1 y 5)
*   **Proveedor**: Groq Cloud (usando la librería compatible de OpenAI).
*   **Modelo de IA**: `openai/gpt-oss-120b`.

---

## Consignas cumplidas en el código

*   **Respuestas en Español (Punto 2):** El bot está configurado para responder siempre en español y con textos cortos (`max_tokens=500`).
*   **Rol de Sistema / System Prompt (Punto 3):** Apenas arranca, se le da la orden al bot de actuar bajo el rol de *"asistente de ventas cordial y profesional"*.
*   **Memoria del chat:** El código tiene una lista que guarda toda la conversación para que el bot recuerde lo que hablamos en los mensajes anteriores.
*   **Separación en la interfaz (Punto 4):** En la consola se ve bien claro quién habla gracias a las etiquetas:
    *   `>> [USUARIO]:` para mis preguntas.
    *   `<< [ASISTENTE]:` para las respuestas de la IA.

---

##  Cómo probarlo

1. Instalar las librerías:
   ```bash
   pip install python-dotenv openai
   ```
2. Crear un archivo `.env` con tu clave de la API:
   ```text
   GROQ_API_KEY=tu_clave_aqui
   ```
3. Correr el programa:
   ```bash
   python .\chatbot.py
   ```
