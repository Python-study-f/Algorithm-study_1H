TC = int(input())
for test_case in range(TC):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(2)]

    arr[0][1] = arr[0][1] + arr[1][0]
    arr[1][1] = arr[1][1] + arr[0][0]

    for k in range(2, N):
        arr[0][k] = arr[0][k] + max(arr[1][k - 1], arr[1][k - 2])
        arr[1][k] = arr[1][k] + max(arr[0][k - 1], arr[0][k - 2])

    answer = max(arr[0][N-1], arr[1][N-1])
    print(answer)
