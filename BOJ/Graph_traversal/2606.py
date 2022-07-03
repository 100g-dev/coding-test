#2606 - 바이러스
from collections import deque


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    count = 0

    while queue:
        count+=1
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)

print(bfs(graph, 1, visited)-1)
