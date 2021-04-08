def change(su, cnt=0):
    a = int(''.join(su))
    if dp[cnt] > a:
        return 0
    dp[cnt] = a
    if cnt == c:
        return 0
    for i in range(len(su)):
        for j in range(i+1,len(su)):
            swap = su[:]
            swap[i], swap[j] = swap[j], swap[i]
            change(swap, cnt+1)


for t in range(int(input())):
    su, c = input().split()
    su = list(su)
    c = int(c)
    dp = [0]*(c+1)
    change(su)
    print('#{}'.format(t+1),dp[-1])