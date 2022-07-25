#q05 - 볼링공 고르기
from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))

combs = list(combinations(balls, 2))
result = len(combs)
for comb in combs:
    if comb[0]==comb[1]:
        result-=1
    
print(result)
    