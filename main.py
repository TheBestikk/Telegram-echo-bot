import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=["text"])
def first (message):
    bot.send_message(message.cgat,id, message.text)

# Run
bot.polling(none_stop=True)