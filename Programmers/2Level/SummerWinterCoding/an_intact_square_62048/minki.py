def solution(w,h):
    answer = 1
    whole = w * h
    broken = w + h - gcd(w, h)
    answer = whole - broken
    return answer

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)