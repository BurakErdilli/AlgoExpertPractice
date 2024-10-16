class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        table = {}
        maxLenght = 0
        l = 0
        for i in range(len(s)):
            if s[i] in table:
                maxLenght = max(maxLenght, i-l)
                l = max(l, table[s[i]]+1)
            table[s[i]] = i
        maxLenght = max(maxLenght, i-l+1)
        return maxLenght


obj = Solution()

s = "au"

result = obj.lengthOfLongestSubstring(s)
