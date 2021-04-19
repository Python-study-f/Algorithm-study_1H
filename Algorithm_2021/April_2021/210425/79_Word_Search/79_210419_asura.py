class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        
        def dfs(start,x,y,target,visit):
            
            

            if start == len(target):
                return True

            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[start]:
                return False
            
            if visit[x][y]:
                return

            visit[x][y] = True
            result = dfs(start+1,x-1,y,target,visit) or dfs(start+1,x+1,y,target,visit) or \
                     dfs( start+1,x,y-1,target,visit) or dfs(start+1,x,y+1,target,visit)
            visit[x][y] = False

            return result

        # Main #

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0,i,j,word,visited):
                    return True

        return False
