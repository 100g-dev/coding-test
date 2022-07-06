#4134 - 다음 소수

def prime_check(num):
    if num==0 or n==1:
        return False
    for i in range(2, int(num**0.5)+1): 
        if num%i==0:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    while True:
        if prime_check(n):
            print(n)
            break
        n+=1


