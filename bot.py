import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from core import get_bot_reply

load_dotenv() 
TOKEN = os.getenv("TOKEN_TELEGRAM")

async def handle_message(update, context):
    user_text = update.message.text
    reply = get_bot_reply(user_text)
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Prohana Bot sedang berjalan...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()