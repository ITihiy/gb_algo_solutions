# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import choices, randint

LOWER_NUM_BOUND = 0
UPPER_NUM_BOUND = 10000
LOWER_COUNT_BOUND = 10
UPPER_COUNT_BOUND = 200

list_of_numbers = choices(range(LOWER_NUM_BOUND, UPPER_NUM_BOUND), k=randint(LOWER_COUNT_BOUND, UPPER_COUNT_BOUND))

max_index = list_of_numbers.index(max(list_of_numbers))
min_index = list_of_numbers.index(min(list_of_numbers))

if min_index > max_index:
    min_index, max_index = max_index, min_index

print(f'Sum of elements between min and max elements is {sum(list_of_numbers[min_index + 1:max_index])}')
