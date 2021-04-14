class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans  = 0
        for i, j in enumerate(s):
            if stack[-1] != -1 and s[stack[-1]] == "(" and  j ==")":
                stack.pop()
                ans = max(ans, i - stack[-1])
            else:
                stack.append(i)
        return ans
