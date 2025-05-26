from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from handlers import start, quiz

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(start.handler)
    app.add_handler(quiz.quiz_handler)
    app.add_handler(quiz.answer_handler)

    app.run_polling()

if __name__ == '__main__':
    main()