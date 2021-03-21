
"""
- 문제해결 : BFS, deque 이용한 다익스트라
- 구현 :
    distance배열 하나 생성 후 최대값으로 다 채워놓는다.
    board[ny][nx] + distance[y][x] < distance[ny][nx] -> distance[ny][nx] 값 갱신
"""

# import sys
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

T = int(input())
for t in range(T):
    INF = 987654321 # 거리 길이는 최대값으로 설정
    n = int(input())
    # board = [list(input().split()) for _ in range(n)] #입력값 사이 공백이 있는 경우
    board = [list(map(int, list(input()))) for _ in range(n)] # 입력값 사이 공백이 없는 경우
    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = 0

    dQ = deque()
    # dQ.append(0, 0)
    dQ.append((0, 0))
    while dQ:
        y, x = dQ.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx] + distance[y][x] < distance[ny][nx]:
                    distance[ny][nx] = distance[y][x] + board[ny][nx]
                    dQ.append((ny, nx))
    # print(distance)
    print("#{} {}".format(t+1, distance[n-1][n-1]))
