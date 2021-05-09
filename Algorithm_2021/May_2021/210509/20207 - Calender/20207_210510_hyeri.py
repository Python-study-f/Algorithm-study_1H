N = int(input())
date = [0] * 367

for i in range(N):
    s, e = map(int, input().split())
    for j in range(s, e+1):
        date[j] += 1

answer = 0
ms = 366
me = 0
mh = 0
for i in range(1, 367):
    if date[i] == 0:
        answer += mh * (me - ms + 1)
        mh = 0
        me = 0
        ms = 366
    else:
        ms = min(ms, i)
        me = max(me, i)
        mh = max(mh, date[i])


print(answer)
