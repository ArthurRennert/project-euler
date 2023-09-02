import math
import numpy as np
import time


def highly_divisible_tringular_number(num_of_divisors_required):
    divisors = 0
    num = 0
    next_num_to_add = 1
    while divisors < num_of_divisors_required + 1:
        # print(num)
        num += next_num_to_add
        # print(num)
        divisors = num_of_divisors2(num)
        next_num_to_add += 1
    return num


def num_of_divisors(num):
    res = 0
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            res += 1
    return res


def num_of_divisors2(num):
    res = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            res += 1
            # print(i)
        if i != (num / i) and num % int(num / i) == 0:
            res += 1
            # print("i: " + str(i) + " num / i: " + str(num / i))
    return res


def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False

    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True


def prime_array_generator(limit):
    prime_arr = np.empty(limit, dtype=int)
    ind = 0
    i = 2
    while ind < limit:
        if is_prime(i):
            prime_arr[ind] = i
            ind += 1
        i += 1

    # for i in range(0, limit):
    #     print(prime_arr[i])
    return prime_arr


def highly_divisible_tringular_number_optimised(num, primes_arr):
    t = 1
    a = 1
    cnt = 0
    while cnt <= num:
        cnt = 1
        a = a + 1
        t = t + a
        tt = t
        for i in range(0, len(primes_arr)):
            if primes_arr[i] * primes_arr[i] > tt:
                cnt *= 2
                break

            exponent = 1
            while tt % primes_arr[i] == 0:
                exponent += 1
                tt /= primes_arr[i]
            if exponent > 1:
                cnt *= exponent
            if tt == 1:
                break
    return t


def highly_divisible_tringular_number_optimised2(num, primes_arr):
    n = 3
    Dn = 2
    cnt = 0
    while cnt <= num:
        n += 1
        n1 = n
        if n1 % 2 == 0:
            n1 = n1 / 2
        Dn1 = 1

        for i in range(0, len(primes_arr)):
            if primes_arr[i] * primes_arr[i] > n1:
                Dn1 *= 2
                break

            exponent = 1
            while n1 % primes_arr[i] == 0:
                exponent += 1
                n1 /= primes_arr[i]
            if exponent > 1:
                Dn1 *= exponent
            if n1 == 1:
                break
        cnt = Dn * Dn1
        Dn = Dn1
    return int(n * (n - 1) / 2)


if __name__ == '__main__':
    arr = prime_array_generator(7000)

    start = time.time()
    print(highly_divisible_tringular_number_optimised(500, arr))
    end = time.time()
    print(end - start)

    start = time.time()
    print(highly_divisible_tringular_number_optimised2(500, arr))
    end = time.time()
    print(end - start)

    # print(highly_divisible_tringular_number(5))
    # print(num_of_divisors2(28))

