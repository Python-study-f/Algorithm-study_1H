class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        def dfs(x, y, idx):
            #print(str(x) + " "+str(y)+ " "+ word[idx])
            if idx == len(word) -1 :
                return True
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if tx < 0 or ty < 0 or tx >= len(board) or ty >= len(board[0]):
                    continue

                if board[tx][ty] == word[idx + 1]:
                    board[x][y] = " "
                    if dfs(tx, ty, idx + 1):
                        return True
                    board[x][y] = word[idx]
            return False
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                    
        return False
