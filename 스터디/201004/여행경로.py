def solution(tickets):

    adj = {}
    n = len(tickets)

    # map
    for s, e in tickets:
        adj[s] = adj.get(s, {})
        adj[s][e] = adj[s].get(e, 0) + 1 # 티켓 수 저장

    for key in adj.keys():
        adj[key] = dict(sorted(adj[key].items()))
        # 사전 순으로 앞선 경로가 필요하므로
        # 탐색할 때 정렬된 순서로 가도록 함 

    answer = ['ICN']

    def dfs(s, cnt):
        nonlocal answer, adj, n
        if cnt == n:
            return True
        elif adj.get(s):
            for key, value in adj[s].items():
                if value:
                    answer.append(key)
                    adj[s][key] -= 1
                    if dfs(key, cnt+1): return True # true 나오면 빠져나오도록
                    adj[s][key] += 1
                    answer.pop()

    dfs('ICN', 0)

    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))