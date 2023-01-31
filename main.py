from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import*



app = ApplicationBuilder().token("Your token").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("new_year", new_year))
app.add_handler(CommandHandler("translate_color", color))

print('Start server')

app.run_polling()