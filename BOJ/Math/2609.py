#2609 - 최대공약수와 최소공배수

a, b = map(int, input().split())

#유클리드 호제법
def gcd(a, b):
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a*b // gcd(a, b)

gcd_value = gcd(a, b)
print(gcd_value)
print(a*b//gcd_value)
