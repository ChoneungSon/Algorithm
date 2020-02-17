R, C = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

# 원래 배열 그대로 출력
for i in range(R):
    for j in range(C):
        print(arr[i][j], end = " ")
    print()
print()

# 180도 회전한 배열 출력
for i in range(R-1, -1, -1):
    for j in range(C-1, -1, -1):
        print(arr[i][j], end = " ")
    print()
print()

# 90도 회전한 배열 출력
for i in range(C):
    for j in range(R-1, -1, -1):
        print(arr[j][i], end = " ")
    print()
print()