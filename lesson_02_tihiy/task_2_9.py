from random import choices, randint

LOWER_NUM_BOUND = 0
UPPER_NUM_BOUND = 10000
LOWER_COUNT_BOUND = 50
UPPER_COUNT_BOUND = 10000
NUMBER = 0
SUM = 1


def sum_of_digits(number):
    return 0 if number == 0 else (number % 10) + sum_of_digits(number // 10)


list_of_numbers = choices(range(LOWER_NUM_BOUND, UPPER_NUM_BOUND), k=randint(LOWER_COUNT_BOUND, UPPER_COUNT_BOUND))
result = max([(x, sum_of_digits(x)) for x in list_of_numbers], key=lambda x: x[SUM])
print(f'Number {result[NUMBER]} has maximum sum of digits: {result[SUM]}')
