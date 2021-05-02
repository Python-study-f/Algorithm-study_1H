"""
N-Queen 풀었던 방식대로 풀면 될줄 알았는데 이 문제는 체스판에 비숍의 위치가 나타난 상황이라 다른 문제.
풀이 참고에 의하면 검은색, 흰색 체스 판 두개를 나눠서 접근.
"""
n=int(input())

MAP=[]
black=[]
white=[]
color=[[0]*n for _ in range(n)]

# 검은색, 흰색 체스판 입히기
for i in range(n):
    for j in range(n):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            color[i][j] = 1
        else:
            color[i][j] = 0

# print(color)

for i in range(n):
    MAP.append(list(map(int, input().split())))
    for j in range(n):
        # 검은색
        if MAP[i][j]==1 and color[i][j]==1:
            black.append((i,j))
        # 흰색
        if MAP[i][j]==1 and color[i][j]==0:
            white.append((i,j))
# print(black)
# print(white)

# 검은색인 경우
Bcnt=0
# 흰색인 경우
Wcnt=0

check1=[0]*(n*2-1) # /
check2=[0]*(n*2-1) # \

def fun(bishop,index,count):
    global Bcnt, Wcnt
    if index==len(bishop):
        rx,ry=bishop[index-1]
        # 검은색
        if color[rx][ry]:
            Bcnt=max(Bcnt,count)
        # 흰색
        else:
            Wcnt=max(Wcnt,count)
        return

    x,y=bishop[index]
    

    if check1[x + y] == 0 and check2[x-y+n-1] == 0:
        check1[x+y]=1
        check2[x-y+n-1]=1
        fun(bishop,index+1,count+1)
        check1[x+y]=0
        check2[x-y+n-1]=0
        fun(bishop,index+1,count)
    else:
        fun(bishop, index+1, count)

if len(black)>0:
    fun(black,0,0)
if len(white)>0:
    fun(white,0,0)

print(Bcnt+Wcnt)
