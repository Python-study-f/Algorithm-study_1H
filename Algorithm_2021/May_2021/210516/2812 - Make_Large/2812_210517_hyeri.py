N, K = map(int, input().split())
num = list(input())

arr = [num[0]]
k = K
for i in range(1, N):
    if arr:
        while k > 0 and arr and arr[-1] < num[i]:
            arr.pop()
            k -= 1
    arr.append(num[i])

for i in range(N-K):
    print(arr[i], end='')
