"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений. Завершение программы
должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""

supported_operations = ['+', '-', '*', '/']
string_for_exit = '0'


while True:
    try:
        print("-------------------------------->")
        int_1 = int(input("Введите первое число: "))
        int_2 = int(input("Введите второе число: "))
        operation = str(input(f"Введите знак операции {supported_operations} или '{string_for_exit}' для "
                              f"выхода: "))

        if operation == '0':
            print("Заходи еще. Пока!")
            break

        if operation not in supported_operations:
            print(f"Внимание! Поддерживаются только операции {supported_operations}")
            operation = str(input(f"Введите знак операции {supported_operations} или '{string_for_exit}' для "
                                  f"выхода: "))

        if operation == '+':
            print(f"{int_1} + {int_2} = {int_1 + int_2}")
        elif operation == '-':
            print(f"{int_1} - {int_2} = {int_1 - int_2}")
        elif operation == '*':
            print(f"{int_1} * {int_2} = {int_1 * int_2}")
        elif operation == '/':
            if int_2 == 0:
                print("Не дели на 0!")
                continue
            print(f"{int_1} / {int_2} = {int_1 / int_2}")
        else:
            print("Произошло что-то из ряда вон!")

    except ValueError:
        print("Введены некорректные значения!")
