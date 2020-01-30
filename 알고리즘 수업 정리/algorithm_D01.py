T = int(input()) # 테스트 케이스의 갯수

for i in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))

    # 첫 번째를 가장 큰 자리로 지정
    max_id = 0

    for k in range(1,n): # 나머지 자리와 비교
        if arr[k] > arr[max_id]: # 최댓값으로 지정된 값보다 현재 자리의 값이 더 크면 최댓값을 현재값으로 변경
            max_id = k

    print('#{0} {1} {2}'.format(i, max_id+1, arr[max_id]))