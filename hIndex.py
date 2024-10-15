class Solution:
    def hIndex(self, citations) -> int:
        citations = sorted(citations, reverse=True)
        i = 0
        h = 0
        while i < len(citations):
            if citations[i] >= i+1:
                h = i+1

            i += 1
        return h


solution = Solution()

citations = [1, 3, 1]

hIndex = solution.hIndex(citations)

print(hIndex)
