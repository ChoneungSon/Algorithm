T = int(input())

for i in range(1,T+1):
    total_page, find_A, find_B = map(int, input().split())
    lA, lB = 1, 1
    rA, rB = total_page, total_page

    while 1:

        cA = int((lA+rA)/2)
        cB = int((lB+rB)/2)

        if find_A >= cA:
            lA = cA
        else:
            rA = cA

        if find_B >= cB:
            lB = cB
        else:
            rB = cB

        if lA == find_A and lB == find_B:
            print('#{0} 0'.format(i))
            break
        elif lA == find_A:
            print('#{0} A'.format(i))
            break
        elif lB == find_B:
            print('#{0} B'.format(i))
            break