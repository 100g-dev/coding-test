#15787 - 기차가 어둠을 헤치고 은하수를
from collections import deque

n, m = map(int, input().split())
train = [deque([0]*20) for _ in range(n)] #0:빈자리, 1:탑승

for i in range(m):
    cmd = list(map(int, input().split()))

    if cmd[0]==1:
        train[cmd[1]-1][cmd[2]-1]=1

    elif cmd[0]==2:
        train[cmd[1]-1][cmd[2]-1]=0

    elif cmd[0]==3:
        train[cmd[1]-1].rotate(1)
        train[cmd[1]-1][0] = 0

    elif cmd[0]==4:
        train[cmd[1]-1].rotate(-1)
        train[cmd[1]-1][19] = 0


result = []
for data in train:
    if data not in result:
        result.append(data)
print(len(result))