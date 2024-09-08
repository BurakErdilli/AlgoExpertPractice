def bubbleSort(array):
    # Outer loop for each pass over the array
    for i in range(len(array)-1):
        # Inner loop to compare adjacent elements
        for j in range(0, len(array) - i - 1):
            # Swap if the current element is greater than the next
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# Example usage
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubbleSort(array)
print("Sorted array:", sorted_array)
