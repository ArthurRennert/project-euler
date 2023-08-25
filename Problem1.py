def func(to_num):
    res = 0
    for i in range(1, to_num):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


if __name__ == '__main__':
    print(func(1000))
