#21920 - 서로소 평균
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

divisor = []
for i in range(1, int(x**0.5)+1):
    if x%i==0:
        divisor.extend([i, x//i])

divisor.remove(1)
    

result = []
for num in a:
    flag = True
    for i in divisor:
        if num%i==0:
            flag = False
            break
    
    if flag:
        result.append(num)

print(sum(result)/len(result))