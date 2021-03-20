import sys
input = sys.stdin.readline

N = int(input().strip()) # 더 빠르게 !
data = []
dp = [0] * 1500001

for _ in range(N):
    T, P = map(int,input().split())
    data.append((T, P))


for i in range(N):
    if i + data[i][0] <= N:
        dp[i+data[i][0]] = max(dp[i+ data[i][0]], dp[i]+data[i][1])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[N])

"""
1. 문제 보자마자 DP 떠오름. 이젠 그냥 본능인듯
2. 항상 dp를 탑다운 방향으로 풀었는데, 이번 문제는 아예 구현이 바텀 업 방향이니깐 좀 많이 헤맨 거 같음
3. 덕분에 하나 더 배워감. 진짜 도움 많이 된 문제인듯.
4. 너 뭐냐 ^-^?
5. 찾아보니
6. sys.stdin.readline() > raw_input() > input() 순서대로 빠르다고 합니다. 그래서 시간초과 뜬 것.
"""


