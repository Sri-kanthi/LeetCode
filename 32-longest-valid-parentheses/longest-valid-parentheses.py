class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = [-1]
        res = 0
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res