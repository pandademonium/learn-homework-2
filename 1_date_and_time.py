"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from time import strptime
from datetime import datetime, timedelta

def print_days():
    while True:
        command = input(". для выхода.\nвыбери сегодня, вчера, или Х дней назад: ")
        if command == '.':
            print("________________________________________")
            break
        elif len(command.split()) > 1:
            try:
                print(f"{command}: {datetime.now() - timedelta(int(command.split()[0]))}")
            except TypeError:
                print(f"неправильный формат комманды /'{command}/'")
        elif command == 'сегодня':
            print(f"{command}: {datetime.now()}")
        elif command == 'вчера':
            print(f"{command}: {datetime.now() - timedelta(1)}")
        else:
            print(f"неправильный формат /'{command}/'")




def str_2_datetime(date_string):
    return strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
        

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
