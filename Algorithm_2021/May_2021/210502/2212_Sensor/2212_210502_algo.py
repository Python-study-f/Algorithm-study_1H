N = int(input())
K = int(input())

sensor = list(map(int, input().split()))
sensor.sort()
cnt = 0
if K >= N: 
    print(0)
else:
    temp=[]
    for i in range(N-1):
        temp.append(sensor[i+1] - sensor[i])
    temp.sort()
    
    for i in range(N-K): 
        cnt += temp[i]
    print(cnt)
