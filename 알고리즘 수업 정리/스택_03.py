def f(n, k):
    global max_value
    if n == k:
        print(max_value)
        return
    else:
        if A[n] > max_value:
            max_value = A[n]
        f(n+1, k)

max_value = 0
A = [1, 3, 2]
f(0, len(A))