n, m = map(int, input().split())
temp = [list(map(int, list(input().rstrip()))) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if i>0 and j>0 and temp[i][j] == 1:
            temp[i][j] += min(temp[i-1][j], temp[i][j-1], temp[i-1][j-1])
        ans = max(ans, temp[i][j])
print(ans*ans)

