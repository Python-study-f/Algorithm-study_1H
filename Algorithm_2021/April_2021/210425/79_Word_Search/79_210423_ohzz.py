# Word Search 79 LeetCode

# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCB"


def exist(board, word):
    n = len(board)
    m = len(board[0])
    if len(word) == 0 or (n == 0 and m == 0):
        return False

    check = [[0] * m for _ in range(n)]

    def dfs(board, word, cnt, x, y):
        if cnt == len(word):
            return True
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx >= 0 and yy >= 0 and xx < n and yy < m:
                if board[xx][yy] == word[cnt] and check[xx][yy] == 0:
                    check[xx][yy] = 1
                    if dfs(board, word, cnt + 1, xx, yy) == True:
                        return True
                    check[xx][yy] = 0
        return False

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                check[i][j] = 1
                if dfs(board, word, 1, i, j) == True:
                    return True
                check[i][j] = 0
    return False


print(exist(board, word))
