def solution(n, weak, dist):
    
    move_dist = [0] * len(weak)
    for i in range(len(weak)-1): move_dist[i] = weak[i+1] - weak[i]
    move_dist[len(weak)-1] = n - weak[len(weak)-1] + weak[0]

    visit = [0] * len(dist)
    min_cnt = 9

    def dfs(start, end, cnt):
        nonlocal visit, dist, move_dist, n, min_cnt
        if cnt >= min_cnt: return
        elif cnt != 0 and start == end:
            min_cnt = cnt
        else:
            for i in range(len(dist)):
                if visit[i] == 0:
                    visit[i] = 1
                    part_len = move_dist[end]
                    part = (end + 1) % len(weak)
                    while part_len <= dist[i] and start != part:
                        part_len += move_dist[part]
                        part = (part+1) % len(weak)
                    dfs(start, part, cnt+1)
                    visit[i] = 0

    for i in range(len(weak)):
        dfs(i, i, 0)

    if min_cnt == 9: return -1
    else: return min_cnt

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))