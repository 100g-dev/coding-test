#18258 - 큐2
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    command = input().split()
    cmd = command[0]

    if cmd == "push":
        q.append(command[1])

    elif cmd == "pop":
        if  q:
            print(q.popleft())
        else:
            print(-1)

    elif cmd =="size":
        print(len(q))

    elif cmd == "empty":
        if len(q)==0:
            print(1)
        else:
            print(0)

    elif cmd == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        continue


        
    
