def pseudo(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

# 회문 판단 함수
def palindrome(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            res1 = pseudo(s, left+1, right)
            res2 = pseudo(s, left, right-1)
            if res1 == True or res2 == True:
                return 1
            else:
                return 2
    return 0

T = int(input())
for i in range(T):
    s = list(input())
    res = palindrome(s, 0, len(s)-1)
    print(res)
