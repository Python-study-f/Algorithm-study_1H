
# python3로 제출했을 때 -> 시간초과
# pypy3로 제출했을 때 통과
# 비교하고자 하는 문자열이 3개인 경우에는?

import sys
input = sys.stdin.readline

# sys.stdin.readline을 사용할거면 strip()를 사용해야함.
s1 = input().strip()
s2 = input().strip()

# 2차원 배열 DP 선언 (2개 문자열 비교 위해)
dp=[[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
result = 0

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        # 같은 문자이면 이 시점부터 count 체크
        if (s1[i-1] == s2[j-1]):
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(dp[i][j], result)

print(result)
