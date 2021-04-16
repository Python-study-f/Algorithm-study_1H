def longestValidParentheses(s):
    lt, rt = 0, 0
    ans = 0
    for i in range(len(s)):
        if s[i] == "(":
            lt += 1
        else:
            rt += 1
        if lt == rt:
            ans = max(ans, lt + rt)
        elif lt < rt:
            lt = 0
            rt = 0

    lt, rt = 0, 0
    for j in range(len(s) - 1, -1, -1):
        if s[j] == "(":
            lt += 1
        else:
            rt += 1
        if lt == rt:
            ans = max(ans, lt + rt)
        elif rt < lt:
            lt = 0
            rt = 0
    return ans


print(longestValidParentheses("(()"))
