def DFS(n, V):
    s = [] # 스택 생성
    used = [0] * V # 중복확인
    s.append(n) # push(n) 시작점 저장
    used[n] = 1
    while len(s) != 0: # 스택이 비어있지 않으면
        n = s.pop() # 방문할 지점을 스택에서 꺼낸다. 갈 수 있는 노드 중 하나를 꺼내 이동.
        print(n+1, end = " ")
        for i in range(V):
            if adj[n][i] == 1 and used[i] == 0: # i가 인접이고, 스택에 들어있지 않으면
                s.append(i) # 인접 목록 추가
                used[i] = 1 # 목록에 추가 표시

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
# 1 3 4 2 5

# 양방향과 무향 그래프는 다르다.
# 이걸로 n queen 해보자!!!!