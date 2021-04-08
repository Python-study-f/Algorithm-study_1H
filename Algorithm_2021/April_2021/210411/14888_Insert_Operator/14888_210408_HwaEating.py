def make(calc,ls=[]):
    if len(ls) == n-1:
        total.append(ls)
        return 0
    for i in range(4):
        if calc[i] > 0:
            calc[i] -= 1
            make(calc, ls+[i])
            calc[i] += 1
    

def calculate(p, c):
    rs = p.pop(0)
    while p:
        cal = c.pop(0)
        nxt = p.pop(0)
        if cal == 0:
            rs += nxt
        elif cal == 1:
            rs -= nxt
        elif cal == 2:
            rs *= nxt
        elif cal == 3:
            rs = int(rs / nxt)
    return rs


n = int(input())
perm = list(map(int, input().split()))
calc = list(map(int, input().split()))
vis = [0]*n
total = []
rs_set = []
make(calc)
for i in total:
    p = [i for i in perm]
    rs_set.append(calculate(p, i))
print(max(rs_set))
print(min(rs_set))