class Solution:
    def countSubstrings(self, s: str) -> int:
        l=len(s)
        count=l
        i=0
        while i<l :
            for k in range(i+1,l):
                sub_s=s[i:k+1]
                if sub_s== sub_s[::-1]:
                    count+=1
            i+=1
        return count
