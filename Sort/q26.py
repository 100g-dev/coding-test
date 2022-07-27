#q26 - 카드 정렬하기
#BOJ 1715

n = int(input())
numbers=[]
for i in range(n):
    numbers.append(int(input()))

numbers.sort()

result = sum(numbers[:2])
for i in range(2, n):
    result += (result+numbers[i])

print(result)