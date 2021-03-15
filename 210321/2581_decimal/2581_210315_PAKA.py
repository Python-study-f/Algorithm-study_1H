minVal = int(input())
maxVal = int(input())
result = []

for i in range(minVal, maxVal+1):
  count = 0
  for j in range(1,i+1):
    if i % j == 0:
      count +=1
    if count > 2:
      break
  if count == 2:
    result.append(i)

if result:
  print(sum(result))
  print(result[0])
else:
  print(-1)