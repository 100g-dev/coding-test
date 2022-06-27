#20922 - 겹치는 건 싫어

n, k = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 0
count = [0]*(max(data)+1)

result = 0
while end < n:
    if count[data[end]] < k:
        count[data[end]]+=1
        end +=1 
    else:
        count[data[start]] -= 1
        start+=1

    result = max(result, end-start)


print(result)