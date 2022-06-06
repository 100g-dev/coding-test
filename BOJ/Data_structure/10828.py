#10828 - 스택

import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.top = []
    
    def __del__(self):
        self.top.clear()

    def push(self, data):
        self.top.append(data)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.top.pop(-1)

    def size(self):
        return len(self.top)

    def empty(self):
        return len(self.top)==0

    def peek(self):
        if self.empty():
            return -1
        else:
            return self.top[-1]


n = int(input())
stack = Stack()

for i in range(n):
    command = input().split()
    cmd = command[0]

    if cmd == "push":
        stack.push(command[1])
    elif cmd == "pop":
        print(stack.pop())
    elif cmd =="size":
        print(stack.size())
    elif cmd == "empty":
        print(int(stack.empty()))
    elif cmd == "top":
        print(stack.peek())
    else:
        continue


        
    
