def solution(n, build_frame):
    
    frame = [[[0]*2 for _ in range(n+1)] for _ in range(n+1)]

    def check(x, y, a):
        nonlocal frame, n
        if a:
            if frame[y-1][x][0] or (x+1<=n and frame[y-1][x+1][0]) \
                or (x-1 >= 0 and frame[y][x-1][1] and x+1 <= n and frame[y][x+1][1]):
                return 1
        else:
            if y == 0 or frame[y-1][x][0] \
                or (x-1 >= 0 and frame[y][x-1][1]) or frame[y][x][1]:
                return 1
        return 0

    for x, y, a, b in build_frame:
        if b:
            if check(x, y, a): frame[y][x][a] = 1
        else:
            if a:
                frame[y][x][1] = 0
                if (x-1>=0 and frame[y][x-1][1] and not check(x-1, y, 1)) or \
                    (x+1<=n and frame[y][x+1][1] and not check(x+1, y, 1)) or \
                    (x+1<=n and frame[y][x+1][0] and not check(x+1, y, 0)) or \
                    (frame[y][x][0] and not check(x, y, 0)):
                    frame[y][x][1] = 1
            elif y+1<=n:
                frame[y][x][0] = 0
                if (frame[y+1][x][1] and not check(x, y+1, 1)) or \
                    (x-1>=0 and frame[y+1][x-1][1] and not check(x-1, y+1, 1)) or \
                    (frame[y+1][x][0] and not check(x, y+1, 0)):
                    frame[y][x][0] = 1

    answer = []
    
    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if frame[j][i][k]:
                    answer.append([i, j, k])

    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))