n = int(input())
atm_list = list(map(int, input().split()))
atm_list.sort()

atm_time = []
temp_time = 0

for i in atm_list:
    temp_time += i
    atm_time.append(temp_time)


print(sum(atm_time))
