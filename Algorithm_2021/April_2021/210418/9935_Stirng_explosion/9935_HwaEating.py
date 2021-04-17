s = input()
bomb = input()
n = len(bomb)
stack = []
for i in s:
    stack.append(i)
    if len(stack) >= n and stack[-1] == bomb[-1]:
        if ''.join(stack[-n:]) == bomb:
            for _ in range(n):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')