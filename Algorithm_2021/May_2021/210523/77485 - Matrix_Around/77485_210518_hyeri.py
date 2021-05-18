def solution(rows, columns, queries):
    answer = []
    # n = columns * (x-1) + y
    mp = [[0] * (columns + 1) for _ in range(rows + 1)]
    n = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            mp[i][j] = n
            n += 1

    for q in queries:
        
        x1 = q[0]
        y1 = q[1]
        x2 = q[2]
        y2 = q[3]
        mp[x1][y1] = mp[x1][y1]
        tmp = mp[x1][y1]
        
        mn = rows*columns
        for i in range(x1, x2):
            mp[i][y1] = mp[i + 1][y1]
            mn = min(mn, mp[i][y1])
        
        for j in range(y1, y2):
            mp[x2][j] = mp[x2][j + 1]
            mn = min(mn, mp[x2][j])
            
        for i in range(x2, x1, -1):
            mp[i][y2] = mp[i - 1][y2]
            mn = min(mn, mp[i][y2])
            
        for j in range(y2, y1, -1):
            mp[x1][j] = mp[x1][j - 1]
            if j == y1 + 1:
                mp[x1][j] = tmp
            mn = min(mn, mp[x1][j])
            
        answer.append(mn)
    return answer
  
  # 그냥 행렬 구현해서 돌림 
