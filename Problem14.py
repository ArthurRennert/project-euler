import time
import numpy as np

MILLION = 1000000


def longest_collatz_sequence():
    res = -1
    max = 0
    arr = np.full(MILLION, -1, dtype=int)
    for num in range(999999, 500000, -1):
        the_num = num
        count = 0
        while num != 1:
            # if num > max_num:
            #     max_num = num
            if num < MILLION and arr[int(num)] != -1:
                count += arr[int(num)]
                break
            if num % 2 == 0:
                num /= 2
                count += 1
            else:
                num = (num*3 + 1)/2
                count += 2
            # print(int(num))
        if count > max:
            max = count
            res = the_num
        arr[the_num] = count
    # print("max_num: " + str(max_num))
    # return max + 1
    return res


def longest_collatz_sequence_recursive():
    arr = np.full(MILLION, 0, dtype=int)
    longest_chain = 0
    res = -1
    for num in range(int(MILLION/2), MILLION-1):
        curr_chain = count_chain(num, arr)
        # arr[num] = curr_chain
        if curr_chain > longest_chain:
            longest_chain = curr_chain
            res = num
    return res


def count_chain(n, arr):
    if n < MILLION and arr[int(n)] != 0:
        return arr[int(n)]
    if int(n) == 1:
        return 1
    if n % 2 == 0:
        if n < MILLION:
            arr[int(n)] = 1 + count_chain(int(n/2), arr)
        else:
            return 1 + count_chain(int(n/2), arr)
    else:
        if n < MILLION:
            arr[int(n)] = 2 + count_chain(int((3*n + 1)/2), arr)
        else:
            return 2 + count_chain(int((3*n + 1)/2), arr)
    return arr[int(n)]


if __name__ == "__main__":
    start = time.time()
    print(longest_collatz_sequence())
    # print(longest_collatz_sequence_recursive())
    end = time.time()
    print("time passed: " + str(end - start))
