string_num = input()
count_zero = 0  # 0 -> 1
count_one = 0  # 1 -> 0

if string_num[0] == '0':
    count_zero += 1
else:
    count_one += 1

for n in range(1, len(string_num)):
    if string_num[n - 1] != string_num[n]:
        if string_num[n] == '0':
            count_zero += 1
        else:
            count_one += 1

print(min(count_zero, count_one))
