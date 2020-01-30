
# A의 원소들로 이루어진 순열 출력하기

A = [1,5,7,4]
n = len(A)

for i1 in range(n):
    for i2 in range(n):
        if i2 != i1:
            for i3 in range(n):
                if i3 != i1 and i3 != i2:
                    print(A[i1],A[i2],A[i3])

# def permutations(A,r):
#     n = len(A)
#
#     if n != 1:
#         for i in range(n):
#             A.pop(i)
#             r -= 1
#             return permutations(A,r)

