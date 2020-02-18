def f(n, k):
    if n == k:
        print(p)
    else:
        for i in range(5):
            if used[i] == 0:
                used[i] = 1
                p[n] = A[i]
                f(n+1, k)
                used[i] = 0

A = [1, 2, 3, 4, 5]
used = [0] * 5
p = [0] * 3
f(0, 3)