# 탑 2493 백준
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
res = []


for i in range(n):
    while stack:
        if stack[-1][0] > arr[i]:
            res.append(stack[-1][1] + 1)
            break
        stack.pop()

    if not stack:
        res.append(0)

    stack.append([arr[i], i])

for j in range(n):
    print(res[j], end=" ")

# 시간초과
# for i in range(n):
#     top.append([arr[i], i + 1])

# for i in range(n):
#     tmp = top[i][0]
#     for j in range(i - 1, -1, -1):
#         if tmp < top[j][0]:
#             stack.append(top[j][1])
#             break
#     else:
#         stack.append(0)

# for i in range(n):
#     print(stack[i], end=" ")
