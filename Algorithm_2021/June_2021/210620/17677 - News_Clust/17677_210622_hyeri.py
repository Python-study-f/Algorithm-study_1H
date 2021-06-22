from collections import Counter
import math
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    def makeset(st):
        arr = []
        for i in range(1, len(st)):
            s = st[i-1]+st[i]
            if s.isalpha():
                arr.append(s)
        return arr
    
    arr = makeset(str1)
    brr = makeset(str2)
    
    inter = set(arr) & set(brr)
    union = set(arr) | set(brr)
        
    if len(union) == 0:
        return 65536
    in_sum = sum([min(arr.count(i), brr.count(i)) for i in inter])
    un_sum = sum([max(arr.count(u), brr.count(u)) for u in union])

    return math.floor((in_sum/un_sum)*65536)
