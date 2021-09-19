# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

BASE = 16

hex_dict = {hex(x)[2:].upper(): x for x in range(BASE)}
reverse_hex_dict = {value: key for key, value in hex_dict.items()}


def prepare_numbers(a, b):
    result_a, result_b = list(a), list(b)
    if len(result_a) > len(result_b):
        result_b = ['0'] * (len(result_a) - len(result_b)) + result_b
    else:
        result_a = ['0'] * (len(result_b) - len(result_a)) + result_a
    return result_a, result_b


def sum_hex_array(hex_array):
    sum_result = ['0']
    for number in hex_array:
        sum_result = sum_hex(*prepare_numbers(sum_result, number))
    return sum_result


def sum_hex(a, b):
    result = []
    carry = 0
    for pair in zip(a[::-1], b[::-1]):
        a, b = hex_dict[pair[0]], hex_dict[pair[1]] + carry
        carry, div_res = divmod(a + b, BASE)
        result.append(reverse_hex_dict[div_res])
    if carry:
        result.append(reverse_hex_dict[carry])
    return result[::-1]


# Умножение наверное можно было сделать и поаккуратнее
def mul_hex(a, b):
    result = []
    for index, current in enumerate(a[::-1]):
        carry = 0
        intermediate_array = [] + ['0'] * index
        for second_current in b[::-1]:
            mul_res = (hex_dict[current] * hex_dict[second_current]) + carry
            carry, div_res = divmod(mul_res, BASE)
            intermediate_array.append(reverse_hex_dict[div_res])
        if carry:
            intermediate_array.append(reverse_hex_dict[carry])
        if all(x != 0 for x in intermediate_array):
            result.append(intermediate_array[::-1])
    return sum_hex_array(result)


raw_a, raw_b = input('Please input two HEX numbers: ').split()
list_a, list_b = prepare_numbers(raw_a.upper(), raw_b.upper())
print(f'Sum of {raw_a.upper()} and {raw_b.upper()}: {sum_hex(list_a, list_b)}')
print(f'Mul of {raw_a.upper()} and {raw_b.upper()}: {mul_hex(list_a, list_b)}')
