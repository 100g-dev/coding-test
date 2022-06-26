#1244 - 스위치 켜고 끄기

def male_change(bulb, num):
    i=1
    while i*num<=len(bulb):
        bulb[i*num-1] = (bulb[i*num-1]+1)%2
        i+=1

def female_change(bulb, num):
    i = num-1
    j = 1

    bulb[i]=(bulb[i]+1)%2

    while i-j>=0 and i+j<num:
        if bulb[i-j] == bulb[i+j]:
            bulb[i-j] = (bulb[i-j]+1)%2
            bulb[i+j] = (bulb[i+j]+1)%2
            j+=1
            print('>>', *bulb)
        else:
            break

n = int(input())
bulb = list(map(int, input().split()))

m = int(input())
for i in range(m):
    gender, num = map(int, input().split())
    if gender == 1:
        male_change(bulb, num)
    elif gender == 2:
        female_change(bulb, num)

for i in range(len(bulb)):
    print(bulb[i],end=' ')
    if (i+1)%20==0:
        print()