"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from time import strptime

def print_days():
    today = input("today: ")
    yesterday = input("yesterday: ")
    thirtydaysago = input("30 days ago: ")


def str_2_datetime(date_string):
    return strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
        

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
