def maxSubsetSum(array):
    if not array:  # Handle empty array case
        return 0
    elif len(array) == 1:  # If only one element, return it
        return array[0]

    # Initialize the two base cases for dynamic programming
    second_last = array[0]  # Max sum including up to the first element
    # Max sum including up to the second element
    last = max(array[0], array[1])

    for i in range(2, len(array)):
        # Max sum including or excluding current element
        current = max(last, second_last + array[i])
        second_last = last  # Update second last to last
        last = current  # Update last to current

    return last


def maxSubsetSumWithIndex(array):
    if not array:  # Handle empty array case
        return 0, [], []  # No sum, no elements, no indexes

    n = len(array)

    if n == 1:  # If only one element, return it
        return array[0], [array[0]], [0]

    # Initialize the base cases for dynamic programming
    dp = [0] * n  # Array to store the max sums up to each index
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])

    # Track which elements are selected
    # Array to track elements included in the sum
    selected_elements = [None] * n
    selected_elements[0] = [0]  # Select first element
    selected_elements[1] = [1] if array[1] > array[0] else [
        0]  # Select second or first element

    # Fill the dp array with max sums and track selected indexes
    for i in range(2, n):
        if dp[i-1] > dp[i-2] + array[i]:
            dp[i] = dp[i-1]
            # Continue with previous selection
            selected_elements[i] = selected_elements[i-1]
        else:
            dp[i] = dp[i-2] + array[i]
            selected_elements[i] = (selected_elements[i-2] if selected_elements[i-2]
                                    is not None else []) + [i]  # Include the current element

    # The final max sum is at the last index
    max_sum = dp[-1]

    # Get the elements and indexes corresponding to the max sum
    indexes = selected_elements[-1]
    elements = [array[i] for i in indexes]

    return max_sum, elements, indexes


# Example usage
array = [7, 10, 12, 7, 9, 14, 99, 98, 97, 103]
max_sum, elements, indexes = maxSubsetSumWithIndex(array)
print("Maximum Subset Sum:", max_sum)
print("Selected Elements:", elements)
print("Selected Indexes:", indexes)


# Example usage
array = [7, 10, 12, 7, 9, 14]
maxSum = maxSubsetSum(array)
print("Maximum Subset Sum:", maxSum)
