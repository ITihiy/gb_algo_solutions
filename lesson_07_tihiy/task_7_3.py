# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
# сложно, то используйте метод сортировки, который не рассматривался на уроках

import random

N = 10


def partition(lst, left, right, pivot_index):
    pivot_value = lst[pivot_index]
    lst[pivot_index], lst[right] = lst[right], lst[pivot_index]
    current_index = left
    for i in range(left, right):
        if lst[i] < pivot_value:
            lst[current_index], lst[i] = lst[i], lst[current_index]
            current_index += 1
    lst[right], lst[current_index] = lst[current_index], lst[right]
    return current_index


# Сделал через quick select, median of medians не осилил
def quick_select(lst, left, right, k):
    if left == right:
        return lst[left]
    pivot_index = partition(lst, left, right, len(lst) // 2)
    if k == pivot_index:
        return lst[k]
    elif k < pivot_index:
        return quick_select(lst, left, pivot_index - 1, k)
    else:
        return quick_select(lst, pivot_index + 1, right, k)


if __name__ == '__main__':
    list_ = random.choices(range(0, 101), k=N * 2 + 1)
    print(f'Unsorted: {list_}')
    print(f'\nMedian: {quick_select(list_, 0, len(list_) - 1, len(list_) // 2)}\n')
    print(f'Sorted: {sorted(list_)}')
