dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def DFS(x, y, s):
    global result
    if len(s) == 7:
        result.add(s)
        return
    for d in range(4):
        nx=  x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            DFS(nx, ny, s + temp[nx][ny])

T = int(input())
for test_case in range(1, 1 + T):
    temp = [list(input().split()) for _ in range(4)]
    result = set()
    for x in range(4):
        for y in range(4):
            DFS(x, y, temp[x][y])
    print('#{} {}'.format(test_case, len(result)))
