class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return True
        s_idx = 0
        t_idx = 0

        while t_idx < t_len:
            if s[s_idx] == t[t_idx]:
                s_idx += 1

            t_idx += 1
            if s_idx == s_len:
                return True

        return False


# Example usage
solution = Solution()
print(solution.isSubsequence("b", "abc"))  # Output: True
print(solution.isSubsequence("axc", "ahbgdc"))  # Output: False
# Output: True (empty string is a subsequence)
print(solution.isSubsequence("", "ahbgdc"))
