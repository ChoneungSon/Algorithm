T = int(input())

for case in range(1, T+1):
    list_str = list(input())
    s = []
    result = 0
    for i in list_str:
        if len(s) == 0 and (i == ')' or i == '}' or i == ']'):
            break
        elif i == '(' or i == '{' or i == '[':
            s.append(i)
        elif i == ')' or i == '}' or i == ']':
            if i == ')' and s[-1] == '(':
                s.pop()
            elif i == '}' and s[-1] == '{':
                s.pop()
            elif i == ']' and s[-1] == '[':
                s.pop()
            else:
                break
    else:
        if len(s) == 0:
            result = 1

    print('#{0} {1}'.format(case, result))