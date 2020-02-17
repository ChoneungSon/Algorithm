def paste(a, log, count):
    
    global m
    global root
    global roots
    global count_max

    for i in range(m):

        if count == 0:
            log[i] = 1
            count += 1
            root.append(a[i][:])
            paste(a, log, count)
            log[i] = 0
            count -= 1
            del root[-1]
    
        elif log[i] == 0 and root[-1][1] == a[i][0]:
            log[i] = 1
            count += 1
            root.append(a[i][:])
            if count > count_max:
                count_max = count
                roots = root[:]
            paste(a, log, count)
            log[i] = 0
            count -= 1
            del root[-1]

T = int(input())

for i in range(1,T+1):
    m = int(input())
    list_ns = list(map(int, input().split()))
    ns = [0] * m
    log = [0] * m
    root = []
    roots = []
    count_max = 0
    count = 0

    for j in range(m):
        ns[j] = list_ns[2*j:2*j+2]

    paste(ns, log, count)

    list_str = [0] * count_max * 2

    for k in range(count_max):
        for k1 in range(2):
            list_str[2*k + k1] = str(roots[k][k1])

    print('#{0} {1}'.format(i ,' '.join(list_str)))