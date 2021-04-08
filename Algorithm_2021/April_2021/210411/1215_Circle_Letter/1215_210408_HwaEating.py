import math

for i in range(10):
    t_no = int(input())
    t_var = math.floor(t_no/2)
    board = []
    chk = 0
    for j in range(8):
        board.append([i for i in input()])
    for k in range(8):
        pal = board[k]
        for z in range(9-t_no):
            ck_s = 0
            if t_no % 2 == 1:
                for t in range(t_var) :
                    if pal[z+t]==pal[z-t+t_no-1]:  # t_no = 4일때 (0, 3) (1, 2) 비교, t_no = 5 일때 (0, 4) (1, 3) 비교
                        ck_s += 1
            else :
                for t in range(t_var) :
                    if pal[z+t]==pal[z-t+t_no-1]:
                        ck_s += 1
            if ck_s == t_var:
                chk += 1
    board_z = list(zip(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7]))
    for a in range(8):
        pal_z = board_z[a]
        for b in range(9-t_no):
            ckz_s = 0
            if t_no % 2 == 1:
                for c in range(t_var) :
                    if pal_z[b+c]==pal_z[b-c+t_no-1]:  # t_no = 4일때 (0, 3) (1, 2) 비교, t_no = 5 일때 (0, 4) (1, 3) 비교
                        ckz_s += 1
            else :
                for c in range(t_var) :
                    if pal_z[b+c]==pal_z[b-c+t_no-1]:
                        ckz_s += 1
            if ckz_s == t_var:
                chk += 1
    
    
    print(f'#{i+1} {chk}')
    