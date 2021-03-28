class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrom(s):
            n = len(s)
            if n == 1:
                return True
            if n % 2 == 0:
                if s[:n//2] == s[n//2:][::-1]:
                    return True
                else:
                    return False
            else:
                if s[:n//2] == s[n//2+1:][::-1]:
                    return True
                else:
                    return False
                
        
        
        n = len(s)
        ans = 0
        for i in range(1,n+1):
            for j in range(n-i+1):
                if isPalindrom(s[j:j+i]):
                    ans += 1
                    
        return ans