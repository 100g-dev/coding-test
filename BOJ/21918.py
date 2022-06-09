#21918 - 전구

n, m = map(int, input().split())
state = list(map(int,input().split()))

for i in range(m):
    cmd, a, b = map(int, input().split())

    if cmd == 1:
        state[a-1]=b
    
    elif cmd == 2:
        for j in range(a-1, b):
            state[j]= int(not state[j])

    elif cmd == 3:
        state[a-1:b]=[0]*(b-a+1)

    elif cmd ==4:
        state[a-1:b]=[1]*(b-a+1)

for i in state:
    print(i, end =' ')