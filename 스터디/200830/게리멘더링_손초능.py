import sys
input = sys.stdin.readline

def dfs(cnt):
    global n, part, visited
    if cnt == n // 2: return
    else:
        for i in range(1,n+1):
            if visited[i] == 0:
                visited[i] = 1
                part.append(i)
                game()
                dfs(cnt + 1)
                visited[i] = 0
                part.pop()

def game():
    global part, n, adj, people, total_people, min_diff
    visit = [0] * (n+1)
    q = [part[0]]
    visit[part[0]] = 1
    part_people = people[part[0]]
    while q:
        x = q.pop(0)
        for i in adj[x]:
            if visit[i] == 0 and i in part:
                visit[i] = 1
                part_people += people[i]
                q.append(i)
    for i in range(1, n+1):
        if visit[i] == 0:
            visit[i] = 1
            q = [i]
            while q:
                x = q.pop(0)
                for j in adj[x]:
                    if visit[j] == 0 and j not in part:
                        visit[j] = 1
                        q.append(j)
            break
    if sum(visit) == n:
        min_diff = min(min_diff, abs(total_people - 2*part_people))

n = int(input())

people = [0] + list(map(int, input().split()))
total_people = sum(people)
min_diff = float('inf')

adj = {i: [] for i in range(1, n+1)}

for i in range(1, n+1):
    nums = list(map(int, input().split()))
    adj[i] = nums[1:]

part = []
visited = [0] * (n+1)

dfs(0)

if min_diff != float('inf'): print(min_diff)
else: print(-1)