import itertools
L,C=map(int,input().split())
temp=set(input().split())
mo=set(['a','e','i','o','u'])
tt=sorted(temp)
for i in itertools.combinations(tt,L):
    #자음이 2개 이상이고 모음이 1개 이상일때 출력
    c=set(i) -mo
    if 2<=len(c) and L-len(c)>=1:
        print(''.join(i))
