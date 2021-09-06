def sum_list(number):
    return sum(range(1, number + 1))


def sum_formula(number):
    return (number * (number + 1)) // 2


def print_short_list(number):
    if number < 4:
        return ' + '.join(str(char) for char in range(1, number + 1))
    else:
        return f'1 + 2 + 3 + ... + {number}'


n = int(input('Please enter any positive number: '))

result_list = sum_list(n)
result_form = sum_formula(n)

print('Init:')
print(f'{print_short_list(n)} = {result_list}')
print(f'n(n + 1) / 2 = {result_form}')
print(f'{result_list} = {result_form}')

result_list_1 = sum_list(n + 1)
result_form_1 = sum_formula(n + 1)

print('\nStep: sum of (n + 1)')
print(f'{print_short_list(n + 1)} = {result_list_1}')
print(f'(n + 1)((n + 1) + 1) / 2 = {result_form_1}')
print(f'{result_list_1} = {result_form_1}')
