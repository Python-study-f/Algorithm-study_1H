def measure(k, m, sup):
    tot=0
    for el in sup:
        tot+=k//el
    if tot>=m:
        return True
    else:
        return False

for i in range(int(input())):
    n, m= map(int, input().split())
    sup=[]
    for _ in range(n):
        sup.append(int(input()))
    lo=0
    hi=1e14
    ans=0
    while lo<=hi:
        mid= (lo+hi)//2
        #print(lo,hi,mid)
        if measure(mid,m,sup):
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    print(f'#{i+1} {int(ans)}')

