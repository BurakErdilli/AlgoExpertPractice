class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        string_array = s.split()
        if len(pattern) != len(string_array):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in table:
                if string_array[i] not in table.values():
                    table[pattern[i]] = string_array[i]
                else:
                    return False

            if table[pattern[i]] != string_array[i]:
                return False
        return True


obj = Solution()
pattern = "abba"
s = "dog cat cat dog"
result = obj.wordPattern(pattern, s)
print(result)
