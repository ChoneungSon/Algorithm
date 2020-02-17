# 배열 arr의 모든 arr[i][j]에 대해, 이웃한 칸의 합이 가장 큰 경우의 합을 출력. (0 오른쪽, 1 아래, 2 왼쪽, 3 위쪽)

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = 4

di = [0, 1, 0, -1] # 각 방향을 나타낼 때 i 행에 더할 값
dj = [1, 0, -1, 0] # 각 방향을 나타낼 때 j 열에 더할 값
max_s = -999

for i in range(n):
    for j in range(n):
        s = A[i][j]
        for k in range(4):
            if 0 <= i + di[k] < n and 0 <= j + dj[k] < n:
                s += A[i+di[k]][j+dj[k]]
        if max_s < s:
            max_s = s

print(max_s)