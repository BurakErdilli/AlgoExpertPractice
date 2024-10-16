class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1
        m = (r+l)//2
        print(m)
        while l <= r:
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m-1
                m = (r+l)//2
            if nums[m] < target:
                l = m+1
                m = (r+l)//2
            print(m)
        return l


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10

obj = Solution()

res = obj.searchInsert(nums, target)
