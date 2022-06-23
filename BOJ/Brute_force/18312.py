#18312 - 시각

n, k = map(int, input().split())

count = (n+1)*60*60
for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            tmp = []
            tmp = list(str(h)+str(m)+str(s))
            print(tmp)
            if str(k) not in tmp:
                count -= 1

print(count)