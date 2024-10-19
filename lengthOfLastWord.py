class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        l = 0
        if len(s) == 1:
            return 1

        i = len(s)-1

        while s[i] != " " and i >= 0:
            l += 1
            i -= 1
            char = s[i]

        return l


obj = Solution()

s = "day"

result = obj.lengthOfLastWord(s)
print(result)
