s = input()

st_1 = []
st_2 = []
coper = 1
isPair = True
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        st_1.append(i)
        coper *= 2
    elif s[i]== '[':
        st_2.append(i)
        coper *= 3
    elif s[i] == ')':
        if st_1:
            if s[i-1] == '(':
                ans += coper
            st_1.pop()
            coper = coper // 2

        else:
            isPair = False
    elif s[i] == ']':
        if st_2:
            if s[i-1] == '[':
                ans += coper
            st_2.pop()
            coper = coper // 3
        else:
            isPair = False
            break

if not st_1 and not st_2 and isPair:
    print(ans)
else:
    print(0)