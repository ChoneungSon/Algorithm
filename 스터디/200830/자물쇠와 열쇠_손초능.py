from copy import deepcopy

def solution(key, lock):

    def game(x, y):
        nonlocal m, n, key, lock, lock_empty
        cnt = 0
        for i in range(m):
            for j in range(m):
                if 0 <= x+i-m+1 < n and 0 <= y+j-m+1 < n:
                    if key[i][j] == lock[i+x-m+1][j+y-m+1]: return 0
                    elif key[i][j] == 1 and lock[i+x-m+1][j+y-m+1] == 0: cnt += 1
        if cnt == lock_empty: return 1
        else: return 0

    def turn_key():
        nonlocal key, m
        copy_key = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                copy_key[i][j] = key[m-1-j][i]
        key = deepcopy(copy_key)

    m, n = len(key), len(lock)
    lock_empty = 0

    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                lock_empty += 1
    
    for i in range(n+m-1):
        for j in range(n+m-1):
            for _ in range(4):
                if game(i, j): return True
                else: turn_key()
    
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))