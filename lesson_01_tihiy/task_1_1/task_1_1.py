number = int(input())

sum_result = 0
sum_number = number
while sum_number != 0:
    sum_result += sum_number % 10
    sum_number //= 10
print(sum_result)

mul_result = 1
mul_number = number
while mul_number != 0:
    mul_result *= mul_number % 10
    mul_number //= 10
print(mul_result)
