#2422 - 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

from itertools import combinations

n, m = map(int, input().split())
ice = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    ice[a-1][b-1] = True
    ice[b-1][a-1] = True

result = 0
for i in combinations(range(n), 3):
    a, b, c = i
    if ice[a][b] or ice[b][c] or ice[a][c]:
        continue
    result += 1

print(result)