from collections import deque

def perm(ls=[]):
    if len(ls) == 5:
        perm_ls.append(ls)
        return
    for i in range(4):
        perm(ls+[i])
def left():
    global mx
    for x in range(n):
        q = deque()
        for y in range(n):
            if bd[x][y] != 0:
                q.append(bd[x][y])
                bd[x][y] = 0
        i = 0
        while q:
            no1, no2 = 0,0
            no1 = q.popleft()
            if q:
                no2 = q.popleft()
            if no1 == no2:
                bd[x][i] = (no1+no2)
                if no1+no2 > mx:
                    mx = no1+no2
            elif no2 != 0:
                q.appendleft(no2)
                bd[x][i] = no1
            else:
                bd[x][i] = no1
            i += 1

def right():
    global mx
    for x in range(n):
        q = deque()
        for y in range(n-1,-1,-1):
            if bd[x][y] != 0:
                q.append(bd[x][y])
                bd[x][y] = 0
        i = n-1
        while q:
            no1, no2 = 0,0
            no1 = q.popleft()
            if q:
                no2 = q.popleft()
            if no1 == no2:
                bd[x][i] = (no1+no2)
                if no1+no2 > mx:
                    mx = no1+no2
            elif no2 != 0:
                q.appendleft(no2)
                bd[x][i] = no1
            else:
                bd[x][i] = no1
            i -= 1
def up():
    global mx
    for y in range(n):
        q = deque()
        for x in range(n):
            if bd[x][y] != 0:
                q.append(bd[x][y])
                bd[x][y] = 0
        i = 0
        while q:
            no1, no2 = 0,0
            no1 = q.popleft()
            if q:
                no2 = q.popleft()
            if no1 == no2:
                bd[i][y] = (no1+no2)
                if no1+no2 > mx:
                    mx = no1+no2
            elif no2 != 0:
                q.appendleft(no2)
                bd[i][y] = no1
            else:
                bd[i][y] = no1
            i += 1
    pass
def down():
    global mx
    for y in range(n):
        q = deque()
        for x in range(n-1,-1,-1):
            if bd[x][y] != 0:
                q.append(bd[x][y])
                bd[x][y] = 0
        i = n-1
        while q:
            no1, no2 = 0,0
            no1 = q.popleft()
            if q:
                no2 = q.popleft()
            if no1 == no2:
                bd[i][y] = (no1+no2)
                if no1+no2 > mx:
                    mx = no1+no2
            elif no2 != 0:
                q.appendleft(no2)
                bd[i][y] = no1
            else:
                bd[i][y] = no1
            i -= 1
    pass

exe = [left,right,up,down]
n=int(input())
o_bd = [list(map(int,input().split())) for i in range(n)]
mx = 0
for x in range(n):
    for y in range(n):
        if o_bd[x][y] > mx:
            mx = o_bd[x][y]  
perm_ls=[]
perm()
for i in perm_ls:
    bd = [i[:] for i in o_bd]
    for j in i:
        exe[j]()
print(mx)
