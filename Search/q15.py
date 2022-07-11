#q15 - 특정 거리의 도시 찾기
#BOJ 18352

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(n+1)
distance[x] = 0
result = []

que= deque([x])
while que:
    v = que.popleft()
    for  i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v]+1
            if distance[i]==k:
                result.append(i)
            que.append(i)

if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)