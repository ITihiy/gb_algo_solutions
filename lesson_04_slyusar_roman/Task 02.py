"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import cProfile


# Используем алгоритм решето Эратосфена
def sieve_of_eratosthenes():
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                numbers[candidate - 2] = 0
    print("Метод 1. Простые числа:", *list(filter(lambda x: x != 0, numbers)))


# Напишем другой алгоритм в лоб. Сложность O(N**2)
def not_sieve_of_eratosthenes():
    prime_numbers = {n: 1 for n in range(2, n + 1)}
    for key, value in prime_numbers.items():
        for i in range(2, key):
            if key % i == 0:
                prime_numbers.update({key: 0})

    print("Метод 2. Простые числа: ", end='')
    for key, value in prime_numbers.items():
        if value != 0:
            print(key, end=' ')


n = int(input("Введите число, до которого необходимо найти простые числа: "))


def main():
    sieve_of_eratosthenes()
    not_sieve_of_eratosthenes()


"""
    Вывод: Очевидно, что тупои перебор ощютимо дольше.
    
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.287    2.287 <string>:1(<module>)
        1    0.003    0.003    0.011    0.011 Task 02.py:11(sieve_of_eratosthenes)
     9999    0.001    0.000    0.001    0.000 Task 02.py:17(<lambda>)
        1    2.250    2.250    2.276    2.276 Task 02.py:21(not_sieve_of_eratosthenes)
        1    0.001    0.001    0.001    0.001 Task 02.py:22(<dictcomp>)
        1    0.000    0.000    2.287    2.287 Task 02.py:37(main)
        1    0.000    0.000    2.287    2.287 {built-in method builtins.exec}
     1231    0.024    0.000    0.024    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
    73669    0.008    0.000    0.008    0.000 {method 'update' of 'dict' objects}
"""

cProfile.run('main()')
