#11728 - 배열 합치기

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0

result = []
while i<n and j<m:
    if a[i] < b[j]:
        result.append(a[i])
        i+=1
    else:
        result.append(b[j])
        j+=1

else: #남은 리스트 처리
    if i==n:
        result+=b[j:]
    else:
        result+=a[i:]

print(*result)