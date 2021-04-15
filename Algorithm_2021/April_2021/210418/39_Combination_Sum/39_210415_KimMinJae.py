# 30 * 500. memory?
# 96.23% 51.23% !!
def combinationSum(candidates,target):
    dp=[[] for _ in range(target+1)] # (address,val)
    candidates.sort()
    for num in candidates:
        for i in range(target+1):
            if i==0 and i+num<=target:
                dp[i+num].append((-1,-i-num))
            elif dp[i] and i+num<=target:
                dp[i+num].append((i,num))
    #[print(i,*dp[i]) for i in range(1,target+1)]
    #print()

    ans=[]
    for ad, v in dp[target]:
        tmp=[]
        #print(ad,v,'start')
        dfs(ad,v,[],tmp,dp)
        #print(tmp)
        ans+=tmp
    return ans

def dfs(address,val,combi,tmp,dp):
    if val<0:
        combi.append(-val)
        tmp.append(combi[::-1])
        combi.pop()
        return

    for na, nv in dp[address]:
        if nv>val or nv<0 and -nv>val:
            continue
        combi.append(val)
        dfs(na,nv,combi,tmp,dp)
        combi.pop()



print(combinationSum([2,7,6,3,5,1],9))   

    
#print(combinationSum([2,3,6,7],7))