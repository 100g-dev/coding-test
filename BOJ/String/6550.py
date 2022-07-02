#6550 - 부분 문자열

while True:
    try:
        s, t = input().split()
        flag = False

        index = 0
        for i in range(len(t)):
            if s[index]==t[i]:
                index+=1

                if index==len(s):
                    flag = True
                    break

        if flag:
            print("Yes")
        else:
            print("No")
    except:
        break