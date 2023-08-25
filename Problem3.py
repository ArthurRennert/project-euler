import math

def largest_prime_factor(of_num):
    sqrt_of_num = int(math.sqrt(of_num))
    for i in range(int(math.sqrt(of_num)), 2, -1):
        print("i: " + str(i))
        if is_prime(i) and of_num % i == 0:
            return i


def is_prime(num):
    divide_by = 2
    divide_by_until = int(math.sqrt(num))
    while divide_by != divide_by_until:
        if num % divide_by == 0:
            return False
        divide_by += 1
    return True


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
    # print(largest_prime_factor(13195))
