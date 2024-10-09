def powerset(array):
    # Start with the empty set
    subsets = [[]]

    # Iterate through each element in the array
    for element in array:
        # For each existing subset, create a new subset with the current element added to it
        for i in range(len(subsets)):
            # Append a new subset that includes the current element
            currentSubset = subsets[i] + [element]
            subsets.append(currentSubset)

    return subsets


# Example usage:
array = [1, 2, 3, 4, 5, 6, 7, 8]
all_subsets = powerset(array)
print(all_subsets)
