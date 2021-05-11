import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
temp=list(map(int,input().strip()))
cnt=0
ans=[]
for i in range(n):
    while cnt<k and ans:
        if ans[-1]<temp[i]:
         
            ans.pop()
            cnt+=1
        else:
            break
    
    ans.append(temp[i])

for i in range(n-k):
    print(ans[i],end="")
