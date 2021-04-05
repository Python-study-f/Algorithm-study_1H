def solution(dirs):
    y, x= 5,5

    dic={}
    dic['U']= (-1,0)
    dic['D']= (1,0)
    dic['R']= (0,1)
    dic['L']= (0,-1)

    ans={}
    for d in dirs:
        dy, dx= dic[d]
        if 0<=y+dy and y+dy<11 and 0<=x+dx and x+dx<11:
            ny=y+dy
            nx=x+dx
            L=sorted([[y,x],[ny,nx]])
            #print(L)
            for a, b in ((0,0), (0,1), (1,0), (1,1)):
                if len(str(L[a][b]))<2:
                    L[a][b]='0'*(2-len(str(L[a][b])))+str(L[a][b])
                else:
                    L[a][b]=str(L[a][b])
            #print(L)
            y=ny
            x=nx
            ans[''.join(L[0])+''.join(L[1])]=1
    answer=len(ans.keys())
    return answer


#print(solution("LULLLLLLU"))