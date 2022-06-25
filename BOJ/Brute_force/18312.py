#18312 - 시각

n, k = map(int, input().split())

count = (n+1)*60*60

for h in range(0, n+1):
    if h<10: h='0'+str(h)
    else: h=str(h)
    for m in range(0, 60):
        if m<10: m='0'+str(m)
        else: m=str(m)
        for s in range(0, 60):
            if s<10: s='0'+str(s)
            else: s=str(s)
            
            tmp = list(h+m+s)
            
            if str(k) not in tmp:
                count -= 1

print(count)