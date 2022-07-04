#2667 - 단지번호붙이기
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    que = deque()
    que.append((x, y))
    graph[x][y] = 0
    count = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny>=n:
                continue
            if  graph[nx][ny]==1:
                graph[nx][ny]=0
                que.append((nx, ny))
                count+=1

    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            result.append(bfs(graph, i, j))

result.sort()
print(len(result))
for cnt in result:
    print(cnt)