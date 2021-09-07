"""
7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def sum_of_natural_numbers(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


def other_side_of_expression(n):
    result = n * (n + 1) / 2
    return int(result)


def is_equal(conclusion=True):
    text = ""
    if conclusion == True:
        text = "ВЫПОЛНЯЕТСЯ"
    else:
        text = "НЕВЫПОЛНЯЕТСЯ"
    print(f"Равенство 1+2+...+n = n(n+1)/2 {text} для {n = }")


while True:
    try:
        n = int(input("Введите число n: "))
        if n < 1:
            raise ValueError()
        break
    except ValueError:
        print("Вы ввели не натуральное число!")

if sum_of_natural_numbers(n) == other_side_of_expression(n):
    is_equal(True)
else:
    is_equal(False)
