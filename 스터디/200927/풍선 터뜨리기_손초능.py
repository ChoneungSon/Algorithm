def solution(a):

    # a 배열의 길이
    n = len(a)

    # 양 옆에서의 최소값이 모두 나보다 작으면, 반대의 경우에는 가능
    if len(a) <= 2:
        # 한 개나 2개일 경우는 바로 출력
        return len(a)
    else:
        # 3개 이상
        # 양 끝 값은 무조건 가능
        answer = 2

        # 왼쪽에서 최댓값
        left = [0] * n
        # 오른쪽에서 최댓값
        right = [0] * n

        # 각각의 위치에서 최솟값 저장
        left_min, right_min = a[0], a[-1]
        left[0], right[-1] = a[0], a[-1]

        # 최솟값 배열 생성
        for i in range(1, n):
            left_min = min(left_min, a[i])
            right_min = min(right_min, a[n-1-i])
            left[i], right[n-1-i] = left_min, right_min

        # 조건에 맞는 값 찾기
        for i in range(1, n-1):
            if not(a[i] > left[i-1] and a[i] > right[i+1]):
                answer += 1

        return answer


print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))