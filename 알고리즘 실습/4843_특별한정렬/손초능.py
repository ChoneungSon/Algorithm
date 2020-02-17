T = int(input())

for i in range(1,T+1):
    n = int(input())
    list_num = list(map(int, input().split()))
    count = 0
    
    for k in range(n-1):
        if count%2 == 0:
            idx = count
            for k1 in range(count,n):
                if list_num[idx] < list_num[k1]:
                    idx = k1
            list_num[count], list_num[idx] = list_num[idx], list_num[count]
            count += 1
        else:
            idx = count
            for k1 in range(count,n):
                if list_num[idx] > list_num[k1]:
                    idx = k1
            list_num[count], list_num[idx] = list_num[idx], list_num[count]
            count += 1
    list_str = list(map(str, list_num))

    print('#{0} {1}'.format(i, ' '.join(list_str[:10])))