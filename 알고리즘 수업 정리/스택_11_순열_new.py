def f(n, k): # n 번 인데그를 n 부터 k-1 까지와 자리를 바꿈. 자기 자신의 오른쪽과 자리를 바꿔간다.
    if n == k:
        print(p)
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            f(n+1, k)
            p[n], p[i] = p[i], p[n]

A = [1, 2, 3, 4]
p = A[:]
f(0, len(p))