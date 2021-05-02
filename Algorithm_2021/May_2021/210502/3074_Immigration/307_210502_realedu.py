"""
이분 탐색.
시키는 대로 풀려고 하면 무조건 꼬임
"""
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    time = []

    for _ in range(N):
        time.append(int(input()))
    left, right = min(time), max(time) * M
    result = right

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for t in time:
            people += mid // t
        # 심사대에 사람들 다 섰을 때
        if people >= M:
            right = mid - 1
            result = min(result, mid)
        # 심사대에 사람들 다 안섰으면 다시 돌리고
        else:
            left = mid + 1


    print("#{} {}".format(tc+1, result))

