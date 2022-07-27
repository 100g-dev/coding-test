#q18 - 괄호 변환

def isRight(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True

def solution(p):
    answer = ''

    if not p:
        return ''
    
    left_cnt=0
    right_cnt=0
    for i in range(len(p)):
        if p[i]=='(':
            left_cnt+=1
        else:
            right_cnt+=1

        if left_cnt==right_cnt: #balanced string
            u = p[:i+1]
            v = p[i+1:]
            break

    if isRight(u):
        return u+solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for i in u[1:-1]:
            if i=='(':
                answer += ')'
            else:
                answer += '('
    return answer