import numpy as np


def solve1():
    number = np.full(1001, 0, dtype=int)
    number[1], number[2], number[3], number[4], number[5], number[6], number[7], number[8], number[9] = 3, 3, 5, 4, 4, 3, 5, 5, 4
    number[10], number[11], number[12], number[13], number[14], number[15], number[16], number[17], number[18], number[19] = 3, 6, 6, 8, 8, 7, 7, 9, 8, 8
    number[20], number[30], number[40], number[50], number[60], number[70], number[80], number[90] = 6, 6, 5, 5, 5, 7, 6, 6

    for i in range(21, 1001):
        num_len = len(str(i))
        if num_len == 2:
            number[i] = number[i % 10] + number[i - (i % 10)]
            continue
        elif num_len == 3:
            number[i] += number[int(i / 100)]
            number[i] += len('hundred')
            if i % 100 != 0:
                number[i] += len('and')
            else:
                continue
            if 1 <= i % 100 <= 19:
                number[i] += number[i % 100]
            elif int(i % 100) % 10 == 0:
                number[i] += number[i % 100]
            else:
                number[i] += number[i % 10] + number[10 * (int(i / 10) % 10)]
        elif num_len == 4:
            number[i] += len('thousand')
            number[i] += number[int(i / 1000)]
            if i % 1000 != 0:
                number[i] += len('and')
            # need to continue this case to include 4-digit numbers

    return sum(number)


def solve2():
    target = 1001
    answer = 0
    for i in range(1, target):
        words = numbers_to_english(i).replace(" ", "").replace("-", "")
        answer += len(words)
    return answer


def numbers_to_english(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n <= 90 and n % 10 == 0:  # 10, 20, 30, ...
        return tens[n // 10]
    elif 20 < n < 100:  # 21, 22, 23, ... (20, 30, ... exclusive)
        return tens[n // 10] + "-" + ones[n % 10]
    elif 100 <= n <= 900 and n % 100 == 0:  # 100, 200, 300, ....
        return ones[n // 100] + " hundred"
    elif 100 < n < 1000:  # 101, 102, 103, ... (100, 200, 300, ... exclusive)
        return ones[n // 100] + " hundred and " + numbers_to_english(n % 100)
    elif 1000 < n < 10000:
        pass
    elif n == 1000:
        return "one thousand"
    else:
        raise ValueError("unexpected input")


if __name__ == '__main__':
    # print(solve1())
    print(solve2())
