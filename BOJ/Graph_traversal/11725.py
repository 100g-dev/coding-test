#11725 - 트리의 부모 찾기

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[]for _ in range(n+1)]
parent = [0]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def BFS(graph, v, parent):
    que = deque([v])
    parent[v] = v

    while que:
        v = que.popleft()
        for i in graph[v]:
            if parent[i]==0:
                parent[i]=v
                que.append(i)

BFS(graph, 1, parent)
for i in range(2, n+1):
    print(parent[i])