T = int(input())

for case in range(1,T+1):
    str1 = input()
    str2 = input()
    n1 = len(str1)
    n2 = len(str2)
    result = 0

    for i in range(n2-n1+1):
        flag = 1
        for j in range(n1):
            if str1[j] != str2[i+j]:
                flag = 0
                break
        if flag:
            result = 1
            break

    print('#{0} {1}'.format(case, result))