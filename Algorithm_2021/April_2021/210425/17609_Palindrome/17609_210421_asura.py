# if 함수 - elif 함수 - else 함수로 하니깐 시간초과가 나옴. 그래서 two-point로 해결함
def palindrome(s):
    return s == s[::-1]

def tot_palindrome(s):
    left, right = 0, len(s)-1

    while left<right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            check_1 = palindrome(s[left:right])
            check_2 = palindrome(s[left+1:right+1])

            if check_1 or check_2:
                return 1
            else:
                return 2
    return 0

N = int(input())
data = []
ans = []

for i in range(N): # 값 입력
    data.append(str(input()))

for i in range(N): #값 반환
    check = tot_palindrome(data[i])
    print(check)
