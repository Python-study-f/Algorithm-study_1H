'''

문제 핵심
1. 테두리만 먼저 상하좌우 DFS 돌린다.
2. 그러면 경우의 수가 2가지 나오는데
    2-1) 가운데 O표시까지 연결되어있으면 모두 다 D로 표시
    2-2) 연결이 안되어있으면, 테두리 부분만 D로 표시
3. 마지막 loop돌려서 O 표시만 X로 표시하고, D는 O로 표시하기

'''

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


class Solution(object):
    def solve(self, board):
        def dfs(x, y, visited):
            if not 0 <= x < len(board) or not 0 <= y < len(board[0]) or board[x][y] != 'O' or visited[x][y]:
                return

            visited[x][y] = True
            board[x][y] = 'D'  # 일단 한번에 안지우고 체크하기

            for dic in range(4):  # 모든 방향으로
                nx, ny = x + dx[dic], y + dy[dic]
                dfs(nx, ny, visited)

        visit = [[False] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1 and board[i][j] == "O":
                    dfs(i, j, visit)

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "D":
                    board[i][j] = "O"
        return board