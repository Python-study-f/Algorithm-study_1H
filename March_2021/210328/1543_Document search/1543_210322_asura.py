data = str(input())
my_str = str(input())

i = 0
cnt = 0

while True:
    if i > len(data):
        break

    if data[i:i+len(my_str)] == my_str:
        i = i + len(my_str)
        cnt += 1
    else:
        i+=1

print(cnt)