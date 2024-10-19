class Solution:
    def threeSum(self, nums):
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = nums[i]+nums[l]+nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return result


obj = Solution()

nums = [-1, 0, 1, 2, -1, -4]

result = obj.threeSum(nums)

print(result)
