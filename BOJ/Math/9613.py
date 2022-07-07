#9613 - GCD 합

import math

t = int(input())
for i in range(t):
    data = list(map(int, input().split()))
    sum = 0
    for j in range(1, len(data)-1):
        for k in range(j+1, len(data)):
            sum += math.gcd(data[j], data[k])
        
    print(sum)