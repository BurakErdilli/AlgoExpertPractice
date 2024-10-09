def merge_repeating_substrings(string):
    n = len(string)
    i = 0

    # Function to find the longest repeating substring starting at index i
    def find_repeat(i):
        for length in range(2, (n - i) // 2 + 1):
            substring = string[i:i+length]
            if string[i+length:i+2*length] == substring:
                return substring, length
        return None, 0

    result = []
    
    while i < n:
        # Try to find the longest repeating substring
        substring, length = find_repeat(i)
        
        if substring:
            # If found, add the substring only once and skip the repeated part
            result.append(substring)
            i += 2 * length  # Skip the repeated part
        else:
            # If no repeat, add the current character to the result
            result.append(string[i])
            i += 1

    return ''.join(result)

# Example usage
string = 'easportstsinthegame'
merged_string = merge_repeating_substrings(string)
print("Original:", string)
print("Merged:", merged_string)
