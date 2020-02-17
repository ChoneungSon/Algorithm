T = 10

for _ in range(T):
    i = int(input())
    n = 10
    total_mat = [[0]*n for _ in range(n)]
    row_sum = 0
    column_sum = 0
    dia_sum = 0
    tdia_sum = 0
    
    for k in range(n):
        total_mat[k] = list(map(int,input().split()))
        
    max_sum = 0
    
    for k in range(n):
        dia_sum += total_mat[k][k]
        tdia_sum += total_mat[k][-(k+1)]
        
    list_sum =[dia_sum, tdia_sum]
    
    for k3 in list_sum:
            if max_sum < k3:
                max_sum = k3
    
    for k1 in range(n):
        row_sum = 0
        column_sum = 0
        for k2 in range(n):
            row_sum += total_mat[k1][k2]
            column_sum += total_mat[k2][k1]

        list_sum =[row_sum, column_sum]

        for k3 in list_sum:
            if max_sum < k3:
                max_sum = k3
            
    print('#{0} {1}'.format(i, max_sum))