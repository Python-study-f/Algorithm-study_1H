from collections import Counter
import math

def make_biagram(getString):
    tmp = []

    for i in range(len(getString)-1):
        check = getString[i:i+2]

        if check.isalpha():
            tmp.append(check)

    return tmp

def solution(str1, str2):
    str1 = str1.lower()
    set_gram1 = make_biagram(str1)

    str2 = str2.lower()
    set_gram2 = make_biagram(str2)

    inter = list((Counter(set_gram1) & Counter(set_gram2)).elements()) # 이떄 element는 중복을 허락하게 해주는 것


    union = list((Counter(set_gram1) | Counter(set_gram2)).elements())

    if len(union) == 0:
        ans = 1
    else:
        ans = len(inter) / len(union)

    return (math.trunc(ans*65536))
