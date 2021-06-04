n = int(input())
arr = list(enumerate(map(int,input().split())))
ans = [0]*n
stack = []
while arr:
    idx, height = arr.pop()
    if not arr:
        break
    if height < arr[-1][1]:
        ans[idx] = arr[-1][0]+1
    else:
        stack.append((idx,height))

    while stack and stack[-1][1] < arr[-1][1]:
        idx,height = stack.pop()
        ans[idx] = arr[-1][0]+1

print(*ans)