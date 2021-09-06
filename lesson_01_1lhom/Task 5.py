# 5.Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько
# между ними находится букв.

first_char = input('enter first character ')
second_char = input('enter second character ')
print(f'first character order number is - {ord(first_char)}\n'
      f'second character order number is - {ord(second_char)}\n'
      f'and there is(are) {(ord(second_char) - ord(first_char)) -1} character(s) between them\n')
