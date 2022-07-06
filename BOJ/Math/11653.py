#11653 - 소인수분해

n = int(input())

result = []
div = 2
while n>1:
    if n%div==0:
        result.append(div)
        n//=div
    else:
        div+=1
        

for i in result:
    print(i)