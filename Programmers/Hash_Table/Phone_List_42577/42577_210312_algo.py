def solution(phoneBook):
    
    phoneBook = sorted(phoneBook) #정렬시키기
    #print(phoneBook)
    
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
       # print(p1,p2)

        if p2.startswith(p1):
            return False
    return True
