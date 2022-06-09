#14467 - 소가 길을 건너간 이유 1

cow = [-1]*11
n = int(input())

count=0
for i in range(n):
    num, road = map(int, input().split())
    if cow[num]==-1:
        cow[num]=road
    else:
        if cow[num]!=road:
            count+=1
            cow[num]=road

print(count)