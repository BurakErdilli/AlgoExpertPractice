class Solution:
    def canJump(self, nums) -> bool:

        target = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):

            if nums[i] + i >= target:
                target = i

        return target == 0

        # if len(nums) == 1:
        #     return True

        # max_reach = 0

        # for i in range(len(nums)):
        #     if i > max_reach:
        #         return False

        #     max_reach = max(max_reach, i + nums[i])
        #     if max_reach >= len(nums) - 1:
        #         return True
        # return False
# Test the function
solution = Solution()
nums = [3, 0, 8, 2, 0, 0, 1]
possible = solution.canJump(nums)
print(possible)  # Output should be True
