class Solution:
    def plusOne(self, digits):
        carry = 1
        res = []
        for i in reversed(range(len(digits))):
            digit = digits[i]+carry
            carry = digit//10
            digit = digit % 10
            res.append(digit)

        if carry:
            res.append(carry)

        return res[::-1]


obj = Solution()

digits = [4, 3, 2, 1, 9, 9, 9]

result = obj.plusOne(digits)
