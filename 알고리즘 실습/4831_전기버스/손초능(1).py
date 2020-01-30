T = int(input())

for i in range(1,T+1):
    limit_move, stop, n_charge = list(map(int,input().split()))
    list_charge = list(map(int,input().split()))
    start_point = 0
    results = 0
    
    while 1:
        
        for k1 in range(start_point+limit_move,start_point,-1):                
            result = 0
            for k2 in range(len(list_charge)-1, -1, -1):
                if k1 == list_charge[k2]:
                    start_point = list_charge[k2]
                    result = 1
                    break  
            if result != 0:
                results += 1
                break
            elif k1 == stop:
                start_point = k1
                break                 

        if start_point == stop:
            break
        elif result == 0:
            results = 0
            break

    print('#{0} {1}'.format(i, results))    