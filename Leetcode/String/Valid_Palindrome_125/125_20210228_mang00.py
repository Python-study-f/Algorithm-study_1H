class Solution:
    def isPalindrome(self, s):
        string = []
        for char in s:
            if char.isalnum():
                string.append(char.lower())

        lens = len(string)

        for i in range(lens):
            lens = lens - 1
            if string[i] != string[lens]:
                return False
        return True


valid = Solution()
print(valid.isPalindrome("A man, a plan, a canal: Panama"))
