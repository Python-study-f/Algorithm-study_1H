mp= [[0]*21]
mp+= [[0]+[*map(int, input().split())]+[0] for _ in range(19)]
mp+=[[0]*21]

b=[0,0]
w=-1
for i in range(0,21-6):
    for j in range(0,21-6):
        if mp[i][j]!=1 and mp[i+1][j+1]==1 and mp[i+2][j+2]==1 and mp[i+3][j+3]==1 and mp[i+4][j+4]==1 and mp[i+5][j+5]==1 and mp[i+6][j+6]!=1:
            w=1
            b=[i+1,j+1]
        if mp[i+6][j]!=1 and mp[i+5][j+1]==1 and mp[i+4][j+2]==1 and mp[i+3][j+3]==1 and mp[i+2][j+4]==1 and mp[i+1][j+5]==1 and mp[i][j+6]!=1:
            w=1
            b=[i+5,j+1]

for i in range(21):
    for j in range(21-6):
        #print(j,i)
        if mp[i][j]!=1 and mp[i][j+1]==1 and mp[i][j+2]==1 and mp[i][j+3]==1 and mp[i][j+4]==1 and mp[i][j+5]==1 and mp[i][j+6]!=1:
            w=1
            b=[i,j+1]
        if mp[j][i]!=1 and mp[j+1][i]==1 and mp[j+2][i]==1 and mp[j+3][i]==1 and mp[j+4][i]==1 and mp[j+5][i]==1 and mp[j+6][i]!=1:
            
            w=1
            b=[j+1,i]


for i in range(0,21-6):
    for j in range(0,21-6):
        if mp[i][j]!=2 and mp[i+1][j+1]==2 and mp[i+2][j+2]==2 and mp[i+3][j+3]==2 and mp[i+4][j+4]==2 and mp[i+5][j+5]==2 and mp[i+6][j+6]!=2:
            w=2
            b=[i+1,j+1]
        if mp[i+6][j]!=2 and mp[i+5][j+1]==2 and mp[i+4][j+2]==2 and mp[i+3][j+3]==2 and mp[i+2][j+4]==2 and mp[i+1][j+5]==2 and mp[i][j+6]!=2:
            w=2
            b=[i+5,j+1]

for i in range(21):
    for j in range(21-6):
        if mp[i][j]!=2 and mp[i][j+1]==2 and mp[i][j+2]==2 and mp[i][j+3]==2 and mp[i][j+4]==2 and mp[i][j+5]==2 and mp[i][j+6]!=2:
            w=2
            b=[i,j+1]
        if mp[j][i]!=2 and mp[j+1][i]==2 and mp[j+2][i]==2 and mp[j+3][i]==2 and mp[j+4][i]==2 and mp[j+5][i]==2 and mp[j+6][i]!=2:
            w=2
            b=[j+1,i]
            
if w!=-1:
    print(w)
    print(*b)
else:
    print(0)


'''
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
'''