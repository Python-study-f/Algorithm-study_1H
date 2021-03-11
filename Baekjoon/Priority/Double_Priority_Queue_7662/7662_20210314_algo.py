import heapq
import sys

T=int(sys.stdin.readline())


for i in range(T):
    n=int(input())
    visit = [False for i in range(0, 1000001)]
    minheap = []
    maxheap = []

    for i in range(n):
        command, data = sys.stdin.readline().split()
        if command == 'I':
            heapq.heappush(minheap, (int(data),i))
            heapq.heappush(maxheap, (int(data)*-1,i))
            visit[i]=True
        else:
            if len(minheap) > 0 or len(maxheap)>0:
                if data == '-1':
                    while minheap and not visit[minheap[0][1]]:
                        heapq.heappop(minheap)
                    if not maxheap: continue
                    if minheap:
                        index=heapq.heappop(minheap)[1]
                        visit[index]=False
                else:
                    while maxheap and not visit[maxheap[0][1]]:
                        heapq.heappop(maxheap)
                    if not minheap: continue
                    if maxheap:
                        index = heapq.heappop(maxheap)[1]
                       # print(index)
                        visit[index] = False

    while minheap and not visit[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visit[maxheap[0][1]]:
        heapq.heappop(maxheap)
    if len(maxheap) == 0:
        print("EMPTY")
    else:
        print(-maxheap[0][0], minheap[0][0])

