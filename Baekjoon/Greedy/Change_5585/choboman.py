price = int(input())
count = 0
get_money = 1000 - price

rests = [500, 100, 50, 10, 5, 1]

for rest in rests:      # [500, 100, 50, 10, 5, 1]
    while get_money - rest >= 0:
        get_money = get_money - rest
        count = count + 1

print(count)

