import telebot

bot = telebot.TeleBot('1019588003:AAG0AVRVX7s0AapaeJyhNR66e_CIVrYmR60')

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты мне написал /start')


bot.polling()



