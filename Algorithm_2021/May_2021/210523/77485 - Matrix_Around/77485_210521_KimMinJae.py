dir= [(0,1), (1,0), (0,-1), (-1,0)]
col=0
mp=[]
def rotate(y,x,loy,lox,hiy,hix,way,prv,mn):
    if mp[y][x]==20000:
        global col
        mp[y][x]=col*y+x+1
    tmp=mp[y][x]
    mn= min(mn,mp[y][x])
    mp[y][x]=prv
    ny= y+dir[way][0]
    nx= x+dir[way][1]
    if loy<=ny<=hiy and lox<=nx<=hix:
        return rotate(ny,nx,loy,lox,hiy,hix,way,tmp,mn)
    else:
        way= (way+1)%4
        if not way:
            return mn
        ny= y+dir[way][0]
        nx= x+dir[way][1]
        return rotate(ny,nx,loy,lox,hiy,hix,way,tmp,mn)
   
def solution(rows, columns, queries):
    global col
    col=columns
    global mp
    answer = []
    mp= [[20000]*columns for _ in range(rows)]    
    for a, b, c, d in queries:
        a-=1
        b-=1
        c-=1
        d-=1
        answer.append(rotate(a,b,a,b,c,d,0,30000,1e9))
        
    return answer

