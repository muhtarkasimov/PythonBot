import telebot
import time
import json
import urllib.request
from datetime import datetime
import pyowm

# API = 'HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6'
# countryCode = 'KG'
# city = 'Bishkek'


# HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6 - AccuWeather API key
# Bishkek code - 222844

# --------------------------------------------------
# Time
current_time = datetime.now()

# format dd.mm.yyyy hh:mm:ss
current_time_string = time_string = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")

# --------------------------------------------------

# ---------------------------------------------------
# Open Weather Map API code
owm = pyowm.OWM('200075eea62023528eb46334e61a76c1')
observation = owm.weather_at_place('Bishkek')
# observation = owm.weather_at_zip_code('720019', 'KG')
print(observation)

# weather
weather = observation.get_weather()
# print(weather)

# time
time_current = weather.get_reference_time()
# print(time_current)

# clouds
status = weather.get_status()
det_status = weather.get_detailed_status()
# print(status)
# print(det_status)

# temperature
temp = weather.get_temperature('celsius')
temp_current = weather.get_temperature('celsius')['temp']
temp_max = weather.get_temperature('celsius')['temp_max']
temp_min = weather.get_temperature('celsius')['temp_min']
print(temp)
print(temp_current, temp_max, temp_min)

wind = weather.get_wind()
# print(wind)

weather_in_text = 'Погода на сегодня:\nТемпература днём   : ' \
                  + str(temp_max) + '*c\nТемпература ночью : ' + str(temp_min) \
                  + '*c\nТемпература сейчас: ' \
                  + str(temp_current) + '*c'


# ----------------------------------------------------

# ----------------------------------------------------
# chat code
bot = telebot.TeleBot('1019588003:AAG0AVRVX7s0AapaeJyhNR66e_CIVrYmR60')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты мне написал /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
        tellGoodMorning()
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'погода':
        bot.send_message(message.chat.id, weather_in_text)
bot.polling()
# ----------------------------------------------------


# ----------------------------------------------------
# due time notifications

# test

def sendMessage(message, text):
    bot.send_message(message.chat.id, text)

def tellGoodMorning():
    sendMessage('Good Morning')

tellGoodMorning()

# ----------------------------------------------------