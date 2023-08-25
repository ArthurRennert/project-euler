import math


def sum_of_squares(num):
    the_sum = 0
    for i in range(1, num + 1):
        the_sum += int(math.pow(i, 2))
    return the_sum


def square_of_sum(num):
    the_sum = 0
    for i in range(1, num + 1):
        the_sum += i
    return int(math.pow(the_sum, 2))


if __name__ == '__main__':
    print(square_of_sum(100) - sum_of_squares(100))



