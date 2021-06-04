import sys
input = sys.stdin.readline
def sqr_sum(a,b,c,d):
    ans = 0
    ans += arr[c][d]
    if a:
        ans -= arr[a-1][d]
    if b:
        ans -= arr[c][b-1]
    if a and b:
        ans += arr[a-1][b-1]
    return ans

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(1,n):
        arr[i][j] += arr[i][j-1]

for j in range(n):
    for i in range(1,n):
        arr[i][j] += arr[i-1][j]

for _ in range(m):
    a,b,c,d = map(int,input().split())
    print(sqr_sum(a-1,b-1,c-1,d-1))
