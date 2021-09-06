import operator


def quit_calc(a, b):
    print(f'Goodbye. (Fun fact {a} ** {b} = {a ** b})')
    exit(0)


operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '0': quit_calc}

while True:
    number_a, operation, number_b = input('Please input request `a op b` (op 0 to quit): ').split()
    if operation not in operations:
        print('Invalid operation (+ - * / 0)')
    elif operation == '/' and int(number_b) == 0:
        print('Can\'t divide by 0')
    else:
        print(f'{number_a} {operation} {number_b} = {operations[operation](float(number_a), float(number_b))}')
