change = int(input())
count = 0

while change > 0:
    if change % 5 == 0:
        count += change // 5
        print(count)
        break
    change -= 2
    count += 1

if change < 0:
    print('-1')
