#20053 - 최소, 최대 2

t = int(input())

for _ in range(t):
    n = int(input())
    
    data = list(map(int,input().split()))
    max = data[0]
    min = data[0]

    for i in range(1, n):
        if data[i]>max:
            max=data[i]
        if data[i]<min:
            min=data[i]
    print(min, max)