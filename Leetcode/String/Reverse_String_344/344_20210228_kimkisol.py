class Solution(object):
    def reverseString(self, s):
        index = 0
        while index < len(s)-index-1:
            s[index], s[len(s)-index-1] = s[len(s)-index-1], s[index]
            index += 1