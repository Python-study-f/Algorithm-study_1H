import sys
input = sys.stdin.readline
n = int(input())
s,e = map(int,input().split())
m = int(input())
ps = [0]*(n+1)
for _ in range(m):
    p, c = map(int,input().split())
    ps[c] = p

dp = [0]*(n+1)
vis = [0]*(n+1)
ans = -1
vis[s] = 1
vis[e] = 1

def find(x,rs=1):
    global ans
    vis[x] = 1
    p = ps[x]
    if p == 0:
        return
    elif vis[p] == 0:
        dp[p] = rs
        find(p, rs+1)
    else:
        ans = dp[p] + rs

find(s)
find(e)

print(ans)