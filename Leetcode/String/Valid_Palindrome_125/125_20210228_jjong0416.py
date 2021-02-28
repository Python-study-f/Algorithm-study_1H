class Solution():
    def isPalindrome(self, s):
        s = s.lower()

        _s = ""

        for i in range(len(s)):
            if s[i].isalpha():
                _s += s[i]

        return _s == _s[::-1]
