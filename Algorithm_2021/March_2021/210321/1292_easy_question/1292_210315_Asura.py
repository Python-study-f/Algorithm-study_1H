N,M = map(int,input().split())
lst = []

for i in range(1,1001):
    for j in range(i):
        lst.append(i)

print(sum(lst[N-1:M]))