#플로이드 워셜 알고리즘

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i]=0

for _ in range(m):
    dep, arriv, cost = map(int, input().split())
    graph[dep][arriv] = cost

for k in range(1, n+1):
    for dep in range(1, n+1):
        for arriv in range(1, n+1):
            graph[dep][arriv] = min(graph[dep][arriv], graph[dep][k]+graph[k][arriv])

for dep in range(1, n+1):
    for arriv in range(1, n+1):
        if graph[dep][arriv]==INF:
            print("INFINITY", end=" ")
        else:
            print(graph[dep][arriv], end=" ")
    print()