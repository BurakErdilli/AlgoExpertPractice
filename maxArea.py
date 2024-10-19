class Solution:
    def maxArea(self, height) -> int:
        l = 0
        r = len(height)-1
        res = 0

        while l < r:
            area = (r-l)*min(height[l], height[r])
            res = max(area, res)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res


obj = Solution()

height = [1, 8, 6, 99, 99, 2, 8, 3, 7]

result = obj.maxArea(height)
print(result)
