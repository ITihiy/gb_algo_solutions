"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random


def pop_min_element(target_list: list) -> int:
    """
    Функция возвращает первый встреченный минимальный жлемент из списка, удаляя данный элемент из списка
    :param target_list:
    :return:
    """
    min_value = target_list.pop(target_list.index(min(target_list)))
    return min_value


emulate_list = [random.randrange(1, 100) for x in range(1, 20)]

print(f"Сгенерированный список: {emulate_list}")

first_min_value = pop_min_element(emulate_list)
second_min_value = pop_min_element(emulate_list)

print(f"Первый минимальный элемент: {first_min_value}\nВторой минимальный элемент: {second_min_value}")
