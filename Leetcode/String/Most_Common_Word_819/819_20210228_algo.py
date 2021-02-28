from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = []
        paragraph = paragraph.lower()
        paragraph+=" "
        print(paragraph)
        idx = 0
        for i in range(len(paragraph)-1):
            if paragraph[i].isalpha() and  not paragraph[i+1].isalpha():
                word.append(paragraph[idx:i+1])
              #  print(idx)
            elif not paragraph[i].isalpha() and paragraph[i+1].isalpha():
                idx = i+1
               #print(idx)
        print(word)
        #공백 전처리 
        cnt = Counter(word)
        cnt= cnt.most_common()
        answer=[]
        print(cnt)
        for i in range(0,len(cnt)):
            if cnt[i][0] not in banned:
                answer.append(cnt[i][0])
        return (answer[0])
        
