def f(n, k):
    global A, B
    if n == k:
        print(B)
        return
    else:
        B[n] = A[n]
        f(n+1, k)

A = [0, 1, 2]
B = [0] * len(A)
f(0, len(A))