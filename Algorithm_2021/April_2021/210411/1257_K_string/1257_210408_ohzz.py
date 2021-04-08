# K번째 문자열 1257

T = int(input())

for t in range(T):
    tmp = []
    k = int(input())
    s = input()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            tmp.append(s[i:j])
    tmp = set(tmp)
    tmp = list(tmp)
    tmp.sort()
    if len(tmp) < k:
        print(f"#{t + 1} none")
    else:
        print(f"#{t + 1} {tmp[k - 1]}")
