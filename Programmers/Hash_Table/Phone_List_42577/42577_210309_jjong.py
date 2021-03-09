# def solution(phone_book):
#     answer = True
#     phone_book.sort(key=len)
#
#     for i in range(len(phone_book)):
#         st = phone_book[i]
#
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[j].startswith(st, 0):
#                 answer = False
#
#     return answer
'''
1. phone_book이 1이상 100만 이하이므로 O(n^2) 했을 경우 시간초과할 거 알고있었지만 한번 해봄
2. startswwith에 대해 설명하기 위해 넣음
3. https://m.blog.naver.com/PostView.nhn?blogId=kaheeyah&logNo=220419259971&proxyReferer=https:%2F%2Fwww.google.com%2F 동작원리
4. https://www.notion.so/jjongdev/_find-startswith-8900d4c856a8440fabe01f3b4f577dd6   startswith 관련 노션
'''

def solution(phone_book):
    answer =True
    hash_map = {}

    for phonenumber in phone_book:
        hash_map[phonenumber] = 1


    for phonenumber in phone_book:
        temp = ""
        for number in phonenumber:
            temp += number
            if temp in hash_map and temp != phonenumber:
                answer = False

    return answer