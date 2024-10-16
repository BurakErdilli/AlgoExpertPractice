class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Early exit if lengths differ
        if len(s) != len(t):
            return False

        lines1 = []
        lines2 = []
        mapS = {}
        mapT = {}

        # Populate mappings and track changes
        for i in range(len(s)):
            # Handle mapping for s
            if s[i] not in mapS:
                mapS[s[i]] = t[i]  # Map s character to t character
            elif mapS[s[i]] != t[i]:
                return False  # Mapped character does not match

            # Handle mapping for t
            if t[i] not in mapT:
                mapT[t[i]] = s[i]  # Map t character to s character
            elif mapT[t[i]] != s[i]:
                return False  # Mapped character does not match

            # Track the indices of the changing characters
            if i == 0 or s[i] != s[i - 1]:
                lines1.append(i)
            if i == 0 or t[i] != t[i - 1]:
                lines2.append(i)

        # Debug prints for mappings
        print(mapS)
        print(mapT)

        # Ensure that the number of unique mappings is the same
        return len(lines1) == len(lines2)


s = "aaeaa"
t = "uuxyy"

obj = Solution()

result = obj.isIsomorphic(s, t)
