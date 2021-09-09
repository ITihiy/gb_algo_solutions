# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

MATRIX_ROWS = 4

matrix = []

for _ in range(MATRIX_ROWS):
    user_input = input('Please input list of 4 integers: ').split()
    int_row = [int(x) for x in user_input]
    matrix.append(int_row + [sum(int_row)])

for row in matrix:
    print(*row, sep='\t')
    print()
