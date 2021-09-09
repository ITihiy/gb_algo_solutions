# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for i in range(2, 10):
    print(f'In range 2-99 {sum(1 for x in range(2, 100) if x % i == 0)} numbers are evenly divided by {i}')
