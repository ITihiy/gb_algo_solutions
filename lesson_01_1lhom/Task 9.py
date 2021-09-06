# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше
# другого).

my_list = [input('first number: '), input('second number: '), input('third number: ')]

for num in my_list:
    if min(my_list) < num < max(my_list):
        print('average number is', num)
