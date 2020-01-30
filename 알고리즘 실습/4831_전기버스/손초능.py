T = int(input())

for i in range(1,T+1):
    limit_move, stop, n_charge = list(map(int,input().split()))
    list_charge = list(map(int,input().split()))
    start_point = 0
    result = 0
    
    while 1:
        
        ok = False

        # 시작 지점에서 최대 이동거리만큼 이동한 지점 사이에 충전소가 있는지 역순서로 판단하고
        for k1 in range(start_point+limit_move,start_point,-1):                
            for k2 in range(len(list_charge)-1, -1, -1):
                if k1 == list_charge[k2]: # 시작지점에서 가장 먼 거리의 충전소가 있으면 그 지점으로 시작지점 이동
                    start_point = list_charge[k2]
                    result += 1
                    ok = True
                    break
            if ok == True:
                break                    
            elif k1 == stop: # 마지막으로 시작시점에서 최대 이동거리만큼 이동한 지점 사이에 End point가 존재하면 정지
                start_point = k1
                ok = True
                break            

        if ok == False:
            print('#{0} 0'.format(i))
            break
        elif start_point == stop:
            print('#{0} {1}'.format(i,result))
            break