class Solution:
    def maxSubArray(self, nums):
        current = 0
        maxSub = nums[0]
        for i in nums:
            if current < 0:
                current = 0
            current += i
            maxSub = max(maxSub, current)
        return maxSub


obj = Solution()
nums = [-2, -1, -3, -4, -1, -2, -1, -5, -4]

result = obj.maxSubArray(nums)
