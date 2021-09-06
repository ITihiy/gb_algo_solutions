import math

number = input('Please input a number: ')

# Cheater version
print(number[::-1])

# Honest version
result = 0
int_number = int(number)
while int_number:
    result += (int_number % 10) * (10 ** int(math.log10(int_number)))
    int_number //= 10
print(result)
