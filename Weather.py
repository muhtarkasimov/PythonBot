import time
import json
import urllib.request

# HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6 - AccuWeather API key
# Bishkek code - 222844

API = 'HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6'
country_code = 'KG'
city = 'Bishkek'

key=''
def getLocation(country_code, city):
    search_address = 'http://dataservice.accuweather.com/locations/v1/cities/' + country_code + '/search?apikey=HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6&q=' + city
    # print(search_address)
    with urllib.request.urlopen(search_address) as search_address:
        data = json.loads((search_address.read().decode()))
    # print(data)
    location_key = data[0]['Key']
    return location_key

def getForcast(location_key):
    daily_forcastUrl = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/' + location_key + '?apikey=HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6'
    with urllib.request.urlopen(daily_forcastUrl) as daily_forcastUrl:
        data = json.loads(daily_forcastUrl.read().decode())
    # print(data)
    return data

key = getLocation(country_code, city)
forecast = getForcast(key)

min_temp = forecast['DailyForecasts'][0]['Temperature']['Minimum']['Value']
print('min temp: ' + str(min_temp))
max_temp = forecast['DailyForecasts'][0]['Temperature']['Maximum']['Value']
print('max temp: ' + str(max_temp))
day_precipitation = forecast['DailyForecasts'][0]['Day']['HasPrecipitation']
print('day precipitation: ' + str(day_precipitation))
day_sky = forecast['DailyForecasts'][0]['Day']['IconPhrase']
print('day sky: ' + str(day_sky))
night_precipitation = forecast['DailyForecasts'][0]['Night']['HasPrecipitation']
print('night precipitation: ' + str(night_precipitation))
night_sky = forecast['DailyForecasts'][0]['Night']['IconPhrase']
print('day sky: ' + str(night_sky))

