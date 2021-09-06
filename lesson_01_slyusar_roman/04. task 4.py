"""
4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

# Тут недостает множества проверок, но мы же про алгоритмы...

print("Сгенерируем случайное целое число в указанных границах.")
left_border_int = int(input("Ограничение слева: "))
right_border_int = int(input("Ограничение справа: "))
print(random.randint(left_border_int, right_border_int))

print("Сгенерируем случайное вещественное число в указанных границах.")
left_border_float = int(input("Ограничение слева: "))
right_border_float = int(input("Ограничение справа: "))
print(random.uniform(left_border_int, right_border_int))

print("Сгенерируем случайный символ в указанных границах.")
left_border_char = str(input("Символ ограничения слева: "))
right_border_char = str(input("Символ ограничения справа: "))

left_border_char_index = alphabet.index(left_border_char)
right_border_char_index = alphabet.index(right_border_char)

print(random.choice(alphabet[left_border_char_index: right_border_char_index]))
