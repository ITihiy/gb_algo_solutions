# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

int_num = int(input('Enter number of character in alphabet :'))
print(f'{int_num} is {chr(int_num + ord("a") - 1)}')
