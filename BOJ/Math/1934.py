#1934 - 최소공배수

#유클리드 호제법
def gcd(a, b):
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a*b//gcd(a,b))