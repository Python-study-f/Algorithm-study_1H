T = int(input())


def pal(st, l, r, chk):
    while st[l] == st[r] and l < r:
        l += 1
        r -= 1
    if l >= r:
        return chk
    if chk == 0:
        ans1 = pal(st, l + 1, r, 1)
        ans2 = pal(st, l, r - 1, 1)a
        return min(ans1, ans2)
    else:
        return 2


for test_case in range(T):
    sent = str(input())
    print(pal(sent, 0, len(sent) - 1, 0))
