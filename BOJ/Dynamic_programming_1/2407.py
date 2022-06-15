#2407 - 조합

n, m = map(int, input().split())

#factorial
d=[0]*101
d[0]=1
d[1]=1
for i in range(2, n+1):
    d[i]=i*d[i-1]

comb = d[n]//(d[m]*d[n-m])
print(comb)
 