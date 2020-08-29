def solution(board):
    
    def move_list(d, p1, p2):
        nonlocal board
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        result = []

        for i in range(4):
            np1 = (p1[0]+dx[i], p1[1]+dy[i])
            np2 = (p2[0]+dx[i], p2[1]+dy[i])
            
            if board[np1[0]][np1[1]] == 0 and board[np2[0]][np2[1]] == 0:
                result.append([d, np1[:], np2[:]])

        rot = [-1, 1]
        d_rot = (d+1) % 2

        for i in rot:
            if p1[0] == p2[0]:
                if board[p1[0]+i][p1[1]] == 0 and board[p2[0]+i][p2[1]] == 0:
                    result.append([d_rot, [p1[0]+i, p1[1]], p1[:]])
                    result.append([d_rot, p2[:], [p2[0]+i, p2[1]]])
            else:
                if board[p1[0]][p1[1]+i] == 0 and board[p2[0]][p2[1]+i] == 0:
                    result.append([d_rot, [p1[0], p1[1]+i], p1[:]])
                    result.append([d_rot, p2[:], [p2[0], p2[1]+i]])

        return result

    n = len(board)
    board = [[1]*(n+2)] + [[1] + board[i] + [1] for i in range(n)] + [[1]*(n+2)]
    visit = [[[float('inf')]*2 for _ in range(n+2)] for _ in range(n+2)]
    visit[1][1][0] = visit[1][2][0] = 0
    
    q = [[0, (1, 1), (1, 2)]]

    while q:
        
        d, p1, p2 = q.pop(0)
        length = max(visit[p1[0]][p1[1]][d], visit[p2[0]][p2[1]][d]) + 1

        for direction, np1, np2 in move_list(d, p1, p2):
            len1, len2 = visit[np1[0]][np1[1]][direction], visit[np2[0]][np2[1]][direction]
            if max(len1, len2) > length:
                if len1 > length: visit[np1[0]][np1[1]][direction] = length
                if len2 > length: visit[np2[0]][np2[1]][direction] = length
                q.append([direction, np1[:], np2[:]])

    return min(visit[n][n])

                
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
                