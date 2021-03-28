
"""
- 문제해결 : DFS
- 구현 : 
    1. 서로 다른 일곱 자리 수들을 구하는 과정에서 set()를 이용.
    
"""
# import sys

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dfs(y, x, b):

    global result
    if len(b) == 7: # 7자리가 되면 result에 추가.
        result.add(b)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(ny, nx, b + board[ny][nx])

# T = int(sys.stdin.readline())
T = int(input())

for t in range(T):
    # board = [list(sys.stdin.readline().split()) for _ in range(4)]
    board = [list(input().split()) for _ in range(4)]
    result = set() # 중복된 값은 가지면 안됨.
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j])

    print("#{} {}".format(t+1, len(result)))
