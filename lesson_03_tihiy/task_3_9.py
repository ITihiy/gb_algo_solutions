# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint, choices

LOWER_SIZE = 5
UPPER_SIZE = 20
LOWER_NUM_BOUND = -100
UPPER_NUM_BOUND = 101

rows = randint(LOWER_SIZE, UPPER_SIZE)
cols = randint(LOWER_SIZE, UPPER_SIZE)

matrix = [choices(range(LOWER_NUM_BOUND, UPPER_NUM_BOUND), k=cols) for _ in range(rows)]

result = max(min(matrix[row][col] for row in range(rows)) for col in range(cols))

print(f'Max element in columns minimums is {result}')
