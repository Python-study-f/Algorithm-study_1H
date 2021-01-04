from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    

if __name__ == "__main__":
    graph = []
    dots, lines, start = map(int, input().split())
    for i in range(lines):
        line = list(map(int, input().split()))
        graph.append(line)

    graph1 = [[] for i in range(dots + 1)]

    for line in graph:
        a, b = line
        graph1[a].append(b)
        graph1[b].append(a)  

    for i in graph1:
        i.sort()
        
    visited = [False] * (dots + 1)
    dfs(graph1, start, visited)
    print()
    visited = [False] * (dots + 1)
    bfs(graph1, start, visited)