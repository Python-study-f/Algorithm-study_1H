
"""
- 문제해결 : DP -> 별로 안풀어봐서 연습 필요 / 너무 느림
- 구현 :
    DP[n]에 대해 n일 까지 일해서 벌 수 있는 돈이라고 설정.

"""
import sys

N = int(sys.stdin.readline())
arr = [[0] * 2 for _ in range(N + 3)]
# print(arr)
DP = [0] * (N + 2)

for i in range(1, N+1):
    T, P = map(int, sys.stdin.readline().split())
    arr[i][0] = T
    arr[i][1] = P

current_Max = 0 # 현 시점 얻을 수 있는 최대값
for i in range(1, N + 2):
    current_Max = max(current_Max, DP[i])

    if i + arr[i][0] > N + 1: # N + 1일을 넘어가면 안됨
        continue
    # i + T일날 벌 수 있는 최대 액수
    # = max(i일까지 일해서 벌 수 있는 최대 액수+ i일날 일한 액수, i + T일날 벌 수 있는 최대 액수)
    DP[i + arr[i][0]] = max(current_Max + arr[i][1], DP[i + arr[i][0]])

print(current_Max)
