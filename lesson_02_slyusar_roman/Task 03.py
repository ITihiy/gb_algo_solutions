"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

try:
    number = int(input("Введите натуральное число: "))

    str_int = str(number)

    print("Перевернули: ", end='')
    for elem in reversed(str_int):
        print(elem, end='')

except ValueError:
    print("Вы ввели не натуральное число!")