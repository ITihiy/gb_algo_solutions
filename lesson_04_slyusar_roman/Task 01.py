"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.

Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# Будем исследовать решение для: "В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве."

# Оценим сложност алгоритма.
#       - В реализации randrange я увидел только условия if, принимаем сложность O(1)
#       - Предположим, что в переменную emulate_list мы генерируем список размерности N, тогда сложность
#       данной строки будет O(N)
#       - print имеет сложность O(1)
#       - Строка с negative_elements будет иметь сложность O(N)
#       - Скорее всего у функции max() сложность будет также O(N)
#       - ИТОГ: верхняя граница оценки сложности данного алгоритма O(N)
import cProfile
import random

emulate_list = [random.randrange(-100, 100) for x in range(1, 100000)]
print(f'Сгенерированный список: {emulate_list}')
negative_elements = [x for x in emulate_list if x < 0]
found_max = max(negative_elements)
print(f'Вариант 1. Максимальный отрицательный элемент: {found_max}. Его индекс'
      f' {emulate_list.index(found_max)}')

# Напишем другую реализацию алгоритма:
the_largest_of_the_negative_key = 0
the_largest_of_the_negative_value = -100
for key, item in enumerate(emulate_list):
    if item > -1:
        continue
    if the_largest_of_the_negative_value < item:
        the_largest_of_the_negative_value = item
        the_largest_of_the_negative_key = key
print(f"Вариант 2. Максимальный отрицательный элемент: {the_largest_of_the_negative_value}. Его индекс"
      f" {the_largest_of_the_negative_key}")


# Оформим для оценки времени выполнения первого варианта:
def option_1():
    negative_elements_2 = [x for x in emulate_list if x < 0]
    found_max_2 = max(negative_elements_2)


# Оформим для оценки времени выполнения второго варианта:
def option_2():
    the_largest_of_the_negative_key_2 = 0
    the_largest_of_the_negative_value_2 = -100
    for key_2, item_2 in enumerate(emulate_list):
        if item_2 > -1:
            continue
        if the_largest_of_the_negative_value_2 < item_2:
            the_largest_of_the_negative_value_2 = item_2
            the_largest_of_the_negative_key_2 = key_2


def main():
    option_1()
    option_2()


"""
    Вывод: первый вариант быстрее
    
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 Task 01.py:43(option_1)
        1    0.003    0.003    0.003    0.003 Task 01.py:44(<listcomp>)
        1    0.005    0.005    0.005    0.005 Task 01.py:49(option_2)
        1    0.000    0.000    0.009    0.009 Task 01.py:60(main)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
cProfile.run('main()')
