#q42 - 탑승구

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] =a
    else:
        parent[a] =b 

g = int(input()) #탑승구
p = int(input()) #비행기
parent = [i for i in range(g+1)]

result = 0
for _ in range(p):
    pos = find_parent(parent, int(input()))
    if pos==0:
        break
    union_parent(parent, pos, pos-1)
    result += 1

print(result)
