import sys; input= lambda: sys.stdin.readline().rstrip()
t= int(input())
n=t*8
gear= ''
for i in range(t):
    gear+=input()
gear=list(gear)

k= int(input())
for _ in range(k):
    id, dir= map(int, input().split())
    id-=1
    rot= [False]*(t+1)
    rot[id]=True

    lo=id*8
    while lo+14<n and gear[lo+2]!=gear[lo+14]:
        rot[lo//8+1]=True
        lo+=8

    hi=id*8
    while -1<hi-6 and gear[hi+6]!=gear[hi-6]:
        rot[hi//8-1]=True
        hi-=8

    for i in range(t):
        if rot[i]:
            m=i*8
            a, b= id%2,i%2
            if (dir>0 and a==b) or (dir<0 and a!=b):
                gear[m:m+8]=[gear[m+7]]+gear[m:m+7]
            else:
                gear[m:m+8]=gear[m+1:m+8]+[gear[m]]

print(sum([1 if gear[i*8]=='1' else 0 for i in range(t)]))