class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        l = 0
        array = list(s)
        for i in range(len(s)):
            if array[i] == "0":
                tmp = s[l]
                array[l] = array[i]
                array[i] = tmp
                res += i-l
                l += 1

        return res


obj = Solution()
s = "11000111"
res = obj.minimumSteps(s)
print(res)
