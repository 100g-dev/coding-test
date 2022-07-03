#2805 - 나무 자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2

    for t in trees:
        if t > mid:
            total += (t-mid)
            
        
    if total >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)