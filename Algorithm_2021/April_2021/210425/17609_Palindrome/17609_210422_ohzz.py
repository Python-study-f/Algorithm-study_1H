# 회문 17609
import sys

n = int(sys.stdin.readline().rstrip())


def palindrome(string):
    if string == string[::-1]:
        return 0
    n = len(string)
    lt = 0
    rt = 0
    tmp = list(string)
    reTmp = list(string)
    reTmp.reverse()
    for i in range(n // 2):
        if tmp[i] != reTmp[i]:
            k = i
            break
    del tmp[k]
    if tmp == tmp[::-1]:
        return 1
    del reTmp[k]
    if reTmp == reTmp[::-1]:
        return 1
    return 2


for i in range(n):
    word = sys.stdin.readline().rstrip()
    print(palindrome(word))


# def palindrome(string):
#     if string == string[::-1]:
#         return 0
#     n = len(string)
#     for i in range(n):
#         tmp = list(string)
#         del tmp[i]
#         if tmp == tmp[::-1]:
#             return 1
#     return 2
