class Solution(object):
    def longestCommonPrefix(self, strs):
        
        temp= zip(*strs)
        answer =""
        for i in temp:
            if len(set(i)) > 1:
                break
            answer += i[0]
        return answer
