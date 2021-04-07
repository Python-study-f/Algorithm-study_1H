# TLE
for t in range(1,int(input())+1):
    num, k= input().split()
    k=int(k)
    L=sorted(list(num),reverse=True)
    le= len(L)
    mx= int(''.join(L))
    ans=0
    remain=1e9
    ls=[0]*10
    dic={}
    for i in range(le):
        if num[i] not in dic:
            dic[num[i]]=[]
        dic[num[i]].append(i)

    for el in num:
        ls[int(el)]+=1
    def backtrack(THS,cnt):
        nm= int(''.join(THS))
        print(nm, cnt)
        global ans, remain
        remain= min(remain,cnt)
        ans= max(ans, nm)
        if nm==mx:
            
            return
        if not cnt:
            return
        
        global le
        for idx, (a, b) in enumerate(zip(THS, L)):
            if a!=b:
                for k in dic[b]:
                    ths=THS[:]
                    #print(idx, k)
                    if idx<k:
                        ths[k], ths[idx]= ths[idx], ths[k]
                        backtrack(ths,cnt-1)
                break
    backtrack(list(num), k)
    #print(remain, ans)
    print(f'#{t}',end=' ')
    if not remain%2:
        print(ans)
    else:
        a= ans//100*100
        b= ans%100//10
        c= ans%10*10
        print(a+b+c)






'''
for t in range(1,int(input())+1):
    num, k= input().split()
    k=int(k)
    L=[]
    for idx, el in enumerate(num):
        L.append((el,idx))
    M=L[:]
    L.sort()

    if list(num)==sorted(num,reverse=True):
        ans=sorted(num,reverse=True)
        if not k%2:
            print(''.join(ans))
        else:
            ans[-1], ans[-2]= ans[-2], ans[-1]
            print(''.join(ans))
        continue
    top=len(num)-1
    left=0
    right=top
    ans=[0]*(top+1)
    ls=[]
    chk=[False]*(top+1)
    while left<=right and k:
        if chk[L[right][1]]==True:
            right-=1
            continue
        if chk[M[left][1]]==True or M[left][0]==L[right][0] :
            left+=1
            continue

        k-=1
        if left==right:
            ls.append(M[left][0])
            chk[M[left][1]]=True
            k+=1
        else:
            ls.append(M[left][0])
            ls.append(L[right][0])
            chk[L[right][1]]=True
            chk[M[left][1]]=True
        left+=1
        right-=1
    
    ls.sort()
    #print(ls)
    #print(chk)
    #print(k)
    print(f'#{t}',end=' ')
    for i in range(top+1):
        if chk[i]:
            ans[i]=ls.pop()
        else:
            ans[i]=num[i]
    if not k%2:
        print(''.join(ans))
    else:
        ans[-1], ans[-2]= ans[-2], ans[-1]
        print(''.join(ans))
    




'''