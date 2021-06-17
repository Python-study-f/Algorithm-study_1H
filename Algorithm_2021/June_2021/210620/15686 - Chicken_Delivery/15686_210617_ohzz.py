# 치킨 배달 15686 백준

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

chicken = []
home = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

comb_chicken = list(combinations(chicken, m))
res = [0] * len(comb_chicken)

for h in home:
    for k in range(len(comb_chicken)):
        tmp = 2147483600
        for c in comb_chicken[k]:
            dis = abs(h[0] - c[0]) + abs(h[1] - c[1])
            tmp = min(tmp, dis)
        res[k] += tmp

print(min(res))
