n = int(input())
times = list(map(int,input().split()))
times.sort(reverse = True)

count = 1
sumn = 0

for time1 in times:
  sumn += count * time1
  count += 1

print(sumn)