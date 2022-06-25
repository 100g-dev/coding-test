#1913 - 달팽이

n = int(input())
m = int(input())
snail = [[0]*n for _ in range(n)]


dir = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def change_dir():
    global dir
    dir += 1
    if dir == 4:
        dir = 0

x = 0
y = 0
result = 0

for i in range(n**2, 0, -1):
    snail[x][y] = i
    if i == m:
        result = (x+1, y+1)

    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0<=nx<n and 0<=ny<n and snail[nx][ny]==0:
        x = nx
        y = ny
    else:
        change_dir()
        x = x + dx[dir]
        y = y + dy[dir]


for data in snail:
    print(*data)

print(result[0], result[1])