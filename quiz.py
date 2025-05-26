from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes
from quiz_data import QUESTIONS
import random

user_scores = {}

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    context.user_data['score'] = 0
    context.user_data['q_index'] = 0
    await send_question(update, context)

async def send_question(update, context):
    q_index = context.user_data['q_index']
    if q_index >= len(QUESTIONS):
        score = context.user_data['score']
        await update.message.reply_text(f"Quiz complete! Your score: {score}/{len(QUESTIONS)}")
        return

    question = QUESTIONS[q_index]
    buttons = [
        [InlineKeyboardButton(opt, callback_data=opt)]
        for opt in question['options']
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(question['question'], reply_markup=reply_markup)

async def answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_answer = query.data
    q_index = context.user_data['q_index']
    question = QUESTIONS[q_index]
    correct = question['answer']

    if user_answer == correct:
        context.user_data['score'] += 1
        await query.edit_message_text(f"Correct! ✅\n\n{question['question']}\nAnswer: {correct}")
    else:
        await query.edit_message_text(f"Wrong ❌\n\n{question['question']}\nCorrect Answer: {correct}")

    context.user_data['q_index'] += 1
    await send_question(query, context)

quiz_handler = CommandHandler("quiz", quiz)
answer_handler = CallbackQueryHandler(answer_callback)