#q03 - 문자열 뒤집기

str = input()
to0 = 0
to1 = 0

if str[0]=='0':
    to1 +=1
else:
    to0 += 1

for i in range(len(str)-1):
    if str[i]!=str[i+1]:
        if str[i+1]=='0':
            to1 += 1
        else:
            to0 += 1

print(min(to0, to1))