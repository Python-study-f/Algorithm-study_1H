quest = input().split("-")
result = 0
for i in quest[0].split("+"):
    result += int(i)
for i in quest[1:]:
    for j in i.split("+"):
        result -= int(j)
print(result)
