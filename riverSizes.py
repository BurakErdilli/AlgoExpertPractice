def riverSizes(matrix):
    sizes = []
    visited = [[False for _ in row]
               for row in matrix]  # Track which nodes are visited
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue  # Skip already visited nodes
            sizes = traverseNode(i, j, matrix, visited, sizes)

    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [(i, j)]  # Stack to explore nodes
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i, j = currentNode
        if visited[i][j]:
            continue  # Skip already visited nodes
        visited[i][j] = True  # Mark node as visited
        if matrix[i][j] == 0:
            continue  # If it's land (0), move to the next node
        currentRiverSize += 1
        # Explore neighboring nodes (up, down, left, right)
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

    return sizes


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:  # Up
        unvisitedNeighbors.append((i - 1, j))
    if i < len(matrix) - 1 and not visited[i + 1][j]:  # Down
        unvisitedNeighbors.append((i + 1, j))
    if j > 0 and not visited[i][j - 1]:  # Left
        unvisitedNeighbors.append((i, j - 1))
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:  # Right
        unvisitedNeighbors.append((i, j + 1))
        # print(unvisitedNeighbors)
    return unvisitedNeighbors


# Example test
matrix = [
    [1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0]
]

sizes = riverSizes(matrix)
print("River Sizes:", sizes)
