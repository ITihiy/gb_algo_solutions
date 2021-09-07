"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
"""

import random

secret_number = random.randint(0, 100)
number_of_attempts = 10  # Колличество попыток
count = 1

print("Начнем!")

while True:
    if number_of_attempts == count:
        print(f"Попытки закончены. Вы не угадали. Было загадано число {secret_number}")
        break

    # Считываем ввод и сразу проверяем его на ValueError, если ошибки нет, то выходим из цикла
    while True:
        try:
            print(f"---> Это попытка номер {count}:")
            answer = int(input("Угадай число: "))
            break
        except ValueError:
            print("Вы ввели не натуральное число!")

    if answer != secret_number:
        print(f"Не угадал. Ваше число {'больше' if answer > secret_number else 'меньше'} загаданного")

    if answer == secret_number:
        print(f"Ты выиграл. Я действительно загадал {secret_number}")
        break
    count += 1
