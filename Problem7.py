
def nth_prime(num):
    curr_num = 2
    prime_found = 0
    while prime_found != num:
        if is_prime(curr_num):
            prime_found += 1
        curr_num += 1
    return curr_num - 1


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(nth_prime(10001))
