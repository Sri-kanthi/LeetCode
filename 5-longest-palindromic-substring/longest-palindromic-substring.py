class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ""

        substr = s[0]

        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        for i in range(len(s)):
            odd = expand(i, i)
            if len(odd) > len(substr):
                substr = odd
            
            even = expand(i, i + 1)
            if len(even) > len(substr):
                substr = even

        return substr