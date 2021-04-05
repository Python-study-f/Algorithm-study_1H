T = int(input())
for tc in range(1, T+1):

    s = input()

    temp = []
    for i in range(1, 11):
        temp.append(s[:i])
    ans = 10
    for i in range(10):
        size = len(temp[i])

        if s[:size] == s[size:size*2]:

            if size < ans:
                ans = size
                break
    print('#{} {}'.format(tc, ans))
