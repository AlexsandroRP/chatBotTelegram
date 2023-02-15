from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
from telegram import Update
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s %(message)s', level=logging.INFO)

# funçõoes de respostas do bot
async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Wecome to my bot')

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() in ('hello', 'good morning'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, welcome!', reply_to_message_id=update.message.id) # responde diretamente a msg enviada   

async def nao_registrado(update: Update, context: ContextTypes.DEFAULT_TYPE):  
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Esse comando não é válido')     


if __name__ == '__main__':
    aplication = ApplicationBuilder().token('6198940500:AAH-Fjw__yxlaNGFK7H2OYiMWODzHiN0qGY').build()

    # registrar um handler de comandos (classe que observa se X comando foi digitado)
    aplication.add_handler(CommandHandler('iniciar',iniciar))
    aplication.add_handler(MessageHandler(filters.COMMAND, nao_registrado)) # trata comandos n registrados
    aplication.add_handler(MessageHandler(filters.TEXT, responder))
    # Ligar o monitoramento de comandos
    aplication.run_polling()
