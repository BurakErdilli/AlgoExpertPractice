class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            if i < len(a):
                digitA = int(a[i])
            else:
                digitA = 0

            if i < len(b):
                digitB = int(b[i])
            else:
                digitB = 0

            total = digitA + digitB + carry
            char = total % 2
            result += str(char)
            carry = total // 2
        if carry:
            result += str(carry)

        result = result[::-1]
        return result


obj = Solution()


a = "11"
b = "1"

res = obj.addBinary(a, b)
print(res)
