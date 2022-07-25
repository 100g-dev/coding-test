#q41 - 여행 계획

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b: parent[b]=a
    else: parent[a]=b


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]==1:
            union_parent(parent, i+1, j+1)
        

plan = list(map(int, input().split()))

flag = True
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if flag: print("YES")
else: print("NO")