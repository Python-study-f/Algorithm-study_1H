class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(int(len(s)/2)):
            tmp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = tmp
        
