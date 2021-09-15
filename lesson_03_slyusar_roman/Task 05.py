"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random

emulate_list = [random.randrange(-100, 100) for x in range(1, 40)]

print(f"Сгенерированный список: {emulate_list}")

negative_elements = [x for x in emulate_list if x < 0]

print(f"Максимальный отрицательный элемент: {max(negative_elements)}")
