from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Quiz Bot!\nUse /quiz to start the quiz.")

handler = CommandHandler("start", start)