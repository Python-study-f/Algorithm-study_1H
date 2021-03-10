import heapq

def doubleHq(bar):
  if bar[0] == "I":
    num = int(bar[2:])
    heapq.heappush(listsMin, (num, j))
    heapq.heappush(listsMax, (-num, j))
    visited[j] = True
    
  else:
    direction = int(bar[2:])
    if direction == -1:
      while listsMin and not visited[listsMin[0][1]]:
        heapq.heappop(listsMin)
      if listsMin:
        idx = heapq.heappop(listsMin)[1]
        visited[idx] = False
    else:
      while listsMax and not visited[listsMax[0][1]]:
        heapq.heappop(listsMax)
      if listsMax:
        idx = heapq.heappop(listsMax)[1]
        visited[idx] = False

# main
for i in range(int(input())):
  numOfelement = int(input())
  listsMin=[]
  listsMax=[]
  visited=[False] * 1000001

  # double heapq
  for j in range(numOfelement):
    doubleHq(input())

  # 정화작업
  while listsMin and not visited[listsMin[0][1]]:
    heapq.heappop(listsMin)
  while listsMax and not visited[listsMax[0][1]]:
    heapq.heappop(listsMax)

  # output  
  if listsMin and listsMax:
    print(-listsMax[0][0],listsMin[0][0])
  else:
    print("EMPTY")
