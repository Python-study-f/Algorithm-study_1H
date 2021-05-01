n= int(input())
k= int(input())
s= [*map(int, input().split())]
s.sort()

gap= []
for idx, (a, b) in enumerate(zip(s, s[1:])):
    gap.append((abs(a-b),idx))
gap.sort(reverse= True)

gap =[el[1] for el in gap[:(k-1)]]
gap.sort()

ans=0
cur=0
for el in gap:
    ans+=(s[el]-s[cur])
    cur=el+1
ans+=(s[-1]-s[cur])
print(ans)