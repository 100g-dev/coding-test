#q08 - 문자열 재정렬

string = input()

sum = 0
result = []

for c in string:
    if c.isalpha():
        result.append(c)
    else:
        sum += int(c)

result.sort()

if sum != 0:
    result.append(str(sum))

print(''.join(result))