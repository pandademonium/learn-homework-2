"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv 

dicty_dict = [
    { 
        "name": "Masha", "age": 19, "job": "bartender"   
    },
    {
        "name": "Dima", "age": 29, "job": "teacher"   
    },
    {
        "name": "Nicolas", "age": 22, "job": "tutor"   
    },
    {
        "name": "Sasha", "age": 33, "job": "doctor"   
    },
    {
        "name": "Olga", "age": 31, "job": "dentist"   
    }
]
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open("sample.csv", "w", newline='') as csv_file:
        field_names = ["name", "age", "job"]
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for item in dicty_dict:
            writer.writerow(item)

if __name__ == "__main__":
    main()
