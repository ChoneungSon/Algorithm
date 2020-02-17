def subset(A, m):

    n = len(A)
    arr_list = []
    arr = []
    min_sub = 9*m
    count = 0

    for i in range(1<<n):
        
        for j in range(n):
            if i & (1<<j):
                count += 1
                arr.append(A[j])
        
        if count == m and min_sub > sum(arr):
            min_sub = sum(arr)
        
        arr = []
        count = 0

    return min_sub

A = [1, 2, 3, 4, 5, 6]

B = subset(A, 3)

print(B)