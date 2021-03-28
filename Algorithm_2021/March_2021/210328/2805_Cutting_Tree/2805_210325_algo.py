n,m=map(int,input().split())
temp=list(map(int,input().split()))
#temp.sort()
start=0
ans=0
sum=max(temp)
end=sum

def calc(height):
    rtn=0
    for i in range(0,n):
        if height<temp[i]:
            rtn+=temp[i]-height

    return rtn


while start<=end:
    mid=(start+end)//2
    tmp=calc(mid)
    if tmp>=m:
        ans=mid
        start=mid+1
    else:
        end=mid-1

print(ans)
