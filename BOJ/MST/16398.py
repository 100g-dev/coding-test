#16398 - 행성 연결

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_root(parent, a)
    b = find_root(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

parent = [0]*(n)
for i in range(n):
    parent[i] = i

edges = []
for i in range(n):
    for j in range(n):
        edges.append((matrix[i][j], i, j))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_root(parent, a) != find_root(parent, b):
        union_parent(parent, a, b)
        result+=cost

print(result)
