from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = re.sub('[^a-z ]', ' ', paragraph.lower())
        paragraph = list(paragraph.split())
        paragraph = Counter(paragraph).most_common()

        for i in range(0, len(paragraph)):
            if paragraph[i][0] not in banned:
                return paragraph[i][0]


valid = Solution()
print(valid.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
