#18511 - 큰 수 구성하기

from itertools import product #중복순열

n, k = map(int, input().split())
data = list(input().split())

result = []
for i in range(1, len(str(n))+1):
    for j in product(data, repeat=i):
        tmp = int(''.join(j))
        if tmp <= n:
            result.append(tmp)
print(max(result))