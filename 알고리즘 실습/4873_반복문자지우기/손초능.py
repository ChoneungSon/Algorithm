T = int(input())

for case in range(1, T+1):
    list_str = list(input())
    s = [list_str[0]]
    for i in range(1, len(list_str)):
        if len(s) == 0:
            s.append(list_str[i])
        elif s[-1] != list_str[i]:
            s.append(list_str[i])
        else:
            s.pop()
    print('#{0} {1}'.format(case, len(s)))