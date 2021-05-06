# 달력 20207 백준

n = int(input())

date = [0 for _ in range(369)]
arr = []

h, w = 0, 0
res = 0

for _ in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])
    date[s] += 1
    date[e + 1] -= 1

arr = sorted(arr, key=lambda x: (-x[1]))

for i in range(1, arr[0][1] + 2):
    date[i] += date[i - 1]
    if date[i] == 0:
        res += w * h
        w, h = 0, 0
    else:
        w += 1
        h = max(h, date[i])

print(res)
