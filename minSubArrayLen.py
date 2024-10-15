class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        l = 0
        subSum = 0
        res = float("inf")

        for r in range(len(nums)):
            subSum += nums[r]
            while subSum >= target:
                res = min(res, r-l+1)
                subSum -= nums[l]
                l += 1

        if res == float("inf"):
            return 0
        return res


obj = Solution()
target = 4
nums = [1, 4, 4]
res = obj.minSubArrayLen(target, nums)
print(res)
