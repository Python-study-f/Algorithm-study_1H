import sys
input = sys.stdin.readline
for T in range(int(input())):
    n = int(input())
    resumes = [0]*(n+1)
    interviews = [0]*(n+1)
    for i in range(1,n+1):
        resume, interview = map(int,input().split())
        resumes[resume] = i
        interviews[i] = interview
    ans = 0
    limit = 1e9
    for i in range(1,n+1):
        if limit > interviews[resumes[i]]:
            limit = interviews[resumes[i]]
            ans += 1

    print(ans)