# 회문1 1215

for t in range(10):
    n = int(input())
    board = [list(input().strip()) for _ in range(8)]
    cnt = 0
    for i in range(9 - n):
        for j in range(8):
            tmp = board[j][i : i + n]
            if tmp == tmp[::-1]:
                cnt += 1
            for k in range(n // 2):
                if board[i + k][j] != board[i + n - 1 - k][j]:
                    break
            else:
                cnt += 1
    print(f"#{t + 1} {cnt}")
