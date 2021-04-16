st = str(input())
boom = str(input())

# 스택처럼 이용
ans = []
for i in st:
    ans.append(i)
    if len(ans) < len(boom):
        continue
    if boom == "".join(ans[len(ans) - len(boom):]):
        for j in range(len(boom)):
            ans.pop()

if len(ans) == 0:
    print("FRULA")
else:
    print(*ans, sep="")
