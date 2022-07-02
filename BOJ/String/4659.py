#4659 - 비밀번호 발음하기

vowels="aeiou"

while True:
    password = input()
    if password=="end":
        break

    vowel_check = False
    vowel_cnt = 0
    conson_cnt = 0
    prev =''
    flag = True

    for s in password:
        if s in vowels: #모음
            vowel_check = True
            vowel_cnt += 1
            conson_cnt = 0

            if vowel_cnt >= 3:
                flag = False
                break

            if prev==s:
                if s in "eo":
                    pass
                else:
                    flag = False
                    break
        
        else: #자음
            vowel_cnt = 0
            conson_cnt += 1

            if conson_cnt >= 3:
                flag = False
                break

            if prev==s:
                flag = False
                break
        prev = s

    if vowel_check == False:
        flag = False

    if flag:
        print(f"<{password}> is acceptable.")
    else:
        print(F"<{password}> is not acceptable.")



