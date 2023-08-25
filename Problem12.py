import math


def highly_divisible_tringular_number(num_of_divisors_required):
    divisors = 0
    num = 0
    next_num_to_add = 1
    while divisors < num_of_divisors_required + 1:
        # print(num)
        num += next_num_to_add
        # print(num)
        divisors = num_of_divisors2(num)
        if divisors > 300:
            print(divisors)
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
        if i != (num / i) and num % (num / i) == 0:
            res += 1
    return res


if __name__ == '__main__':
    print(highly_divisible_tringular_number(500))
    # print(num_of_divisors2(28))
