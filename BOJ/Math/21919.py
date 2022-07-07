#21919 - 소수 최소 공배수

import sys
input = sys.stdin.readline

def prime_check(num):
    for i in range(2, num):
        if i**2 > num:
            break
        if num%i == 0:
            return False
    return True

n = int(input())
data = list(map(int, input().split()))

result = 1
prime = []
for num in data:
    if prime_check(num) and num not in prime:
        result *= num
    
if result != 1:
    print(result)
else:
    print(-1)