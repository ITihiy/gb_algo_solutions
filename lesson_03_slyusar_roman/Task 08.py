"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""
import random


def generate_custom_matrix(square_dimension: int) -> list:
    """
    Функция генерирует матрицу размерностью square_dimension, таким образом, что в каждой строке
    добавляется дополнительное значение для суммы, которое заполняется 0
    :param square_dimension: квадратная размерность матрицы для генерации
    :return: вернем сгенерированный список, который иммитирует матрицу
    """
    list_like_matrix = []
    for item in range(square_dimension):
        list_like_matrix += [random.randrange(1, 20) for x in range(1, square_dimension + 1)] + [0]
    return list_like_matrix


def show_matrix(some_list_like_matrix: list, dimension: int) -> None:
    """
    Функция выводит матрицу в удобном формате
    :param some_list_like_matrix: список для вывода
    :param dimension: сколько элементов в строке нужно выводить
    :return: Ничего не возвращает, просто печатает в консоль
    """
    output = ''
    count = 1
    output += "----------------------------\n"
    for value in some_list_like_matrix:
        if count % dimension == 0:
            output += str(value) + '\t\n'
        else:
            output += str(value) + '\t'
        count += 1
    output += "----------------------------\n"
    print(output)


def sum_items_in_matrix(some_list: list, dimension: int) -> None:
    """
    Функция считает сумму каждой строки матрицы и дописывает ее в последний жлемент строки
    :param some_list: список для подсчета суммы
    :param dimension: размерность строки матрицы
    :return: Ничего не возвращает, изменяя полученный список
    """
    sum_of_elements = 0
    count = 1
    for value in some_list:
        if count % dimension == 0:
            some_list[count - 1] = sum_of_elements
            sum_of_elements = 0
        else:
            sum_of_elements += value
        count += 1


square_dimension_for_matrix = 4
dimension_for_matrix_with_sum_column = 5

emulate_list_like_matrix = generate_custom_matrix(square_dimension_for_matrix)
print("Сгенерированная матрица:")
show_matrix(emulate_list_like_matrix, dimension_for_matrix_with_sum_column)

# Посчитаем сумму в строках
sum_items_in_matrix(emulate_list_like_matrix, dimension_for_matrix_with_sum_column)

# Выведем результат
print("Результирующая матрица:")
show_matrix(emulate_list_like_matrix, dimension_for_matrix_with_sum_column)
