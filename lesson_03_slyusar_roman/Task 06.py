"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random


def get_sum(from_index: int, to_index: int, in_list: list) -> int:
    """
    Функция служит для возвращения суммы элементов между заданными индексами в списке.
    Значения заданных индексов не включаются в сумму.
    :param from_index: с какого индекса
    :param to_index: по какой индекс
    :param in_list: в каком списке суммировать
    :return: возвращает сумму элеметнтов списка
    """
    sum_of_values = sum(in_list[from_index + 1: to_index])
    return sum_of_values


emulate_list = [random.randrange(-100, 100) for x in range(1, 20)]

print(f"Сгенерированный список: {emulate_list}")

min_element_index = emulate_list.index(min(emulate_list))
max_element_index = emulate_list.index(max(emulate_list))

if min_element_index < max_element_index:
    print(f"Сумма элементов между минимальным и максимальным значениями: "
          f"{get_sum(min_element_index, max_element_index, emulate_list)}")
else:
    print(f"Сумма элементов между минимальным и максимальным значениями: "
          f"{get_sum(max_element_index, min_element_index, emulate_list)}")
