#17626 - Four Squares

import math
import sys
input = sys.stdin.readline

n = int(input())

dp = [50001]*(n+1)

i=1
while i**2 <= n:
    dp[i**2]=1
    i+=1

for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i],dp[i-(j**2)]+1)

print(dp[n])

