#4396 - 지뢰

n = int(input())
answer = [list(input()) for _ in range(n)]
player = [list(input()) for _ in range(n)]

result = []
bomb = False

dx = [-1, -1, -1, 0, 0, 1, 1, 1] 
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    tmp = []
    for j in range(n):
        if player[i][j]=='x' and answer[i][j]=='*':
            bomb=True
        if player[i][j]=='x': #answer[i][j]=='.'
            count=0
            for k in range(len(dx)):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx<n and 0<=ny<n and answer[nx][ny]=='*':
                    count+=1
            tmp.append(str(count))
        else:
            tmp.append('.')

    result.append(tmp)

if bomb:
    for i in range(n):
        for j in range(n):
            if answer[i][j]=='*':
                result[i][j]='*'
                
for data in result:
    print(''.join(data))