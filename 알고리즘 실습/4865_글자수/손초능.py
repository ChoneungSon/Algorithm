T = int(input())

for case in range(1,T+1):
    str1 = input()
    str2 = input()
    n1 = len(str1)
    n2 = len(str2)
    max_count = 0
    for i in range(n1):
        a = str1[i]
        count = 0
        for j in range(n2):
            if a == str2[j]:
                count += 1
        if count > max_count:
            max_count = count

    print('#{0} {1}'.format(case, max_count))