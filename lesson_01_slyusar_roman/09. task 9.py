"""
9. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).
"""

first_int = int(input("Введите первое число: "))
second_int = int(input("Введите второе число: "))
third_int = int(input("Введите третье число: "))

if first_int <= second_int <= third_int or third_int <= second_int <= first_int:
    print(f"Среднее число: {second_int}")
elif (second_int <= first_int <= third_int) or (third_int <= first_int <= second_int):
    print(f"Среднее число: {first_int}")
else:
    print(f"Среднее число: {third_int}")
