#왕실의 나이트

position = input()
col = int(ord(position[0]))-int(ord('a')) +1
row = int(position[1])

move_type = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

result = 0
for move in move_type:
  nr = row + move[0]
  nc = col + move[1]

  if nr>=1 and nr<=8 and nc>=1 and nc<=8:
    result+=1

print(result)