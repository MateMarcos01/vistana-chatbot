import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import responses

load_dotenv(override=True)
API_KEY = os.getenv('TELEGRAM_TOKEN')

if not API_KEY:
    raise SystemExit('Falta TELEGRAM_TOKEN: copiá .env.example como .env y poné tu token.')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hola, soy el asistente virtual de Vistana. ¿En que puedo ayudarte?')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Podés preguntarme:\n'
        '- ¿Cómo instalo Vistana?\n'
        '- ¿Cómo la uso?\n'
        '- ¿Qué formato tiene que tener el archivo?'
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = responses.sample_responses(text)
    await update.message.reply_text(response)


async def error(update: object, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(API_KEY).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error)

    app.run_polling()
