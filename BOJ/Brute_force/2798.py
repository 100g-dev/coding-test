#2798 - 블랙잭

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
combs = combinations(data, 3)

result = 0
for comb in combs:
    if(sum(comb)<=m):
        result = max(result, sum(comb))

print(result)
