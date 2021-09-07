"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

import random

digit_frequency = 0

emulate_sequence_of_numbers = []

for i in range(10):
    emulate_sequence_of_numbers += [random.randint(100, 1000000)]

print("Введенная последовательность чисел: ", emulate_sequence_of_numbers)

while True:
    try:
        search_digit = int(input("Введите цифру для поиска: "))
        if search_digit < 0 or search_digit > 9:
            raise ValueError()
        break
    except ValueError:
        print("Вы ввели не натуральное число!")

search_digit = str(search_digit)

for number in emulate_sequence_of_numbers:
    for digit in str(number):
        if digit == search_digit:
            digit_frequency += 1

print(f"--> Цифра {search_digit} встречалась {digit_frequency} раз")
