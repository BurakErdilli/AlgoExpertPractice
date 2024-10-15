class Solution:
    def maxProfit(self, prices) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r

            elif prices[r]-prices[l] > maxProfit:
                maxProfit = prices[r]-prices[l]
            r += 1
        return maxProfit


prices = [7, 6, 4, 3, 1]
solution = Solution()
output = solution.maxProfit(prices)
print(output)
