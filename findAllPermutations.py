def findAllPermutations(array):
    # Initialize the list to store all the permutations
    permutations = []
    # Call the helper function to start the recursive process
    helper(array, [], permutations)
    return permutations


def helper(arr, perm, perms):
    # Base case: if the current permutation's length is equal to the original array's length
    if len(arr) == 0:
        # Add the current permutation to the list of permutations
        perms.append(perm)
    else:
        # Iterate through the array and recursively build permutations
        for i in range(len(arr)):
            # Create a new array excluding the current element (arr[i])
            newArr = arr[:i] + arr[i+1:]
            # Call helper recursively, adding arr[i] to the current permutation
            helper(newArr, perm + [arr[i]], perms)


# Example usage:
array = [1, 2, 3, 4, 5]
permutations = findAllPermutations(array)
print(permutations)
