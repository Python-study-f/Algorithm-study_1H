#from time import *
t = 1
#t = int(input())
for _ in range(t):
    r , c = map(int, input().split())
    n , m = map(int, input().split())
    Dy = [-1 , 0 , 1 , 0]
    Dx = [0 , 1 , 0, -1]
    # N E S W
    way = {'W':0 , 'N':1 , 'E':2 , 'S':3 , 'R':1 , 'L':-1}
    R = [[] for _ in range(n + 1)]
    mp = [ [0] * c for _ in range(r)]
    for i in range(1 , n + 1):
        y , x , d = input().split()
        y = int(y) - 1
        x = int(x) - 1
        R[i] = [y , x , way[d]]
        mp[y][x] = i
    #[print(*el) for el in mp]
    def chk(y , x):
        #print(y , x)
        
        if y < 0 or y >= r or x < 0 or x >= c:
            return 'the wall'
        elif mp[y][x]:
            return 'robot '+str(mp[y][x])
        else:
            return ''
    flag=False
    for _ in range(m):
        rob , cmd , num =  input().split()
        rob = int(rob)
        num = int(num)  
        if flag:
            continue
        if cmd != 'F':
            num %= 4
            R[rob][2] =( (R[rob][2] + way[cmd]* num + 4 ) % 4)
        else:
            y = R[rob][0]
            x = R[rob][1]
            w = R[rob][2]
            mp[y][x] = 0
            for _ in range(num):
                #print(w)
                res = chk(y + Dy[w] , x + Dx[w])
                if res:
                    flag=True
                    print(f'Robot {rob} crashes into {res}')
                    break
                else:
                    y += Dy[w]
                    x += Dx[w]
            mp[y][x] = rob
            R[rob] = [y , x , w]
        #print()
        #[print(*el) for el in mp]
    if not flag:

        print('OK')
    #sleep(1)
'''
5 4
2 3
1 1 E
5 2 E
1 F 4
1 L 3
1 F 2


5 4
2 2
1 4 E
5 4 W
1 F 3
2 F 1


5 5
2 3
3 3 E
4 5 N
2 L 3
2 R 8
2 F 3
Robot 2 crashes into the wall

'''