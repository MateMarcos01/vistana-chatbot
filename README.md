# Vistana Chatbot

Bot de Telegram que responde preguntas básicas sobre el uso de Vistana:
cómo instalarla, cómo usarla y qué formato debe tener el archivo de datos.

Probarlo en Telegram: @VistanaBot

## Cómo ejecutarlo

1. Crear y activar el entorno virtual:
   python -m venv venv
   venv\Scripts\Activate.ps1

2. Instalar dependencias:
   pip install -r requirements.txt

3. Copiar `.env.example` como `.env` y poner el token del bot (se obtiene con @BotFather).

4. Ejecutar:
   python main.py

## Comandos

- /start — Inicia el asistente
- /help — Muestra las preguntas disponibles