class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start_index = 0

        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total < 0:
                total = 0
                start_index = i+1

        return start_index


obj = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
ans = obj.canCompleteCircuit(gas, cost)
print(ans)
