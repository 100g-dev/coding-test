#서로소 집합
import sys
input = sys.stdin.readline

def find_root(parent, x):
    if parent[x]!=x:
        #return find_root(parent, parent[x]) 비효율
        parent[x] = find_root(parent, parent[x]) #경로 압축: 호출하며 갱신
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

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_root(parent,i), end=' ')
print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
print()