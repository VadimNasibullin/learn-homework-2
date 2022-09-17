"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():


    from datetime import date, timedelta
    dt = date(2022, 9, 11)
    delta = timedelta(days=1)
    print(f'Вчерашняя дата:', dt - delta)
    print(f'Дата сегодня:', dt)
    delta = timedelta(days=30)
    print(f'Дата 30 дней назад:', dt - delta)




def str_2_datetime(date_string):


    from datetime import datetime
    date_string = '01/01/25 12:10:03.234567'
    date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    print(date_dt)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
