"""
문자열 연습하기
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        result = 0
        start = 0
        while start <= len(s): # 시작점이 마지막 지점에 갈 때 까지
            
            for end in range(start + 1, len(s)+1): # 끝점 설정 / a ab abc b bc c 이런 식으로
                sub_string = s[start:end]
                if sub_string == sub_string[::-1]:
                    result += 1
            
            start += 1
            
        return result
               
