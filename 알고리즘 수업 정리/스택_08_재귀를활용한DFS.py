def DFS(n, V):
    visited[n] = 1 # n번 노드에 방문 표시
    print(n+1)
    for i in range(V): # 인접행렬의 n행에 대해서 검색하는 과정. n번 노드에서 갈 수 있는 노드를 검색.
        if adj[n][i] != 0 and visited[i] == 0:
            DFS(i, V)

# input
# 5 6
# 1 2 1 3 3 2 2 5 3 4 5 4

V, E = map(int, input().split())
adj = [[0]*V for _ in range(V)]
edge = list(map(int, input().split()))
visited = [0] * V
for i in range(E):
    adj[edge[2*i]-1][edge[2*i+1]-1] = 1 # 방향성이 있으면 이렇게
    # adj[edge[2*i+1]-1][edge[2*i]-1] = 1 뱡향성이 없으면 이것도 추가

DFS(0, V)

# output
# 1 2 5 4 3

# 양방향과 무향 그래프는 다르다.
# 이걸로 n queen 해보자!!!!