def groupAnagrams(words):
    # Sort each word and store the sorted version in sortedWords
    sortedWords = ["".join(sorted(w)) for w in words]

    # Create a list of indices and sort them based on the sorted words
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sortedWords[x])

    result = []
    # Start with the first word in the original list
    currentAnagramGroup = [words[indices[0]]]
    currentAnagram = sortedWords[indices[0]]

    # Iterate through indices, starting from the second word
    for i in range(1, len(indices)):
        if sortedWords[indices[i]] == currentAnagram:
            # Add to current group if the sorted version matches the current anagram
            currentAnagramGroup.append(words[indices[i]])
        else:
            # Append the current group to the result and reset for a new group
            result.append(currentAnagramGroup)
            currentAnagram = sortedWords[indices[i]]
            currentAnagramGroup = [words[indices[i]]]

    # Append the last anagram group
    result.append(currentAnagramGroup)

    return result


words = ["yot", "act", "flop", "tac", "cat", "toy", "olfp"]
a = groupAnagrams(words)
print(a)
