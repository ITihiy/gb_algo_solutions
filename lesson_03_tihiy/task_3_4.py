# 4. Определить, какое число в массиве встречается чаще всего.

from random import choices, randint

LOWER_NUM_BOUND = 0
UPPER_NUM_BOUND = 10000
LOWER_COUNT_BOUND = 50
UPPER_COUNT_BOUND = 10000
NUMBER = 0
COUNT = 1

list_of_numbers = choices(range(LOWER_NUM_BOUND, UPPER_NUM_BOUND), k=randint(LOWER_COUNT_BOUND, UPPER_COUNT_BOUND))
result = max([(x, list_of_numbers.count(x)) for x in list_of_numbers], key=lambda x: (x[COUNT], x[NUMBER]))

print(f'Most common number in list_of_numbers is {result[NUMBER]}, with {result[COUNT]} occurrences')
