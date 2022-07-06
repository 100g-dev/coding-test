#9934- - 완전이진트리

import sys
input = sys.stdin.readline

k = int(input())
buildings = list(map(int, input().split()))
tree = [[] for _ in range(k)]


def make_tree(buildings, level):
    if len(buildings) == 1:
        tree[level].extend(buildings)
        return
    
    mid  = len(buildings)//2
    tree[level].append(buildings[mid])
    make_tree(buildings[:mid],level+1) #left child
    make_tree(buildings[mid+1:], level+1) #right child


make_tree(buildings, 0)
for i in tree:
    print(*i)