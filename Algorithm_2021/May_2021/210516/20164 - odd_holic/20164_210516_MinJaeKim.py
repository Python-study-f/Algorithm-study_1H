N = input()
mn = int(1e9)
mx=-1
def div(s,cnt):
    global mn, mx
    #print('s, cnt: ',s,cnt)
    for el in s:
        if int(el)%2:
            cnt+=1
    if len(s)>=3:
        for i in range(1,len(s)-1):
            for j in range(i+1,len(s)):
                #print('\t',len(s), i, j)
                #print(s[:i], s[i:j], s[j:])
                a = str(sum([int(s[:i]), int(s[i:j]), int(s[j:])]))
                if len(a)>=3:
                    div(a,cnt)
                else:
                    div(a,cnt)
    elif len(s)==2:
        a = str(int(s[0])+int(s[1]))
        div(a,cnt)
    else: # len 1
        if cnt<mn:
            mn=cnt
        if cnt>mx:
            mx=cnt
        #print('답 추가', cnt)
        
div(N,0)

print(mn,mx)