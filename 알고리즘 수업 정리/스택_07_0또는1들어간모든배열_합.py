def f(n, k):
    global count
    if n == k:
        print(count)
    else:
        f(n+1, k)
        count += A[n]
        f(n+1, k)
        count -= A[n]

A = [1, 2, 3]
count = 0

f(0, len(A))