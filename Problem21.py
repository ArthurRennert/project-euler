import math


def find_all_divisors(num):
    divisors_list = []
    for i in range(1, int((num/2)+1)):
        if num/i - math.floor(num/i) == 0:
            divisors_list.append(i)
    return divisors_list


if __name__ == '__main__':

    amicable_numbers_list = []
    for i in range(1, 10001):
        res = sum(find_all_divisors(i))
        if i == res:
            continue
        res2 = sum(find_all_divisors(res))
        if i == res2:
            if i not in amicable_numbers_list:
               amicable_numbers_list.append(i)
            if res not in amicable_numbers_list:
              amicable_numbers_list.append(res)

    # print(amicable_numbers_list)
    print(sum(amicable_numbers_list))


