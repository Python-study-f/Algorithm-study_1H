"""
1. 배경지식 - 에라토스테네스체
2. 문제 해결 기법 - 구현
3. 구현 - 소수 판별 return 과정에서 True, False 제대로 적기
"""
import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
lst = []
arr = [True] * (N + 1)
# arr = [True for _ in range(N + 1)]

for i in range(2, int(N ** 0.5) + 1): # + 1해줘야됨.
        if arr[i] == True:
            for j in range(i*2, N+1, i):
                arr[j] = False
                
for i in range(M, N + 1):
    if i >= 2:
        if arr[i] == True:
            lst.append(i)
        
# print(lst)
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))
    
        
