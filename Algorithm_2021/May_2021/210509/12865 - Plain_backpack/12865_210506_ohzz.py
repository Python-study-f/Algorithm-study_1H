# 평범한 배낭 12865 백준

# 동등한 물건이 무한개 있는 줄 알았음
# 그래서 아래처럼 풀었고 틀린 코드

# n, k = map(int, input().split())

# dy = [0] * (k + 1)

# for _ in range(n):
#     w, v = map(int, input().split())
#     for i in range(w, k + 1):
#         dy[i] = max(dy[i], dy[i - w] + v)

# print(dy[k])

# 물건이 하나만 있다고 생각하면 index를 나누고 그전 것에 더해주면 된다.

n, k = map(int, input().split())

dy = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    w, v = map(int, input().split())
    for j in range(k + 1):
        if j < w:
            dy[i][j] = dy[i - 1][j]
        else:
            dy[i][j] = max(dy[i - 1][j], dy[i - 1][j - w] + v)

print(dy[n][k])
