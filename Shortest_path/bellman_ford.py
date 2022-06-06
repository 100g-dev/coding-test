#벨만포드 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []
distance = [INF]*(n+1)

for _ in range(m):
    dep, arriv, cost = map(int, input().split())
    edges.append((dep, arriv, cost))

def bellmanford(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            now, next, cost = edges[j]

            if distance[now] != INF and distance[next] > distance[now]+cost:
                distance[next] = distance[now]+cost
                if i == n-1:
                    return True
    return False

if bellmanford(1):
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])