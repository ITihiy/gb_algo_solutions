import matplotlib.pyplot as plt
import math
from lesson_04.task_4_1 import time_function


# В обоих варианах сложность O(n^2).
# get_nth_prime_sieve_of_eratosthenes несмотря на гораздо медленнее растущий run_count выполняется практически
# в два раза дольше. Как я понимаю, за счет операции просеивания решета.
# run_count в обоих случаях растет линейно (рисование графика закомментировано), но тут не учитывается внутренний цикл.
# При n = 10 ** 4 время выполнения становится уже неприличным.


@time_function
def get_nth_prime_conventional(number):
    run_count = 0
    primes = [2]
    prime_candidate = 3
    while len(primes) < number:
        for prime in primes:
            if prime_candidate % prime == 0:
                break
        else:
            primes.append(prime_candidate)
        prime_candidate += 2
        run_count += 1
    return primes[-1], run_count


@time_function
def get_nth_prime_sieve_of_eratosthenes(number):
    sieve = range(2, int(number * math.log(number * math.log(number, math.e), math.e)) + 1)
    primes = []
    run_count = 0
    while sieve:
        p_current = sieve[0]
        primes.append(p_current)
        sieve = [i for i in sieve if i % p_current != 0]
        run_count += 1
        if len(primes) == number:
            break
    return primes[-1], run_count


if __name__ == '__main__':
    n = 30 ** 3

    # xsc = []
    # ysc_conventional = []
    # ysc_eratosthenes = []
    # for i in range(20, 10 ** 4):
    #     _, y_c = get_nth_prime_conventional(i)
    #     _, y_e = get_nth_prime_sieve_of_eratosthenes(i)
    #     xsc.append(i)
    #     ysc_conventional.append(y_c)
    #     ysc_eratosthenes.append(y_e)
    # plt.plot(xsc, ysc_conventional)
    # plt.plot(xsc, ysc_eratosthenes)
    # plt.show()

    print(get_nth_prime_conventional(n))
    print(get_nth_prime_sieve_of_eratosthenes(n))
