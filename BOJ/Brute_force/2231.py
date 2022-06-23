#2231 - 분해합

n = int(input())
result = 0

for num in range(1, n+1):
    digit = list(map(int, str(num)))
    m = num + sum(digit)
    if m == n:
        result = num
        break

print(result)