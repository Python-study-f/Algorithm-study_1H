n = int(input())
atm_list = list(map(int, input().split()))
atm_list.sort()

atm_time = []
temp_time = 0

for i in atm_list:
    temp_time += i
    atm_time.append(temp_time)


print(sum(atm_time))

"""

n = int(input())
s = list(map(int, input().split()))
num = 0
s.sort()

for i in range(n):  # n회 반복
    for j in range(i + i):
        num = num + s[j]

"""
