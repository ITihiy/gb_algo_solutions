"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

even_digits_count = 0
odd_digits_count = 0

try:
    number = int(input("Введите натуральное число: "))

    str_int = str(number)

    for i in str_int:
        if int(i) % 2 == 0:
            even_digits_count += 1
        else:
            odd_digits_count += 1

    print(f"В этом числе {even_digits_count} четных цифр и {odd_digits_count} нечетных цифр.")

except ValueError:
    print("Вы ввели не натуральное число!")
