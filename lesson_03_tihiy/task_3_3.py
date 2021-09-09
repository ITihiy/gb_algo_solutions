# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import choices, randint

LOWER_NUM_BOUND = 0
UPPER_NUM_BOUND = 10000
LOWER_COUNT_BOUND = 10
UPPER_COUNT_BOUND = 20

list_of_numbers = choices(range(LOWER_NUM_BOUND, UPPER_NUM_BOUND), k=randint(LOWER_COUNT_BOUND, UPPER_COUNT_BOUND))

max_index = list_of_numbers.index(max(list_of_numbers))
min_index = list_of_numbers.index(min(list_of_numbers))

list_of_numbers[max_index], list_of_numbers[min_index] = list_of_numbers[min_index], list_of_numbers[max_index]
