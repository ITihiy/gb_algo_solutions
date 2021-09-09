# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from random import choices, randint

LOWER_NUM_BOUND = 0
UPPER_NUM_BOUND = 10000
LOWER_COUNT_BOUND = 50
UPPER_COUNT_BOUND = 10000

list_of_numbers = choices(range(LOWER_NUM_BOUND, UPPER_NUM_BOUND), k=randint(LOWER_COUNT_BOUND, UPPER_COUNT_BOUND))
result = [index for index, value in enumerate(list_of_numbers) if not value & 1]

print(f'Indices of even elements in list_of_numbers: {result}')
