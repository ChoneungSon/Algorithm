T = int(input())

for i in range(1,T+1):
    n = int(input())
    list_int = list(map(int,input().split()))
    max_x = list_int[0]
    min_x = list_int[0]
    
    for k in range(1,n):
        if list_int[k] > max_x:
            max_x = list_int[k]
        elif list_int[k] < min_x:
            min_x = list_int[k]
            
    print('#{0} {1}'.format(i, max_x - min_x))