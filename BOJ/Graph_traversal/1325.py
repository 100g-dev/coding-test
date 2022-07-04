#1325 - 효율적인 해킹
from collections import deque
import sys
input = sys.stdin.readline

def BFS(graph, v):
    que = deque([v])
    visited = [False]*(n+1)
    visited[v] = True
    
    count = 1
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                count += 1
    return count

n, m = map(int, input().split())

graph =[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    #graph[a].append(b)

result = []
max_cnt = 0
for i in range(1, n+1):
    tmp = BFS(graph, i)
    if tmp > max_cnt:
        max_cnt = tmp
        result.clear()
        result.append(i)
    elif tmp == max_cnt:
        result.append(i)

print(*result)