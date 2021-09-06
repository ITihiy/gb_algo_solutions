"""
5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

first_char = str(input("Первая буква: "))
second_char = str(input("Вторая буква: "))

first_char_index = alphabet.index(first_char)
second_char_index = alphabet.index(second_char)
amount_char_between_input = len(alphabet[first_char_index+1: second_char_index])

print(
    "Индекс первого символа: ", first_char_index, "\n",
    "Индекс второго символа: ", second_char_index, "\n",
    "Букв между введеными символами: ", amount_char_between_input
)
