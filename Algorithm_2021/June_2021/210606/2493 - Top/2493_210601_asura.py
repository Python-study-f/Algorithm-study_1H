# brute-force 시간초과
# Stack + memozation으로 해결
N = int(input())
top = list(map(int,input().split()))
st = []
ans = []
memo = [0] * N

for i in range(N):
    check = top[i]

    while st and top[st[-1]] < check:
        st.pop()

    if st:
        memo[i] = st[-1] +1

    st.append(i)

for i in range(len(memo)):
    print(memo[i], end = ' ')