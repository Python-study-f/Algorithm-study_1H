N = int(input())

date = [0 for _ in range(366)] # 366개의 크기를 만듬.
hor, vert, tot_area = 0,0,0 # 가로, 세로, 총 넓이

for _ in range(N):
    first, last = map(int,input().split())

    for i in range(first,last+1): #1차원 배열로 날짜 체크
        date[i] += 1


for i in range(1,len(date)):
    if date[i] != 0:
        hor += 1
        vert = max(date[i],vert)

    else:
        tot_area += vert * hor
        vert = 0
        hor = 0

tot_area += vert * hor # 특수 TC : 마지막까지 0을 안만나는 경우
print(tot_area)