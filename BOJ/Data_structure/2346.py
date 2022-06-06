#2346 - 풍선 터뜨리기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split()))) #순서 부여
result = []

while q:
    index, count = q.popleft()
    result.append(index+1)

    if count > 0:
        q.rotate(-(count-1))
    else:
        q.rotate(-count) #양수로 처리(시계)

print(' '.join(map(str, result)))