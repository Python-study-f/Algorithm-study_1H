import sys; input= lambda:sys.stdin.readline().rstrip(); 
n= int(input())
L=[*map(int, input().split())]
op=[*map(int, input().split())]

mx=-1e9
mn=1e9
def backtrack(i,s):
    if i==n:
        global mx, mn
        mx= max(mx, s)
        mn= min(mn, s)
        return

    for j in range(4):
        if op[j]>0:
            op[j]-=1
            if j==0:
                ns=s+L[i]
            elif j==1:
                ns=s-L[i]
            elif j==2:
                ns=s*L[i]
            else:
                if s<0:
                    ns= -s//L[i]
                    ns=-ns
                else:
                    ns=s//L[i]
            backtrack(i+1, ns)
            op[j]+=1

backtrack(1,L[0])           
print(mx,mn,sep='\n')


