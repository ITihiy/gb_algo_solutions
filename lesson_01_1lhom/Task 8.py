# 8. Определить, является ли год, который ввел пользователем, високосным или не високосным.

year = int(input('enter year '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'{year} is leap year ')
else:
    print(f'{year} is not leap year ')
