# 감시 15683 백준

import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 동 0 서 1 남 2 북 3
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

dir = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [3, 1], [1, 2], [0, 2]],
    [[0, 3, 1], [3, 1, 2], [1, 2, 0], [2, 0, 3]],
    [[0, 1, 2, 3]],
]

cctv_pos = []
res = 2147483600


def lookArea(x, y, arr, d):
    nx = x
    ny = y
    while True:
        nx = nx + dx[d]
        ny = ny + dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 6:
            if arr[nx][ny] == 0:
                arr[nx][ny] = "#"
        else:
            break


def dfs(cnt, arr):
    global res
    if cnt == len(cctv_pos):
        area = 0
        for k in range(n):
            for u in range(m):
                if arr[k][u] == 0:
                    area += 1
        res = min(res, area)
        return
    else:
        x, y, val = cctv_pos[cnt]
        for di in dir[val]:
            n_arr = copy.deepcopy(arr)
            for d in di:
                lookArea(x, y, n_arr, d)
            dfs(cnt + 1, n_arr)


for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 6:
            cctv_pos.append([i, j, arr[i][j]])

dfs(0, arr)
print(res)
