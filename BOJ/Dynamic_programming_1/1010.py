#1010 - 다리 놓기

f = [0]*30
f[0] = 1
f[1] = 1
for i in range(2, 30):
    f[i]=i*f[i-1]

t = int(input())
for i in range(t):
    n, m =map(int ,input().split())
    result = int(f[m]/(f[n]*f[m-n]))
    print(result)
