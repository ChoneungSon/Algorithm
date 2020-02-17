def f(n, k):
    global log
    if n == k:
        print(log)
    else:
        f(n+1, k)
        log.append(A[n])
        f(n+1, k)
        log.pop()

A = [1, 2, 3]
log = []

f(0, len(A))