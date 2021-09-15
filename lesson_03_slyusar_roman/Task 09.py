"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random


def generate_square_matrix(square_dimension: int) -> list:
    """
    Функция генерирует матрицу размерностью square_dimension
    :param square_dimension: квадратная размерность матрицы для генерации
    :return: вернем сгенерированный список, который иммитирует матрицу
    """
    list_like_matrix = []
    for item in range(square_dimension):
        list_like_matrix += [random.randrange(1, 20) for x in range(1, square_dimension + 1)]
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


def is_index_in_list(some_list: list, index: int) -> bool:
    """
    Функция проверяет, есть ли в списке элемент по зананному индексу
    :param some_list: список для поиска элементов
    :param index: индекс для поиска в списке
    :return: вернет True в случае, если элемент существует, иначе вернет False
    """
    try:
        some_list[index]
    except IndexError:
        return False
    return True


def get_minimum_items_in_columns(some_list_like_matrix: list, dimension: int) -> list:
    """
    Функция вернет список минимальных элементов в каждом столбце для матрицы и ее размерности
    :param some_list_like_matrix: матрица для поиска минимальных значений в столбцах
    :param dimension: размерность квадратной матрицы
    :return: список минимальных элементов в каждом столбце
    """
    count = 0
    row_from_matrix_with_min = []
    for value in emulate_list_like_matrix:
        if count % 5 == 0:
            count = 0
        if is_index_in_list(row_from_matrix_with_min, count):
            row_from_matrix_with_min[count] = min(value, row_from_matrix_with_min[count])
        else:
            row_from_matrix_with_min.insert(count, value)
        count += 1
    return row_from_matrix_with_min


square_dimension_for_matrix = 5

emulate_list_like_matrix = generate_square_matrix(square_dimension_for_matrix)
print("Сгенерированная матрица:")
show_matrix(emulate_list_like_matrix, square_dimension_for_matrix)
min_elements = get_minimum_items_in_columns(emulate_list_like_matrix, square_dimension_for_matrix)

print(f"Минимальный элемент в каждом столбце: {min_elements}")
print(f"Максимальный элемент среди минимальных элементов столбцов матрицы: {max(min_elements)}")
