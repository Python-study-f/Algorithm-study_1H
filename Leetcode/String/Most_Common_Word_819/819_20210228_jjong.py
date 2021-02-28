import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = re.sub('[^a-z]', ' ', paragraph.lower())

        lst = list(map(str, paragraph.split()))

        dic = {}

        for w in lst:
            if w not in banned:
                if dic.get(w) is None:
                    dic[w] = 1
                else:
                    dic[w] += 1

        cnt = 0
        answer = ""
        for key, val in dic.items():
            if cnt < val:
                cnt = val
                answer = key
        return answer
