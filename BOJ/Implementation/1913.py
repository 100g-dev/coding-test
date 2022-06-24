#1913 - 달팽이

n = int(input())
m = int(input())
snail = [[0]*n for _ in range(n)]

x = (n-1)//2
y = (n-1)//2
snail[x][y] = 1

dir = 0
dx = [0, -1, 0 , 1]
dy = [-1, 0, 1, 0]

def next_index(dir):
    dir += 1
    if dir == 4:
        dir = 0
    return dir

def turn_dir():
    global dir
    dir += 1
    if dir==4:
        dir=0

result_x = -1
result_y = -1

for i in range(2, n**2+1):
    tmp = next_index(dir)
    nx = x + dx[tmp]
    ny = y + dy[tmp]

    if snail[nx][ny]==0:
        turn_dir()
        x, y = nx, ny
        snail[x][y] = i
    else:
        x = x + dx[dir]
        y = y + dy[dir]
        snail[x][y] = i
    
    if i==m:
        result_x = x+1
        result_y = y+1


for i in range(n):
    for j in range(n):
        print(snail[i][j], end =' ')
    print()
    
print(result_x, result_y)