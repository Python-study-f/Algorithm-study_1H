"""
Solution1 시간 초과가 일어나므로 list를 slice하여 접두어가 일치하는지 확인한다.
"""
def solution(phone_book):

    phone_book.sort()

    for i in range(len(phone_book)-1):
        # 시간을 단축하기 위해 slice하여 접두어가 뒤에 문자열 앞에 있는지 확인한다.

        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:

            return False

    return True

"""
Solution 2 찾은 솔루션: zip으로 묶고 startswith으로 찾는다.
"""

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True