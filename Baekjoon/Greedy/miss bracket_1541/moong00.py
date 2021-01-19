quest = input().split("-")
result = 0
for i in quest[0].split("+"):
    result += int(i)
for y in quest[1].split("+"):
    result -= int(y)
print(result)