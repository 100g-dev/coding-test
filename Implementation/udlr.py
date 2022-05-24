#상하좌우

n = int(input())
x, y = 1, 1
move_list = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dir = ['U', 'D', 'L', 'R']

for move in move_list:
  for i in range(len(dir)):
    if move == dir[i]:
      nx = x+dx[i]
      ny = y+dy[i]

  if nx < 1 or nx > n or ny < 1 or ny > n:
      continue
    
  x, y = nx, ny

print(x, y)
    