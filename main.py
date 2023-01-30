from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import*



app = ApplicationBuilder().token("Your Token").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("new_year", new_year))

print('Start server')

app.run_polling()