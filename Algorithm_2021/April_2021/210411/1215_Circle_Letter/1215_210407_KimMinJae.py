for t in range(1,11):
    ans=0
    n= int(input())
    mp= [list(input()) for _ in range(8)]
    
    for i in range(8):
        for j in range(8-n+1):
            s=mp[i][j:j+n]
            if s==s[::-1]:
                ans+=1
    rot= [[' ']*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            rot[j][8-i-1]= mp[i][j]
    for i in range(8):
        for j in range(8-n+1):
            s=rot[i][j:j+n]
            if s==s[::-1]:
                ans+=1
    print(f'#{t}', end=' ')
    print(ans)
