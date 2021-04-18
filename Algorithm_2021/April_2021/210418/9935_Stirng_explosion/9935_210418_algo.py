import sys
input = sys.stdin.readline

string = input().rstrip()
bom = input().rstrip()
length = len(bom)
stack = []
for c in string:
    #print(c)
    stack.append(c)
    if c == bom[-1] and ''.join(stack[-length:]) == bom:
        del stack[-length:]
if stack:
    print(''.join(stack))
else:
    print('FRULA')
