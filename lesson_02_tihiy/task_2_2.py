number = input('Please input a number: ')
print(f'Even numbers: {sum(1 for x in number if not int(x) & 1)}')
print(f'Odd numbers: {sum(1 for x in number if int(x) & 1)}')
