N, M = map(int,input().split())
data = list(str(input()))
cnt = 0
visited = [False] * N

for cur in range(N):
    if data[cur] == 'P':
        for i in range(max(0,cur-M), min(cur+M+1,N)): # 왼쪽부터 기준
            if data[i] == 'H' and not visited[i]:
                cnt += 1
                visited[i] = True

print(cnt)