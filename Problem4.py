import math


def biggest_palindrome_product(of_digits):
    first_num = int(math.pow(10, of_digits) - 1)
    second_num = first_num
    curr_max = 0
    while first_num > 1:
        if is_palindrom(first_num * second_num):
            if first_num * second_num > curr_max:
                curr_max = first_num * second_num
            first_num = first_num - 1
            second_num = first_num - 1
        else:
            second_num -= 1
    return curr_max


def is_palindrom(num):
    num_in_str = str(num)
    for i in range(0, int(len(str(num)) / 2)):
        if num_in_str[i] != num_in_str[int(len(str(num)) - 1 - i)]:
            return False
    return True


if __name__ == '__main__':
    print(biggest_palindrome_product(3))
    # print(is_palindrom(9009))


