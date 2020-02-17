# 전치 행렬

arr = [[1,2,3],[4,5,6],[7,8,9]]
n = 3
print(arr)

for i in range(n-1):
    for j in range(i,n-1):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)