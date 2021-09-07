"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
(n) вводится с клавиатуры.
"""

count = 1
sum_series_elements = 1
element = sum_series_elements
set_minus = True

while True:
    try:
        n = int(input("Введите число элементов в ряду: "))
        break
    except ValueError:
        print("Вы ввели не натуральное число элементов!")

while count <= n:

    element = element / 2
    if set_minus:
        element = -element
        set_minus = False
    else:
        element = abs(element)
        set_minus = True

    sum_series_elements += element
    count += 1

print(f"Результат вычислений: {sum_series_elements}")
