"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


def check_function(number: int, range_list: list) -> bool:
    """
    Функция проверяет кратность числа по каждому числу из заданного диапазона
    :param number: число для проверки
    :param range_list: список чисел для проверки кратности
    :return: вернет True, если число кратно всем числам из списка, иначе вернет False
    """
    is_multiple_of_all_numbers = True
    for item in range_list:
        if number % item != 0:
            is_multiple_of_all_numbers = False
    return is_multiple_of_all_numbers


# Странное задание, потому как таких чисел нет в этом диапазоне
print([x for x in range(2, 100) if check_function(x, list(range(2, 10)))])
