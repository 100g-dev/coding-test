#q01 - 모험가 길드

n = int(input())
array = list(map(int, input().split()))

array.sort()
result = 0

tmp = 0
for i in array:
    tmp+=1
    if tmp >= i:
        result += 1
        tmp = 0

print(result)