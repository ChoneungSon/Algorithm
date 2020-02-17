T = int(input())

for i in range(1, T+1):
    color_num = int(input())
    list_color = [0] * color_num
    for k in range(color_num):
         list_color[k]= list(map(int, input().split()))
    n = 10
    total_mat = [[0]*n for _ in range(n)]
    count = 0
    
    for k in range(color_num):
        for k1 in range(list_color[k][0], list_color[k][2]+1):
            for k2 in range(list_color[k][1], list_color[k][3]+1):
                total_mat[k1][k2] += list_color[k][4]
                if total_mat[k1][k2] == 3:
                    count += 1
    
    print('#{0} {1}'.format(i, count))