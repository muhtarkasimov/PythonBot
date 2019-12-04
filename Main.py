import telebot
# import pyowm

# HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6 - AccuWeather API key

# --------------------------------------------------
# Open Weather Map API code
# owm = pyowm.OWM('200075eea62023528eb46334e61a76c1')
# observation = owm.weather_at_place('Bishkek')
# # print(observation)
# weather = observation.get_weather()
# temperature = weather.get_temperature('celsius')['temp']
# print(temperature)
# wind = weather.get_wind()
# print(wind)
# ----------------------------------------------------

bot = telebot.TeleBot('1019588003:AAG0AVRVX7s0AapaeJyhNR66e_CIVrYmR60')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты мне написал /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling()



