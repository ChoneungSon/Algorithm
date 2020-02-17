def f(n, k, s):
    if n == k:
        print(s)
    else:
        f(n+1, k, s)
        s += A[n]
        f(n+1, k, s)

A = [10, 20, 30]
f(0, 3, 0)