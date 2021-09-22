# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

LIST_SIZE = 20


def merge_sort(lst):
    if len(lst) > 1:
        middle = len(lst) // 2
        left_part = lst[:middle]
        right_part = lst[middle:]
        merge_sort(left_part)
        merge_sort(right_part)

        # Merge
        left_index = 0
        right_index = 0
        main_index = 0
        while left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index] <= right_part[right_index]:
                lst[main_index] = left_part[left_index]
                left_index += 1
            else:
                lst[main_index] = right_part[right_index]
                right_index += 1
            main_index += 1
        while left_index < len(left_part):
            lst[main_index] = left_part[left_index]
            left_index += 1
            main_index += 1
        while right_index < len(right_part):
            lst[main_index] = right_part[right_index]
            right_index += 1
            main_index += 1


if __name__ == '__main__':
    random.seed(56)
    list_ = [round(random.uniform(0.0, 50.0), 2) for _ in range(LIST_SIZE)]
    print(f'Unsorted: {list_}')
    merge_sort(list_)
    print(f'Sorted: {list_}')
