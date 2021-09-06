# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# version 1.0
from functools import reduce
num = input('Enter 3 digit number ')
s = sum(map(int, num))
p = reduce((lambda x, y: x * y), list(map(int, num)))
print(s, p)


# version 2.0
number = input('Enter 3 digit number ')
if 1000 > int(number) > 99:
    s = 0
    p = 1
    for i in number:
        s += int(i)
        p *= int(i)
    print(s, p)
else:
    print('Invalid number!')
