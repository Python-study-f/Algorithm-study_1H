# 풀이1. Brute-force TLE
'''
N, K = map(int,input().split())
data = list(map(str,input()))

for i in range(N):
    if cnt != K:
        del data[data.index(min(data))]
        cnt += 1

print(''.join(data))
'''

# 풀이2. 그리디
# 다 풀고나서 찾아보니 좋은 해설 발견 https://steady-coding.tistory.com/54

from collections import deque

N, K = map(int,input().split())
data = list(map(str,input()))
cnt = 0
ans = deque()


for i in range(N):
    while ans and cnt != K:
        if ans[-1] < data[i]:
            ans.pop()
            cnt += 1
        else:
            break
    ans.append(data[i])

# 만약에 K 개수만큼 삭제하기 전에 과정이 끝나는 경우 EX) data = 55555, N = 5, K= 2
# 갯수에 맞게 끝내도 인덱스 범위에 안넘어감
for i in range(N-K):
    print(ans[i], end = '')
