# 스마트 물류 414

n, k = map(int, input().split())
line = input()
check = set()
res = 0

for i in range(n):
    if line[i] == "P":
        for j in range(max(0, i - k), min(n, i + k + 1)):
            if line[j] == "H" and j not in check:
                check.add(j)
                res += 1
                break

print(res)
