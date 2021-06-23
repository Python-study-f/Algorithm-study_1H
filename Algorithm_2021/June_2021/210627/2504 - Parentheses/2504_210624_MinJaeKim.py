s = input()

def cal():
    stc = []
    layer = [0] * 31
    top = 0
    for el in s:
        if el == '(' or el == '[':
            top +=1
            if top>30: # 이거 안해줘서 문제
                return 0
            stc.append(el)
        elif el == ')':
            tmp = sum(layer[top + 1:])
            if not tmp:
                layer[top] += 2
            else:
                layer[top] += 2 * tmp
            if not stc:
                return 0
            cur = stc.pop()
            if cur != '(': # 이거 안해줘서 문제
                return 0
            for i in range(top + 1, 31):
                layer[i] = 0
            top -=1
        elif el == ']':
            tmp = sum(layer[top + 1:])
            if not tmp:
                layer[top] += 3
            else:
                layer[top] += 3 * tmp
            if not stc:
                return 0
            cur = stc.pop()
            if cur != '[': # 이거 안해줘서 문제
                return 0
            for i in range(top + 1, 31):
                layer[i] = 0
            top -=1
        #print(layer)
    if stc:
        return 0
    return sum(layer)

print(cal())
