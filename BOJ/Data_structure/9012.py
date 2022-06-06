#9012 - 괄호

def vps(test):
    stack = []
    for i in test:
        if i == '(':
            stack.append(i)
        elif i== ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
            

t = int(input())
for i in range(t):
    test = input()
    vps(test)