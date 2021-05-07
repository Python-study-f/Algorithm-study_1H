n, k = map(int, input().split(' '))
temp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = map(int, input().split(' '))
    for j in range(1, k + 1):
        if j < w:
            temp[i][j] = temp[i - 1][j]
        else:
            temp[i][j] = max(temp[i - 1][j], temp[i - 1][j - w] + v)

print(temp[n][k])
