#1789 - 수들의 합

s = int(input())

result = 0
sum = 0
for i in range(1, s+1):
    sum += i
    result += 1
    
    if sum > s:
        result -= 1
        break
    
print(result)