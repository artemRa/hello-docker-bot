import json
import platform
import sqlite3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)
TOKEN = config['TOKEN']
DB_PATH = "data/hello-docker-log.db"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    system_type = platform.system()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO actions DEFAULT VALUES;")
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM actions;")
    count = cursor.fetchone()[0]
    conn.close()

    await update.message.reply_text(
        f"Тип операционной системы: {system_type}\n"
        f"Количество обращений: {count}"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
