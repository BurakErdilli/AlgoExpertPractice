class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res | (bit << (31-i))

        return res


obj = Solution()

n = 0o00000010100101000001111010011100

res = obj.reverseBits(n)
