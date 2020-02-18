def dfs(p):
    global arr, visited, di, dj, n
    stack = [p]
    visited = [[0]*n for _ in range(n)]
    visited[p[0]][p[1]] = 1
    while len(stack) != 0:
        np = stack.pop()
        if arr[np[0]][np[1]] == '3':
            return 1
        else:
            for i in range(4):
                new_p = [np[0]+di[i], np[1]+dj[i]]
                if 0 <= new_p[0] < n and 0 <= new_p[1] < n and arr[new_p[0]][new_p[1]] != '1' and visited[new_p[0]][new_p[1]] == 0:
                    visited[new_p[0]][new_p[1]] = 1
                    stack.append(new_p)
    return 0

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for case in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                sp = [i ,j]
                flag = 1
                break
        if flag:
            break
    print('#{0} {1}'.format(case, dfs(sp)))