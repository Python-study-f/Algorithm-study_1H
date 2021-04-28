# 계산기3 1224 SW Expert


for t in range(10):
    n = int(input())
    a = input()
    stack = []
    res = ""
    for x in a:
        if x.isdecimal():
            res += x
        else:
            if x == "(":
                stack.append(x)
            elif x == "*":
                while stack and stack[-1] == "*":
                    res += stack.pop()
                stack.append(x)
            elif x == "+":
                while stack and stack[-1] != "(":
                    res += stack.pop()
                stack.append(x)
            elif x == ")":
                while stack and stack[-1] != "(":
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()

    stack = []
    for k in res:
        if k.isdecimal():
            stack.append(int(k))
        else:
            tmp = 0
            if k == "*":
                tmp += stack.pop() * stack.pop()
                stack.append(tmp)
            elif k == "+":
                tmp += stack.pop() + stack.pop()
                stack.append(tmp)
    print(f"#{t + 1} {stack[0]}")
