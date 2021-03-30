import sys
sys.setrecursionlimit(4000)

def calc(x,y):
    rs = 0
    while x < n and y < m:
        if arr[x][y]:
            rs += 1
        else:
            break
        x+=1
        y+=1
    return rs



A = input()
B = input()
n,m = len(A), len(B)

arr = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if A[i] == B[j]:
            arr[i][j] = 1

ans = 0

for x in range(n):
    y = 0
    cnt = 0
    while x < n and y < m:
        if arr[x][y]:
            cnt += 1
        elif cnt:
            ans = max(ans,cnt)
            cnt = 0
        x+=1
        y+=1
    ans = max(ans,cnt)

for y in range(m):
    x = 0
    cnt = 0
    while x < n and y < m:
        if arr[x][y]:
            cnt += 1
        elif cnt:
            ans = max(ans,cnt)
            cnt = 0
        x+=1
        y+=1
    ans = max(ans,cnt)

print(ans)