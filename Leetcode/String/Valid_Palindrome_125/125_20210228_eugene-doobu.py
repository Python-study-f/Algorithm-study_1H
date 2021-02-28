class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                tmp += c.lower()
                
        for i in range(int(len(tmp)/2)):
            if tmp[i] != tmp[len(tmp)-i-1]:
                return False
        return True
