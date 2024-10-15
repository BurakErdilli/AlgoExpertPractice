class Solution:
    def candy(self, ratings) -> int:
        candy = [1] * len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                candy[i+1] += candy[i]
        print(candy)
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i] and candy[i-1] <= candy[i]:
                candy[i-1] = candy[i]+1
        print(candy)

        return sum(candy)


ratings = [1, 6, 10, 8, 7, 3, 2]
obj = Solution()

res = obj.candy(ratings)
print(res)
