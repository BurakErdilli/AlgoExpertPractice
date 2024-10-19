class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack)+1-len(needle)):
            print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


obj = Solution()


haystack = "sadbutsad"
needle = "sad"

result = obj.strStr(haystack, needle)

print(result)
