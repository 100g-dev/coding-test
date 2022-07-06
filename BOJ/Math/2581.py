#2581 - 소수

def prime_check(num):
    if num==1:
        return False
    for i in range(2, num):
        if num%i==0:
            return False
    return True

m = int(input())
n = int(input())

result = []
for i in range(m, n+1):
    if prime_check(i):
        result.append(i)

if result:
    print(sum(result))
    print(result[0])

else:
    print(-1)