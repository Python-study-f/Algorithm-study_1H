
N,K = map(int,input().split())
nums = list(map(int,input()))

result = []
delNum = K

for i in range(N):
    while delNum>0 and result:
        if result[len(result)-1] < nums[i]:
            result.pop()
            delNum-=1
        else:
            break
    result.append(nums[i])
    
for i in range(N-K):
    print(result[i],end="")
