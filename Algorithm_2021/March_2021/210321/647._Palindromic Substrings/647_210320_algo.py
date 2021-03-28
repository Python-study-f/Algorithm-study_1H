class Solution:
    def countSubstrings(self, s: str) -> int:
        count=len(s)
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                sub_s=s[i:j+1]
                if sub_s== sub_s[::-1]:
                    count+=1
        return count
