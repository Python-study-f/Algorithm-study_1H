# AC
for t in range(1,int(input())+1):
    num, k= input().split()
    k=int(k)
    num=list(num)
    n= len(num)
    mx_val= int(''.join(sorted(list(num),reverse=True)))
    
    chk= {}
    mx=[-1,1]
    def backtrack(cnt,num):
        global mx, mx_val, n;
        ans= int(''.join(num))
        if ans==mx_val: #
            if mx[0]<ans:
                mx= [ans,cnt]
            else:
                if mx[1]%2:
                    mx= [ans,cnt]
        if not cnt: #
            if ans==mx[0]:
                mx[1]= cnt
            elif ans>mx[0]:
                mx= [ans, cnt]
            return True
        for i in range(n):
            for j in range(n):
                if i!=j:
                    nxt= num[:]
                    nxt[i], nxt[j]= nxt[j], nxt[i]
                    new= int(''.join(nxt))
                    if new>=ans and (new,cnt-1) not in chk:
                        chk[(new,cnt-1)]=1
                        backtrack(cnt-1, nxt)
    
    backtrack(k, num)

    print(f'#{t}',end=' ')
    if mx[1]%2:
        a= mx[0]//100*100
        b= mx[0]%100//10
        c= mx[0]%10*10
        print(a+b+c)
    else:
        print(mx[0])