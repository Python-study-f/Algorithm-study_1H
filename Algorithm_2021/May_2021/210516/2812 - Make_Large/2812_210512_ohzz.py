# 크게 만들기 2812 백준

# n, k = map(int, input().split())

# number = list(map(int, list(input())))
# comp = sorted(number)

# for i in range(k):
#     del number[number.index(comp[i])]
# number = list(map(str, number))

# print(int("".join(number)))

n, k = map(int, input().split())
number = list(input())
stack = []
ck = k

for i in range(n):
    while stack and ck > 0 and stack[-1] < number[i]:
        del stack[-1]
        ck -= 1
    stack.append(number[i])
    
print("".join(stack[:n - k]))