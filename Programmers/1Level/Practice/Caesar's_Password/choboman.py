# 97 <= ord('s') and ord('s') <= 122
# 65 <= ord('s') and ord('s') <= 90
# ord('s') == 32

def solution(s, n):
    answer = ''
    for i in s:                               # A, B, ..
        if i.islower():                       # 소문자일시
            if ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        elif i.isupper():                     # 대문자일시
            if ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        elif ord(i) == 32:
            answer += ' '
    return answer
