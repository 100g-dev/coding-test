#q02 - 곱하기 혹은 더하기

str = input()

result = int(str[0])
for i in range(1, len(str)):
    num = int(str[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)