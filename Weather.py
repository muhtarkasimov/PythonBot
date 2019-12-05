import time
import json
import urllib.request

API = 'HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6'
country_code = 'KG'
city = 'Bishkek'

key=''
def getLocation(country_code, city):
    search_address='http://dataservice.accuweather.com/locations/v1/cities/' + country_code + '/search?apikey=HCgKwXyCl8E6ZqKV3iXfGAqPt1IKxPr6&q=' + city
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
    print(data)
key = getLocation(country_code, city)
getForcast(key)
