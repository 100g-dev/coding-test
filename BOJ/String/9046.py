#9046 - 복호화

# 문자열 카운트
# - 공백이면 continue
# - 알파벳 ord()-ord('a') 로 인덱스 처리
# - freq, count, max_char, max값 count 값 갱신
# - count가 1이면 max 알파벳 출력, 

t = int(input())

for i in range(t):
    string = input()
    alphabet = [0]*26
    max, count, max_char = 0, 0, '\0' #최대값, 개수, 알파벳

    for a in string:
        if a==' ':
            continue
        index = ord(a)-ord('a')
        alphabet[index]+=1
        if alphabet[index] > max:
            max = alphabet[index]
            count = 1
            max_char = a
        elif alphabet[index] == max:
            count += 1
            max_char = '?'
         
    print(max_char)

        

