# 등굣길 42898 프로그래머스


def solution(m, n, puddles):
    road = [[0] * (m + 1) for _ in range(n + 1)]
    road[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                continue
            road[i][j] = road[i - 1][j] + road[i][j - 1]
    return road[n][m] % 1000000007


print(solution(4, 3, [[2, 2]]))
