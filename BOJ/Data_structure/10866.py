#10866 - 덱
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deq = deque()

for i in range(n):
    command = input().split()
    cmd = command[0]

    if cmd == "push_front":
        deq.appendleft(command[1])

    elif cmd == "push_back":
        deq.append(command[1])

    elif cmd == "pop_front":
        if  deq:
            print(deq.popleft())
        else:
            print(-1)

    elif cmd == "pop_back":
        if  deq:
            print(deq.pop())
        else:
            print(-1)

    elif cmd =="size":
        print(len(deq))

    elif cmd == "empty":
        if len(deq)==0:
            print(1)
        else:
            print(0)

    elif cmd == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif cmd == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)
    else:
        continue


        
    
