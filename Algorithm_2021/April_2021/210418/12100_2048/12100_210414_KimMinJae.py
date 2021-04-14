# WA why? ? wheteullyoyo?.?
import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
import time
n= int(input())
ans=0
B= [[*map(int, input().split())] for _ in range(n)]
for i in range(n):
        for j in range(n):
            ans= max(ans, B[i][j])
ans= -ans
def rec(stage,B):

    for i in range(4):
        if stage<=4:
            rec(stage+1,move(i,B))
        else:
            move(i,B)

def move(d,L):
    #time.sleep(1)
    global n,ans
    # d별로 회전
    R=[]
    #0
    if d==0:
        R=[el for el in L]
    #90
    elif d==1:
        R= list(map(list, zip(*[el[::-1] for el in L])))
    #180
    elif d==2:
        R= [el[::-1] for el in L[::-1]]
    #270
    elif d==3:
        R= list(map(list, zip(*[el for el in L[::-1]])))

    
    print('rotated',d)
    [print(*el) for el in R]
    print()
    for i in range(n):
        for j in range(n):
            ths=R[i][j]
            if ths<=0:
                continue
            for k in range(j+1,n):
                if R[i][k]:
                    if R[i][k]==ths:
                        R[i][k]=0
                        R[i][j]=-ths*2
                    break #1
    
    print('block put together')
    [print(*el) for el in R]
    print()
    for i in range(n):
        for j in range(n):
            if not R[i][j]:
                find=j+1
                while find<n and not R[i][find]:
                    find+=1
                if find<n:
                    R[i][j], R[i][find]= R[i][find], R[i][j]
            ans= min(ans,R[i][j])
    print('converged')
    [print(*el) for el in R]
    print()


    # d 맞춰 원상태
    if d==0:
        return R
    #90
    elif d==1:
        return list(map(list, zip(*[el for el in R[::-1]])))
        
    #180
    elif d==2:
        return [el[::-1] for el in R[::-1]]
    #270
    elif d==3:
        return list(map(list, zip(*[el[::-1] for el in R])))


rec(1,B)
print(-ans)




    
    # d별로 원상태

'''
4
4 2 0 0
0 0 0 0
0 0 0 0
2 0 0 0

4
2 0 2 8
0 0 2 2
0 0 0 0
0 0 0 0
'''