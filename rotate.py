class Solution:
    def rotate(self, nums, k: int) -> None:
        k = k % len(nums)
        l = 0
        r = len(nums)-1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1

        l = 0
        r = k-1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1
        l = k
        r = len(nums)-1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 7


solution = Solution()
output = solution.rotate(nums, k)
print(nums)
