n=int(input())
temp=list(map(int,(input().split())))
temp.sort(reverse=True)
sum=0
cnt=1
for i in temp:
  sum += cnt * i
  cnt += 1
print(sum)
