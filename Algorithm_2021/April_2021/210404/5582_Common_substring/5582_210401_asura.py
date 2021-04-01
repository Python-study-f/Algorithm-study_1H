# import sys
# input = sys.stdin.readline
#
# N = str(input())
# M = str(input())
# cnt = 0
# left, right = 0, 1
#
# while left != len(N):
#
#     tmp = N[left:right]
#
#     if right >= len(N):
#         left += 1
#         right = left + 1
#         continue
#
#     if tmp in M:
#         cnt = max(cnt,len(tmp))
#         right += 1
#     else:
#         left += 1
#         right = left + 1
#
# print(cnt)
# # Two-Point 시간초과

# 새로운 알고리즘 LCS 공부하자.
# https://lmcoa15.tistory.com/73

N = str(input())
M = str(input())
dp = [[0]*(len(M)+1) for _ in range(len(N)+1)]

ans = -int(1e9)

for i in range(1,len(N)+1):
    for j in range(1,len(M)+1):
        if N[i-1] == M[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        ans = max(ans, dp[i][j])

print(ans)