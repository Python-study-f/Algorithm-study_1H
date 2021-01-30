from collections import deque

n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]


# print(visited)
def bfs():
    q.append((0, 0))
    visited[0][0] = 1
    dist[0][0] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and temp[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1

    return dist[n - 1][m - 1]


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
temp = [list(map(int, list(input()))) for _ in range(n)]
dist = [[0] * m for _ in range(n)]
q = deque()
ans = bfs()
print(ans)