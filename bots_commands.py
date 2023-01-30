from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import date

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/help\n/sum\n/new_year')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[3])
    await update.message.reply_text(f'{x} + {y} = {x + y}')
async def new_year(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now_date = date.today()
    next_date = date(2024, 1, 1)
    rem_date = next_date - now_date
    await update.message.reply_text(f'До Нового Года осталось: {rem_date}')