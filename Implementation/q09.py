#q09 - 문자열 압축
#programmers - 60057

# 나누는 단위 범위는 len(string)//2

s = input()
answer = len(s)

for i in range(1, len(s)//2+1):
    result = ''
    count = 1
    tmp = s[:i] 
    
    for j in range(i, len(s)+i, i):
        if tmp == s[j:i+j]:
            count += 1
        else:
            if count == 1:
                result += tmp
            else:
                result += (str(count)+tmp)
            tmp = s[j:i+j]
            count = 1

    answer = min(answer, len(result))
