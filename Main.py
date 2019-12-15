import telebot
import pyowm
from Weather import Weather
from MyTime import Time
import time

# ---------------------
weather = Weather()
my_time = Time()


# () создавать один раз каждый жень запрос на ежедневную погоду и хранить в тексте.
#    чтобы каждый раз не просить c API
#    и в дальнейших вызовах в течение дня использовать его
# ---------------------

# ----------------------------------------------------
# chat code
bot = telebot.TeleBot('1019588003:AAG0AVRVX7s0AapaeJyhNR66e_CIVrYmR60')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты мне написал /start')

# def start_weather_bot():


# start_weather_bot()

# small reply dicts
heyWords = ['эй','ау','аууу','ты тут?']
weatherWords = ['погода', 'какая сегодня погода?', 'какая погода','какая погода?','что с погодой?','что с погодой']
whatYouCan = ['что ты можешь?']
helloWords = ['привет','салам','здаров','здрарова','еу','ёу']
byeWords = ['пока','прощай','досвидание','досвидания','bye']

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() in helloWords:
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() in byeWords:
        bot.send_message(message.chat.id, 'Пока :(')
    elif message.text.lower() in heyWords:
        bot.send_message(message.chat.id, 'Да, я тут! Слушаю...')
    elif message.text.lower() in weatherWords:
        bot.send_message(message.chat.id, weather.get_weather_in_text())
        print(message)
    elif message.text.lower() in whatYouCan:
        bot.send_message(message.chat.id, 'Могу сказать какая сегодня погода\nМогу выслушать и не понять все равно ¯\_(ツ)_/¯')
    else:
        bot.send_message(message.chat.id, 'Мой создатель еще на придумал как мне на это отвечать ¯\_(ツ)_/¯')
        # Вот тут написать метод для рассылки
    # elif message.text.lower() == 'погоду всем':
    #     bot.send_message(message.chat.id, weather.get_weather_in_text())
bot.polling()
# ----------------------------------------------------