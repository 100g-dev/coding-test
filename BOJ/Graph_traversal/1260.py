#1260 - DFS와 BFS

from collections import deque
import sys
input = sys.stdin.readline

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, v, visited):
    que = deque([v])
    visited[v] = True
    
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and not visited[i]:
                que.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
d_visit = [False]*(n+1)
b_visit = [False]*(n+1)

graph = [[0]*(n+1) for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

DFS(graph, v, d_visit)
print()
BFS(graph, v, b_visit)
print()
