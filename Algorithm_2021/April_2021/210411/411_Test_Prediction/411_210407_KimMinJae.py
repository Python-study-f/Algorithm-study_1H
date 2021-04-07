n, k= map(int, input().split())

belt= list(input())
ans=0
for rob in range(n):
    if belt[rob]=='P':
        for i in range(max(0,rob-k), min(n,rob+k+1)):
            if belt[i]=='H':
                ans+=1
                belt[i]='X'
                break
print(ans)

