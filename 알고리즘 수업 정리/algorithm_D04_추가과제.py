T = int(input())

for m in range(1,T+1):
    n = int(input())
    list_ns = list(map(int, input().split()))
    ns = [0] * n
    log = [0] * n
    root = []

    for j in range(n):
        ns[j] = list_ns[2*j:2*j+2]

    for j in range(n):
        for k in range(n):
            if ns[j][0] == ns[k][1]:
                break
        else:
            start = ns[j]
            idx = j
            break
    
    root.append(start[0])
    root.append(start[1])
    b_count = 0 
    count = 1

    while b_count != count:
        for i in range(n):
            if log[i] == 0 and ns[i][0] == start[1]:
                start = ns[i]
                root.append(start[0])
                root.append(start[1])
                count += 1
                break
        b_count += 1
    
    list_str = list(map(str, root))
    
    print('#{0} {1}'.format(m, ' '.join(list_str)))