#도시 분할 계획
import sys
input = sys.stdin.readline

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

n, m = map(int,input().split())
parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i

edges = []
result = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
max = 0

for edge in edges:
    cost, a, b = edge
    if find_root(parent, a) != find_root(parent, b):
        union_parent(parent, a, b)
        result += cost
        max = cost
    
print(result - max)