#2960 - 에라토스테네스의 체

n, k = map(int, input().split())

data= [i for i in range(2, n+1)] #2부터 n
erase = [False]*(n+1) #data 요소로 인덱스 접근

div = 0
result = 0
while k>0:
    for value in data:
        if erase[value]==False:
            div = value
            break
    erase[div] = True
    k-=1
    if k==0:
        result = div
        break

    for value in data:
        if value%div==0 and not erase[value]:
            erase[value] = True
            
            k-=1
        if k==0:
            result = value
            break    

print(result)



