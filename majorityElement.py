class Solution:
    def majorityElement(self, nums) -> int:
        # i = 0
        # maxCount = 0
        # result = 0
        # count = {}
        # while i < len(nums):
        #     count[nums[i]] = 1 + count.get(nums[i], 0)
        #     if count[nums[i]] > maxCount:
        #         maxCount = count[nums[i]]
        #         result = nums[i]
        #         if maxCount >= (len(nums)//2)+1:
        #             return result
        #     i += 1

        # return result
        res = 0
        count = 0
        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1

        return res


nums = [1, 1, 1,  1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 5, 5, 5]


solution = Solution()
k = solution.majorityElement(nums)
print(k)
