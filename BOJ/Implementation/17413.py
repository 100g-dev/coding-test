#17413 - 단어 뒤집기 2

string = input()

tag = False
tmp = []
result = []

for s in string:
    if tag == True:
        tmp.append(s)
        if s == '>':
            tag = False
            result += tmp
            tmp = []

    elif tag == False:
        if s == '<':
            tag = True
            tmp.append(s)

        elif s == ' ':
            result += tmp[::-1]
            result.append(s)
            tmp = []
        
        else:
            tmp.append(s)

if tmp:
    result += tmp[::-1]
    
print(''.join(result))