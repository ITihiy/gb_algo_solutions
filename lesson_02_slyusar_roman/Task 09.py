"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

import random


def get_sum_of_digits_for_number(number: int):
    if not isinstance(number, int):
        return 0
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)
    return sum_of_digits


# Получил рандомный список, как будто это ввод натуральных чисел с клавиатуры
emulate_integers = []
for i in range(10):
    emulate_integers += [random.randint(100, 1000000)]

# Притворимся, что нужное нам число это первое в списке
greatest_number_of_digits = emulate_integers[0]
sum_of_digit = get_sum_of_digits_for_number(emulate_integers[0])

print("Введенные натуральные числа: ", emulate_integers)

# А теперь проверим весь список
for number in emulate_integers:
    temp_sum = get_sum_of_digits_for_number(number)
    if temp_sum > sum_of_digit:
        greatest_number_of_digits = number
        sum_of_digit = temp_sum

print(f"Наибольшее по сумме цифр число {greatest_number_of_digits}, сумма его цифр {sum_of_digit}")
