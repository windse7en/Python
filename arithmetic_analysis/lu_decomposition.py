"""Lower-Upper (LU) Decomposition."""

# lower–upper (LU) decomposition - https://en.wikipedia.org/wiki/LU_decomposition
"""LU decomposition
解决矩阵的问题，L是对角线是1的矩阵，之后按这个方向一行一行来计算值，填入分别的矩阵。
"""
import numpy


def LUDecompose(table):
    # Table that contains our data
    # Table has to be a square array so we need to check first
    rows, columns = numpy.shape(table)
    L = numpy.zeros((rows, columns))
    U = numpy.zeros((rows, columns))
    if rows != columns:
        return []
    for i in range(columns):
        for j in range(i - 1):
            sum = 0
            for k in range(j - 1):
                sum += L[i][k] * U[k][j]
            L[i][j] = (table[i][j] - sum) / U[j][j]
        L[i][i] = 1
        for j in range(i - 1, columns):
            sum1 = 0
            for k in range(i - 1):
                sum1 += L[i][k] * U[k][j]
            U[i][j] = table[i][j] - sum1
    return L, U


if __name__ == "__main__":
    matrix = numpy.array([[2, -2, 1],
                          [0, 1, 2],
                          [5, 3, 1]])
    L, U = LUDecompose(matrix)
    print(L)
    print(U)
