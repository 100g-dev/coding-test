#1654 - 랜선 자르기

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

start = 1
end = max(lines)

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2

    for l in lines:
        if l >= mid:
            total += (l//mid)

    if total >= n:
        start = mid+1
        result = mid
    else:
        end =mid-1 

print(result)