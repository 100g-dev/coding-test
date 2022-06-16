#21942 - 도시 건설
#pypy3

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

parent = [i for i in range(n+1)]

edges = [] 
sum = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    sum += cost
    edges.append((cost, a, b))
edges.sort()

result = 0
connect = 0
for edge in edges:
    cost, a, b = edge
    if find_root(parent, a) != find_root(parent, b):
        union_parent(parent, a, b)
        result+=cost
        connect += 1 

if connect==n-1:
    #모든 노드 연결: 간선 갯수 == (노드-1)
    print(sum-result)
else:
    print(-1)
        