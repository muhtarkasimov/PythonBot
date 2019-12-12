import time
from _datetime import datetime


class Time:

    def __init__(self):
        self.current_time = datetime.now()

        # format dd.mm.yyyy hh:mm:ss
        self.current_time_string = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
        self.current_date = self.current_time_string[:10]
        self.current_year = self.current_time_string[6:10]
        self.current_month = self.current_time_string[3:5]
        self.current_day = self.current_time_string[0:2]
        self.current_hour = self.current_time_string[11:13]
        self.current_minute = self.current_time_string[14:16]
        self.current_second = self.current_time_string[17:]

    # --------------------------------------------------
    # Time

    # format dd.mm.yyyy hh:mm:ss
    # current_time_string = time_string = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")

    # print(current_time_string)
    # --------------------------------------------------

    # current_date = current_time_string[:10]
    # current_year = current_time_string[6:10]
    # current_month = current_time_string[3:5]
    # current_day = current_time_string[0:2]


    def print_time(self):
        self.update_time()
        print('date: ' + self.current_date)
        print('year: ' + self.current_year)
        print('month: ' + self.current_month)
        print('day: ' + self.current_day)
        print('hour: ' + self.current_hour)
        print('minute: ' + self.current_minute)
        print('second: ' + self.current_second)

    def get_time(self):
        self.update_time()
        return [self.current_year, self.current_month, self.current_day, self.current_hour, self.current_minute]

    def update_time(self):
        # format dd.mm.yyyy hh:mm:ss
        #--------0123456789012345678
        self.current_time = datetime.now()
        self.current_date = self.current_time_string[:10]
        self.current_year = self.current_time_string[6:10]
        self.current_month = self.current_time_string[3:5]
        self.current_day = self.current_time_string[0:2]
        self.current_hour = self.current_time_string[11:13]
        self.current_minute = self.current_time_string[14:16]
        # self.current_second = self.current_time_string[17:19]
        # print(self.current_time_string)
        # print(self.current_second)
        if (self.get_time()[4] == '35'):
            print('true')

    # def update_time_per_hour(self):
    #     current_time = datetime.now()
    #
    #     # format dd.mm.yyyy hh:mm:ss
    #     current_time_string = time_string = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")

time = Time()
time.update_time()