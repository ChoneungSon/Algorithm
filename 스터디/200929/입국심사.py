def solution(n, times):

    left, right = 0, min(times) * n

    while left < right:
        
        mid = (left + right) // 2
        
        # 시간이 주어졌을 때, 처리할 수 있는 사람 수 구하기
        cnt = 0
        for i in times:
            cnt += mid // i

        if cnt < n: left = mid + 1
        elif cnt >= n: right = mid
        print(left, right)

    return (left + right) // 2

print(solution(6, [7, 10]))