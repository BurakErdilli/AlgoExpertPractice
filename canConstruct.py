class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashSet = {}

        for char in magazine:
            if char in hashSet:
                hashSet[char] += 1
            else:
                hashSet[char] = 1

        for i in range(len(ransomNote)):
            if ransomNote[i] not in hashSet or hashSet[ransomNote[i]] == 0:
                return False
            hashSet[ransomNote[i]] -= 1
        return True


obj = Solution()

ransomNote = "aa"
magazine = "aab"

result = obj.canConstruct(ransomNote, magazine)
print(result)
