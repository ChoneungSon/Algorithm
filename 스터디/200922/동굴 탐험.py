import sys
sys.setrecursionlimit(10**9)

def solution(n, path, order):

    # 인접 dictionary
    adj = {i:[] for i in range(n)}
    for s, e in path:
        adj[s].append(e)
        adj[e].append(s)

    # 먼저 방문해야 할 방 체크
    pre_visit = [0] * n
    for f, s in order:
        pre_visit[s] = f

    # 나중에 방문해야 할 방
    post_visit = [0] * n

    # 방문 체크 리스트
    visit = [0] * n
    visit[0] = 1

    def dfs(point):
        nonlocal visit, adj, pre_visit, n
        if visit[point]: return
        if not visit[pre_visit[point]]:
            post_visit[pre_visit[point]] = point
            return
        visit[point] = 1
        if post_visit[point]: dfs(post_visit[point])
        for i in adj[point]:
            dfs(i)

    if not pre_visit[0]:
        for i in adj[0]: dfs(i)

    if sum(visit) == n: return True
    return False

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))