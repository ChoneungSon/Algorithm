T = int(input())

for case in range(1, T+1):
    cand = list(input().split())
    stack = []
    for i in cand:
        if i == '+':
            if len(stack) < 2:
                flag = 'error'
                break
            b = stack.pop()
            f = stack.pop()
            stack.append(f + b)
        elif i == '-':
            if len(stack) < 2:
                flag = 'error'
                break
            b = stack.pop()
            f = stack.pop()
            stack.append(f - b)
        elif i == '*':
            if len(stack) < 2:
                flag = 'error'
                break
            b = stack.pop()
            f = stack.pop()
            stack.append(f * b)
        elif i == '/':
            if len(stack) < 2:
                flag = 'error'
                break
            b = stack.pop()
            f = stack.pop()
            stack.append(f // b)
        elif i == '%':
            if len(stack) < 2:
                flag = 'error'
                break
            b = stack.pop()
            f = stack.pop()
            stack.append(f % b)
        elif i == '.':
            if len(stack) == 1:
                flag = stack.pop()
            else:
                flag = 'error'
                break
        else:
            stack.append(int(i))
    print('#{0} {1}'.format(case, flag))