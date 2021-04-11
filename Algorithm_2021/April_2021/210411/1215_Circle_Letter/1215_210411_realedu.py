


for t in range(1, 11):
    N = int(input())
    MAP = [list(input().rstrip()) for _ in range(8)]

    Count = 0
    # 가로줄 탐색
    for row in range(8):
        for col in range(9 - N):
            row_list = []
            for i in range(N):
                row_list.append(MAP[row][col + i])
            if row_list == row_list[::-1]: # 원문이 거꾸로한 것과 같으면
                Count += 1

    # 세로줄 탐색
    for col in range(8):
        for row in range(9 - N):
            col_list = []
            for i in range(N):
                col_list.append(MAP[row + i][col])
            if col_list == col_list[::-1]:
                Count += 1

    print("#{} {}".format(t, Count))
