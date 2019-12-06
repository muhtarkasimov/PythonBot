import time
import json
import urllib.request


# HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6 - AccuWeather API key
# Bishkek code - 222844

class Weather:

    def __init__(self):
        self.API = 'HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6'
        self.country_code = 'KG'
        self.city = 'Bishkek'
        self.key = ''
        self.forecast = ''
        self.location_key = ''
        self.forecast = ''
        self.weather_array = []

    def getLocation(self):
        search_address = 'http://dataservice.accuweather.com/locations/v1/cities/' + self.country_code + '/search?apikey=HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6&q=' + self.city
        # print(search_address)
        with urllib.request.urlopen(search_address) as search_address:
            data = json.loads((search_address.read().decode()))
        # print(data)
        self.location_key = data[0]['Key']

    def getForcast(self):
        daily_forcastUrl = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/' + self.location_key + '?apikey=HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6'
        with urllib.request.urlopen(daily_forcastUrl) as daily_forcastUrl:
            data = json.loads(daily_forcastUrl.read().decode())
        # print(data)
        self.forecast = data

    def get_weather(self):
        self.getLocation()
        self.getForcast()

        min_temp = self.forecast['DailyForecasts'][0]['Temperature']['Minimum']['Value']
        max_temp = self.forecast['DailyForecasts'][0]['Temperature']['Maximum']['Value']
        # convert to celsius
        min_temp = int(min_temp - 32) * (5.0 / 9.0)
        max_temp = int(max_temp - 32) * (5.0 / 9.0)
        day_precipitation = self.forecast['DailyForecasts'][0]['Day']['HasPrecipitation']
        day_sky = self.forecast['DailyForecasts'][0]['Day']['IconPhrase']
        night_precipitation = self.forecast['DailyForecasts'][0]['Night']['HasPrecipitation']
        night_sky = self.forecast['DailyForecasts'][0]['Night']['IconPhrase']

        self.weather_array = [min_temp, max_temp, day_precipitation, day_sky, night_precipitation, night_sky]

        # print('min temp: ' + str(min_temp))
        # print('max temp: ' + str(max_temp))
        # print('day precipitation: ' + str(day_precipitation))
        # print('day sky: ' + str(day_sky))
        # print('night precipitation: ' + str(night_precipitation))
        # print('day sky: ' + str(night_sky))

    def get_weather_in_text(self):
        self.get_weather()

        if (self.weather_array[2]):
            day_prec = 'ожидаются'
        else:
            day_prec = 'не ожидаются'
        if (self.weather_array[4]):
            night_prec = 'ожидаются'
        else:
            night_prec = 'не ожидаются'

        text =  'Максимальная температура ' + str(float("{0:.1f}".format(self.weather_array[0]))) + '°C' + \
                '\nМинимальная температура ' + str(float("{0:.1f}".format(self.weather_array[1]))) + '°C' + \
                '\nДнем:\n Осадки ' + day_prec + \
                '\n Небо ' + str(self.weather_array[3]) + \
                '\nНочью:\n Осадки ' + night_prec + \
                '\n Небо ' + str(self.weather_array[5])
        return text

main_weather = Weather()
print(main_weather.get_weather_in_text())
