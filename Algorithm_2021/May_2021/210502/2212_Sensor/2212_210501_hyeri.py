N = int(input())
K = int(input())

arr = list(map(int, input().split()))
arr.sort()

if K == 1:
    print(arr[len(arr)-1] - arr[0])
elif K >= N:
    print(0)
else:
    dp = []
    for i in range(1, N):
        dp.append(arr[i]-arr[i-1])
    dp.sort()
    for i in range(K-1):
        if len(dp) == 0:
            dp.append(0)
            break
        else:
            dp.pop()
    print(sum(dp))

# 탐욕알고리즘
# 전체 구간에서 K-1개 만큼 구간 삭제 
