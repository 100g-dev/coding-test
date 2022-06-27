
#21921 - 블로그
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
day = list(map(int, input().split()))

count = 1
tmp  = sum(day[0:x])
max_visited = tmp

for i in range(0, n-x):
    tmp = tmp - day[i] + day[i+x]

    if tmp==max_visited:
        count+=1
    elif tmp>max_visited:
        max_visited = tmp
        count = 1
    

if max_visited==0:
    print("SAD")
else:
    print(max_visited)
    print(count)