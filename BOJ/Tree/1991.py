#1991 - 트리 순회

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*3 for _ in range(26)]

for i in range(n):
    a, b, c = input().split() 
    pos = graph[ord(a)-ord('A')]
    pos[0], pos[1], pos[2] = a, b, c


def preorder(v): #DLR
    print(v, end='')
    if graph[ord(v)-ord('A')][1] != '.':
        preorder(graph[ord(v)-ord('A')][1])
    
    if graph[ord(v)-ord('A')][2] != '.':
        preorder(graph[ord(v)-ord('A')][2])

def inorder(v):#LDR
    if graph[ord(v)-ord('A')][1] != '.':
        inorder(graph[ord(v)-ord('A')][1])
    print(v, end='')
    if graph[ord(v)-ord('A')][2] != '.':
        inorder(graph[ord(v)-ord('A')][2])

def postorder(v): #LRD
    if graph[ord(v)-ord('A')][1] != '.':
        postorder(graph[ord(v)-ord('A')][1])
    if graph[ord(v)-ord('A')][2] != '.':
        postorder(graph[ord(v)-ord('A')][2])
    print(v, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')