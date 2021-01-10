# a, b

def solution(a, b):
    ans = 0
    for i in range(len(a)):
        ans += a[i] * b[i]
    return ans
