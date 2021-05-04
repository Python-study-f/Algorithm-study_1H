N, K = map(int, input().split())
item = []
dp = [[-1] * (K+1) for _ in range(N)]

# Brute force -  시간 초과
def Brute_force(idx, cnt):
    if idx == N:
        return 0
    res = 0
    if item[idx][0] + cnt <= K:
        res = Brute_force(idx + 1, cnt + item[idx][0]) + item[idx][1]
    return max(res, Brute_force(idx + 1, cnt))

# 동적계획법
def knapsack(idx, cnt):
    if idx == N:
        return 0
    res = dp[idx][cnt]
    if res != -1:
        return res
    if item[idx][0] <= cnt:
        res = knapsack(idx + 1, cnt - item[idx][0]) + item[idx][1]
    dp[idx][cnt] = max(res, knapsack(idx + 1, cnt))
    return dp[idx][cnt]


for i in range(N):
    W, V = map(int, input().split())
    item.append([W, V])

print(knapsack(0, K))
