class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # nums.sort()
        # return nums[-k]

        k = len(nums)-k

        def quickselect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickselect(l, p-1)
            elif p < k:
                return quickselect(p+1, r)
            else:
                return nums[p]

        return quickselect(0, len(nums)-1)


obj = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 3

res = obj.findKthLargest(nums, k)
