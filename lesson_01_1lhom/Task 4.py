# 4.Написать программу, которая генерирует в указанных пользователем границах
#    ● случайное целое число,
#    ● случайное вещественное число,
#    ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если
# надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна
# вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import uniform, randint


def my_random(num1, num2):
    if num1 > num2:  # checking in case user entered first bigger number then second
        val_1 = num2, val_2 = num1
    else:
        val_1 = num1, val_2 = num2

    random_int = randint(val_1, val_2)
    if random_int > 0:  # checking in case user entered negative number
        random_char = chr(random_int)
    else:
        random_char = f'random number is negative'
    random_float = uniform(val_1, val_2)

    return f'My random integer is - {random_int}\n' \
           f'My random float number is - {random_float}\n' \
           f'My random character is - {random_char}\n'


num_1, num_2 = int(input('enter first number, ex. "97" ')), int(input('enter second number, ex. "122" '))
print(my_random(num_1, num_2))  # printing random character a-z
print(my_random(99, 1))  # program can work vise versa from higher to less
print(my_random(-0, -20))  # and also can work with negative numbers
