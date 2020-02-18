def f(n, k):
    for i in range(len(n)):


    if n == k:
        s = 0
        for i in range(k):
            if L[i] == 1:
                s += A[i]
        print(s)
    else:

A = [10, 20, 30]
L = [0]*3
f(0, 3)