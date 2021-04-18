s = ")(((((()())()()))()(()))("

stack = []
temp = []
ans = 0
tmp = 0
for char in s:
    if char == '(':
        if tmp:
            temp.append(tmp)
            tmp = 0
        stack.append(char)
        temp.append(char)
    elif stack and stack[-1] == '(':
        while type(temp[-1]) == int:
            tmp += temp[-1]
            temp.pop()
        temp.pop()
        stack.pop()
        tmp += 2
    else:
        if tmp:
            temp.append(tmp)
            tmp = 0
        stack.append(char)
        temp.append(char)


if tmp:
    temp.append(tmp)
    tmp = 0


while temp:
    if temp[-1] == '(' or temp[-1] == ')':
        temp.pop()
        tmp = 0
    else:
        tmp += temp.pop()
        ans = max(tmp,ans)

print(ans)