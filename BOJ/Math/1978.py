#1978 - 소수 찾기

def prime_check(n):
    if n==1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True

n = int(input())
data = list(map(int, input().split()))

result = 0
for num in data:
    if prime_check(num):
        result+=1

print(result)