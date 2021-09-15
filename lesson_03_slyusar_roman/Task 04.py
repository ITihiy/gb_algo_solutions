"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

emulate_list = []

for i in range(100):
    emulate_list += [random.randint(1, 20)]

print(f"Сгенерированный список: {emulate_list}")

# Решение из сети
print("Число в массиве,которое встречается чаще всего", max(emulate_list, key=emulate_list.count))

# Мое решение с частотным распределением

frequency = {}
for number in emulate_list:
    if number in frequency.keys():
        frequency.update({number: (frequency.get(number) + 1)})
    else:
        frequency.update({number: 1})

sorted_tuples = sorted(frequency.items(), key=lambda item: item[1])

sorted_frequency = dict(sorted_tuples[::-1])

print("Частотное распределение: ")
print("Число\tколичество вхождений")
for key, value in sorted_frequency.items():
    print(f"{key} \t\t ({value}) {'+' * value}")

