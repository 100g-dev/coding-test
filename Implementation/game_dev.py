#게임 개발

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]
def change_direction():
  global direction
  direction -=1
  if direction == -1:
    direction = 3

#map
maze = []
for i in range(n):
  maze.append(list(map(int, input().split())))
maze[x][y] = 2 #방문처리

#simulation
count = 1
turn_time = 0

while True:
  change_direction()
  nx = x + dx[direction]
  ny = y + dy[direction]
  turn_time += 1
  
  if maze[nx][ny]==0:
    x = nx
    y = ny
    count += 1
    maze[nx][ny]=2
    turn_time = 0
    continue

  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if maze[nx][ny] != 1: #0(육지) 또는 2(방문)
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)
  