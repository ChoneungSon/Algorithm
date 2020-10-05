import heapq

def solution(jobs):

    answer = 0
    n = len(jobs)

    jobs.sort(key=lambda x: [x[0], -x[1]])

    # 시간을 설정
    time = 0

    # 우선순위 큐
    q = []

    i = 0
    while i < n or q:
        # 현재 시간보다 작거나 같은 애들 전부 큐에 넣기
        # 어차피 현재 시간 보다 작으면 작업 시간이 적은 애를 넣는게 작업 시간을 줄일 수 있음
        if i < n and time >= jobs[i][0]:
            # heapq 는 배열의 앞에서부터 우선순위를 검사함
            heapq.heappush(q, [jobs[i][1], jobs[i][0]])
            i += 1
            continue
        if q:
            # 현재 시간과 작업시간 최신화
            work, insert = heapq.heappop(q)
            time += work
            answer += time - insert
        else:
            # q가 비어있을 때는 현재 시간만 최신화
            time = jobs[i][0]

    return answer // n
  
print(solution([[0,3], [1,9], [2,8]]))
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))
print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))
print(solution([[0, 3], [4, 4], [5, 3], [4, 1]]))
print(solution([[0, 3], [1, 9], [500, 6]]))