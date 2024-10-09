def searchInSortedMatrix(matrix, n):

    length = len(matrix)
    width = len(matrix[0])

    i = 0
    j = 0

    possible_row = length//2
    possible_col = width//2

    while possible_row < length-1:
        value = matrix[possible_row][j]

        if value == n:
            return possible_row, j

        # if valueDown is None or valueUp is None:
        #     break

        if value > n:
            if matrix[possible_row-1][j] is None:
                return -1, -1
            elif matrix[possible_row-1][j] < n:
                possible_row -= 1
                break
            else:
                possible_row -= possible_row//2

        elif value < n:
            if matrix[possible_row+1][j] is None:
                break
            elif matrix[possible_row+1][j] > n:
                break
            else:
                possible_row += possible_row//2

    while possible_col < width-1:
        value = matrix[possible_row][possible_col]
        valueRight = matrix[possible_row][possible_col+1]
        valueDown = matrix[possible_row][possible_col-1]

        # if valueDown is None or valueUp is None:
        #     break

        if value == n:
            return possible_row, possible_col

        if valueRight > n:
            possible_col -= possible_col//2

        if valueUp < n:
            possible_col += possible_col//2


matrix = [
    [1,  3,  5,  7,  9,  11],
    [2,  6,  8,  12, 14, 16],
    [4,  10, 15, 17, 18, 20],
    [13, 19, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]


n = 13
length = len(matrix)
i, j = searchInSortedMatrix(matrix, n)
