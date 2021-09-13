# Поверяем как ведут себя различныеязыковые конструкциина примере задания 3.5 (В массиве найти максимальный
# отрицательный элемент. Вывести на экран его значение и позицию в массиве.)
# Формально сложность всех вариантов O(n)

import timeit
import sys
import random


def time_function(func):
    def inner(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        total = timeit.default_timer() - start
        print(f'Function {func.__name__}: {total:.5f}s')
        return result

    return inner


# Вполне ожидаемо последнее место
@time_function
def c_style_while_func(array):
    min_value = -sys.maxsize - 1
    position = -1
    counter = 0
    while counter < len(array):
        if 0 > array[counter] > min_value:
            min_value = array[counter]
            position = counter
        counter += 1
    return min_value, position


# Второе место
@time_function
def for_cycle_func(array):
    min_value = -sys.maxsize - 1
    position = -1
    for index, value in enumerate(array):
        if 0 > value > min_value:
            min_value = value
            position = index
    return min_value, position


###############################################################################
# And we have a winner
@time_function
def list_comprehension_func(array):
    min_value = max(x for x in array if x < 0)
    return min_value, array.index(min_value)


# Разница ровно в 2 раза. Вариант без filter быстрее.

# 3-е место
@time_function
def filter_func(array):
    min_value = max(x for x in filter(lambda n: n < 0, array))
    return min_value, array.index(min_value)


###############################################################################

# Неожиданно предпоследнее место
@time_function
def list_comprehension_short_func(array):
    return max(((x, i) for i, x in enumerate(array) if x < 0), key=lambda t: t[0])


if __name__ == '__main__':
    random.seed(56)
    sample_array = random.choices(range(-(10 ** 5), (10 ** 5) + 1), k=10 ** 7)
    result_1 = c_style_while_func(sample_array)
    result_2 = for_cycle_func(sample_array)
    result_3 = list_comprehension_func(sample_array)
    result_4 = list_comprehension_short_func(sample_array)
    result_5 = filter_func(sample_array)
    print(result_1, result_2, result_3, result_4, result_5)
