class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        result = 0
        visit = [[1]*len(matrix[0]) for _ in range(len(matrix))]
        
        def dfs(x, y, n):   
            ans = n
            for d in range(4):
                tx = x + dx[d]
                ty = y + dy[d]
                if tx < 0 or ty < 0 or tx >= len(matrix) or ty >= len(matrix[0]):
                    continue
                if matrix[tx][ty] > matrix[x][y] and visit[tx][ty] <= visit[x][y] + 1:
                    visit[tx][ty] = visit[x][y] + 1
                    ans = max(dfs(tx, ty, n + 1), ans)
            return ans
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(dfs(i, j, 1), result)
        return result
            

# visit 배열을 이용해 해당 위치에 올 수 있는 가장 긴 거리를 기록
# 해당 위치의 기록보다 짧으면 검사 X -> 시간 단축 
