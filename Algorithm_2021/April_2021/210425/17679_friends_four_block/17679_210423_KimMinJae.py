def solution(n, m, b):
    flag=True
    while flag:
        flag=False
        chk=[[False]*m for _ in range(n)]
        for i in range(n-1):
            for j in range(m-1):
                if b[i][j]==b[i+1][j] and b[i+1][j]==b[i+1][j+1] and b[i][j]==b[i][j+1]:
                    if b[i][j]==' ':
                        continue
                    flag=True
                    chk[i][j]=True
                    chk[i+1][j]=True
                    chk[i][j+1]=True
                    chk[i+1][j+1]=True
        if not flag:
            break
        rot=list(map(list, zip(*b[::-1])))
        rotchk=list(map(list, zip(*chk[::-1])))
        [print(*el) for el in rot]
        print()
        for i in range(m):
            for j in range(n):
                if rotchk[i][j]==True:
                    rot[i][j]=' '
                    y, x= i, j
                    while x<n and rotchk[y][x]==True:
                        x+=1
                    if x==n:
                        continue
                    #print(i,j,y,x)
                    rot[i][j], rot[y][x]= rot[y][x],rot[i][j]
                    rotchk[i][j], rotchk[y][x]= rotchk[y][x],rotchk[i][j]
        [print(*el) for el in rot]
        print()
        b=list(map(list, zip(*[el[::-1] for el in rot])))
        [print(*el) for el in b]
        print()
    answer = 0
    for i in range(n):
        for j in range(m):
            if b[i][j]==' ':
                answer+=1
    
    return answer
'''
print(solution(6,6,['TTTANT',
'RRFACC',
'RRRFCC',
'TRRRAA',
'TTMMMF',
'TMMTTJ']))
'''
#print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))


print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))



