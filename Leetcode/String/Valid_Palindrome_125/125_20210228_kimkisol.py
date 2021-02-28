class Solution(object):
    def isPalindrome(self, s):
        self.s = s
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i.lower()
        new_s_list = list(new_s)
        index = 0
        while index < len(new_s)-index-1:
            print(new_s_list[index])
            print(new_s_list[len(new_s)-index-1])
            if new_s_list[index] == new_s_list[len(new_s)-index-1]:
                index += 1
            else:
                print('"{0}" is not a palindrome'.format(new_s))
                return False
                break
        print('"{0}" is a palindrome'.format(new_s))
        return True

a = Solution()
a.isPalindrome("A man, a plan, a canal: Panama")