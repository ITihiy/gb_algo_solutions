"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

some_list = [7, 1, 4, 15, 4, 30, 99, 5]

# Найдет первое вхождение для минимального и максимального элемента, даже если в списке есть еще такие же
min_element_index = some_list.index(min(some_list))
min_element_value = some_list[min_element_index]

max_element_index = some_list.index(max(some_list))
max_element_value = some_list[max_element_index]

# Меняем местами
some_list[min_element_index] = max_element_value
some_list[max_element_index] = min_element_value

print(some_list)
