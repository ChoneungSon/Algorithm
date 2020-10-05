# 우선 순위 큐 이용 효율성 1, 3만 통과
import heapq

def solution1(n, cores):

    result = [(0, i) for i in range(1, len(cores)+1)]

    while n:
        time, core = heapq.heappop(result)
        heapq.heappush(result, (time+cores[core-1], core))
        n -= 1

    return core

# parametric search
def solution(n, cores):

    # 코어의 개수
    N = len(cores)

    # 코어가 작업량보다 많으면 n을 그대로 반환
    if n <= N:
        return n

    # 모든 코어가 동일한 처리시간을 가진다고 가정할 때 최대와 최소 걸리는 시간을 구한다.
    min_core, max_core = min(cores), max(cores)
    left = (min_core * (n-N)) // N
    right = (max_core * (n-N)) // N

    while left <= right:
        
        # 작업 시작부터 코어 개수 만큼 작업이 할당됨
        core_work = N # 현재 코어들이 할당받은 일의 수
        current_work = 0 # 코어들이 완료한 일의 수

        mid = (left + right) // 2

        # 중간 시간을 현재 시점으로 해서 코어별로 작업량 구하기
        for core in cores:
            core_work += mid // core # 현재 코어의 작업량 더하기
            if not(mid % core):
                current_work += 1 # 현재 막 작업을 할당 받은 코어

        if core_work < n:
            left = mid + 1
        elif n <= (core_work - current_work):
            right = mid - 1
        else:
            cnt = core_work - current_work
            for i in range(N):
                if mid % cores[i] == 0: cnt += 1
                if cnt == n: return i+1

print(solution(6, [1,2,3]))