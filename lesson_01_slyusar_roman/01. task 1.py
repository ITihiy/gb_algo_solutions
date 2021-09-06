"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

three_digit_number = int(input("Введите трехзначное число: "))

# Можно и математическими операциями наити единица, десятки и сотни, но так проще
srt_three_digit_number = str(three_digit_number)

if len(srt_three_digit_number) != 3:
    print("Error! This is not three-digit number.")
else:
    units = int(srt_three_digit_number[-1])
    tens = int(srt_three_digit_number[-2])
    hundreds = int(srt_three_digit_number[-3])

    print(f"Сумма цифр трехзначного числа: {units+tens+hundreds}")
    print(f"Произведение цифр трехзначного числа: {units*tens*hundreds}")
