class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Convert string to lowercase
        s = s.lower()

        # Remove non-alphanumeric characters (and spaces)
        result = []
        for char in s:
            if char.isalnum():  # Check if the character is alphanumeric
                result.append(char)

        # Join the result to form a new string
        processed_string = ''.join(result)

        i = 0
        j = len(processed_string)-1

        while i < len(processed_string)/2:
            if processed_string[i] != processed_string[j]:
                return False
            i += 1
            j -= 1
        return True


obj = Solution()
s = "A man, a plan, a canal: Panama"
result = obj.isPalindrome(s)
print(result)
