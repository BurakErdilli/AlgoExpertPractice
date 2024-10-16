class Solution:
    def climbStairs(self, n: int) -> int:

        def helper(n, mem={1: 1, 2: 2}):
            if n in mem:
                return mem[n], mem
            else:
                mem[n], _ = helper(n-1, mem)
                mem[n] += helper(n-2, mem)[0]

            return mem[n], mem
        res, mem = helper(n)
        print(res)
        return res

        helper

        # total=0
        # def helper(n):
        #     if n  == 1:
        #         return 1
        #     if n == 0:
        #         return 0
        #     if n == 2 :
        #         return 2
        #     else:
        #         return helper(n-1)+helper(n-2)

        # return helper(n)


obj = Solution()

n = 4

res = obj.climbStairs(n)
