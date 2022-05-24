#큰 수의 법칙

n, m, k =map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
set = m // (k+1)

result = set*(k*first+second) + m%(k+1)*first
print(result)