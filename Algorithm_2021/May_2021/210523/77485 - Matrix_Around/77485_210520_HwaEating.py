def rotate(x1,y1,x2,y2,arr):
    ans = arr[x1][y1]
    temp = arr[x1][y1]
    for i in range(y1+1,y2+1):
        temp2 = arr[x1][i]
        arr[x1][i] = temp
        temp = temp2
        ans = min(ans,temp)
        
    for j in range(x1+1,x2+1):
        temp2 = arr[j][y2]
        arr[j][y2] = temp
        temp = temp2
        ans = min(ans,temp)
        
    for i in range(y2-1,y1-1,-1):
        temp2 = arr[x2][i]
        arr[x2][i] = temp
        temp = temp2
        ans = min(ans,temp)
    
    for j in range(x2-1,x1-1,-1):
        temp2 = arr[j][y1]
        arr[j][y1] = temp
        temp = temp2
        ans = min(ans,temp)
        
    return ans
        
def solution(rows, columns, queries):
    answer = []
    arr = []
    for i in range(rows):
        row = [i*columns+j for j in range(1,columns+1)]
        arr.append(row)
        
    for x1,y1,x2,y2 in queries:
        answer.append(rotate(x1-1,y1-1,x2-1,y2-1,arr))
        
    return answer

rows, columns, querise = 3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(*solution(rows,columns,querise))