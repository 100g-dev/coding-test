#14621 - 나만 안되는 연애

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_root(parent, a)
    b = find_root(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n, m = map(int, input().split())
gender = list(input().split())
parent = [i for i in range(n+1)]

edges = []
for _ in range(m):
    u, v, distance = map(int, input().split())
    if gender[u-1]!=gender[v-1]:
        edges.append((distance, u, v))
edges.sort()

result = 0
connect = 0
for edge in edges:
    distance, u, v = edge
    if find_root(parent, u) != find_root(parent, v):
        union_parent(parent, u, v)
        connect+=1
        result+=distance

if connect == n-1:
    print(result)
else:
    print(-1)
    