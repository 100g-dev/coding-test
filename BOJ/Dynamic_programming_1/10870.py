#10870 - 피보나치 수 5
import sys
input = sys.stdin.readline

n = int(input())
d = [0]*21 #0<=n<20

d[0]=0
d[1]=1

for i in range(2, n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n])