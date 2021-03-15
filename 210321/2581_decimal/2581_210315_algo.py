m = int(input())
n = int(input())
temp = []


def sosu(start):
    check = True
    if start == 1:
        check = False
        return check
    if start == 2:
        return start
    else:
        for i in range(2, start):
            if start % i == 0:
                check = False
                break
        if check:
            return start
        else:
            check = False
            return check


for i in range(m, n + 1):
    tt = sosu(i)
    if tt:
        temp.append(tt)

if len(temp) == 0:
    print(-1)
else:
    print(sum(temp))
    temp.sort()
    print(temp[0])
