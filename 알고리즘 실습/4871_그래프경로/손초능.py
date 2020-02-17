def dfs(n, k, end):
    if n == end:
        return end+1
    else:
        for i in range(V):
            if arr[n][i] == 1 and visited[i] == 0:
                visited[i] = 1
                if dfs(i, k, end) == end+1:
                    return end+1
    return -1

T = int(input())

for case in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*V for _ in range(V)]
    for _ in range(E):
        i, j = map(int, input().split())
        arr[i-1][j-1] = 1
    S, G = map(int, input().split())
    visited = [0] * V
    visited[S - 1] = 1
    A = dfs(S-1, V, G-1)
    print('#{0} {1}'.format(case, A))