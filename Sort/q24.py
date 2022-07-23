#q24 - 안테나
#BOJ 18310

n = int(input())
houses = list(map(int, input().split()))
houses.sort()

if n%2:
    print(houses[n//2])
else:
    print(houses[(n-1)//2])