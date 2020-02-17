def f(n, k, v):
    if n == k:
        return
    elif A[n] == v:
        return n
    else:
        return f(n+1, k, v)

A = [1, 2, 3, 7, 5, 4, 9, 8]
print('인덱스 번호는 {0} 입니다.'.format(f(0, len(A), 10)))