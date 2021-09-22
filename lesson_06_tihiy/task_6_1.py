# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
#
# Python 3.9.7 Windows 64 bit

from array import array

MATRIX_ROWS = 4


# Самый очевидный вариант, но и в то же время самый затратный по памяти (цифры не считал так как их тут мало,
# да и sys.getsizeof не лучший вариант, а с tracemalloc не разобрался)
def matrix_conventional():
    matrix = []
    for _ in range(MATRIX_ROWS):
        user_input = input('Please input list of 4 integers: ').split()
        int_row = [int(x) for x in user_input]
        matrix.append(int_row + [sum(int_row)])

    for row in matrix:
        print(*row, sep='\t')
        print()


# Простая замена скобок уже дает экономию ибо генератор.
def matrix_generator():
    matrix = []
    for i in range(MATRIX_ROWS):
        user_input = input('Please input list of 4 integers: ').split()
        int_row = (int(x) for x in user_input)
        matrix.append([])
        sum_ = 0
        for item in int_row:
            sum_ += item
            matrix[i].append(item)
        matrix[i].append(sum_)

    for row in matrix:
        print(*row, sep='\t')
        print()


# Почти самый правильный вариант на мой взляд. Если размерность чисел известна заранее, то лучше использовать
# array заранее заданной величины. Хотя по памяти занимает и больше чем генератор.
def matrix_array():
    matrix = []
    for i in range(MATRIX_ROWS):
        matrix_row = array('Q', [0, 0, 0, 0, 0])
        sum_ = 0
        for index, value in enumerate(input('Please input list of 4 integers: ').split()):
            int_value = int(value)
            matrix_row[index] = int_value
            sum_ += int_value
        matrix_row[4] = sum_
        matrix.append(matrix_row)
    for row in matrix:
        print(*row, sep='\t')
        print()


if __name__ == '__main__':
    matrix_conventional()
    print('*' * 80)
    matrix_generator()
    print('*' * 80)
    matrix_array()
