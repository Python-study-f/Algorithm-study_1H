"""
리스트 슬라이싱 이용한 브루트포스 문제 풀이 -> 시간 초과
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))

    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            # print(phone_book[j][0:len(phone_book[i])])

            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False

    return answer
"""

# 해시 맵, 딕셔너리 이용한 풀이 연습 필요
def solution(phone_book):
    
    dic = {} # key, value의 해시 테이블 표현할 때 dictionary 사용
    
    for number in phone_book:
        dic[number] = 1 # number -> key / 1 -> value
    
    for number in phone_book: # [123, 456, 789] 에서 123, 456, 789
        temp = ""
        for idx in number: # 123에서 1, 2, 3
            temp += idx
            # print(temp, dic)
            # number로부터 얻은 temp가 dic 내에 있는지 찾아야 하므로 temp != number
            if temp in dic and temp != number: 
                return False
                
    return True
