from itertools import combinations

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
store = {}
house = []

cnt = 1
for x in range(n):
    for y in range(n):
        if arr[x][y] == 2:
            store[cnt] = (x,y)
            cnt += 1
        elif arr[x][y] == 1:
            house.append((x,y))

combs = list(combinations(store.keys(),m))
ans = 1e9
for comb in combs:
    chick_dist = 0
    
    for x,y in house:
        house_store = 1e9
        for num in comb:
            i,j = store[num]
            house_store = min(house_store,abs(x-i) + abs(y-j))
        chick_dist += house_store
    ans = min(ans, chick_dist)

print(ans)