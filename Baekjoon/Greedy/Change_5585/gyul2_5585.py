coin=[500, 100, 50, 10, 5, 1]
change = 1000-int(input())
count = 0
for i in coin:
    count = count + (change // i)
    change = change % i

print( count)