# 660ms, 5.10% ? slow.
class Solution:
    def __init__(self):
        self.tmp=0

    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        ls= set(list(s))

        for alp in ls:
            stc=0
            lo=0
            hi=0
            n= len(s)
            if s[0]!=alp:
                stc+=1
            while hi<n:
                if stc>k:
                    if s[lo]!=alp:
                        stc-=1
                    lo+=1
                    continue
                if stc<=k:
                    ans= max(ans, hi-lo+1)
                hi+=1
                if hi<n and s[hi]!=alp:
                    stc+=1
        return ans

a= Solution()
print(a.characterReplacement("ABAB", 2))