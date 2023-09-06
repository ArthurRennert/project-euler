import numpy as np

with open('0067_triangle.txt', 'r') as file:
    data = file.read().splitlines()

arr = np.full((len(data), len(data)), 0, dtype=np.int64)


for i in range(0, len(data)):
    list_row = list(map(int, data[i].split(" ")))
    for j in range(0, i + 1):
        arr[i][j] = list_row[j]

for i in range(1, len(data)):
    for j in range(0, i + 1):
        try:
            arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])
        except IndexError:
            arr[i][j] += arr[i-1][j]

# print(arr)
print(max(arr[len(arr) - 1]))


