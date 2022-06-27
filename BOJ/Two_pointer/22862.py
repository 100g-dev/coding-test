#22862 - 가장 긴 짝수 연속한 부분

n, k = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 0
count = 0

result = 0
while start<n and end < n:

    if data[start]%2==1:
        start+=1
        if count > 0: count-=1
        else: end = max(start, end)
    
    else:
        if data[end]%2==1:
            if count > k:
                start+=1
            else:
                count+=1
                end+=1
        else:
            end+=1

    result = max(result, end-start)

print(result-k)