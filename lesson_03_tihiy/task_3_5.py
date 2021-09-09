# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import choices, randint

LOWER_NUM_BOUND = -10000
UPPER_NUM_BOUND = 10000
LOWER_COUNT_BOUND = 50
UPPER_COUNT_BOUND = 10000

list_of_numbers = choices(range(LOWER_NUM_BOUND, UPPER_NUM_BOUND), k=randint(LOWER_COUNT_BOUND, UPPER_COUNT_BOUND))
max_negative = max(x for x in list_of_numbers if x < 0)

print(f'Max negative number in list_of_numbers is {max_negative}, on position {list_of_numbers.index(max_negative)}')
