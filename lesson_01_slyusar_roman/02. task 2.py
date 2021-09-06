""""
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
Объяснить полученный результат.
"""

a = 5
b = 6

a_byte = format(a, 'b')
b_byte = format(b, 'b')

rez = []

print("Логическое \"И\": ")
for i in range(len(a_byte)):
    rez.insert(i, int(a_byte[i]) and int(b_byte[i]))

print("Результат: ", ''.join(str(e) for e in rez))

rez = []

print("Логическое \"ИЛИ\": ")
for i in range(len(a_byte)):
    rez.insert(i, int(a_byte[i]) or int(b_byte[i]))

print("Результат: ", ''.join(str(e) for e in rez))


print("Побитовый сдвиг числа 5 на два знака вправо: ")
# Отрезаем у скиска два знака с конца и дописываем два нуля вначале
list_to_right = [0, 0] + list(a_byte)[0:-2]
print(''.join(str(e) for e in list_to_right))

print("Побитовый сдвиг числа 5 на два знака влево: ")
list_to_left = list(a_byte)[2:len(a_byte)] + [0, 0]
print(''.join(str(e) for e in list_to_left))
