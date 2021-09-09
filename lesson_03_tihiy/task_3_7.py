# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

from random import choices, randint

LOWER_NUM_BOUND = 0
UPPER_NUM_BOUND = 10000
LOWER_COUNT_BOUND = 10
UPPER_COUNT_BOUND = 200

list_of_numbers = choices(range(LOWER_NUM_BOUND, UPPER_NUM_BOUND), k=randint(LOWER_COUNT_BOUND, UPPER_COUNT_BOUND))

two_min_numbers = sorted(list_of_numbers)[0:2]

print(f'Two minimum numbers in list_of_numbers are {two_min_numbers[0]} and {two_min_numbers[1]}')
