comb = [[0]*301 for _ in range(301)]
comb[0][0] = 1

for i in range(1, 301):
    for j in range(301):
        if j == 0 or i == j: 
            comb[i][j] = 1
        else: comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
        comb[i][j] %= 10**7 + 19

def solution(a):
    global comb

    r, c = len(a), len(a[0])

    DP = [[0]*(r+1) for _ in range(c+2)]
    counts = [0] * c

    for i in range(c):
        cnt = 0
        for j in range(r):
            if a[j][i]: cnt += 1
        counts[i] = cnt

    DP[1][r-counts[0]] = comb[r][r-counts[0]]

    for i in range(1, c):
        for j in range(r):
            if DP[i][j] == 0: continue
            for k in range(counts[i]+1):
                if j < k or j + counts[i] - 2*k > r: continue
                result = comb[j][k] * comb[r-j][counts[i]-k] % (10**7 + 19)
                DP[i+1][j+counts[i]-2*k] = DP[i+1][j+counts[i]-2*k] + DP[i][j] * result
                DP[i+1][j+counts[i]-2*k] %= 10**7 + 19

    return DP[c][r]

print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]]))
print(solution([[1,0,0],[1,0,0]]))