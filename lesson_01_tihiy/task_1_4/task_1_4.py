import random

# Random int within boundaries
lower = int(input())
upper = int(input())
print(random.randint(lower, upper))

# Random float within boundaries
lower = float(input())
upper = float(input())
print(random.uniform(lower, upper))

# Random symbol
lower = input()
upper = input()
if lower < 'a' or upper > 'z':
    print('ERROR')
print(chr(random.randint(ord(lower), ord(upper))))
