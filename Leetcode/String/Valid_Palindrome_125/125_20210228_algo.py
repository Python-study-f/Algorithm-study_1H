class Solution:
    def isPalindrome(self, s: str) -> bool:
        strings = [ string.lower() for string in s if string.isalnum() ]
        return strings == strings[::-1]
