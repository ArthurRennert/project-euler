import numpy as np


def solve1():
    return sum(map(int, str(2**1000)))


def solve2():
    res = 2 ** 1000
    res_len = len(str(res))

    res_digits_sum = 0
    for i in range(1, res_len + 1):
        res_digits_sum += res % 10
        res = res // 10
    return res_digits_sum


def solve3():
    order = 0
    digits = int(np.floor(1 + 1000 * np.log10(2)))
    number = np.full(digits, 0, dtype=np.int64)
    number[0] = 1
    for i in range(0, 1000):
        carry = 0
        j = 0
        # for j in range(0, order + 1): python evaluates 'order' only first time the loop enters and changes to 'order' doesn't cause python to evaluate 'order' again in this loop run
        while j <= order:
            product = 2 * number[j] + carry
            number[j] = product % 10
            carry = int(product / 10)

            if j == order and carry > 0:
                order += 1
            j += 1
    # print(number[0])
    # print(np.flip(number))
    return sum(number)


if __name__ == "__main__":
    print(solve3())
    # print(solve1())
