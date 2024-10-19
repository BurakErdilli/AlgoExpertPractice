class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        base = x

        while n > 0:
            if n % 2 == 1:
                result *= base
            base *= base
            n //= 2

        return result


obj = Solution()

x = 0.00001
n = 2147483647

res = obj.myPow(x, n)

print(res)
