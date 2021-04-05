def solution(dirs):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    d = {"U": 0, "L":1, "D":2, "R": 3}
    visited = set()
    answer = 0
    x, y = 0, 0
    for dir in dirs:
        i = d[dir]
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y)) 
            answer += 1
        x = nx
        y = ny

    return answer
