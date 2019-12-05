# import time
# from datetime import datetime
#
# now = datetime.now()
#
# print(now)
#
# time_string = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
#
# # print(time_string[-2:])
# # print(time_string)
# # if (time_string[-2:] == 00):
# #     print("Pop")
# # else:
# #     print("not Pop")
#
# one_second = 1
# one_minute = 60
# one_hour = one_minute * 60
# while True:
#     print(datetime.now())
#     time.sleep(one_minute)

import json

with open("file.json", "r") as read_file:
    data = json.load(read_file)

print(data['DailyForecasts'][0]['Temperature']['Minimum']['Value'])
