def dfs(idx,c,rs=0):
    ans[c] = max(ans[c],rs)
    for i in range(idx,2*n,2):
        if ht.get(i):
            for x,y in ht[i]:
                if vis[x+y] == 0:
                    vis[x+y] = 1
                    dfs(i+2, c, rs+1)
                    vis[x+y] = 0

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = [0,0]
ht = {}
vis = [0]*(2*n)

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            ht[i-j+n] = ht.get(i-j+n,[]) + [(i,j)]

dfs(0,0)
dfs(1,1)
print(sum(ans))