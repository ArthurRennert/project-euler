import math
import sympy
import numpy as np
import time

def sieve(limit):
    crosslimit = math.floor(math.sqrt(limit))
    sieve_arr = np.full(limit + 1, False)
    for i in range(4, limit + 1, 2):
        sieve_arr[i] = True
    for i in range(3, crosslimit + 1, 2):
        if not sieve_arr[i]:
            for j in range(i * i, limit + 1, 2 * i):
                sieve_arr[j] = True
    sum = 0
    for i in range(2, limit + 1):
        if not sieve_arr[i]:
            sum += i
    return sum


def sieve_optimised(limit):
    sievebound = (limit - 1) / 2
    crosslimit = (math.floor(math.sqrt(limit)) - 1) / 2
    sieve_arr = np.full(int(sievebound) + 1, False)
    for i in range(1, int(crosslimit)):
        if not sieve_arr[i]:
            for j in range(2 * i * (i+1), int(sievebound) + 1, 2 * i + 1):
                sieve_arr[j] = True
    sum = 2
    for i in range(1, int(sievebound) + 1):
        if not sieve_arr[i]:
            sum += (2 * i + 1)
    return sum


def summation_of_primes(below):
    sum = 0
    curr_num = 1
    while curr_num < below:
        print(curr_num)
        # if is_prime(curr_num):
        if sympy.isprime(curr_num):
            sum += curr_num
            curr_num += 1
        curr_num += 1
    return sum


def is_prime(num):
    divide_by_until = int(num / 2 + 1)
    divide_by = 2
    while divide_by <= divide_by_until:
        if num % divide_by == 0:
            return False
        divide_by += 1
    return True


if __name__ == '__main__':
    # print(summation_of_primes(2000000))
    # start = time.time()
    # print(sieve(2000000))
    # end = time.time()
    # print(end - start)

    start = time.time()
    print(sieve_optimised(2000000))
    end = time.time()
    print(end - start)