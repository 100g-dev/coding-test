#16918 - 봄버맨
from collections import deque
import sys
input = sys.stdin.readline


r, c, n = map(int, input().split())
graph = [list(input()) for _ in range(r)] #step1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while que:
        x, y = que.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=r or ny<0 or ny>=c:
                continue
            graph[nx][ny]='.'
            
def find_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j]=='O':
                que.append((i,j))       

def set_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j]=='.':
                graph[i][j] = 'O'

time = n-1 #step2
que = deque()
while time:
    find_bomb()
    set_bomb()   #step3     
    time -= 1
    if time == 0:
        break
    bfs() 
    time -= 1

for a in graph:
    print(*a, sep='', end='')
