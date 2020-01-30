T = int(input())

for i in range(1,T+1):
    n, m = list(map(int,input().split()))
    list_num = list(map(int,input().split()))
    
    max_x = sum(list_num[0:m])
    min_x = sum(list_num[0:m])
    
    for k in range(m,n):
        if sum(list_num[k-m+1:k+1]) > max_x:
            max_x = sum(list_num[k-m+1:k+1])
        elif sum(list_num[k-m+1:k+1]) < min_x:
            min_x = sum(list_num[k-m+1:k+1])
            
    print('#{0} {1}'.format(i, max_x-min_x))