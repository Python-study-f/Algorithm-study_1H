n = int(input())
num = list(sorted(map(int, input().split())))

len_num = len(num)
count = []

for i in range(len_num):
    if i == 0:
        count.append(num[i])
    elif i > 0:
        count.append(count[i - 1] + num[i])

print(sum(count))