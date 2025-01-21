import json
import platform
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)
TOKEN = config['TOKEN']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    system_type = platform.system()
    await update.message.reply_text(f"Тип операционной системы: {system_type}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
