def subarraySort(array):
    # Helper function to check if a number is out of order
    def isOutOfOrder(i, num, array):
        if i == 0:
            return num > array[i + 1]
        if i == len(array) - 1:
            return num < array[i - 1]
        return num > array[i + 1] or num < array[i - 1]

    # Step 1: Find the unsorted elements
    minOutOfOrder = float('inf')
    maxOutOfOrder = float('-inf')

    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)

    # If no out-of-order elements are found, the array is sorted
    if minOutOfOrder == float('inf'):
        return [-1, -1]

    # Step 2: Find where the subarray starts and ends
    leftIndex = 0
    while minOutOfOrder >= array[leftIndex]:
        leftIndex += 1

    rightIndex = len(array) - 1
    while maxOutOfOrder <= array[rightIndex]:
        rightIndex -= 1

    return [leftIndex, rightIndex]


# Example usage
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
result = subarraySort(array)
print(result)  # Output will be [3, 9]
