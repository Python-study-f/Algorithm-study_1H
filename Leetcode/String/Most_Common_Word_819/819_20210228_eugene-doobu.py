import operator

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # 특수문자 제거를 위해
        paragraph = paragraph.lower().replace('!', ' ').replace('?', ' ').replace('\'', ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ')
        
        words = paragraph.split(' ')
        wordCountDict = {}
        for word in words:
            # 특수문자를 공백으로 변환시 공백 키값이 생기는것을 방지
            if word == '':
                continue
            if word in wordCountDict:
                wordCountDict[word] += 1
            else:
                wordCountDict[word] = 1
        
        # 딕셔너리를 벨류값을 기준으로 정렬
        sdict= sorted(wordCountDict.items(), key=operator.itemgetter(1))

        banCheker = 1
        for key in wordCountDict:
            for banword in banned:
                if(sdict[len(sdict) - banCheker][0] == banword):
                    banCheker += 1
                    break
                    
        return sdict[len(sdict) - banCheker][0]
            
