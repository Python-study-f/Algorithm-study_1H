N = int(input())
temp = list(map(int, input().rstrip().split()))
visited = [0 for _ in range(N)]
stack = []

for i in range(len(temp) - 1, -1, -1):
    if len(stack) == 0:
        stack.append([i, temp[i]])
    else:
        while temp[i] > stack[len(stack) - 1][1]:
            tower = stack.pop()
            visited[tower[0]] = i + 1
            if len(stack) == 0:
                break

        stack.append([i, temp[i]])

for num in visited:
    print(num, end=" ")
