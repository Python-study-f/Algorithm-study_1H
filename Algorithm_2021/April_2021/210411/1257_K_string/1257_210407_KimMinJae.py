for t in range(1,int(input())+1):
    k= int(input())
    s=input()
    le= len(s)
    Set=set()
    for i in range(1,le+1):
        for j in range(0,le-i+1):
            Set.add(s[j:j+i])

    print(f'#{t}',end=' ')
    if k>=len(Set):
        print('none')
    else:
        print(sorted(list(Set))[k-1])