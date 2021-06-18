# 월드컵 6987 백준

import sys
from itertools import combinations

input = sys.stdin.readline


def dfs(cnt):
    global ans
    if cnt == 15:
        for p in play:
            if p[0] == 0 and p[1] == 0 and p[2] == 0:
                pass
            else:
                break
        else:
            ans = 1
        return
    else:
        p1, p2 = versus[cnt]
        if play[p1][0] > 0 and play[p2][2] > 0:
            play[p1][0] -= 1
            play[p2][2] -= 1
            dfs(cnt + 1)
            play[p1][0] += 1
            play[p2][2] += 1
        if play[p1][1] > 0 and play[p2][1] > 0:
            play[p1][1] -= 1
            play[p2][1] -= 1
            dfs(cnt + 1)
            play[p1][1] += 1
            play[p2][1] += 1
        if play[p1][2] > 0 and play[p2][0] > 0:
            play[p1][2] -= 1
            play[p2][0] -= 1
            dfs(cnt + 1)
            play[p1][2] += 1
            play[p2][0] += 1


for _ in range(4):
    tmp = list(map(int, input().split()))
    play = []
    ans = 0
    for i in range(0, 18, 3):
        play.append([tmp[i], tmp[i + 1], tmp[i + 2]])
    versus = list(combinations([0, 1, 2, 3, 4, 5], 2))
    dfs(0)
    print(ans, end=" ")
