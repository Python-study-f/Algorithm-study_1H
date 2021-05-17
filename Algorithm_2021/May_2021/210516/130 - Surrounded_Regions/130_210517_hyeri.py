class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        arr = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    arr.append([i, j])
                
        def dfs(x, y):
            ans = False
            for d in range(4):
                tx = x + dx[d]
                ty = y + dy[d]
                if tx < 0 or ty < 0 or tx >= len(board) or ty >= len(board[0]):
                    return True
                if board[tx][ty] == "O":
                    board[tx][ty] = "A"
                    ans = ans or dfs(tx, ty)
            return ans
        def make_mp(x, y, c):
            board[x][y] = c
            for d in range(4):
                tx = x + dx[d]
                ty = y + dy[d]
                if tx < 0 or ty < 0  or tx >= len(board) or ty >= len(board[0]):
                    continue
                if board[tx][ty] == "A":
                    make_mp(tx, ty, c)
        for a in arr:
            ax = a[0]
            ay = a[1]
            if board[ax][ay] == "O":
                board[ax][ay] = "A"
                res = dfs(ax, ay)
                if not res:
                    make_mp(ax, ay, "X")
                else:
                    make_mp(ax, ay, "O")
        return board
                
