"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    referat_file = open("referat.txt", "rt")
    referat = referat_file.read()
    words = referat.split()
    words_count = len(words)
    print(f'Количество слов = {words_count}')
    referat = referat.replace('.', '!')
    result_file = open('referat2.txt', 'wt')
    result_file.write(referat)
    


if __name__ == "__main__":
    main()
