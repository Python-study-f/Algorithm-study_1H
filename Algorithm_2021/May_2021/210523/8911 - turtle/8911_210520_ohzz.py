# 거북이 8911 백준

n = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def tutleMoveSquare(move):
    x, y = 0, 0
    minX, maxX = 0, 0
    minY, maxY = 0, 0
    direct = 0
    for i in move:
        if i == "F":
            x = x + dx[direct]
            y = y + dy[direct]
            minX = min(minX, x)
            maxX = max(maxX, x)
            minY = min(minY, y)
            maxY = max(maxY, y)
        if i == "B":
            x = x - dx[direct]
            y = y - dy[direct]
            minX = min(minX, x)
            maxX = max(maxX, x)
            minY = min(minY, y)
            maxY = max(maxY, y)
        if i == "L":
            if direct == 0:
                direct = 3
            else:
                direct -= 1
        if i == "R":
            if direct == 3:
                direct = 0
            else:
                direct += 1
    area = (abs(minX) + abs(maxX)) * (abs(minY) + abs(maxY))
    return area


for i in range(n):
    command = input()
    print(tutleMoveSquare(command))
