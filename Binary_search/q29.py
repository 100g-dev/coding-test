#q29 - 공유기 설치
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
homes = []
for _ in range(n):
    homes.append(int(input()))

homes.sort()

start = 1
end = homes[-1]
result = 0

while start<=end:
    mid = (start+end)//2
    cur = homes[0]
    cnt = 1

    for i in range(1, n):      
        if homes[i]-cur >= mid:
            cnt+=1
            cur= homes[i]
    if cnt >= c:
        result = mid
        start = mid+1
    else:
        end=mid-1
print(result)