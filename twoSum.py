class Solution:
    def twoSum(self, nums, target):
        table = {}
        for i in range(len(nums)):
            if (target - nums[i]) in table:
                return [table[target-nums[i]], i]
            else:
                table[nums[i]] = i


obj = Solution()

nums = [2, 7, 11, 15]

target = 9

result = obj.twoSum(nums, target)

print(result)
