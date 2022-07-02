#1316 - 그룹 단어 체커

n = int(input())
result=0
for i in range(n):

    word = input()
    group_check=True

    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            continue
        elif word[i] in word[i+2:]:
            group_check=False

    if group_check:
        result+=1

print(result)