#1747 - 소수&팰린드롬

import sys
input = sys.stdin.readline

def prime_check(n):
    if n==0:
        return False
    for i in range(2, int(n**0.5+1)):
        return False
    return True

n = int(input())
result = 0

for i in range(n, 10000001):
    if str(i)==str(i)[::-1]:
        if prime_check(i):
            result = i
            break

if result==0:
    result = 1003001
    
print(result)