
def smallest_num_evenly_divisible(to_num):
    the_num = to_num
    while True:
        if is_evenly_divisible(the_num, to_num):
            return the_num
        else:
            the_num += 1


def is_evenly_divisible(the_num, to_num):
    for i in range(to_num, 1, -1):
        if the_num % i != 0:
            return False
    return True


if __name__ == '__main__':
    print(smallest_num_evenly_divisible(20))



