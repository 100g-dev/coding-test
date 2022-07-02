#16171 - 나는 친구가 적다(small)

string = input()
target = input()

tmp = ''
for s in string:
    if s.isalpha():
        tmp+=s

tmp = ''.join(tmp)

if target in tmp:
    print(1)
else:
    print(0)