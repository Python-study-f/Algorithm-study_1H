# 신입사원 1946 백준

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
    arr = sorted(arr, key=lambda x: (x[1], x[0]))
    prev = arr[0][0]
    cnt = 1
    for k in arr:
        if k[0] < prev:
            prev = k[0]
            cnt += 1
    print(cnt)
