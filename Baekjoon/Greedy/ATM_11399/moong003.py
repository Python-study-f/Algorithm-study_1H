N = int(input())
use_time = list(map(int, input().split()))
use_time.sort()
for i in range(1, len(use_time)):
    use_time[i] = use_time[i] + use_time[i-1]

print(sum(use_time))