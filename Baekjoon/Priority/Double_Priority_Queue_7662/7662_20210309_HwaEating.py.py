import sys
from heapq import heappop, heappush
input = sys.stdin.readline

for t in range(int(input())):
    mnh = []
    mxh = []
    check = {}
    cnt = 0
    k = int(input())
    for _ in range(k):
        order, num = input().split()
        if order == 'I':
            num = int(num)
            heappush(mnh, num)
            heappush(mxh, -num)
            cnt += 1
            if check.get(num):
                check[num] += 1
            else:
                check[num] = 1
        elif cnt:
            cnt -= 1
            if num == '1':
                su = -heappop(mxh)
                while not check[su]:
                    su = -heappop(mxh)
            else:
                su = heappop(mnh)
                while not check[su]:
                    su = heappop(mnh)     
            check[su] -= 1
    if cnt:
        mx = -heappop(mxh)
        while not check[mx]:
            mx = -heappop(mxh)
        mn = heappop(mnh)
        while not check[mn]:
            mn = heappop(mnh)
        print(mx,mn)
    else:
        print('EMPTY')

