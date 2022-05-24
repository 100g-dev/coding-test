#숫자 카드 게임

n, m = map(int, input().split())

#min() 함수 사용
"""
result = 0
for i in range(n):
  data = list(map(int, input().split()))
  result = max(result, min(data))

print(result)
"""

#이중반복문
result = 0
for i in range(n):
  data = list(map(int, input().split()))
  
  min_num = 10001
  for num in data:
    min_num = min(min_num, num)
    
  result = max(result, min_num)

print(result)