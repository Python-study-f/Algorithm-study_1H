change = 1000 - int(input())
count = 0
money_list = [500, 100, 50, 10, 5, 1]

for money in money_list:
    count += change // money
    change %= money

print(count)