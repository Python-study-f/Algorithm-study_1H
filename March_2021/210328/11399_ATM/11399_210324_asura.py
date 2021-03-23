N = int(input())
data = list(map(int,input().split()))

data.sort()
prev_tot = 0
answer = 0

for i in range(len(data)):
    prev_tot += data[i]
    answer += prev_tot

print(answer)


