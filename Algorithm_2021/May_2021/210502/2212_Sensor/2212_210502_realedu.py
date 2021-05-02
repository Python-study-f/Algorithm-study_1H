
N = int(input())
K = int(input())
# sensor = [map(int, input().split())] - [<map object at 0x00000219C8E07670>]
sensor = list(map(int, input().split()))
sensor.sort()
result = 0
if K >= N: # 기지국 개수 == 센서 개수 -> 해당 기지국 당 해당 센서 담당하면 되니까
    print(0)

else:
    diff=[]
    for i in range(N-1):
        diff.append(sensor[i+1] - sensor[i])
    diff.sort()
    
    # ex : 6개 센서, 2개 기지국 -> 6-2 만큼 커버하면 됨.
    for i in range(N-K): 
        result += diff[i]
    print(result)
