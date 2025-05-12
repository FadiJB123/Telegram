import telebot  
import requests

bot = telebot.TeleBot("7521599695:AAGAviSpucke3gkW31xNXL-LuEcIFFQdI0o")

@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(message.chat.id, "Yo")  

try:
    bot.polling()
except Exception as e:
    print(f"Error: {e}")