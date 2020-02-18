def f(r, s):
    global arr, min_s, n, used
    if r == n:
        if s < min_s:
            min_s = s
    elif s > min_s:
        return
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                f(r+1, s + arr[n][i]) # 이러면 초기화할 필요가 없다.
                used[i] = 0

T = int(input())

for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_s = 100
    used = [0]*n
    f(0, 0)
    print('#{0} {1}'.format(case, min_s))