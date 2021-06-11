from collections import deque

dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
L, D = (3, 2, 0, 1), (2, 3, 1, 0)

def sol():
    x, y, z, d, ans = 0, 0, 0, 0, 0
    a[0][0] = 2
    q = deque()
    q.append((0, 0))
    
    while True:
        x, y = x+dx[d], y+dy[d]
        ans += 1
        if x < 0 or x >= n or y < 0 or y >= n or a[x][y] == 2:
            print(ans)
            return
          
        if not a[x][y]:
            nx, ny = q.popleft()
            a[nx][ny] = 0
            
        a[x][y] = 2
        q.append((x, y))
        t, c = b[z]
        
        if ans == int(t):
            if c == 'L':
                d = L[d]
            else:
                d = D[d]
            z = (z+1)%m

n = int(input())
a = [[0]*n for _ in range(n)]

for _ in range(int(input())):
    u, v = map(int, input().split())
    a[u-1][v-1] = 1
    
m = int(input())
b = [list(map(str, input().split())) for _ in range(m)]

sol()
