import sys; input= lambda: sys.stdin.readline().rstrip()
s= input()
ths=input()
n= len(s)
m=len(ths)

cur=0

flag=True
remain=[True]*n
candi=[[0,n]]
while flag:
    #print('new turn',candi)
    flag=False
    nxt=[]
    for st, ed in candi:
        #print(st,ed)
        for i in range(st,ed):
            if not remain[i]:
                continue
            if s[i]==ths[cur]:
                cur+=1
                if cur==m:
                    flag=True
                    k=i
                    tmp=m
                    while tmp and 0<=k: ##########
                        if remain[k]:
                            remain[k]=False
                            tmp-=1
                        k-=1
                    #print(s[k+1],k+1,'st   ',s[i],i,'ed')
                    left, right= k,i
                    tmp=m-1
                    while tmp and 0<=left:
                        if remain[left]:
                            tmp-=1
                        left-=1
                    tmp=m-1
                    while tmp and right<=n-1:
                        if remain[right]:
                            tmp-=1
                        right+=1
                    #print(''.join([(s[i] if remain[i] else ' ') for i in range(n)]))
                    cur=0
                    nxt.append((max(0,left+1),min(n,right+1)))
            else:
                cur=0
                if s[i]==ths[cur]:
                    cur+=1
    candi=nxt[:]
ans=''.join([(s[i] if remain[i] else '') for i in range(n)])
print([ans,'FRULA'][not ans])