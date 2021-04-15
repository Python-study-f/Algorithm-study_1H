# 10*50
# 50*10 valid
def solution(begin, target, words):
    n= len(begin)
    m= len(words)
    similar= [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if words[i][j]==begin[j]:
                similar[i][j]=1
    
    done=[False]*m
    ans=backtrack(begin, target, words,0,n,m,done)
    return [ans,0][ans==1e9]


def backtrack(ths,target,words,cnt,n,m,done):
    print(ths,cnt)
    if ths==target:
        return cnt

    similar= [[0]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if words[i][j]==ths[j]:
                similar[i][j]=1
    mn= 1e9
    for i in range(m):
        if not done[i] and sum(similar[i])==n-1:
            done[i]=True
            mn=min(mn,backtrack(words[i],target,words,cnt+1,n,m,done))
            done[i]=False
    return mn


    
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))