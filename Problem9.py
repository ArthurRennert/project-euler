import math


def special_pythagorean_triplet(of_num):
    first_num = 1
    second_num = 1
    third_num = of_num - first_num - second_num

    while True:
        if int(math.pow(first_num, 2)) + int(math.pow(second_num, 2)) == int(math.pow(third_num, 2)):
            # print("first_num: " + str(first_num) + "\nsecond_num: " + str(second_num) + "\nthird_num: " + str(third_num))
            return first_num * second_num * third_num
        else:
            second_num += 1
            if second_num == of_num - 2:
                first_num += 1
                second_num = first_num + 1
            third_num = of_num - first_num - second_num


if __name__ == '__main__':
    print(special_pythagorean_triplet(1000))
