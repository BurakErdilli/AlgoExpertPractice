class Solution:
    def rob(self, nums):
        maxVal = 0
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            temp = max(nums[i]+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


obj = Solution()

nums = [1, 2, 3, 1, 2, 3, 4, 90]

result = obj.rob(nums)
