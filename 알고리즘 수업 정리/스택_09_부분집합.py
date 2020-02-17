def f(n, k):
    if n == k:
        s = 0
        for i in range(k):
            if L[i] == 1:
                s += A[i]
        print(s)
    else:
        L[n] = 0
        f(n+1, k)
        L[n] = 1
        f(n+1, k)

A = [10, 20, 30]
L = [0]*3
f(0, 3)