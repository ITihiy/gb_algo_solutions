# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
# реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import choices, seed

LIST_SIZE = 10


def bubble_sort(lst):
    n = 0
    run_count = 0
    while n < len(lst) - 1:
        for j in range(n + 1, len(lst)):
            if lst[j] > lst[n]:
                lst[n], lst[j] = lst[j], lst[n]
            run_count += 1
        n += 1
    return run_count


def bubble_sort_with_swapped(lst):
    n = 0
    run_count = 0
    swapped = True
    while n < len(lst) - 1 and swapped:
        swapped = False
        for j in range(n + 1, len(lst)):
            if lst[j] > lst[n]:
                lst[n], lst[j] = lst[j], lst[n]
                swapped = True
            run_count += 1
        n += 1
    return run_count


if __name__ == '__main__':
    seed(56)
    list_ = choices(range(-100, 100), k=LIST_SIZE)
    print(list_)
    run_count_swapped = bubble_sort_with_swapped(list_)
    print(list_)
    print(f'with swapped {run_count_swapped} runs.')

    print('*' * 80)

    seed(56)
    list_ = choices(range(-100, 100), k=LIST_SIZE)
    print(list_)
    run_count_vanilla = bubble_sort(list_)
    print(list_)
    print(f'without swapped {run_count_vanilla} runs.')
