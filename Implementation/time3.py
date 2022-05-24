#시각

n = int(input())

result = 0
hour = 0
for i in range(n+1):
  if i%10==3:
    hour += 1

result += hour*(5*9*5*9) #(시간 3포함)*(분, 초에 3 제외)
result += (n+1)*(6*10*6*10-5*9*5*9) #분, 초에 적어도 1개 이상의 3

print(result)