from itertools import combinations

n, m = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(n)]
home, chicken = [], []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            home.append((i,j))
        elif maps[i][j] == 2:
            chicken.append((i,j))

answer = 10000
for i in combinations(chicken, m):
    tmp = 0
    for j in home:
        minVal = 10000
        for k in i:
            distance = abs(k[0] - j[0]) + abs(k[1] - j[1])
            minVal = min(minVal, distance)
        tmp += minVal
    answer = min(answer, tmp)

print(answer)
