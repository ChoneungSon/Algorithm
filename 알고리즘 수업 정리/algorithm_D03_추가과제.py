T = int(input())

for i in range(1,T+1):
    n, m = map(int,input().split())
    total_mat = [0]*n
    max_fly = 0
    
    for k in range(n):
        total_mat[k] = list(map(int,input().split()))
        
    for k1 in range(n-m+1):
        for k2 in range(n-m+1):
            sum_fly = 0
            for k3 in range(m):
                for k4 in range(m):
                    sum_fly += total_mat[k1+k3][k2+k4]
            if max_fly < sum_fly:
            	max_fly = sum_fly

    print('#{0} {1}'.format(i, max_fly))