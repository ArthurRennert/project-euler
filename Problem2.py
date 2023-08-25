def fib_sum_to_num(to_num):
    res = 0
    cnt = 0
    fib_sum = fibonacci(cnt)
    while fib_sum <= to_num:
        if fib_sum % 2 == 0:
            res += fib_sum
        cnt += 1
        fib_sum = fibonacci(cnt)
    return res


def fibonacci(to_num):
    if to_num == 1:
        return 1
    if to_num == 0:
        return 0
    return fibonacci(to_num - 1) + fibonacci(to_num - 2)


if __name__ == '__main__':
    print(fib_sum_to_num(4000000))
