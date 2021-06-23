def f(k, C):
    a, b = 0, 0
    for el in C:
        if el>= k:
            b += 1
        if el <= k:
            a += 1
    if b >= k and a <= k:
        return True
    return False

def solution(citations):
    citations.sort()
    n = max(citations)
    ans = 0 # 왜 초기를 0으로 해놔야하는지 ? [0] 일떄 답이 0이 아닌데?
    lo = 0
    hi = 10000
    while lo <= hi:
        m = (lo + hi) //2
        if f(m, citations):
            ans = m
            lo = m + 1
        else:
            hi = m - 1
            
    return ans