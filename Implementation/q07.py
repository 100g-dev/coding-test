#q07 - 럭키 스레트
#BOJ 18406

n = input()

count = 0
for i in range(len(n)):
    if i==len(n)//2:
        count *= -1
    count+=int(n[i])

if count==0:
    print("LUCKY")
else:
    print("READY")