import numpy as np

DIM = 20


def lattice_paths_recursive(row, col, mat):
    if row < 0 or row >= len(mat) or col < 0 or col >= len(mat[0]):
        return 0

    if row == len(mat) - 1 and col == len(mat[0]) - 1:
        return 1

    return lattice_paths_recursive(row, col + 1, mat) + lattice_paths_recursive(row + 1, col, mat)


def lattice_paths_recursive_faster(row, col, mat):
    if row < 0 or row >= len(mat) or col < 0 or col >= len(mat[0]):
        return 0

    if row == len(mat) - 1 and col == len(mat[0]) - 1:
        return 1

    mat[row][col] = lattice_paths_recursive_faster(row+1, col, mat) + lattice_paths_recursive_faster(row, col+1, mat)

    if mat[row][col] != -1:
        return mat[row][col]

    return mat[0][0]


def lattice_paths_dynamic_programming(mat):
    for j in range(len(mat[0]) - 1, -1, -1):
        mat[len(mat) - 1][j] = 1

    for i in range(len(mat) - 1, -1, -1):
        mat[i][len(mat[0]) - 1] = 1

    for i in range(len(mat) - 2, -1, -1):
        for j in range(len(mat) - 2, -1, -1):
            mat[i][j] = mat[i+1][j] + mat[i][j+1]

    return mat[0][0]


#2*DIM nCr DIM
def lattice_paths_combinational_solution(dim):
    res = 1
    for i in range(1, dim+1):
        res *= (dim + i)/i

    return int(np.ceil(res))


if __name__ == "__main__":
    mat = np.full((DIM, DIM), -1, dtype=np.int64)

    # print(lattice_paths_recursive(0, 0, mat))
    # print(lattice_paths_recursive_faster(0, 0, mat))
    # print(mat)
    # print(lattice_paths_dynamic_programming(mat))
    print(lattice_paths_combinational_solution(DIM))
