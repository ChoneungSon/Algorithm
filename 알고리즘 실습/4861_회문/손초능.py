T = int(input())

for case in range(1,T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    dirs = 0

    for i in range(n):
        for j in range(n-m+1):
            flag = 1
            for k in range(m//2):
                dirs = 1
                if arr[i][j+k] != arr[i][m+j-k-1]:
                    flag = 0
                    break
            if flag:
                break
            flag = 1
            for k in range(m // 2):
                dirs = 2
                if arr[j+k][i] != arr[m+j-k-1][i]:
                    flag = 0
            if flag:
                break
        if flag:
            break

    print('#{0}'.format(case), end=' ')
    if dirs == 1:
        for k in range(m):
            print(arr[i][j+k], end='')
    elif dirs == 2:
        for k in range(m):
            print(arr[j+k][i], end='')
    print()