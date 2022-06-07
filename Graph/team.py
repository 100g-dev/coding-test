#팀 결성
from gettext import find
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

n, m = map(int, input().split())
parent = [0]*(n+1)

for i in range(0, n+1):
    parent[i]=i

for i in range(m):
    cmd, a, b = map(int,input().split())

    if cmd == 0: #union
        union_parent(parent, a, b)
    elif cmd == 1: #find
        if find_root(parent, a) == find_root(parent, b):
            print("YES")
        else:
            print("NO")