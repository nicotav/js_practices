def solution(matrix):
    # array of 0's the same length as the matrix array
    banned = [0] * len(matrix[0])
    matrixElementsSum = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 0):
                banned[j] = 1
            else:
                if (banned[j] == 0):
                    matrixElementsSum += matrix[i][j]
    return matrixElementsSum


toPrint = solution([[1, 1, 1, 0],
                    [0, 5, 0, 1],
                    [2, 1, 3, 10]])


print(toPrint)
