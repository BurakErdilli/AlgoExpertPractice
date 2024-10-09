def zigzagTraverse(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    traversed = []

    # Start from the top-left corner
    i, j = 0, 0
    direction = 1  # 1 for down-right, -1 for up-left

    while len(traversed) < rows * cols:
        traversed.append(matrix[i][j])

        # Determine the next cell
        if direction == 1:  # Moving down-right
            if j == cols - 1:  # Reached the last column
                i += 1
                direction = -1
            elif i == 0:  # Reached the first row
                j += 1
                direction = -1
            else:
                i -= 1
                j += 1
        else:  # Moving up-left
            if i == rows - 1:  # Reached the last row
                j += 1
                direction = 1
            elif j == 0:  # Reached the first column
                i += 1
                direction = 1
            else:
                i += 1
                j -= 1

    return traversed


# Example usage
matrix = [
    [1,  3,  4,  10],
    [2,  5,  9,  11],
    [6,  8,  12, 15],
    [7,  13, 14, 16]
]

result = zigzagTraverse(matrix)
print(result)  # Output should be the zigzag traversal of the matrix
