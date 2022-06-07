#서로소 집합을 이용한 사이클 판별

import sys
input = sys.stdin.readline

def find_root(parent, x):
    if parent[x]!=x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_root(parent, a)
    b = find_root(parent, b)
    if a<b:
        parent[b] = a 
    else:
        parent[a] = b


v, e = map(int, input().split())

parent = [0] *(v+1)
for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_root(parent, a)==find_root(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")