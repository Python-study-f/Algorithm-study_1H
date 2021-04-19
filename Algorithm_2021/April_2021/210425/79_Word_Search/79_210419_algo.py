class Solution:
    def dfs(self, board, x, y, word, position, visited):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        
        if position == len(word):
            return True
        
        if visited[x][y]:
            return False
        
        if board[x][y] != word[position]:
            return False
        
        dx=[-1,1,0,0]
        dy=[0,0,1,-1]
        
        for i in range(4):
            visited[x][y] = True
            nextx=x+dx[i]
            nexty=y+dy[i]
            result = self.dfs(board, nextx,nexty, word, position+1, visited)
            
            if result:
                return True
            
            visited[x][y] = False
            
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 1 and board[0][0] == word:
            return True
        
        visited = [[False for col in range(len(board[0]))] for row in range(len(board))]
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                result = self.dfs(board, x, y, word, 0, visited)
                
                if result:
                    return True

        return False
