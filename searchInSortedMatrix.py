def searchInSortedMatrix(matrix, n):

    length = len(matrix)
    width = len(matrix[0])
    print(width, length)
    i = 0
    j = width-1

    while i < (width-1) and j >= 0:
        if matrix[i][j] == n:
            return i, j
        if matrix[i][j] > n:
            j -= 1

        if matrix[i][j] < n:
            i += 1

    return -1, -1


matrix = [
    [1,  3,  5,  7,  9,  11],
    [2,  6,  8,  12, 14, 16],
    [4,  10, 15, 17, 18, 20],
    [13, 19, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]


n = 5
length = len(matrix)
i, j = searchInSortedMatrix(matrix, n)
