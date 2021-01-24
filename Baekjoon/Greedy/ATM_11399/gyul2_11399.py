people = int(input())
time = list(map(int, input().split()))

time.sort()

answer = 0
for i in range(people):
    answer = answer + time[i]*(people-i)
    
print(answer)