def kadane(array):
    maxSum = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        maxSum = max(maxSum+array[i], array[i])
        maxSoFar = max(maxSoFar, maxSum)

    return maxSoFar


array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

a = kadane(array)
