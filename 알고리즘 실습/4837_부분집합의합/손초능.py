T = int(input())
total = list(map(int,range(1,13)))
n = len(total)

for i in range(1,T+1):
    num_ele, sum_sub = map(int, input().split())
    count_sum = 0

    for k1 in range(1<<n):
        count_sub = 0
        sub_sum = 0
        for k2 in range(n):
            if k1 & (1<<k2):
                count_sub += 1
                sub_sum += total[k2]
        if count_sub == num_ele and sub_sum == sum_sub:
            count_sum += 1

    print('#{0} {1}'.format(i, count_sum))