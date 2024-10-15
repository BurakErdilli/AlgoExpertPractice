class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += (prices[i+1]-prices[i])

        return profit


solution = Solution()

prices = [7, 6, 4, 3, 1]

maxProfit = solution.maxProfit(prices)

print(maxProfit)
