#2512 - 예산

n = int(input())
cities = list(map(int, input().split()))
m = int(input())

start = 1
end = max(cities)

result = 0
while start<=end:
    total = 0
    mid = (start+end)//2

    for c in cities:
        if c > mid:
            total += mid
        else:
            total += c

    if total <= m:
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)