N = int(input())
st = []

for i in range(N):
    my_str = str(input())
    cur = 1

    for j in range(len(my_str)):
        if len(my_str) == 0:
            st.append(0)
            break

        if my_str[:cur] == my_str[cur:(cur*2)]:
            st.append(len(my_str[:cur]))
            break
        cur += 1

for i in range(N):
    print("#{0} {1}".format(i,st[i]))