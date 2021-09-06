"""
7. По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков.

Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или равносторонним.
"""

first_length = int(input("Введите длину первого отрезка: "))
second_length = int(input("Введите длину второго отрезка: "))
third_length = int(input("Введите длину третьего отрезка: "))

if first_length <= 0 or second_length <= 0 or third_length <= 0:
    print("Error. Some length incorrect.")
else:
    if first_length == second_length == third_length:
        print("Случай 1. Треугольник равносторонний.")
    elif (first_length == second_length) or (second_length == third_length) or (third_length == first_length):
        print("Случай 2. Треугольник равнобедренный.")
    else:
        print("Случай 3. Треугольник разносторонний.")


