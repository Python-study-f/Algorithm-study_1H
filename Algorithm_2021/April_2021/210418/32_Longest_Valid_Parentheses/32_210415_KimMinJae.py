# 효율?
def longestValidParentheses(s: str):
    n=len(s)
    q=[]
    dp=[False]*n
    for i in range(n):
        if s[i]=='(':
            q.append(i)
        else:
            if q:
                dp[i]=True
                dp[q.pop()]=True
    ans=0
    accum=0
    for i in range(n):
        if dp[i]:
            accum+=1
        else:
            ans=max(ans,accum)
            accum=0
    ans=max(ans,accum)

    return ans
