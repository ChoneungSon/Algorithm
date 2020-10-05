def solution(distance, rocks, n):

    rocks.sort()
    rocks = [0] + rocks + [distance]

    left, right = 1, 1000000000

    while left <= right:
        cnt = 0
        prev = 0
        mid = (left+right) // 2

        for i in range(1, len(rocks)):
            if rocks[i] - rocks[prev] < mid:
                cnt += 1
            else:
                prev = i

        if cnt <= n:
            left = mid + 1
        else:
            right = mid - 1

    return (left + right) // 2

print(solution(25, [2,14,11,21,17], 2))