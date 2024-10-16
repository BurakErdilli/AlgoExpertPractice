class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = 0
        r = len(str(x))-1
        array = str(x)
        while l < r:
            if array[l] != array[r]:
                return False
            l += 1
            r -= 1

        return True


obj = Solution()
x = 31219291213
res = obj.isPalindrome(x)
