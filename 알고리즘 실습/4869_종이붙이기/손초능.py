def f(N):
    if N < 2:
        return memo[N]
    elif N >= 2 and memo[N] == 0:
        memo[N] = f(N-1) + 2*f(N-2)
        return memo[N]
    else:
        return memo[N]

T = int(input())
memo = [0] * 300
memo[0] = 1
memo[1] = 3

for case in range(1, T+1):
    n = int(input())
    num = n // 10
    print('#{0} {1}'.format(case,f(num-1)))