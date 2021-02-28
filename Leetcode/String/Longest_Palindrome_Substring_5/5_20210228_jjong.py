def isPalindrome(s):
    return s == s[::-1]

def longestPalindrome(s):
    sub = ''
    left_idx = 0

    while left_idx + len(sub) < len(s): #탈출 조건
        right_idx = len(s) - 1

        while not isPalindrome(s[left_idx:right_idx+1]): # 범위 내에 좌우 대칭이 아니면
            right_idx -= 1 # 기준인 왼쪽 index가 아니라 오른쪽 index를 빼고

        if len(sub) < len(s[left_idx:right_idx+1]):
            sub = s[left_idx:right_idx+1] # 만약 새로운 값이 isPalindreome를 만족하며, 더 길다면 substring을 갱신

        left_idx += 1
    return sub

# Solution :  Brute Force  O(n^3)




def checkCenter(st, left, right): # 센터의 갯수를 확인해주는 함수.
    while left >= 0 and right < len(st) and st[left] == st[right]:
        left -= 1
        right += 1

    # 원래 길이보다 2만큼 길기 때문에.
    return right - left - 1

s = "babad"

start, end = 0, 0

for i in range(len(s)):
    check = max(checkCenter(s,i,i),checkCenter(s,i,i+1))
    print(check)
    if check > (end - start):
        start = i - (check-1)//2
        end = i + check//2

print(s[start:end+1])

# Solution :  O(n^2)
