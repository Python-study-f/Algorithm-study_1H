T = int(input())

for test_case in range(1, T + 1):
    K = int(input())
    S = str(input())

    value = set()
    for i in range(1, len(S)):
        for j in range(len(S)):
            if j+i > len(S):
                break;
            value.add(S[j:j + i])

    value.add(S)
    value = list(value)
    value.sort()

    if K >= len(value):
        answer = "none"
    else:
        answer = value[K-1]

    print("#{} {}".format(test_case, answer));
