#1이 될 때까지

n, k = map(int, input().split()))

count = 0

while True:
  target = (n//k)*k
  result += (n-target) #1빼기
  n = target
  
  if n<k:
    break
  result += 1 #나누기
  n //= k

result += (n-1)
print(result)