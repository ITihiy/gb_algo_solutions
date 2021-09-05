# Read 3 numbers
a, b, c = (float(input()) for _ in range(3))

if b <= a <= c or c <= a <= b:
    print(f'Middle number is {a}')
elif a <= b <= c or c <= b <= a:
    print(f'Middle number is {b}')
else:
    print(f'Middle number is {c}')
