T = int(input())

for i in range(1,T+1):
    n = int(input())
    card = list(map(int,list(input())))
    count_num = [0]*10

    for k in card:
        count_num[k] += 1

    max_id = 0

    for k in range(1,10):
        if count_num[k] >= count_num[max_id]:
            max_id = k

    print('#{0} {1} {2}'.format(i, max_id, count_num[max_id]))

# 모드연산으로 나눠서 띄어쓰기 없이 연속으로 들어오는 숫자 처리하는 방법 알아놔야함