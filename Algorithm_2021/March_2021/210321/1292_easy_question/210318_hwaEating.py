arr = [0]*1001
start = 1
idx = 0
while idx <= 1000:
    for i in range(start):
        arr[idx] = start
        idx += 1
        if idx > 1000:
            break
    start += 1
a,b = map(int,input().split())

print(sum(arr[a-1:b]))